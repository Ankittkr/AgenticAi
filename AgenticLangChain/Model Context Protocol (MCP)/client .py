from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()
async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "transport" : "stdio",
                "command" : "python",
                "args":["E:/AgenticAi/AgenticLangChain/Model Context Protocol (MCP)/mathserver.py"]
            },
            "weather":{
                "transport" :"streamable-http",
                "url" : "http://127.0.0.1:8000/mcp"
            }
        }
    )
    tools = await client.get_tools()

    agent = create_agent(
        "groq:openai/gpt-oss-20b",
        tools
    )

    math_response = await agent.ainvoke({"messages":[{"role":"user","content":"what's (3 + 5) x 12?"}]})
    print(math_response['messages'][-1].content)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    )
    print(weather_response['messages'][-1].content)


    
if __name__ == "__main__":
    asyncio.run(main())


