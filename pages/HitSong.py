import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import settings
import streamlit as st

client_id = settings.client_id
client_secret = settings.client_secret

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# yearのデフォルト値の設定
year = 2022
st.text('年代を半角で入力してくだい')
year=st.text_input('年代：2022')
results = sp.search(q=(f'year:{year}'), limit=50, offset=0, type='track', market='JP')
for idx, track in enumerate(results['tracks']['items']):
    st.text((idx, track['name']))

st.markdown('#### 参考記事')
st.markdown('1. [PythonのSpotify APIで指定したアーティストの人気曲を取得する \- Qiita](https://qiita.com/Prgckwb/items/21ec6cdbfa7fcf5aa466)')
st.markdown('2. [plamere/spotipy: Spotify Web API 用の軽量 Python ライブラリ](https://github.com/plamere/spotipy)')
st.markdown('3. [Web API Libraries \| Spotify for Developers](https://developer.spotify.com/documentation/web-api/libraries/#basic-snippets)')
st.markdown('4. [PythonでSpotify APIを使ってみる \| ハムレット型エンジニアのカンニングノート](https://www.hamlet-engineer.com/posts/spotify01.html#%E3%83%86%E3%82%99%E3%83%A2%E3%81%AE%E5%AE%9F%E8%A1%8C)')
st.markdown('5. [spotify APIを触ってるときのメモ](https://zenn.dev/arei/scraps/2c0f2db12ecf0c)')
