from constants import WEBHOOK_PORT, WEBHOOK_HOST, WEBHOOK_PATH

async def on_startup(dp):
    await dp.bot.set_webhook(WEBHOOK_HOST+WEBHOOK_PATH)

async def on_shutdown(dp):
    await dp.bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
	from handlers import dp
	from aiogram.utils.executor import start_webhook
	start_webhook(
        dispatcher=dp,
        host=WEBHOOK_HOST,
        port=WEBHOOK_PORT,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown)
