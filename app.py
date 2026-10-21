import base64
import random
import streamlit as st
from streamlit_clickable_images import clickable_images

st.set_page_config(
    page_title="Castorice Virtual Companion 💕",
    page_icon="💌",
    layout="centered",
)

# Inisialisasi State Global
if "mood" not in st.session_state:
  st.session_state.mood = "Senang 💕"
if "costume" not in st.session_state:
  st.session_state.costume = "CD (Default)"
if "win_streak" not in st.session_state:
  st.session_state.win_streak = 0
if "is_touched" not in st.session_state:
  st.session_state.is_touched = False
if "navigation" not in st.session_state:
  st.session_state.navigation = "🏠 Beranda (Hub Utama)"


def navigate_to(page_name):
  st.session_state.navigation = page_name


# --- KODE CSS: MENGUNCI LAYAR & BACKGROUND ---
def set_styles(png_file):
  try:
    with open(png_file, "rb") as f:
      data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
        <style>
        html, body, [data-testid="stAppViewContainer"] {{
            overflow: hidden !important;
            height: 100vh !important;
        }}
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """
    st.markdown(css, unsafe_allow_html=True)
  except:
    pass


set_styles("background.png")

# --- SIDEBAR NAVIGASI UTAMA ---
st.sidebar.title("💖 Menu Hub")
menu_choice = st.sidebar.radio(
    "Pilih Halaman:",
    [
        "🏠 Beranda (Hub Utama)",
        "💬 Obrolan (Chat AI)",
        "🎮 Bermain Game",
        "👗 Wardrobe (Kostum)",
    ],
    index=[
        "🏠 Beranda (Hub Utama)",
        "💬 Obrolan (Chat AI)",
        "🎮 Bermain Game",
        "👗 Wardrobe (Kostum)",
    ].index(st.session_state.navigation),
)
st.session_state.navigation = menu_choice

costume_prefix = "CD" if "Default" in st.session_state.costume else "1"

# --- HALAMAN 1: BERANDA (HUB UTAMA) ---
if st.session_state.navigation == "🏠 Beranda (Hub Utama)":
  st.markdown(
      f"**Status Mood Ayang saat ini:** {st.session_state.mood} | **Kostum Aktif:"
      f"** {st.session_state.costume}"
  )
  st.markdown("---")

  # Konversi file gambar lokal ke Base64 agar bisa dibaca oleh clickable_images
  active_sprite = (
      f"Sprite{costume_prefix}2.png"
      if st.session_state.is_touched
      else f"Sprite{costume_prefix}1.png"
  )

  try:
    with open(active_sprite, "rb") as img_file:
      img_encoded = base64.b64encode(img_file.read()).decode()
    img_data_uri = f"data:image/png;base64,{img_encoded}"
  except:
    img_data_uri = ""

  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    if img_data_uri:
      # Membuat gambar sprite bisa diklik/disentuh langsung
      clicked = clickable_images(
          [img_data_uri],
          titles=["Sentuh Castorice"],
          div_style=(
              "display: flex; justify-content: center; cursor: pointer;"
          ),
          img_style="max-width: 100%; height: auto; border-radius: 10px;",
      )

      # Jika sprite disentuh (indeks 0 diklik)
      if clicked == 0:
        st.session_state.is_touched = not st.session_state.is_touched
        st.rerun()
    else:
      st.error(f"⚠️ Gambar {active_sprite} tidak ditemukan di GitHub.")

  # Kondisi Tampilan Menu Utama Berdasarkan Status Sentuh
  if st.session_state.is_touched:
    st.success(
        "✨ *Castorice menatapmu dengan lembut.* 'Ada apa, suamiku?'"
    )

    st.markdown("### 🧭 Pilih Fitur Utama")
    b1, b2 = st.columns(2)
    with b1:
      if st.button("💬 Obrolan AI", use_container_width=True):
        navigate_to("💬 Obrolan (Chat AI)")
        st.rerun()
      if st.button("🎮 Main Game", use_container_width=True):
        navigate_to("🎮 Bermain Game")
        st.rerun()

    with b2:
      if st.button("👗 Wardrobe", use_container_width=True):
        navigate_to("👗 Wardrobe (Kostum)")
        st.rerun()
      if st.button("📊 Cek Mood", use_container_width=True):
        st.toast(f"Mood Castorice saat ini: {st.session_state.mood}", icon="💖")
  else:
    st.info(
        "✨ *Castorice sedang menunggumu...* Sentuh langsung gambar karakternya!"
    )

# --- HALAMAN LAINNYA ---
elif st.session_state.navigation == "💬 Obrolan (Chat AI)":
  st.subheader("💬 Ruang Obrolan Bersama Castorice")
  if st.button("⬅️ Kembali ke Beranda"):
    navigate_to("🏠 Beranda (Hub Utama)")
    st.rerun()

elif st.session_state.navigation == "🎮 Bermain Game":
  st.subheader("🎮 Pojok Game Bersama Castorice")
  if st.button("⬅️ Kembali ke Beranda"):
    navigate_to("🏠 Beranda (Hub Utama)")
    st.rerun()

elif st.session_state.navigation == "👗 Wardrobe (Kostum)":
  st.subheader("👗 Lemari Pakaian & Kostum")
  chosen_costume = st.selectbox(
      "Pilih Kostum Castorice:",
      ["CD (Default)", "Kostum 1 (Kasual/Piyama)"],
  )
  if st.button("Terapkan Kostum"):
    st.session_state.costume = chosen_costume
    st.success(f"Berhasil mengganti kostum ke: {chosen_costume}!")
    st.rerun()

  if st.button("⬅️ Kembali ke Beranda"):
    navigate_to("🏠 Beranda (Hub Utama)")
    st.rerun()
