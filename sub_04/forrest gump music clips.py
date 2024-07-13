from matplotlib import pyplot as plt
import nibabel as nib

# data for Subject 04
path = 'C:/Users/kenne/OneDrive/Desktop/miscellaneous/education/Springboard/Machine Learning/datasets/Music_Psychotherapy/sub_04/sub-04_ses-auditoryperception_task-auditoryperception_run-04_bold.nii'

img = nib.load(path).get_fdata()
img.shape

# there are 36x153 fMRI brain scans for Study Subject #4 for Run #4 of eight total runs
# totaling 5,508 data samples of fMRI scans for one run out of a total of 44,064 scans for one subject
# there are 20 subjects for this Task, with eight Runs each
print(img.shape)

plt.style.use('default')
fig, axes = plt.subplots(4,4, figsize=(12,12))
for i, ax in enumerate(axes.reshape(-1)):
    ax.imshow(img[:,:,7,1 + i])
plt.show()