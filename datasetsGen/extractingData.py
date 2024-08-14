import pandas as pd
from ucimlrepo import fetch_ucirepo 

##PRIMEIRO DATASET

# # fetch dataset 
# rice_cammeo_and_osmancik = fetch_ucirepo(id=545) 
# X = rice_cammeo_and_osmancik.data.features.Area
# y = rice_cammeo_and_osmancik.data.features.Perimeter

# print(X)
# print(y)

# # Save X and Y to a text file as points
# with open("rice_cammeo_and_osmancik.txt", "w") as file:
#     for x_value, y_value in zip(X, y):
#         file.write(f"{x_value} {y_value}\n")

# print("Data saved to points.txt")

# # # metadata 
# # print(rice_cammeo_and_osmancik.metadata) 
  
# # # variable information 
# # print(rice_cammeo_and_osmancik.variables) 

##SEGUNDO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition = fetch_ucirepo(id=544) 
  
# # data (as pandas dataframes) 
# X = estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.data.features.Age
# y = estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.data.features.Height

# print(X)
# print(y)

# # Save X and Y to a text file as points
# with open("estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.txt", "w") as file:
#     for x_value, y_value in zip(X, y):
#         file.write(f"{x_value} {y_value}\n")
  
# # metadata 
# #print(estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.metadata) 
  
# # variable information 
# print(estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.variables) 

##TERCEIRO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# concrete_compressive_strength = fetch_ucirepo(id=165) 
  
# # data (as pandas dataframes) 
# X = concrete_compressive_strength.data.features.Cement
# y = concrete_compressive_strength.data.features.Water

# print(X)
# print(y)

# # Save X and Y to a text file as points
# with open("concrete_compressive_strength.txt", "w") as file:
#     for x_value, y_value in zip(X, y):
#         file.write(f"{x_value} {y_value}\n")
  
# # metadata 
# #print(concrete_compressive_strength.metadata) 
  
# # variable information 
# print(concrete_compressive_strength.variables) 

##QUARTO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# yeast = fetch_ucirepo(id=110) 
  
# # data (as pandas dataframes) 
# X = yeast.data.features.mcg
# y = yeast.data.features.gvh

# # Save X and Y to a text file as points
# with open("yeast.txt", "w") as file:
#     for x_value, y_value in zip(X, y):
#         file.write(f"{x_value} {y_value}\n")

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

# print(X)
# print(y)

# # Save X and Y to a text file as points
# with open("banknote_authentication.txt", "w") as file:
#     for x_value, y_value in zip(X, y):
#         file.write(f"{x_value} {y_value}\n")
  
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

# print(X)
# print(y)

# # Save X and Y to a text file as points
# with open("waveform_database_generator_version_1.txt", "w") as file:
#     for x_value, y_value in zip(X, y):
#         file.write(f"{x_value} {y_value}\n")
  
# # metadata 
# #print(waveform_database_generator_version_1.metadata) 
  
# # variable information 
# print(waveform_database_generator_version_1.variables) 

##SETIMO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# drug_consumption_quantified = fetch_ucirepo(id=373) 
  
# # data (as pandas dataframes) 
# X = drug_consumption_quantified.data.features.age
# y = drug_consumption_quantified.data.features.nscore

# print(X)
# print(y)

# # Save X and Y to a text file as points
# with open("drug_consumption_quantified.txt", "w") as file:
#     for x_value, y_value in zip(X, y):
#         file.write(f"{x_value} {y_value}\n")
  
# # metadata 
# #print(drug_consumption_quantified.metadata) 
  
# # variable information 
# print(drug_consumption_quantified.variables) 

##OITAVO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# cardiotocography = fetch_ucirepo(id=193) 
  
# # data (as pandas dataframes) 
# X = cardiotocography.data.features.LB
# y = cardiotocography.data.features.ASTV

# print(X)
# print(y)

# # Save X and Y to a text file as points
# with open("cardiotocography.txt", "w") as file:
#     for x_value, y_value in zip(X, y):
#         file.write(f"{x_value} {y_value}\n")
  
# # metadata 
# #print(cardiotocography.metadata) 
  
# # variable information 
# print(cardiotocography.variables) 

##NONO DATASET
# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# cloud = fetch_ucirepo(id=155) 
  
# # data (as pandas dataframes) 
# X = cloud.data.features.contrast
# y = cloud.data.features.entropy

# print(X)
# print(y)

# # Save X and Y to a text file as points
# with open("cloud.txt", "w") as file:
#     for x_value, y_value in zip(X, y):
#         file.write(f"{x_value} {y_value}\n")
  
# # metadata 
# #print(cloud.metadata) 
  
# # variable information 
# print(cloud.variables) 

##DECIMO DATASET
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
mice_protein_expression = fetch_ucirepo(id=342) 
  
# data (as pandas dataframes) 
X = mice_protein_expression.data.features.ITSN1_N
y = mice_protein_expression.data.features.NR1_N 

print(X)
print(y)

# Save X and Y to a text file as points
with open("mice_protein_expression.txt", "w") as file:
    for x_value, y_value in zip(X, y):
        file.write(f"{x_value} {y_value}\n")
  
# metadata 
#print(mice_protein_expression.metadata) 
  
# variable information 
print(mice_protein_expression.variables) 
