import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(1)

for i in range(10):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラムです')


expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の内容')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の内容')
# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：', text

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition

# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )

# 'あなたの好きな数字は、', option,'です。'


# if st.checkbox('Show Image'):
#     img = Image.open('cat.jpeg')
#     st.image(img, caption='cat', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns=['lat','lon']
# )

# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# st.map(df)