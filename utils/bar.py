
# importing package 
efe2o3a =     -221.46498991
efe2o3li =     -226.13401858
efe2o3lib =     -226.13426224
efe2o3li2 =     -229.35308573
efe2o3li4 =     -238.32978469
efe2o3li6 =     -245.49173505


v1 = -(efe2o3li - efe2o3a - li)
v2 = -(efe2o3li2 - efe2o3li - li)
v4 = -(efe2o3li4 - efe2o3li2 - 2*li)/2
v6 = -(efe2o3li6 - efe2o3li4 - 2*li)/2
v6b = -(efe2o3li6 - efe2o3a - 6*li)/6

ae1 = (efe2o3li - efe2o3a - li)
ae2 = (efe2o3li2 - efe2o3li - li)
ae4 = (efe2o3li4 - efe2o3li2 - 2*li)/2
ae6 = (efe2o3li6 - efe2o3li4 - 2*li)/2
ae6b = (efe2o3li6 - efe2o3a - 6*li)/6


# create data 
x = np.arange(4) 
y1 = [ae1, ae2, ae4, ae6] 
y2 = [v1, v2, v4, v6 ]  
width = 0.60

plt.figure(figsize=(6,5))
plt.rcParams.update({'font.size': 24})
# plot data in grouped manner of bar type 
plt.bar(x, y1, width) 
#plt.bar(x+0.2, y2, width) 

plt.xticks(x, ['1' , '2', '4', '6']) 
plt.xticks(rotation = 0)
plt.xlabel("No. of Li adsorbed") 
plt.ylabel("Adsorption energy (eV)") 
#plt.legend(["Fully lithiated", "Fully delithiated"]) 
#plt.grid(True)
plt.savefig("AdsE-FO-bulk.png", 
            bbox_inches ="tight", 
            pad_inches = 0.1, 
            transparent = True, 
            facecolor ="w", 
            edgecolor ='b', 
            orientation ='landscape', dpi=400 ) 





## values on top of bar


fig, ax = plt.subplots(figsize=(12,8))
#plt.figure(figsize=(12,8))
plt.rcParams.update({'font.size': 20})
ax.set_xticks(x, ['1' , '2', '4', '6'], fontsize = 12) 
bar_container = ax.bar(x, y)
ax.set(ylabel='Formation energy per atom (eV)', title='Formation energy per atom (eV)', ylim=(-1.6, 0))
ax.bar_label(bar_container, fmt=lambda x: f'{x :.2f} eV')

