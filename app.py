import random
import streamlit as st

st.set_page_config(
    page_title="Castorice Virtual Companion 💕",
    page_icon="💌",
    layout="centered",
)

# Inisialisasi State Global (Mood, Kostum, & Game Streak)
if "mood" not in st.session_state:
  st.session_state.mood = "Senang 💕"
if "costume" not in st.session_state:
  st.session_state.costume = "Default"
if "win_streak" not in st.session_state:
  st.session_state.win_streak = 0

# --- HEADER / HOME SALUTATION ---
st.title("💖 Castorice Virtual Companion")
st.markdown(f"**Status Mood Ayang saat ini:** {st.session_state.mood}")
st.markdown(f"**Kostum Aktif:** {st.session_state.costume}")
st.markdown("---")

# --- MENU NAVIGASI UTAMA ---
menu = st.sidebar.selectbox(
    "Pilih Menu Hub",
    [
        "🏠 Beranda (Hub Utama)",
        "💬 Obrolan (Chat AI)",
        "🎮 Bermain Game",
        "👗 Wardrobe (Kostum)",
    ],
)

if menu == "🏠 Beranda (Hub Utama)":
  st.subheader("Selamat datang kembali, suamiku! ✨")
  st.write(
      "Ini adalah rumah kita. Pilih menu di sebelah kiri untuk mulai"
      " berinteraksi dengan Castorice."
  )

  # Tampilan sambutan berdasarkan mood
  if "Senang" in st.session_state.mood:
    st.info(
        "Castorice menyambutmu dengan senyuman manis dan tatapan penuh kasih"
        " sayang."
    )
  elif "Ngambek" in st.session_state.mood:
    st.warning(
        "Castorice melipat kedua tangannya di dada dan sedikit cemberut"
        " manja..."
    )
  else:
    st.success("Castorice sedang membaca buku dengan tenang di dekat jendela.")

elif menu == "💬 Obrolan (Chat AI)":
  st.subheader("💬 Ruang Obrolan")
  st.write("Fitur obrolan dengan stiker kustom akan diaktifkan di sini.")

elif menu == "🎮 Bermain Game":
  st.subheader("🎮 Pojok Game Bersama Castorice")
  st.write("Pilih game favorit kalian: Tic-Tac-Toe atau Catur Mini.")
  st.write(
      f"Streak kemenanganmu saat ini: {st.session_state.win_streak} kali"
      " berturut-turut."
  )
  if st.button("Simulasi Menang Game (+1 Streak)"):
    st.session_state.win_streak += 1
    if st.session_state.win_streak >= 5:
      st.session_state.mood = "Ngambek 💢"
      st.warning(
          "Kamu menang 5x berturut-turut! Castorice mulai ngambek karena kamu"
          " terlalu serius bermain!"
      )
    else:
      st.success("Kamu menang! Castorice tersenyum bangga padamu.")
    st.rerun()

elif menu == "👗 Wardrobe (Kostum)":
  st.subheader("👗 Lemari Pakaian & Kostum")
  st.write(
      "Ganti kostum Castorice di sini untuk mengubah set stiker di obrolan!"
  )

  chosen_costume = st.selectbox(
      "Pilih Kostum Castorice:", ["Default", "Kostum 1 (Kasual/Piyama)"]
  )
  if st.button("Terapkan Kostum"):
    st.session_state.costume = chosen_costume
    st.success(f"Berhasil mengganti kostum ke: {chosen_costume}!")
    st.rerun()
