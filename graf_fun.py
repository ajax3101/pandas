import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm



# Преобразование данных в DataFrame
#data = pd.read_csv('kie2_ukr.csv', sep=';', index_col=(0), )
#data = pd.read_csv('kli_ukr.csv', sep=';', index_col=(0), )
data = pd.read_csv('kle_zap.csv', sep=';', index_col=(0), )


#print(data)
df = pd.DataFrame(data)
df = df.astype(float)

# Создание 3D графика
fig = plt.figure(figsize=(7, 4))
ax_3d = fig.add_subplot(projection='3d')

X, Y = np.meshgrid(df.columns.astype(float), df.index)
Z = df.values


ax_3d.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False) # Используй cmap для выбора цветовой схемы
#ax_3d.plot_trisurf(X, Y, Z, cmap='viridis')  

ax_3d.set_xlabel('I(T)')
ax_3d.set_ylabel('L(T)')
ax_3d.set_zlabel('K(T)')
ax_3d.set_title('3D Поверхня')

plt.show()

