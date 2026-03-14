import asyncio
import websockets
import datetime
import webbrowser
import random
import os
        
async def handle_client(websocket):
    async for message in websocket:
        msg = message.lower().strip()
        print(f"User said: {msg}")

        response = "I'm not sure how to help with that."

        # Greetings
        if "hello" in msg or "hi" in msg:
            response = "Hello! How can I assist you today?"

        # Time & Date
        elif "time" in msg:
            response = f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
        elif "date" in msg:
            response = f"Today's date is {datetime.datetime.now().strftime('%A, %d %B %Y')}"

        # YouTube
        elif "youtube" in msg:
            if "search" in msg:
                query = msg.replace("youtube search", "").strip()
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
                response = f"Searching YouTube for {query}..."
            else:
                webbrowser.open("https://www.youtube.com")
                response = "Opening YouTube..."

        # Google
        elif "google" in msg:
            if "search" in msg:
                query = msg.replace("google search", "").strip()
                webbrowser.open(f"https://www.google.com/search?q={query}")
                response = f"Searching Google for {query}..."
            else:
                webbrowser.open("https://www.google.com")
                response = "Opening Google..."

        # General search
        elif msg.startswith("search "):
            query = msg.replace("search", "").strip()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                response = f"Searching Google for {query}..."
            else:
                response = "Please tell me what to search for."

        # Wikipedia
        elif "wikipedia" in msg:
            webbrowser.open("https://www.wikipedia.org")
            response = "Opening Wikipedia..."

        # Calculator
        elif msg.startswith("calculate "):
            try:
                expression = msg.replace("calculate", "").strip()
                result = eval(expression)
                response = f"The result of {expression} is {result}"
            except Exception:
                response = "Sorry, I couldn’t calculate that."

        # Weather
        
        elif "weather in" in msg:
               city = msg.replace("weather in", "").strip()
               webbrowser.open(f"https://www.google.com/search?q=weather+{city}")
               response = f"Showing weather in {city}..."

        elif "weather" in msg:
            webbrowser.open("https://www.google.com/search?q=weather")
            response = "Showing today’s weather..."


        # News
        elif "news about" in msg:
            topic = msg.replace("news about", "").strip()
            webbrowser.open(f"https://news.google.com/search?q={topic}")
            response = f"Fetching latest news about {topic}..."
        elif "news" in msg:
            webbrowser.open("https://news.google.com")
            response = "Opening Google News..."

        # Jokes
        elif " tell me a joke" in msg or "funny jokes" in msg:
            jokes = [
                "Why don’t programmers like nature? It has too many bugs.",
                "Parallel lines have so much in common… it’s a shame they’ll never meet.",
                "Why did the scarecrow win an award? Because he was outstanding in his field!"
            ]
            response = random.choice(jokes)

        # Motivation
        elif "motivate me " in msg or "inspire me" in msg or "quote" in msg:
            quotes = [
                "Push yourself, because no one else is going to do it for you.",
                "Dream it. Wish it. Do it.",
                "Great things never come from comfort zones.",
                "Don’t stop when you’re tired. Stop when you’re done."
            ]
            response = random.choice(quotes)

        # Fun facts
        elif "fact" in msg:
            facts = [
                "Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs.",
                "Bananas are berries, but strawberries are not.",
                "Octopuses have three hearts."
            ]
            response = random.choice(facts)

        # Apps
        elif "notepad" in msg:
            os.system("notepad")
            response = "Opening Notepad..."
        elif "open calculator" in msg:
            os.system("calc")
            response = "Opening Calculator..."
        elif "paint" in msg:
            os.system("mspaint")
            response = "Opening Paint..."
        elif "explorer" in msg or "files" in msg:
            os.system("explorer")
            response = "Opening File Explorer..."

        # System control
        elif "shutdown" in msg:
            response = "Shutting down the system..."
            os.system("shutdown /s /t 1")
        elif "restart" in msg:
            response = "Restarting the system..."
            os.system("shutdown /r /t 1")

        # Music
        elif "music" in msg or "spotify" in msg:
            webbrowser.open("https://open.spotify.com")
            response = "Opening Spotify for music..."

        await websocket.send(response)
        
async def main():
    try:
        async with websockets.serve(handle_client, "0.0.0.0", 8765):

            print("Voice Assistant running on ws://localhost:8765")
            await asyncio.Future()
    except KeyboardInterrupt:
        print("Server stopped manually.")

if __name__ == "__main__":
    asyncio.run(main())