from .db import get_connection, search_products
from .llm_free import query_openrouter

def get_product_context(query: str):
    """Retrieve product details from SQLite for RAG prompt composition."""
    conn = get_connection()
    cur = conn.cursor()
    row = cur.execute(
        "SELECT name, description, price FROM products WHERE name LIKE ? OR description LIKE ? LIMIT 1",
        (f"%{query}%", f"%{query}%")
    ).fetchone()
    conn.close()
    if row:
        name, desc, price = row
        return f"{name}، {desc}، با قیمت تقریبی {price:,.0f} تومان."
    return None


async def rag_pipeline(query: str) -> str:
    """ retrieve product info from SQLite - build prompt and send to free LLM model. """
    context = get_product_context(query)

    if not context:
        prompt = f"پرسش کاربر: {query}\nهیچ محصولی در دیتابیس یافت نشد. پاسخ عمومی بده."
        return await query_openrouter(prompt)

    prompt = f"اطلاعات محصول: {context}\n\nپرسش کاربر: {query}\nپاسخ را دقیق و فارسی بده."
    return await query_openrouter(prompt)
