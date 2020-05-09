#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Importing Libraries


# In[1]:


import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
import math
import librosa
import librosa.display
import IPython.display as ipd
import cv2


# # Extracting Features

# ## Dataset

# The dataset contains 6 singers:
# 
# 1. Arijit singh
# 2. Avril lavigne
# 3. Ed sheeran
# 4. Lata mangeshkar
# 5. Sonu nigam
# 6. Taylor swift
# 
# Each singer folder has 40 songs. Total dataset= 240 songs.

# In[2]:


root_dir= os.getcwd()
root_dir


# In[3]:


src_dir= root_dir + '/songs_dataset'
src_dir


# In[4]:


dest_dir= root_dir + '/split'
dest_dir


# # Extracting Clips
# 
# ## 5 clips of 20 sec from each song

# In[5]:


folders=os.listdir(src_dir)


# In[6]:


print(folders)
folders=os.listdir(dest_dir)
print(folders)
#same on src_dir and dest_dir


# In[8]:


for folder in folders:
    #folder='taylor_swift'
    ctr=0
    songs=os.listdir(src_dir + '/' + folder )
    for song in songs:
        rate, X = scipy.io.wavfile.read(src_dir+'/'+folder+'/'+song)
        length=np.shape(X)[0]/float(rate)
        
        if length>=160:
            clips=[]
            
            clips.append(X[rate*35:rate*55])
            clips.append(X[rate*55:rate*75])
            clips.append(X[rate*75:rate*95])
            clips.append(X[rate*120:rate*140])
            clips.append(X[rate*140:rate*160])
            
        for clip in clips:
            # No augmentation
            ctr+=1
            
            clip = scipy.mean(clip, axis=1)
                    
            plt.axis('off')
            plt.specgram(clip, Fs=rate, cmap=plt.get_cmap("viridis"))
            #plt.show()
            print(dest_dir+'/'+folder+'/'+"_clip_"+str(ctr)+".png")
            plt.axis('off')
            plt.savefig(dest_dir+'/'+folder+'/'+"_clip_"+str(ctr)+".png", bbox_inches='tight') 
            plt.close()
            
            #time_shift (Augmentation)
            ctr+=1      
            start_ = int(np.random.uniform(-4800,4800))
            if start_ >= 0:
                wav_time_shift = np.r_[clip[start_:], np.random.uniform(-0.001,0.001, start_)]
            else:
                wav_time_shift = np.r_[np.random.uniform(-0.001,0.001, -start_), clip[:start_]]
                    
           
            plt.specgram(wav_time_shift, Fs=rate, cmap=plt.get_cmap("viridis"))
            #plt.show()
            print(dest_dir+'/'+folder+'/'+"_clip_"+str(ctr)+".png")
            plt.axis('off')
            plt.savefig(dest_dir+'/'+folder+'/'+"_clip_"+str(ctr)+".png", bbox_inches='tight') 
            plt.close()
            
            
            #speed tuning (Augmentation)
            ctr+=1   
            speed_rate = np.random.uniform(0.9,1.1)
            wav_speed_tune = cv2.resize(clip, (1, int(len(clip) * speed_rate))).squeeze()
               #     print(wav_speed_tune.shape)
              #      print('speed rate: %.3f' % speed_rate, '(lower is faster)')
            if len(wav_speed_tune) < 441000:
                pad_len = 441000 - len(wav_speed_tune)
                wav_speed_tune = np.r_[np.random.uniform(-0.001,0.001,int(pad_len/2)),
                                               wav_speed_tune,
                                               np.random.uniform(-0.001,0.001,int(np.ceil(pad_len/2)))]
            else: 
                cut_len = len(wav_speed_tune) - 441000
                wav_speed_tune = wav_speed_tune[int(cut_len/2):int(cut_len/2)+441000]
                #    print('wav length: ', wav_speed_tune.shape[0])
                    
            
            plt.axis('off')
            plt.specgram(wav_speed_tune, Fs=rate, cmap=plt.get_cmap("viridis"))
            #plt.show()
            print(dest_dir+'/'+folder+'/'+"_clip_"+str(ctr)+".png")
            plt.axis('off')
            plt.savefig(dest_dir+'/'+folder+'/'+"_clip_"+str(ctr)+".png", bbox_inches='tight') 
            plt.close()
            
        
            
           
        
    
    
    


# ## Resizing the spectrograms to 225x150x3

# In[9]:


for folder in folders:
    count=0
    specs=os.listdir(dest_dir+'/'+folder)
    for spec in specs:
        count+=1
        q = dest_dir + '/' + folder + '/' + spec
        pixels=cv2.imread(q)
        pixels=cv2.resize(pixels, (225,150))
        cv2.imwrite(q, pixels)
        print(q)


# In[9]:


count


# In[ ]:




