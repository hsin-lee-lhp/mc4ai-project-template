import pandas as pd
df = pd.read_csv('py4ai-score.csv')
df['S1'].fillna(0, inplace=True)  
df['S2'].fillna(0, inplace=True)  
df['S3'].fillna(0, inplace=True)  
df['S4'].fillna(0, inplace=True)  
df['S5'].fillna(0, inplace=True)  
df['S6'].fillna(0, inplace=True)  
df['S7'].fillna(0, inplace=True)  
df['S8'].fillna(0, inplace=True)  
df['S9'].fillna(0, inplace=True)  
df['S10'].fillna(0, inplace=True)  
df['BONUS'].fillna(0, inplace=True)  
df['REG-MC4AI'].fillna('N', inplace=True)  

class_mapping = {
        '10CT1': 'Chuyên Toán',
        '10CT2': 'Chuyên Toán',
        '11CT1': 'Chuyên Toán',
        '11CT2': 'Chuyên Toán',
        '11CT3': 'Chuyên Toán',
        '10CTIN': 'Chuyên Tin',
        '10CL1': 'Chuyên Lý',
        '10CL2': 'Chuyên Lý',
        '10CA1': 'Chuyên Anh',
        '10CA2': 'Chuyên Anh',
        '11CA3': 'Chuyên Anh',
        '10CV1': 'Chuyên Văn',
        '10CV2': 'Chuyên Văn',
        '10CSD': 'Chuyên Sử Địa',
        '11CSD': 'Chuyên Sử Địa',
        '10TH1': 'Tích Hợp',
        '10TH2': 'Tích Hợp',
        '10SN': 'Song Ngữ',
        '10CH2': 'Chuyên Hóa',
        '12CH1': 'Chuyên Hóa',
        '10CTRN': 'Chuyên Trung Nhật',
        '10A1': 'Khác',
        '10A2': 'Khác',
        '10A3': 'Khác',
        '11A': 'Khác',
        '11B': 'Khác',
        
    }

df['CLASS-GROUP'] = df['CLASS'].map(class_mapping)


class_mapping1 = {
        '10CT1': 'Lớp 10',
        '10CT2': 'Lớp 10',
        '11CT1': 'Lớp 11',
        '11CT2': 'Lớp 11',
        '11CT3': 'Lớp 11',
        '10CTIN': 'Lớp 10',
        '10CL1': 'Lớp 10',
        '10CL2': 'Lớp 10',
        '10CA1': 'Lớp 10',
        '10CA2': 'Lớp 10',
        '11CA3': 'Lớp 11',
        '10CV1': 'Lớp 10',
        '10CV2': 'Lớp 10',
        '10CSD': 'Lớp 10',
        '11CSD': 'Lớp 11',
        '10TH1': 'Lớp 10',
        '10TH2': 'Lớp 10',
        '10SN': 'Lớp 10',
        '10CH2': 'Lớp 10',
        '12CH1': 'Lớp 12',
        '10CTRN': 'Lớp 10',
        '10A1': 'Lớp 10',
        '10A2': 'Lớp 10',
        '10A3': 'Lớp 10',
        '11A': 'Lớp 11',
        '11B': 'Lớp 11',
        
    }

df['GRADE'] = df['CLASS-GROUP'].map(class_mapping1)
