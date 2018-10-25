# %%
import numpy as np
from scipy.interpolate import interp1d
import pandas as pd
import matplotlib.pyplot as plt

# %%


def prepare_data(csv_fname):
    dat = pd.read_csv(csv_fname, names=["ndens", "alt"], sep=";")
    dat1 = dat.copy()

    for i in range(len(dat)):
        dat1['ndens'][i] = eval(dat['ndens'][i].replace(',', '.'))
        dat1['alt'][i] = eval(dat['alt'][i].replace(',', '.'))
    return dat1


# %%
csv_names = ["solar_min.csv", "solar_men.csv", "solar_max.csv"]
legend = ["Solar Minimum", "Standard Atmosphere", "Solar Maximum", "ISS"]

fsize = 17
from matplotlib import rc
rc('font', **{'family': 'sans-serif',
              'sans-serif': ['Lato'],
              'size': fsize})

c_ls = ['k-', 'k--', 'k-.']
c_ls = ['C0-', 'C1-', 'C2-']

csvs = []
for csvn in csv_names[:-1]:
    csvs.append(prepare_data(csvn))
csvs.append(pd.read_csv(csv_names[-1], names=["ndens", "alt"], sep=";"))

# %%
# with plt.style.context('ggplot'):
with plt.style.context('seaborn'):
    plt.figure()
    plt.xscale("log")
    for i, csv in enumerate(csvs):
        plt.plot(csv['ndens'], csv['alt'], c_ls[i])
    plt.axhline(400, c="0.3", ls=":")
    plt.legend(legend, loc="best", fontsize=int(fsize*0.8))
    plt.xlabel("Number density [1/cm³]", fontsize=fsize)
    plt.ylabel("Altitude [km]", fontsize=fsize)
    plt.xticks(fontsize=int(fsize*0.8))
    plt.yticks(fontsize=int(fsize*0.8))
    plt.tight_layout(True)
    plt.savefig("ao_solar.png", dpi=300)
    plt.show()
    plt.close('all')

## %% # NO FUNCIONA
#with plt.style.context('seaborn'):
    #f, ax = plt.subplots()
    #ax.set_xscale("log")
    #dat = []
    #for csv in csv_names:
        #dat.append(prepare_data(csv))
    #dat0 = interp1d(dat[0]['ndens'], dat[0]['alt'])
    #dat2 = interp1d(dat[2]['ndens'], dat[2]['alt'])

    #ndens = np.logspace(max([d['ndens'].min() for d in dat]),
                        #min([d['ndens'].max() for d in dat]), num=100)

    #ax.fill_between(ndens, dat0(ndens), dat2(ndens))
    #plt.plot(dat[1]['ndens'], dat[1]['alt'])
    #ax.axhline(400, c="0.3", ls=":")
    #ax.legend(legend, loc="best", fontsize=int(fsize*0.8))
    #ax.set_xlabel(u"Number density [1/cm³]", fontsize=fsize)
    #ax.set_ylabel("Altitude [km]", fontsize=fsize)
    #ax.set_xticks(fontsize=int(fsize*0.8))
    #ax.set_yticks(fontsize=int(fsize*0.8))
    #f.tight_layout(True)
    #f.savefig("ao_solar1.png", dpi=300)
    #plt.show()
    #plt.close('all')
