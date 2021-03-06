import numpy as np
import pickle

name = '/home/rafajdus/data_parsed/32x32/train_Temperature_32x32.pkl'
name2 = '/home/rafajdus/data_parsed/32x32/train_Cloud_cover_32x32.pkl'
name3 = '/home/rafajdus/data_parsed/32x32/train_Specific_humidity_32x32.pkl'

names_32 = [name, name2, name3]

name = '/home/rafajdus/data_parsed/64x64/train_Temperature_64x64.pkl'
name2 = '/home/rafajdus/data_parsed/64x64/train_Cloud_cover_64x64.pkl'
name3 = '/home/rafajdus/data_parsed/64x64/train_Specific_humidity_64x64.pkl'
name4 = '/home/rafajdus/data_parsed/64x64/train_Logarithm_of_surface_pressure_64x64.pkl'
name5 = '/home/rafajdus/data_parsed/64x64/train_Geopotential_64x64.pkl'

names_64 = [name, name2, name3, name4, name5]

# if dataset is 64x64 = is big
big = True

if big:
    data_64 = []
    for name in names_64:
        with open(name,'rb') as f:
            x = pickle.load(f, encoding='bytes')
            data_64.append(x)
else:
    data_32 = []
    for name in names_32:
        with open(name,'rb') as f:
            x = pickle.load(f, encoding='bytes')
            data_32.append(x)

if not big:
    data_all = []
    for x in data_32:
        data_values = [i[0] for i in x]
        data_values = [i.reshape([1,1,32,32,1]) for i in data_values]
        data_v = np.concatenate(data_values, axis=0)
        data_all.append(data_v)
    data_all = np.concatenate(data_all, axis=4)
    values = data_all

    temp = values[:,:,:,:,0]
    cc = values[:,:,:,:,1]
    hum = values[:,:,:,:,2]
      
    print('Temp')
    mmm = np.mean(temp)
    std = np.std(temp)
    print('mean:', mmm,'std:', std)
    norm2 = ((temp-mmm)/(std))
    print('min:',np.min(norm2),'max:', np.max(norm2))
    ttt = {'Temperature_mean':mmm, 'Temperature_std':std}

    print('CC')
    mmm = np.mean(cc)
    std = np.std(cc)
    print('mean:', mmm,'std:', std)
    norm2 = ((cc-mmm)/(std))
    print('min:',np.min(norm2),'max:', np.max(norm2))
    ccc = {'Cloud_cover_mean':mmm, 'Cloud_cover_std':std}

    print('Humidity')
    mmm = np.mean(hum)
    std = np.std(hum)
    print('mean:', mmm,'std:', std)
    norm2 = ((hum-mmm)/(std))
    print('min:',np.min(norm2),'max:', np.max(norm2))
    hhh = {'Specific_humidity_mean':mmm, 'Specific_humidity_std':std}

    meta32 = {**ttt, **ccc, **hhh}
    with open('/home/rafajdus/data_parsed/32x32/meta32x32.pkl','wb') as f:
        pickle.dump(meta32, f)
else:
    data_all = []
    for x in data_64:
        data_values = [i[0] for i in x]
        data_values = [i.reshape([1,1,64,64,1]) for i in data_values]
        data_v = np.concatenate(data_values, axis=0)
        data_all.append(data_v)
    data_all = np.concatenate(data_all, axis=4)
    values = data_all

    temp = values[:,:,:,:,0]
    cc = values[:,:,:,:,1]
    hum = values[:,:,:,:,2]
    sp = values[:,:,:,:,3]
    geo = values[:,:,:,:,4]

    print('Temp')
    mmm = np.mean(temp)
    std = np.std(temp)
    print('mean:', mmm,'std:', std)
    norm2 = ((temp-mmm)/(std))
    print('min:',np.min(norm2),'max:', np.max(norm2))
    ttt = {'Temperature_mean':mmm, 'Temperature_std':std}

    print('CC')
    mmm = np.mean(cc)
    std = np.std(cc)
    print('mean:', mmm,'std:', std)
    norm2 = ((cc-mmm)/(std))
    print('min:',np.min(norm2),'max:', np.max(norm2))
    ccc = {'Cloud_cover_mean':mmm, 'Cloud_cover_std':std}

    print('Humidity')
    mmm = np.mean(hum)
    std = np.std(hum)
    print('mean:', mmm,'std:', std)
    norm2 = ((hum-mmm)/(std))
    print('min:',np.min(norm2),'max:', np.max(norm2))
    hhh = {'Specific_humidity_mean':mmm, 'Specific_humidity_std':std}

    print('Geopotential')
    mmm = np.mean(geo)
    std = np.std(geo)
    print('mean:', mmm,'std:', std)
    norm2 = ((geo-mmm)/(std))
    print('min:',np.min(norm2),'max:', np.max(norm2))
    ggg = {'Geopotential_mean':mmm, 'Geopotential_std':std}

    print('SP')
    mmm = np.mean(sp)
    std = np.std(sp)
    print('mean:', mmm,'std:', std)
    norm2 = ((sp-mmm)/(std))
    print('min:',np.min(norm2),'max:', np.max(norm2))
    sss = {'Logarithm_of_surface_pressure_mean':mmm, 'Logarithm_of_surface_pressure_std':std}

    meta64 = {**ttt, **ccc, **hhh, **ggg, **sss}
    with open('/home/rafajdus/data_parsed/64x64/meta64x64.pkl','wb') as f:
        pickle.dump(meta64, f)
