import time


async def clear_channel(ctx):
    await ctx.response.send_message('Messages are being cleared, please wait', ephemeral=True)
    async for message in ctx.channel.history():
        await message.delete()
        time.sleep(0.5)

async def shy(ctx):
    await ctx.response.send_message(':point_right::point_left:')