from matplotlib import image
from sqlalchemy import true
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title('Streamlit 入門')

st.write('プログレスバー表示')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)



left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容3')



# test = st.sidebar.text_input('あなたの趣味は？')
# 'あなたの趣味は', test , 'です'

# condition = st.sidebar.slider('あなたのコンディションは？：', 0, 100, 50)
# 'あなたのコンディションは', condition , 'です'



# test = st.text_input('あなたの趣味は？')

# 'あなたの趣味は', test , 'です'

# option = st.selectbox(
#     'input your favorite number:',
#     list(range(1,11))
# )

# 'あなたの好きな数字は', option, 'です'

# if st.checkbox('Show Image'):
#     img = Image.open('header1.jpg')
#     st.image(img, caption='Imanishi', use_column_width=true)


# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
# })

# df = pd.DataFrame(
#     np.random.rand(120,2)/[50, 50]+[35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.dataframe(df)

# st.dataframe(df.style.highlight_max(axis=0)  )

# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項
# ```
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """


# st.map(df)

