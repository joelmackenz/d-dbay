async def runTestAuctions():
    await message.channel.send("Running test auctions...")
    numOfTestAuctions = 30
    for i in range(numOfTestAuctions):
        randomitem_value = random.randint(1, 300)
        for x in range(20):
            state.current_user = str("Joel-debug")
            state.item = str("test example")
            state.item_value = int(randomitem_value)
            state.hype = str("performance")
            state.modifier = int(0)
            state.item_percent = int(10)
            state.rarity = "common"
            await debugAuction(message)
        await message.channel.send("Debugs " + str(i + 1) + "/" + str(numOfTestAuctions) + " complete")
    # for i in range(numOfTestAuctions):
    #     randomitem_value = random.randint(1, 300)
    #     for x in range(20):
    #         state.current_user = str("Joel-debug")
    #         state.item = str("test example")
    #         state.item_value = int(randomitem_value)
    #         state.hype = str("performance")
    #         state.modifier = int(0)
    #         state.item_percent = int(50)
    #         state.rarity = "uncommon"
    #         await debugAuction(message)
    #     await message.channel.send("Debugs " + str(i + 1) + "/" + str(numOfTestAuctions) + " complete")
    # for i in range(numOfTestAuctions):
    #     randomitem_value = random.randint(1, 300)
    #     for x in range(20):
    #         state.current_user = str("Joel-debug")
    #         state.item = str("test example")
    #         state.item_value = int(randomitem_value)
    #         state.hype = str("performance")
    #         state.modifier = int(0)
    #         state.item_percent = int(50)
    #         state.rarity = "rare"
    #         await debugAuction(message)
    #     await message.channel.send("Debugs " + str(i + 1) + "/" + str(numOfTestAuctions) + " complete")