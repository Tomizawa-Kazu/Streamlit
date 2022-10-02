import streamlit as st

st.header('自己紹介')
st.text('作成者：Kazu\n'
        '生年月日：1999年10月14日\n'
        '趣味：バレーボール、ゲーム（最近はAPEX）、マニキュア\n'
        '持ってる資格：高等学校教諭一種免許状(工業)、ITパスポート\n')

st.write('触れたことのあるプログラミング言語と使用場面(書籍を活用したものも含む)')
st.markdown('1. Python(Flask,Django,FastAPI)')
st.text('画像アップロードサイト(Flask)、ブック評価サイト(Django)、TODOリスト(FastAPI)、\n'
        'マインスイーパーの作成')

st.markdown('2. Processing')
st.text('マインスイーパー、シューティングゲーム\n')

st.markdown('3. PHP')
st.text('Twitterのような掲示板、ショッピングカート\n')

st.markdown('4. C言語')
st.text('掃除ロボットの制御\n')

st.markdown('5. Visual Basic.net')
st.text('仕事のWCFとデスクトップアプリ作成\n')

st.markdown('6. Google Apps Script')
st.text('大学の卒業研究　研究室管理システムの作成\n')

st.write('簡単な経歴　詳しくは、サイドバーのCareer参照')
st.text('地元の工業高校に入学し、初めてプログラミングに触れる(当時C言語)\n'
        '3年生の課題研究で、モップ掛けするロボットの作成\n')
