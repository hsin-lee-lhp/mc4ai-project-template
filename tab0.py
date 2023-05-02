import streamlit as st
from dataframe import df

def student_list():
    with st.container():
        col1,col2,col3,col4,col5 = st.columns(5)
        with col1:
            st.write('Giới tính')
            nam = st.checkbox('Nam')
            nu = st.checkbox('Nữ')
           
            if nam:
                pass
                # df2.append(df[['GENDER'] == 'M'],ignore_index=True) 
                
            if nu:
                pass
                # df2.append(df[df['GENDER'] == 'F'])
        with col2:
            grade_names = ('Tất cả','Lớp 10','Lớp 11','Lớp 12')
            grade = st.radio('Khối lớp',grade_names)
            
        with col3:
            room_names = ('Tất cả',
                    'A114',
                    'A115')
            room = st.selectbox('Phòng',options=room_names)
            if room == 'Tất cả':
                pass
            elif room == 'A114':
                pass
            else:
                pass
            
        with col4:
            buoi_names = ('Sáng','Chiều')
            buoi = st.selectbox('Buổi',buoi_names)
            
    st.write('Lớp chuyên')
    with st.container():
        col1b, col2b, col3b,col4b,col5b = st.columns(5)
        with col1b:
            van_cl = st.checkbox('Văn')
            toan_cl = st.checkbox('Toán')
        with col2b:
            ly_cl = st.checkbox('Lý')
            hoa_cl = st.checkbox('Hóa')
        with col3b:

            anh_cl = st.checkbox('Anh')
            tin_cl = st.checkbox('Tin')
        with col4b:
            
            su_dia_cl = st.checkbox('Sử Địa')
            trn_cl = st.checkbox('Trung Nhật')
        with col5b:
            th_sn_cl = st.checkbox('TH/SN')
            khac_cl = st.checkbox('Khác')
    st.write('Số HS')
    st.write('GPA cao nhất','thấp nhất','trung bình')
    st.dataframe(df)
    