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


# --- FUNGSI AGAR BACKGROUND.PNG MUNCUL DENGAN SEMPURNA ---
def set_background(png_file):
  try:
    with open(png_file, "rb") as f:
      data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
        <style>
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


# Terapkan background
set_background("background.png")

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

# Tentukan awalan penamaan file berdasarkan kostum aktif
costume_prefix = "CD" if "Default" in st.session_state.costume else "1"

# --- HALAMAN 1: BERANDA (HUB UTAMA) ---
if st.session_state.navigation == "🏠 Beranda (Hub Utama)":
  # Teks judul besar sudah dihapus sesuai permintaan
  st.markdown(
      f"**Status Mood Ayang saat ini:** {st.session_state.mood} | **Kostum Aktif:"
      f"** {st.session_state.costume}"
  )
  st.markdown("---")

  # Tampilkan Sprite Berdasarkan Status Sentuh
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

    # Tombol interaksi menyentuh sprite
    touch_label = (
        "✨ Sentuh lagi untuk merapikan"
        if st.session_state.is_touched
        else "👆 Sentuh Castorice"
    )
    if st.button(touch_label, use_container_width=True, type="primary"):
      st.session_state.is_touched = not st.session_state.is_touched
      st.rerun()

  # Kondisi Tampilan Berdasarkan Apakah Sudah Disentuh atau Belum
  if st.session_state.is_touched:
    st.success(
        "✨ *Castorice menatapmu dengan lembut dan merona.* 'Ada apa, suamiku?'"
    )

    st.markdown("### 🧭 Pilih Fitur Utama")
    # 4 Tombol Opsi HANYA MUNCUL JIKA SUDAH DISENTUH (Sprite 2)
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
        "✨ *Castorice sedang diam menunggumu...* Sentuh tombol di atas untuk"
        " berinteraksi dengannya dan membuka menu!"
    )

# --- HALAMAN 2: OBROLAN (CHAT AI) ---
elif st.session_state.navigation == "💬 Obrolan (Chat AI)":
  st.subheader("💬 Ruang Obrolan Bersama Castorice")
  st.write(
      f"Stiker aktif menggunakan set: **Stiker{costume_prefix}X.png** sesuai"
      " kostum."
  )
  if st.button("⬅️ Kembali ke Beranda"):
    navigate_to("🏠 Beranda (Hub Utama)")
    st.rerun()

# --- HALAMAN 3: BERMAIN GAME ---
elif st.session_state.navigation == "🎮 Bermain Game":
  st.subheader("🎮 Pojok Game Bersama Castorice")
  st.write(
      f"Streak kemenanganmu saat ini: {st.session_state.win_streak} kali"
      " berturut-turut."
  )
  if st.button("Simulasi Menang Game (+1 Streak)"):
    st.session_state.win_streak += 1
    if st.session_state.win_streak >= 5:
      st.session_state.mood = "Ngambek 💢"
      st.warning("Kamu menang 5x berturut-turut! Castorice ngambek manja.")
    else:
      st.success("Kamu menang! Castorice tersenyum bangga.")
    st.rerun()

  if st.button("⬅️ Kembali ke Beranda"):
    navigate_to("🏠 Beranda (Hub Utama)")
    st.rerun()

# --- HALAMAN 4: WARDROBE (KOSTUM) ---
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
