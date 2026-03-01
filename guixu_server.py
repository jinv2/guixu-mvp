import asyncio
import websockets
import json
import random

# 金威原创诗文库（仅作占位，未来大模型将直接生成或精准调取）
poems = [
    "时间就像一把杀猪刀，无情地割裂着一切……",
    "扶桑震颤，现金流如弱水倒流，命盘崩裂。",
    "资方逼宫，龙吟九天，撕裂值已破十万。",
    "高管甩锅，月黑风高，背叛如九尾狐现。"
]

async def guixu_brain(websocket):
    print("⚡ 归墟驾驶舱已连接！神识注入成功。")
    try:
        async for message in websocket:
            data = json.loads(message)
            user_text = data.get("text", "")
            print(f"📥 收到驾驶员诉求: {user_text}")

            # ==========================================
            # 核心推演区：这里目前是轻量逻辑，未来直接替换为调用本地大模型的推演代码
            # ==========================================
            
            # 1. 意图感知 (未来由大模型提取)
            scene = "现金流告急"
            if "逼宫" in user_text or "撤资" in user_text: scene = "资方逼宫"
            elif "甩锅" in user_text or "推责" in user_text: scene = "高管甩锅"
            elif "背叛" in user_text or "离职" in user_text: scene = "骨干背叛"
            
            # 2. 数值剥夺计算 (未来由大模型根据商战策略的高下，返回浮动值)
            mingpan_change = 22 if any(k in user_text for k in ["赢", "胜", "成"]) else -12
            shayi_change = 15
            sile_change = random.randint(3000, 5000)
            
            # 3. 远古神祇召唤
            god = random.choice(["刑天", "饕餮", "穷奇", "混沌"])
            reply_poem = random.choice(poems)

            # 打包神识反馈
            response = {
                "scene": scene,
                "god": god,
                "reply": f"{user_text}<br><br><span style='color:#0ff; font-size:24px;'>「{reply_poem}」</span>",
                "mingpan_change": mingpan_change,
                "shayi_change": shayi_change,
                "sile_change": sile_change
            }
            
            print(f"📤 大妖反击已发送: {god} - 杀意激增 {shayi_change}%")
            await websocket.send(json.dumps(response))
            
    except websockets.exceptions.ConnectionClosed:
        print("归墟驾驶舱连接断开。等待下一次唤醒...")

async def main():
    # 启动轻量级神经节点，监听本地 8765 端口
    async with websockets.serve(guixu_brain, "localhost", 8765):
        print("🌌 归墟·山海经商战宇宙 AUI 神经节点已启动 (ws://localhost:8765)")
        print("等待驾驶舱接入...")
        await asyncio.Future()  # 持续运行

if __name__ == "__main__":
    asyncio.run(main())
