---
title: WINBIO_BIOMETRIC_TYPE Constants (Winbio\_types.h)
description: Standard biometric types defined by National Institute of Standards and Technology Information (NISTIR) 6529-A, otherwise known as the Common Biometric Exchange Formats Framework (CBEFF) Patron Format A.
ms.assetid: DCBDB5F9-FF81-44C1-B439-2B8C02483212
topic_type:
- apiref
api_name:
- WINBIO_STANDARD_TYPE_MASK
- WINBIO_NO_TYPE_AVAILABLE
- WINBIO_TYPE_MULTIPLE
- WINBIO_TYPE_FACIAL_FEATURES
- WINBIO_TYPE_VOICE
- WINBIO_TYPE_FINGERPRINT
- WINBIO_TYPE_IRIS
- WINBIO_TYPE_RETINA
- WINBIO_TYPE_HAND_GEOMETRY
- WINBIO_TYPE_SIGNATURE_DYNAMICS
- WINBIO_TYPE_KEYSTROKE_DYNAMICS
- WINBIO_TYPE_LIP_MOVEMENT
- WINBIO_TYPE_THERMAL_FACE_IMAGE
- WINBIO_TYPE_THERMAL_HAND_IMAGE
- WINBIO_TYPE_GAIT
- WINBIO_TYPE_SCENT
- WINBIO_TYPE_DNA
- WINBIO_TYPE_EAR_SHAPE
- WINBIO_TYPE_FINGER_GEOMETRY
- WINBIO_TYPE_PALM_PRINT
- WINBIO_TYPE_VEIN_PATTERN
- WINBIO_TYPE_FOOT_PRINT
- WINBIO_TYPE_OTHER
- WINBIO_TYPE_PASSWORD
- WINBIO_TYPE_ANY
api_location:
- winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_BIOMETRIC\_TYPE Constants

The following constants represent the standard biometric types defined by National Institute of Standards and Technology Information (NISTIR) 6529-A, otherwise known as the Common Biometric Exchange Formats Framework (CBEFF) Patron Format A. Only **WINBIO\_TYPE\_FINGERPRINT** is currently supported.



| Constant                                                                                                                                                                                                            | Description                                                                                                                              |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WINBIO_STANDARD_TYPE_MASK"></span><span id="winbio_standard_type_mask"></span><dl> <dt>**WINBIO\_STANDARD\_TYPE\_MASK**</dt> </dl>                 | Bitmask that specifies the supported set of biometric factors.<br/>                                                                |
| <span id="WINBIO_NO_TYPE_AVAILABLE"></span><span id="winbio_no_type_available"></span><dl> <dt>**WINBIO\_NO\_TYPE\_AVAILABLE**</dt> </dl>                    | No biometric type is available.<br/>                                                                                               |
| <span id="WINBIO_TYPE_MULTIPLE"></span><span id="winbio_type_multiple"></span><dl> <dt>**WINBIO\_TYPE\_MULTIPLE**</dt> </dl>                                 | Multiple types are specified.<br/>                                                                                                 |
| <span id="WINBIO_TYPE_FACIAL_FEATURES"></span><span id="winbio_type_facial_features"></span><dl> <dt>**WINBIO\_TYPE\_FACIAL\_FEATURES**</dt> </dl>           | Facial features are used to determine the identity of an individual.<br/>                                                          |
| <span id="WINBIO_TYPE_VOICE"></span><span id="winbio_type_voice"></span><dl> <dt>**WINBIO\_TYPE\_VOICE**</dt> </dl>                                          | Frequency and volume patterns in the voice of an individual are used to determine the identity of an individual.<br/>              |
| <span id="WINBIO_TYPE_FINGERPRINT"></span><span id="winbio_type_fingerprint"></span><dl> <dt>**WINBIO\_TYPE\_FINGERPRINT**</dt> </dl>                        | Fingerprint patterns are used to determine the identity of an individual.<br/>                                                     |
| <span id="WINBIO_TYPE_IRIS"></span><span id="winbio_type_iris"></span><dl> <dt>**WINBIO\_TYPE\_IRIS**</dt> </dl>                                             | Iris patterns are used to determine the identity of an individual. This value is supported starting in Windows 10.<br/>            |
| <span id="WINBIO_TYPE_RETINA"></span><span id="winbio_type_retina"></span><dl> <dt>**WINBIO\_TYPE\_RETINA**</dt> </dl>                                       | Vein patterns in the retina are used to determine the identity of an individual.<br/>                                              |
| <span id="WINBIO_TYPE_HAND_GEOMETRY"></span><span id="winbio_type_hand_geometry"></span><dl> <dt>**WINBIO\_TYPE\_HAND\_GEOMETRY**</dt> </dl>                 | The shape of a hand of an individual is used to determine the identity of an individual.<br/>                                      |
| <span id="WINBIO_TYPE_SIGNATURE_DYNAMICS"></span><span id="winbio_type_signature_dynamics"></span><dl> <dt>**WINBIO\_TYPE\_SIGNATURE\_DYNAMICS**</dt> </dl>  | The patterns of force that the individual uses when they sign their name are used to determine the identity of an individual.<br/> |
| <span id="WINBIO_TYPE_KEYSTROKE_DYNAMICS"></span><span id="winbio_type_keystroke_dynamics"></span><dl> <dt>**WINBIO\_TYPE\_KEYSTROKE\_DYNAMICS**</dt> </dl>  | The speed and error patterns in typing by an individual are used to determine the identity of an individual.<br/>                  |
| <span id="WINBIO_TYPE_LIP_MOVEMENT"></span><span id="winbio_type_lip_movement"></span><dl> <dt>**WINBIO\_TYPE\_LIP\_MOVEMENT**</dt> </dl>                    | The changes in the lips of an individual that occur when they speak are used to determine the identity of an individual.<br/>      |
| <span id="WINBIO_TYPE_THERMAL_FACE_IMAGE"></span><span id="winbio_type_thermal_face_image"></span><dl> <dt>**WINBIO\_TYPE\_THERMAL\_FACE\_IMAGE**</dt> </dl> | The temperature patterns in the face of an individual are used to determine the identity of an individual.<br/>                    |
| <span id="WINBIO_TYPE_THERMAL_HAND_IMAGE"></span><span id="winbio_type_thermal_hand_image"></span><dl> <dt>**WINBIO\_TYPE\_THERMAL\_HAND\_IMAGE**</dt> </dl> | The temperature patterns in the hand of an individual are used to determine the identity of an individual.<br/>                    |
| <span id="WINBIO_TYPE_GAIT"></span><span id="winbio_type_gait"></span><dl> <dt>**WINBIO\_TYPE\_GAIT**</dt> </dl>                                             | The patterns of movement that occur when the individual walks are used to determine the identity of an individual.<br/>            |
| <span id="WINBIO_TYPE_SCENT"></span><span id="winbio_type_scent"></span><dl> <dt>**WINBIO\_TYPE\_SCENT**</dt> </dl>                                          | The scent of an individual is used to determine the identity of an individual.<br/>                                                |
| <span id="WINBIO_TYPE_DNA"></span><span id="winbio_type_dna"></span><dl> <dt>**WINBIO\_TYPE\_DNA**</dt> </dl>                                                | Deoxyribonucleic acid (DNA) sequences are used to determine the identity of an individual.<br/>                                    |
| <span id="WINBIO_TYPE_EAR_SHAPE"></span><span id="winbio_type_ear_shape"></span><dl> <dt>**WINBIO\_TYPE\_EAR\_SHAPE**</dt> </dl>                             | The shape of an ear of the individual is used to determine the identity of an individual.<br/>                                     |
| <span id="WINBIO_TYPE_FINGER_GEOMETRY"></span><span id="winbio_type_finger_geometry"></span><dl> <dt>**WINBIO\_TYPE\_FINGER\_GEOMETRY**</dt> </dl>           | The shapes of the fingers of an individual are used to determine the identity of an individual.<br/>                               |
| <span id="WINBIO_TYPE_PALM_PRINT"></span><span id="winbio_type_palm_print"></span><dl> <dt>**WINBIO\_TYPE\_PALM\_PRINT**</dt> </dl>                          | The shape of the palm is used to determine the identity of an individual.<br/>                                                     |
| <span id="WINBIO_TYPE_VEIN_PATTERN"></span><span id="winbio_type_vein_pattern"></span><dl> <dt>**WINBIO\_TYPE\_VEIN\_PATTERN**</dt> </dl>                    | Patterns in the veins underneath the skin of the hand of an individual are used to determine the identity of an individual.<br/>   |
| <span id="WINBIO_TYPE_FOOT_PRINT"></span><span id="winbio_type_foot_print"></span><dl> <dt>**WINBIO\_TYPE\_FOOT\_PRINT**</dt> </dl>                          | The shape of the foot is used to determine the identity of an individual.<br/>                                                     |
| <span id="WINBIO_TYPE_OTHER"></span><span id="winbio_type_other"></span><dl> <dt>**WINBIO\_TYPE\_OTHER**</dt> </dl>                                          | The supported biometric data is not defined by the current constants.<br/>                                                         |
| <span id="WINBIO_TYPE_PASSWORD"></span><span id="winbio_type_password"></span><dl> <dt>**WINBIO\_TYPE\_PASSWORD**</dt> </dl>                                 | Password data is used to determine the identity of an individual.<br/>                                                             |
| <span id="WINBIO_TYPE_ANY"></span><span id="winbio_type_any"></span><dl> <dt>**WINBIO\_TYPE\_ANY**</dt> </dl>                                                | Any type of data is used to determine the identity of an individual.<br/>                                                          |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                                                                                  |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h for client applications or Winbio\_adapters.h for adapters)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Constants](client-application-constants.md)
</dt> </dl>

 

 





