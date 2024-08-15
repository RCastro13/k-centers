import pandas as pd
from ucimlrepo import fetch_ucirepo 
from sklearn.datasets import fetch_openml

##PRIMEIRO DATASET

# # Fetch dataset
# rice_cammeo_and_osmancik = fetch_ucirepo(id=545)
# X = rice_cammeo_and_osmancik.data.features.Area
# y = rice_cammeo_and_osmancik.data.features.Perimeter
# label = rice_cammeo_and_osmancik.data.targets

# X = X.astype(int)
# y = y.astype(int)

# # Verificar se 'label' é uma Series e não um DataFrame
# if isinstance(label, pd.DataFrame):
#     label = label.squeeze()  # Converter DataFrame para Series se necessário

# # Criar um dicionário de mapeamento
# unique_labels = label.unique()
# label_dict = {lbl: idx for idx, lbl in enumerate(unique_labels)}

# # Converter os rótulos para valores numéricos
# label_numeric = label.map(label_dict)

# print(label_numeric)

# #Salvar X e Y em um arquivo txt com os rótulos numéricos
# with open("rice_cammeo_and_osmancik.txt", "w") as file:
#     for x_value, y_value, label_value in zip(X, y, label_numeric):
#         file.write(f"{x_value} {y_value} {label_value}\n")

# print("Data saved to rice_cammeo_and_osmancik.txt")

# #Print metadata and variable information
# print(rice_cammeo_and_osmancik.metadata)
# print(rice_cammeo_and_osmancik.variables)


##SEGUNDO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition = fetch_ucirepo(id=544) 
  
# # data (as pandas dataframes) 
# X = estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.data.features.Age
# y = estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.data.features.Height
# label = estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.data.targets

# X = X.astype(int)
# y = y.astype(int)

# # Verificar se 'label' é uma Series e não um DataFrame
# if isinstance(label, pd.DataFrame):
#     label = label.squeeze()  # Converter DataFrame para Series se necessário

# # Criar um dicionário de mapeamento
# unique_labels = label.unique()
# label_dict = {lbl: idx for idx, lbl in enumerate(unique_labels)}

# # Converter os rótulos para valores numéricos
# label_numeric = label.map(label_dict)

# # print(label_numeric)

# num_unique_labels = label.nunique()
# print("Quantidade de valores diferentes em 'label':", num_unique_labels)

# #Salvar X e Y em um arquivo txt com os rótulos numéricos
# with open("estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.txt", "w") as file:
#     for x_value, y_value, label_value in zip(X, y, label_numeric):
#         file.write(f"{x_value} {y_value} {label_value}\n")
  
# # metadata 
# #print(estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.metadata) 
  
# # variable information 
# print(estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.variables) 

##TERCEIRO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# hepatitis_c_virus_hcv_for_egyptian_patients = fetch_ucirepo(id=503) 
# print(hepatitis_c_virus_hcv_for_egyptian_patients.variables)
  
# # data (as pandas dataframes) 
# X = hepatitis_c_virus_hcv_for_egyptian_patients.data.features.WBC 
# y = hepatitis_c_virus_hcv_for_egyptian_patients.data.features.BMI
# label = hepatitis_c_virus_hcv_for_egyptian_patients.data.targets 

# X = X.astype(int)
# y = y.astype(int)

# # Verificar se 'label' é uma Series e não um DataFrame
# if isinstance(label, pd.DataFrame):
#     label = label.squeeze()  # Converter DataFrame para Series se necessário

# # Criar um dicionário de mapeamento
# unique_labels = label.unique()
# label_dict = {lbl: idx for idx, lbl in enumerate(unique_labels)}

# # Converter os rótulos para valores numéricos
# label_numeric = label.map(label_dict)

# # print(label_numeric)

# num_unique_labels = label.nunique()
# print("Quantidade de valores diferentes em 'label':", num_unique_labels)

# #Salvar X e Y em um arquivo txt com os rótulos numéricos
# with open("hepatitis_c_virus_hcv_for_egyptian_patients.txt", "w") as file:
#     for x_value, y_value, label_value in zip(X, y, label_numeric):
#         file.write(f"{x_value} {y_value} {label_value}\n")
  
# # metadata 
# print(hepatitis_c_virus_hcv_for_egyptian_patients.metadata) 
  
# variable information 
# print(hepatitis_c_virus_hcv_for_egyptian_patients.variables) 


##QUARTO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# yeast = fetch_ucirepo(id=110) 
  
# # data (as pandas dataframes) 
# X = yeast.data.features.mcg
# y = yeast.data.features.gvh
# label = yeast.data.targets

# # X = X.astype(int)
# # y = y.astype(int)

# # Verificar se 'label' é uma Series e não um DataFrame
# if isinstance(label, pd.DataFrame):
#     label = label.squeeze()  # Converter DataFrame para Series se necessário

# # Criar um dicionário de mapeamento
# unique_labels = label.unique()
# label_dict = {lbl: idx for idx, lbl in enumerate(unique_labels)}

# # Converter os rótulos para valores numéricos
# label_numeric = label.map(label_dict)

# num_unique_labels = label.nunique()
# print("Quantidade de valores diferentes em 'label':", num_unique_labels)

# #print(label_numeric)

# #Salvar X e Y em um arquivo txt com os rótulos numéricos
# with open("yeast.txt", "w") as file:
#     for x_value, y_value, label_value in zip(X, y, label_numeric):
#         file.write(f"{x_value} {y_value} {label_value}\n")

# print(X)
# print(y)
  
# # metadata 
# #print(yeast.metadata) 
  
# # variable information 
# print(yeast.variables) 

##QUINTO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# banknote_authentication = fetch_ucirepo(id=267) 
  
# # data (as pandas dataframes) 
# X = banknote_authentication.data.features.variance
# y = banknote_authentication.data.features.skewness
# label = banknote_authentication.data.targets

# X = X.astype(int)
# y = y.astype(int)

# # Verificar se 'label' é uma Series e não um DataFrame
# if isinstance(label, pd.DataFrame):
#     label = label.squeeze()  # Converter DataFrame para Series se necessário

# # Criar um dicionário de mapeamento
# unique_labels = label.unique()
# label_dict = {lbl: idx for idx, lbl in enumerate(unique_labels)}

# # Converter os rótulos para valores numéricos
# label_numeric = label.map(label_dict)

# num_unique_labels = label.nunique()
# print("Quantidade de valores diferentes em 'label':", num_unique_labels)

# #print(label_numeric)

# #Salvar X e Y em um arquivo txt com os rótulos numéricos
# with open("banknote_authentication.txt", "w") as file:
#     for x_value, y_value, label_value in zip(X, y, label_numeric):
#         file.write(f"{x_value} {y_value} {label_value}\n")
  
# # metadata 
# #print(banknote_authentication.metadata) 
  
# # variable information 
# print(banknote_authentication.variables) 

##SEXTO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# waveform_database_generator_version_1 = fetch_ucirepo(id=107) 
  
# # data (as pandas dataframes) 
# X = waveform_database_generator_version_1.data.features.Attribute1
# y = waveform_database_generator_version_1.data.features.Attribute2
# label = waveform_database_generator_version_1.data.targets

# X = X.astype(int)
# y = y.astype(int)

# # Verificar se 'label' é uma Series e não um DataFrame
# if isinstance(label, pd.DataFrame):
#     label = label.squeeze()  # Converter DataFrame para Series se necessário

# # Criar um dicionário de mapeamento
# unique_labels = label.unique()
# label_dict = {lbl: idx for idx, lbl in enumerate(unique_labels)}

# # Converter os rótulos para valores numéricos
# label_numeric = label.map(label_dict)

# num_unique_labels = label.nunique()
# print("Quantidade de valores diferentes em 'label':", num_unique_labels)

# #print(label_numeric)

# #Salvar X e Y em um arquivo txt com os rótulos numéricos
# with open("waveform_database_generator_version_1.txt", "w") as file:
#     for x_value, y_value, label_value in zip(X, y, label_numeric):
#         file.write(f"{x_value} {y_value} {label_value}\n")
  
# # metadata 
# #print(waveform_database_generator_version_1.metadata) 
  
# # variable information 
# print(waveform_database_generator_version_1.variables) 

##SETIMO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# statlog_landsat_satellite = fetch_ucirepo(id=146) 
  
# # data (as pandas dataframes) 
# X = statlog_landsat_satellite.data.features.Attribute31
# y = statlog_landsat_satellite.data.features.Attribute32
# label = statlog_landsat_satellite.data.targets 

# X = X.astype(int)
# y = y.astype(int)

# # Verificar se 'label' é uma Series e não um DataFrame
# if isinstance(label, pd.DataFrame):
#     label = label.squeeze()  # Converter DataFrame para Series se necessário

# # Criar um dicionário de mapeamento
# unique_labels = label.unique()
# label_dict = {lbl: idx for idx, lbl in enumerate(unique_labels)}

# # Converter os rótulos para valores numéricos
# label_numeric = label.map(label_dict)

# num_unique_labels = label.nunique()
# print("Quantidade de valores diferentes em 'label':", num_unique_labels)

# #print(label_numeric)

# #Salvar X e Y em um arquivo txt com os rótulos numéricos
# with open("statlog_landsat_satellite.txt", "w") as file:
#     for x_value, y_value, label_value in zip(X, y, label_numeric):
#         file.write(f"{x_value} {y_value} {label_value}\n")
  
# # metadata 
# print(statlog_landsat_satellite.metadata) 
  
# # variable information 
# print(statlog_landsat_satellite.variables) 


##OITAVO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# absenteeism_at_work = fetch_ucirepo(id=445) 
  
# # data (as pandas dataframes) 
# X = absenteeism_at_work.data.features.Son 
# y = absenteeism_at_work.data.features.Pet
# label = absenteeism_at_work.data.targets

# X = X.astype(int)
# y = y.astype(int)

# # Verificar se 'label' é uma Series e não um DataFrame
# if isinstance(label, pd.DataFrame):
#     label = label.squeeze()  # Converter DataFrame para Series se necessário

# # Criar um dicionário de mapeamento
# unique_labels = label.unique()
# label_dict = {lbl: idx for idx, lbl in enumerate(unique_labels)}

# # Converter os rótulos para valores numéricos
# label_numeric = label.map(label_dict)

# num_unique_labels = label.nunique()
# print("Quantidade de valores diferentes em 'label':", num_unique_labels)

# #print(label_numeric)

# #Salvar X e Y em um arquivo txt com os rótulos numéricos
# with open("absenteeism_at_work.txt", "w") as file:
#     for x_value, y_value, label_value in zip(X, y, label_numeric):
#         file.write(f"{x_value} {y_value} {label_value}\n")
  
# # metadata 
# #print(absenteeism_at_work.metadata) 
  
# # variable information 
# print(absenteeism_at_work.variables) 

##NONO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# annealing = fetch_ucirepo(id=3) 
  
# # data (as pandas dataframes) 
# X = annealing.data.features.thick
# y = annealing.data.features.width
# label = annealing.data.targets 

# # X = X.astype(int)
# # y = y.astype(int)

# # Verificar se 'label' é uma Series e não um DataFrame
# if isinstance(label, pd.DataFrame):
#     label = label.squeeze()  # Converter DataFrame para Series se necessário

# # Criar um dicionário de mapeamento
# unique_labels = label.unique()
# label_dict = {lbl: idx for idx, lbl in enumerate(unique_labels)}

# # Converter os rótulos para valores numéricos
# label_numeric = label.map(label_dict)

# num_unique_labels = label.nunique()
# print("Quantidade de valores diferentes em 'label':", num_unique_labels)

# #print(label_numeric)

# #Salvar X e Y em um arquivo txt com os rótulos numéricos
# with open("annealing.txt", "w") as file:
#     for x_value, y_value, label_value in zip(X, y, label_numeric):
#         file.write(f"{x_value} {y_value} {label_value}\n")
  
# # metadata 
# #print(annealing.metadata) 
  
# # variable information 
# print(annealing.variables) 

##DECIMO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# wine_quality = fetch_ucirepo(id=186) 
  
# # data (as pandas dataframes) 
# X = wine_quality.data.features.chlorides
# y = wine_quality.data.features.pH
# label =  wine_quality.data.targets
# # X = X.astype(int)
# # y = y.astype(int)

# # Verificar se 'label' é uma Series e não um DataFrame
# if isinstance(label, pd.DataFrame):
#     label = label.squeeze()  # Converter DataFrame para Series se necessário

# # Criar um dicionário de mapeamento
# unique_labels = label.unique()
# label_dict = {lbl: idx for idx, lbl in enumerate(unique_labels)}

# # Converter os rótulos para valores numéricos
# label_numeric = label.map(label_dict)

# num_unique_labels = label.nunique()
# print("Quantidade de valores diferentes em 'label':", num_unique_labels)

# #print(label_numeric)

# #Salvar X e Y em um arquivo txt com os rótulos numéricos
# with open("wine_quality.txt", "w") as file:
#     for x_value, y_value, label_value in zip(X, y, label_numeric):
#         file.write(f"{x_value} {y_value} {label_value}\n")
  
  
# metadata 
#print(wine_quality.metadata) 
  
# variable information 
#print(wine_quality.variables) 

##EXTRA
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
statlog_german_credit_data = fetch_ucirepo(id=144) 
  
# data (as pandas dataframes) 
X = statlog_german_credit_data.data.features.Attribute2
y = statlog_german_credit_data.data.features.Attribute13
label = statlog_german_credit_data.data.targets 

# X = X.astype(int)
# y = y.astype(int)

# Verificar se 'label' é uma Series e não um DataFrame
if isinstance(label, pd.DataFrame):
    label = label.squeeze()  # Converter DataFrame para Series se necessário

# Criar um dicionário de mapeamento
unique_labels = label.unique()
label_dict = {lbl: idx for idx, lbl in enumerate(unique_labels)}

# Converter os rótulos para valores numéricos
label_numeric = label.map(label_dict)

num_unique_labels = label.nunique()
print("Quantidade de valores diferentes em 'label':", num_unique_labels)

#print(label_numeric)

#Salvar X e Y em um arquivo txt com os rótulos numéricos
with open("statlog_german_credit_data.txt", "w") as file:
    for x_value, y_value, label_value in zip(X, y, label_numeric):
        file.write(f"{x_value} {y_value} {label_value}\n")
  
# metadata 
print(statlog_german_credit_data.metadata) 
  
# variable information 
print(statlog_german_credit_data.variables) 

