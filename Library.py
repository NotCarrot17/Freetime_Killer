
import streamlit as st
from io import BytesIO

# Display saved images in a grid layout
st.subheader("Past Generated and Saved Images/Code/Audio.")
st.divider()

if "saved_images" in st.session_state and st.session_state.saved_images:
    num_columns = 3  # Define the number of columns for the grid
    images = st.session_state.saved_images
    for row_start in range(0, len(images), num_columns):
        # Generate a row with num_columns columns
        cols = st.columns(num_columns)
        for i, col in enumerate(cols):
            img_idx = row_start + i
            if img_idx < len(images):
                # Display the image in the current column
                col.image(images[img_idx], caption=f"Character {img_idx + 1}", width=200)
else:
    st.write("No images have been saved yet.")

st.divider()

# Saved Code Display with Expander and Error Handling
st.write("Generated Code:")
if "saved_codes" in st.session_state and st.session_state.saved_codes:
    genre_count = {}  # To track code indices per genre
    
    for idx, code_info in enumerate(st.session_state.saved_codes):
        # Check that each item is a dictionary with the expected keys
        if isinstance(code_info, dict) and "code" in code_info and "genre" in code_info:
            genre = code_info["genre"]
            code = code_info["code"]

            # Count codes by genre
            if genre not in genre_count:
                genre_count[genre] = 1
            else:
                genre_count[genre] += 1

            # Set expander title as "{Genre} - Code {count}"
            expander_title = f"{genre} - Code {genre_count[genre]}"
            
            # Create an expander for each code
            with st.expander(expander_title):
                st.code(code, language="html")  # Display code inside expander
        else:
            # Error message for unexpected format
            st.write("Unexpected data format in saved codes:", st.session_state.saved_codes)

else:
    st.write("No codes have been saved yet.")

st.divider()
st.write("Generated Music:")
if "audio_library" in st.session_state and st.session_state.audio_library:
    # Display each stored audio file with a playback option
    for idx, audio_entry in enumerate(st.session_state.audio_library):
        st.write(f"Audio {idx + 1}")
        audio_file = BytesIO(audio_entry["audio_data"])  # Recreate BytesIO for playback
        audio_file.seek(0)
        st.audio(audio_file, format="audio/mpeg", loop=False)
else:
    st.write("No audio has been saved yet.")