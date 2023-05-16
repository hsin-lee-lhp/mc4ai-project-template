import streamlit as st
from graph import box,histogram,pie
from dataframe import df

def score():                                
    s_names = ('S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','GPA')
    s = st.radio('Điểm từng session',s_names,horizontal=True)
    if s == 'S1':
        box(df,'CLASS-GROUP','S1','GENDER')
        histogram(df,'S1',None,'PYTHON-CLASS')
    
    if s == 'S2':
        box(df,'CLASS-GROUP','S2','GENDER')
        histogram(df,'S2',None,'PYTHON-CLASS')

    if s == 'S3':
        box(df,'CLASS-GROUP','S3','GENDER')
        histogram(df,'S3',None,'PYTHON-CLASS')    
    if s == 'S4':
        box(df,'CLASS-GROUP','S4','GENDER')
        histogram(df,'S4',None,'PYTHON-CLASS')

    if s == 'S5':
        box(df,'CLASS-GROUP','S5','GENDER')
        histogram(df,'S5',None,'PYTHON-CLASS')

    if s == 'S6':
        box(df,'CLASS-GROUP','S6','GENDER')
        histogram(df,'S6',None,'PYTHON-CLASS')

    if s == 'S7':
        box(df,'CLASS-GROUP','S7','GENDER')
        histogram(df,'S7',None,'PYTHON-CLASS')    

    if s == 'S8':
        box(df,'CLASS-GROUP','S8','GENDER')
        histogram(df,'S8',None,'PYTHON-CLASS')   

    if s == 'S9':
        box(df,'CLASS-GROUP','S9','GENDER')
        histogram(df,'S9',None,'PYTHON-CLASS')    

    if s == 'S10':
        box(df,'CLASS-GROUP','S10','GENDER')
        histogram(df,'S10',None,'PYTHON-CLASS')  

    if s == 'GPA':
        box(df,'CLASS-GROUP','GPA',None)
        st.success('Các lớp khối tự nhiên học tốt hơn lớp khối xã hội')
        st.success('Lớp Chuyên Tin học giỏi nhất')
        box(df,'PYTHON-CLASS','GPA',None)
        st.success('Lớp 114 học tốt hơn lớp 115')
        histogram(df,'GPA',None,'GENDER')
        st.success('Nam sinh học tốt hơn nữ sinh')
        pie(df[df['GPA'] >= 6],'CLASS-GROUP','Tỉ lệ đậu lớp MC')
def graph():
    a_names = ('PHÂN BỐ HS NAM - NỮ','PHÂN BỐ HS LỚP SÁNG - CHIỀU','PHÂN BỐ HS CHUYÊN - THƯỜNG','PHÂN BỐ HS CÁC KHỐI')
    a = st.radio('Loại biểu đồ',a_names,horizontal=True)
    if a=='PHÂN BỐ HS NAM - NỮ':
        pie(df, df["GENDER"],"PHÂN BỐ HS NAM - NỮ")
        st.write('Nam hứng thú với AI hơn')
    if a=='PHÂN BỐ HS LỚP SÁNG - CHIỀU':
        pie(df, df["PYTHON-CLASS"],"PHÂN BỐ HS LỚP SÁNG CHIỀU")
        st.write('Học sinh lớp sáng chiều phân bố khá đồng đều')
    if a=='PHÂN BỐ HS CHUYÊN - THƯỜNG':
        pie(df, df["CLASS-GROUP"],"PHÂN BỐ HS CHUYÊN - THƯỜNG")
        st.write('Học sinh lớp chuyên có hứng thú với AI hơn')
    if a=='PHÂN BỐ HS CÁC KHỐI':
        pie(df, df["GRADE"],"PHÂN BỐ HS CÁC KHỐI")
        st.write("Học sinh lớp 12 ít có số lượng đăng kí học AI ít nhất do bận ôn thi THPTQG")
