# --- PART 1: IMPORTS ---
# These lines bring in the Android/Kivy building blocks (buttons, text boxes)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

# --- PART 2: THE APP DASHBOARD ---
class MyConvertedApp(App):
    def build(self):
        # This acts as the main container box on your phone screen
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # This creates the text screen that will show your program's results
        self.output_label = Label(text="Tap below to run your script")
        
        # This makes the text scrollable so long outputs don't get cut off
        scroll = ScrollView(size_hint=(1, 0.8))
        scroll.add_widget(self.output_label)
        
        # This creates the visual button you will tap on your phone
        run_btn = Button(text="Launch Program", size_hint=(1, 0.2))
        
        # CRITICAL: This links the button to your actual code below!
        run_btn.bind(on_press=self.execute_my_script)
        
        # Put the screen and button inside the main container
        layout.add_widget(scroll)
        layout.add_widget(run_btn)
        return layout

# --- PART 3: THE ENGINE (YOUR SCRIPT GOES HERE) ---
    def execute_my_script(self, instance):
        try:
		import os
		import subprocess
		import speech_recognition as sr
		from google import genai

		# Initialize the Gemini client 
		# (It automatically reads the GEMINI_API_KEY environment variable)
		client = genai.Client()

		def speak(text):
		    """Uses Termux API to speak out loud."""
		    print(f"Friday: {text}")
		    subprocess.run(["termux-tts-speak", text])

		def listen():
		    """Uses Android's native speech-to-text via Termux API."""
		    print("Listening...")
		    try:
		        # Calls the built-in Android speech recognizer
		        result = subprocess.run(["termux-speech-to-text"], capture_output=True, text=True)
		        command = result.stdout.strip()
		        if command:
		            print(f"You: {command}")
		            return command.lower()
		    except Exception as e:
		        print(f"Speech recognition error: {e}")
		    return ""

		def open_app(package_name, app_name):
		    """Launches an Android app using its package name via Termux-am."""
		    speak(f"Opening {app_name} for you, buddy.")
		    subprocess.run(["am", "start", "--user", "0", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		def main():
		    speak("Friday is online. What's up, buddy?")
		    
		    # App dictionary mapping voice commands to Android package names
		        # Expanded app dictionary mapping voice commands to Android package names
		    apps = {
		        # Social Media & Communication
		        "youtube": "com.google.android.youtube",
		        "chrome": "com.android.chrome",
		        "whatsapp": "com.whatsapp",
		        "spotify": "com.spotify.music",
		        "instagram": "com.instagram.android",
		        "facebook": "com.facebook.katana",
		        "messenger": "com.facebook.orca",
		        "snapchat": "com.snapchat.android",
		        "telegram": "org.telegram.messenger",
		        "x": "com.twitter.android",
		        "twitter": "com.twitter.android",
		        "pinterest": "com.pinterest",
		        "linkedin": "com.linkedin.android",
		        
		        # Google Productivity & Tools
		        "maps": "com.google.android.apps.maps",
		        "gmail": "com.google.android.gm",
		        "drive": "com.google.android.apps.docs",
		        "calendar": "com.google.android.calendar",
		        "photos": "com.google.android.apps.photos",
		        "keep": "com.google.android.keep",
		        "clock": "com.google.android.deskclock",
		        "calculator": "com.google.android.calculator",
		        
		        # Entertainment & Streaming
		        "netflix": "com.netflix.mediaclient",
		        "prime video": "com.amazon.avod.thirdpartyclient",
		        "disney": "com.disney.disneyplus",
		        "vlc": "org.videolan.vlc",
		        
		        # System & Shopping
		        "settings": "com.android.settings",
		        "play store": "com.android.vending",
		        "amazon": "com.amazon.mShop.android.shopping",
		        "flipkart": "in.flipkart.android"
		    }

		    
		    while True:
		        command = listen()
		        if not command:
		            continue
		            
		        # Exit Condition
		        if "goodbye" in command or "exit" in command:
		            speak("Goodbye! Hit me up whenever you need me.")
		            break
		            
		        # Hardware Control: Vibrate
		        elif "vibrate" in command:
		            speak("Vibrating your phone now.")
		            subprocess.run(["termux-vibrate", "-d", "1000"])
		            
		        # Hardware Control: Battery Status
		        elif "battery" in command:
		            result = subprocess.run(["termux-battery-status"], capture_output=True, text=True)
		            speak(f"Here is your battery data: {result.stdout}")
		            
		        # App Launcher Control
		        elif "open" in command or "launch" in command:
		            opened = False
		            for app_name, package in apps.items():
		                if app_name in command:
		                    open_app(package, app_name)
		                    opened = True
		                    break
		            if not opened:
		                speak("I couldn't find that app package in my system mapping.")
		                
		        # AI Buddy Conversation (Fallback for everything else)
		        else:
		            try:
		                # Prompt forces Gemini to act like your casual friend named Friday
		                prompt = f"You are Friday, a friendly, casual, and witty AI buddy. Respond to your friend's comment briefly and conversationally: {command}"
		                
		                response = client.models.generate_content(
		                    model='gemini-3.5-flash',
		                    contents=prompt,
		                )
		                
		                speak(response.text)
		            except Exception as e:
		                print(f"Error: {e}")
		                speak("My brain caught an error. Make sure your API key is exported.")

		if __name__ == "__main__":
		    main()


            
            # This final line takes your script's output and updates the app screen
            self.output_label.text = str(my_termux_data)
            
        except Exception as e:
            # If your script has a bug, this displays the error on the app screen instead of crashing
            self.output_label.text = f"Error: {str(e)}"

# --- PART 4: THE LAUNCHER ---
if __name__ == '__main__':
    MyConvertedApp().run()

