import streamlit as st
import os
from openai import OpenAI
from io import BytesIO
import requests
from elevenlabs import ElevenLabs

# keys
client = OpenAI(api_key = st.secrets['OPENAI_API_KEY'])
LAB11_API_KEY ="sk_efa86e88a54a50a37f63b9ce1a501e6abe4317cb37f43a02"

# --------------------
#     functions
# --------------------

#takes user's character description and refine's it for dall-e image generation
def char_prompt_refine(input):
  response = client.chat.completions.create(
    model = 'gpt-4o-mini',
        messages=[
            {"role": "system", "content": """You are a professional AI prompter.
                You will be given a character description and have to turn it into a prompt for DALL-E-2 model to generate a character image.
                The image should have a white background and be <= the 256x256 dimensions.
                The character will be in a retro pixel art form
                The prompt should be within 50 words, while still conveying the character's appearance and style.
            """},
            {"role": "user", "content": input}
    ],
    max_tokens= 80
  )
  return(response.choices[0].message.content)
 
#generates character design using char_prompt_refine
def char_design(input):
  response = client.images.generate(
    model = "dall-e-2",
    prompt = input,
    size = "256x256",
    n =1,
)
  return (response.data[0].url)

#generates general game code from user input
def code_generator(game_prompt, char_design_url):
  code_prompt = f"""
        You are a professional game programmer. 
        You will be given a game idea prompt and an image URL, and you need to generate a game code that uses the image as a player character.
        Ensure that the image is injected into the HTML as: <img src="{char_design_url}" alt="Character Player">.
        The game should be having some instruction about how to play that game at the starting page and a restart button
        The image should be movable using JavaScript and CSS.
        Include HTML, CSS, and JavaScript with proper indentation.
        Do not include any explanation, and HTML.
                """
  response = client.chat.completions.create(
      model='gpt-4o-mini',
      messages=[
          {"role": "system", "content": code_prompt},
          {"role": "user", "content": game_prompt}
      ],
  )
  return response.choices[0].message.content

# Generates shooting game code with additional features
def shooting_code_generator(game_prompt, char_design_url):
  shooting_prompt = f"""
  You are a professional game programmer. 
  You will be given a game idea prompt and an image URL, and you need to generate a shooting game code that uses the image as a player character.
  Ensure that the image is injected as <img src="{char_design_url}" alt="Character Player">.
  Include HTML, CSS, and JavaScript with proper indentation.
  Do not include any explanation and HTML
  
  > Generate a 2D top-down shooter game. The game should feature:
    > - A player character controlled with WASD keys for movement and mouse click for shooting.
    > - Basic shooting mechanics with projectiles that move towards the mouse cursor. Each projectile should have a defined speed and direction based on where the player clicks.
    > - Simple enemy AI where enemies spawn randomly and chase the player. Enemies should take damage when hit by player bullets.
    > - Player health and an enemy counter to display how many enemies have been defeated.
    > - Collision detection between bullets and enemies, and between enemies and the player.
    > - A simple start screen, main gameplay loop, and game-over screen.
    > - Basic sound effects for shooting, enemy defeat, and game-over.
    """
  response = client.chat.completions.create(
      model='gpt-4o-mini',
      messages=[
          {"role": "system", "content": shooting_prompt},
          {"role": "user", "content": game_prompt}
      ],
  )
  return response.choices[0].message.content

# Endless runner (Dino) game code generator
def dino_code_generator(game_prompt, char_design_url):
  dino_prompt = f"""
  1. You are a professional game programmer. 
  2. You will be given a game idea prompt and an image URL, and you need to generate an endless runner code that uses the image as a player character.
  3. Include HTML, CSS, JAVASCRIPT only and proper indentation, also do not include any explanation, and HTML.
  4. A instruction to guide user on how to play the game during the start page and have a start button to start the game.
  5. The background color should be white 
  
  6. Create a simple endless runner game similar to the classic Dino game. The player character, represented by {char_design_url}, should run automatically from left to right across the screen. 
  7. The player can only press the space bar to make the character jump over obstacles that appear at random intervals on the ground. 
  8. Each successful jump should increase the player's score, displayed in the top corner of the screen.
  9. The game should get progressively faster as the score increases. 
  10. If the player hits an obstacle, the game should end, displaying the final score and an option to restart. 
  11. The character image should be used as the runner, and the obstacles should be simple blocks or cacti."                
  """
  response = client.chat.completions.create(
      model='gpt-4o-mini',
      messages=[
          {"role": "system", "content": dino_prompt},
          {"role": "user", "content": game_prompt}
      ],
  )
  return response.choices[0].message.content


  platform_prompt = f"""
  1. You are a professional game programmer. 
  2. You will be given a game idea prompt and an image URL, and you need to generate an endless runner code that uses the image as a player character.
  3. Ensure that the image is injected as <img src="{char_design_url}" alt="Character Player">.
  5. Include HTML, CSS, and JavaScript only and proper indentation, also do not include any explanation, and HTML.
  6. A instruction to guide user on how to play the game during the start page.
  
  > Generate a 2D top-down shooter game. The game should feature:
    A player character controlled with arrow keys or WASD for movement and space bar for jumping.
    Platformer physics including gravity, adjustable jump height, and collision detection with platforms.
    Enemies that patrol a platform and can damage the player on contact. When the player jumps on an enemy, the enemy is defeated.
    Collectible items scattered across platforms that increase the player’s score when collected.
    A health counter for the player, a score counter, and a basic UI to display them.
    A structured game loop with a start screen, main gameplay, and game-over screen.
    Basic sound effects for jumping, collecting items, and game-over. 
    """
  response = client.chat.completions.create(
      model='gpt-4o-mini',
      messages=[
          {"role": "system", "content": platform_prompt},
          {"role": "user", "content": game_prompt}
      ],
  )
  return response.choices[0].message.content

# Dungeon Crawler game code generator
def dungeon_code_generator(game_prompt, char_design_url):
  dungeon_prompt = f"""
  1. You are a professional game programmer skilled in HTML, CSS and Javascript. 
  2. You will be given a game idea prompt and an image URL, and you need to generate a simple code that uses the {char_design_url} as a player character.
  3. The background of the game should be white.
  5. Include HTML, CSS, and JavaScript only and proper indentation, also do not include any explanation, and ```HTML.
  6. A instruction to guide user on how to play the game during the start page.
  
  > Generate a 2D dungeon crawler game, a subgenre of action-adventure game. Here are the game requirements:
      Player Character: The player can move up, down, left, and right using arrow keys or WASD controls.
      Dungeon Layout: Create a grid-based dungeon with walls, open paths, and rooms. Randomly generate a few rooms with corridors connecting them.
      Enemies: Populate the dungeon with randomly placed enemies. When the player encounters an enemy, a simple combat system should initiate where the player can attack or take damage.
      Items and Pickups: Include items that the player can collect, such as health potions (to restore health) and keys (to unlock doors or reach the exit).
      Objective and Exit: The goal is to explore the dungeon, defeat enemies, find keys or treasures, and locate an exit to complete the game.
      HUD: Display the player's health, collected items, and score on the screen.
      Game Over Condition: If the player's health reaches zero, display a game-over message.
    """
  response = client.chat.completions.create(
      model='gpt-4o-mini',
      messages=[
          {"role": "system", "content": dungeon_prompt},
          {"role": "user", "content": game_prompt}
      ],
  )
  print(response.usage)
  return response.choices[0].message.content

# takes game input of user and use it to generate music
def music_prompt_refine(music_input):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": """you are a professional ai prompter.
            you will be given a music description and have to turn it into a prompt for elevenlabs model to generate suitable background music for a game.
            your prompt should be within 30 word."""},
            {"role": "user", "content": music_input}
        ],
        max_tokens=40,
    )
    return response.choices[0].message.content



st.subheader("This is the generator tab where you can create a character and game code!")

st.divider()
st.text("Creating Husbando/Waifu...")

char_input = st.text_input("provide character prompt: ")
char_refine = char_prompt_refine(char_input)
st.write(char_refine)

#columns for 'generate character' button and 'save image' button
col1, col2 = st.columns([0.3, 0.7])



#generate character
with col1:
    if st.button("Generate character design"):
        url = char_design(char_refine)
        st.session_state.image_url = url  # Store image URL in session state
        st.session_state.saved = True   # Set 'saved' to True to show the generation was successful
        st.session_state.saved_msg = "Character generated!"   # Clear the saved message

            
#variable set up
if "saved" not in st.session_state:
    st.session_state.saved = False      #variable 'saved' = false
if "saved_msg" not in st.session_state:
    st.session_state.saved_msg = "You have not generated anything yet!"

#Save image URL        
with col2:
    if st.button("Save Image"):
        if "saved_images" not in st.session_state:
            st.session_state.saved_images = []  # Initialize saved images list
        st.session_state.saved_images.append(st.session_state.image_url)
        st.session_state.saved = True
        st.session_state.saved_msg = "Image saved successfully!"
    # else:
    #   st.session_state.saved_msg = "The image has not been saved yet." 
    #   st.warning("The image has not been saved yet." ) 

# Display the character image if already generated
if "image_url" in st.session_state:
    st.image(st.session_state.image_url)
        
# Display status message based on generation and save status
if st.session_state.saved:
    st.success(st.session_state.saved_msg)  # "Image saved successfully!"
elif "image_url" in st.session_state:
    st.warning(st.session_state.saved_msg)  # "Successfully generated! The image has not been saved yet."
else:
    st.error("You have not generated anything yet!")




# ==============
# Game Section
# ==============
st.divider()
st.text("Games Factory..")
col1, col2 = st.columns([0.4, 0.7])

# Game prompt input and generation based on genre selection
with col1:
    option = st.selectbox(
    "Select your game genre:",
    ("Shooting Game", "Dungeon Crawler", "Endless Running Game (Dino Game)", "Self-Defined")
    )

with col2:
    game_input = st.text_area("Provide additional game details (Optional):")


# Initialize the saved codes list if it doesn’t exist
if "saved_codes" not in st.session_state:
    st.session_state.saved_codes = [] # Each entry is a dictionary with "code" and "genre"

# Generate code based on selected genre
if st.button("Generate Code") and "image_url" in st.session_state:
    if option == "Shooting Game":
        game_code = shooting_code_generator(game_input, st.session_state.image_url)
    elif option == "Endless Runner (Dino Game)":
        game_code = dino_code_generator(game_input, st.session_state.image_url)
    elif option == "Dungeon Crawler":
        game_code = dungeon_code_generator(game_input, st.session_state.image_url)
    else:
        game_code = code_generator(game_input, st.session_state.image_url)
        
    # Store the generated code in session state
    st.session_state.game_code = game_code
    st.success("Game generated Successfully!")
    st.code(st.session_state.game_code)  

#Save code into session_state and accessing it in library
if st.button("Save code") and "game_code" in st.session_state:
    st.success("Code saved successfully!")
    st.code(st.session_state.game_code)

    # Append the code and genre as a dictionary
    st.session_state.saved_codes.append({"code": st.session_state.game_code, "genre": option})


# ==============
# Audio Section
# ==============
st.divider()
st.text("Mozart Wannabe..")

st.write("This is the Music Generation tab.")
music_input = st.text_input("Enter your music prompt:")
music_generated = str(music_prompt_refine(music_input))
st.write(music_generated)

# Layout for Generate and Save buttons
col1, col2 = st.columns([0.2, 0.8])
response = None

if col1.button("Generate Music"):
    # API request setup
    headers = {"xi-api-key": LAB11_API_KEY}
    json_data = {   
        "text": music_generated,
        "duration_seconds": 2.0,
        "prompt_influence": 0.5,
    }

    # Make the request
    response = requests.post(
        "https://api.elevenlabs.io/v1/sound-generation",
        headers=headers,
        json=json_data
    )

    # Check if the request was successful
    if response is not None and response.status_code == 200:
        # Store audio data in session state for future use
        st.session_state.audio_data = response.content

        # Create a BytesIO object for immediate playback
        audio_file = BytesIO(st.session_state.audio_data)
        audio_file.seek(0)
        st.audio(audio_file, format="audio/mpeg", loop=True)
    else:
        st.write("Error generating sound. Please try again.")

# Initialize audio library in session state if not already present
if "audio_library" not in st.session_state:
    st.session_state.audio_library = []

# Save Audio Button
if col2.button("Save Audio"):
    # Retrieve audio data from session state
    if "audio_data" in st.session_state and st.session_state.audio_data:
        st.session_state.audio_library.append({
            "audio_data": st.session_state.audio_data  # Store raw binary data
        })
        st.success("Audio saved to library!")
    else:
        st.write("No audio to save. Generate music first.")