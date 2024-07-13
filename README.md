# Music-Psychotherapy
This repository explores using music to elicit desired moods of a subject.

Source:  [https://www.studyforrest.org/data.html](https://www.studyforrest.org/data.html#Highres7TfMRIListeningtoMusicCardiacRespiration)
Publication:  https://f1000research.com/articles/4-174/v1
Task Title:  High-res 7T fMRI Listening to Music (+Cardiac/Respiration)
Task Description:  "High-resolution, ultra high-field (7 Tesla) functional magnetic resonance imaging (fMRI) data from 20 participants that were repeatedly stimulated with a total of 25 music clips, with and without speech content, from five different genres using a slow event-related paradigm. Physiological recordings of heart beat and breathing were simultaneously recorded as well."
More Description:  Functional imaging - Auditory Perception Session
Participants were repeatedly stimulated with a total of 25 music clips, with and without speech content, from five different genres using a slow event-related paradigm.

Data:  https://openneuro.org/datasets/ds000113/versions/1.3.0
Subset:   ../SUB-04/SES-AUDITORYPERCEPTION/FUNC/SUB-04_SES-AUDITORYPERCEPTION_TASK-AUDITORYPERCEPTION_RUN-04_BOLD.NII.GZ

Filename examples for subject 01 and run 01:
./sub-01/ses-auditoryperception/func/sub-01_ses-auditoryperception_task-auditoryperception_run-01_bold.nii.gz ./sub-01/ses-auditoryperception/func/sub-01_ses-auditoryperception_task-auditoryperception_run-01_events.tsv

Data Statistics:
Uploaded data has 36x153 fMRI brain scans for Study Subject #4 for Run #4 of eight total runs.
This totals 5,508 data samples of fMRI scans for one run out of a total of 44,064 scans for one subject.
There are 20 subjects for this Task, with eight Runs each, thus totaling over 880,000 images.

Data Type/Size:
The uploaded dataset is a gunzip file with .nii files of size 169MB and "Git Large File Extension" was used to facilitate the transfer and version control.

Data Inspection:
File "forrest gump music clips.py" has code that was used to look at the images in the dataset which are .nii files.
Python package "nibabel" is necessary to view .nii files.
