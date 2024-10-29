import pyttsx3 # type: ignore

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties for voice, rate, and volume
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():  # Select a male voice if available
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 200)  # Set rate to a higher value for faster speech
engine.setProperty('volume', 1)  # Max volume

# Convert text to speech and save to file
mytext = "From pure evil to hero, these villains’ transformations stunned fans and left lasting impacts. Today, we're looking at the top 5 anime villains with redemption arcs that changed everything! Starting at number 5, we have Vegeta from Dragon Ball Z. Once a ruthless Saiyan bent on destroying Earth, Vegeta’s character growth is one of anime’s finest. Through his complex journey, he finds honor, loyalty, and, eventually, his own family, redeeming himself as a true hero. Number 4 brings us Meruem from Hunter x Hunter. Known as the powerful King of the Chimera Ants, Meruem begins as an unfeeling dictator. But his bond with the human girl Komugi brings out a profound change in him, making his end both heart-wrenching and memorable. At number 3 is Gaara from Naruto. Once driven by vengeance and hatred, Gaara learns the meaning of friendship and peace after meeting Naruto. His path from feared monster to a beloved Kazekage is both inspiring and moving.Coming in at number 2, Itachi Uchiha from Naruto Shippuden. At first seen as a merciless traitor, Itachi’s true motives reveal his self-sacrifice to protect his brother and village, making his story one of anime’s most tragic redemptions.And finally, at number 1, Zuko from Avatar: The Last Airbender. Zuko’s journey from banished prince to trusted friend of the Avatar is filled with internal struggles and growth. His redemption is one of the most beloved arcs in anime history.There you have it, five villains whose paths to redemption brought depth and emotion to their stories! Who’s your favorite redeemed villain? Let us know in the comments, and be sure to like and subscribe for more amazing anime insights!"
engine.save_to_file(mytext, 'top_5_anime_villans_with_redemption_arc.mp3')
engine.runAndWait()
