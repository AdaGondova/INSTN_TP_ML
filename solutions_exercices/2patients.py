# -*- coding: utf-8 -*-

src = './data/preprocessed/'
patient1_t1 = process_one_subject(src, count=0, image_type='t1')
patient1_t1_normalize_path = 'patient1_t1_normalize.nii.gz'
sitk.WriteImage(patient1_t1, patient1_t1_normalize_path)

patient1_t1ce = process_one_subject(src, count=0, image_type='t1ce')
patient1_tce1_normalize_path = 'patient1_t1ce_normalize.nii.gz'
sitk.WriteImage(patient1_t1ce, patient1_tce1_normalize_path)

patient1_t2 = process_one_subject(src, count=0, image_type='t2')
patient1_t2_normalize_path = 'patient1_t2_normalize.nii.gz'
sitk.WriteImage(patient1_t2, patient1_t2_normalize_path)

patient1_flair = process_one_subject(src, count=0, image_type='flair')
patient1_flair_normalize_path = 'patient1_flair_normalize.nii.gz'
sitk.WriteImage(patient1_flair, patient1_flair_normalize_path)

patient1_segmentations = process_one_subject(src, count=0, image_type='seg') # return a dict with {label_full, label_nec, label_core, label_et}
patient1_seg_label_full_path = 'patient1_seg_label_full.nii.gz'
sitk.WriteImage(patient1_segmentations['label_full'], patient1_seg_label_full_path)
patient1_seg_label_nec_path = 'patient1_seg_label_nec.nii.gz'
sitk.WriteImage(patient1_segmentations['label_nec'], patient1_seg_label_nec_path)
patient1_seg_label_core_path = 'patient1_seg_label_core.nii.gz'
sitk.WriteImage(patient1_segmentations['label_core'], patient1_seg_label_core_path)
patient1_seg_label_et_path = 'patient1_seg_label_et.nii.gz'
sitk.WriteImage(patient1_segmentations['label_et'], patient1_seg_label_et_path)


patient2_t1 = process_one_subject(src, count=1, image_type='t1')
patient2_t1_normalize_path = 'patient2_t1_normalize.nii.gz'
sitk.WriteImage(patient2_t1, patient2_t1_normalize_path)

patient2_t1ce = process_one_subject(src, count=1, image_type='t1ce')
patient2_tce1_normalize_path = 'patient2_t1ce_normalize.nii.gz'
sitk.WriteImage(patient2_t1ce, patient2_tce1_normalize_path)

patient2_t2 = process_one_subject(src, count=1, image_type='t2')
patient2_t2_normalize_path = 'patient2_t2_normalize.nii.gz'
sitk.WriteImage(patient2_t2, patient2_t2_normalize_path)

patient2_flair = process_one_subject(src, count=1, image_type='flair')
patient2_flair_normalize_path = 'patient2_flair_normalize.nii.gz'
sitk.WriteImage(patient2_flair, patient2_flair_normalize_path)

patient2_segmentations = process_one_subject(src, count=1, image_type='seg')
patient2_seg_label_full_path = 'patient2_seg_label_full.nii.gz'
sitk.WriteImage(patient2_segmentations['label_full'], patient2_seg_label_full_path)
patient2_seg_label_nec_path = 'patient2_seg_label_nec.nii.gz'
sitk.WriteImage(patient2_segmentations['label_nec'], patient2_seg_label_nec_path)
patient2_seg_label_core_path = 'patient2_seg_label_core.nii.gz'
sitk.WriteImage(patient2_segmentations['label_core'], patient2_seg_label_core_path)
patient2_seg_label_et_path = 'patient2_seg_label_et.nii.gz'
sitk.WriteImage(patient2_segmentations['label_et'], patient2_seg_label_et_path)

