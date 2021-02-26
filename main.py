from utils.db import set_sql
from constants import DATA_DIR


async def on_startup(_):
    with open(DATA_DIR / 'db.sql', 'r') as f:
        await set_sql(sql=f.read(), script=True)


if __name__ == '__main__':
    from handlers import dp
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup)
