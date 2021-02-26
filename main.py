if __name__ == '__main__':
    from handlers import dp
    from aiogram import executor
    executor.start_polling(dp)
