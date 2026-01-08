import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="My YouTube Downloader", page_icon="🎥")
st.title("🎥 Universal Video Downloader")
st.write("Paste a link below to download it to your device!")

url = st.text_input("Enter YouTube URL:", placeholder="https://www.youtube.com/...")

if st.button("Prepare Download"):
    if url:
        with st.spinner("Downloading to our server first... please wait."):
            try:
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': 'video.mp4', 
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                with open("video.mp4", "rb") as file:
                    st.download_button(
                        label="📥 Click here to Save to Gallery",
                        data=file,
                        file_name="my_video.mp4",
                        mime="video/mp4"
                    )
                st.success("Success! Use the button above to save the file.")
                os.remove("video.mp4") 
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please paste a link first!")