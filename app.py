import base64
import random
import streamlit as st

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


# --- KODE CSS: BACKGROUND & MENGUNCI SCROLL AGAR TIDAK BISA DIGULIR ---
def set_styles(png_file):
  try:
    with open(png_file, "rb") as f:
      data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
        <style>
        /* Mengunci halaman agar tidak bisa scroll ke bawah */
        html, body, [data-testid="stAppViewContainer"] {{
            overflow: hidden !important;
            height: 100vh !important;
        }}
        
        /* Mengatur background agar pas di layar HP */
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

  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    sprite_filename = (
        f"Sprite{costume_prefix}2.png"
        if st.session_state.is_touched
        else f"Sprite{costume_prefix}1.png"
    )
    try:
      st.image(sprite_filename, use_container_width=True)
    except:
      st.info(
          f"⚠️ Gambar {sprite_filename} belum di-upload di repository GitHub."
      )

    # Menggunakan tombol interaktif tepat di bawah sprite sebagai pemicu sentuh
    touch_label = (
        "✨ Sentuh lagi untuk merapikan"
        if st.session_state.is_touched
        else "👆 Sentuh Castorice"
    )
    if st.button(touch_label, use_container_width=True, type="primary"):
      st.session_state.is_touched = not st.session_state.is_touched
      st.rerun()

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
        "✨ *Castorice sedang menunggumu...* Sentuh tombol di atas untuk"
        " berinteraksi!"
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
