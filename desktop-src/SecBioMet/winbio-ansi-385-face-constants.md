---
title: WINBIO_ANSI_385_FACE Constants (Winbio\_types.h)
description: Specify the frontal face image types for facial recognition.
ms.assetid: 16D21E40-C158-4674-80D0-AE9494124B96
topic_type:
- apiref
api_name:
- WINBIO_ANSI_385_FACE_TYPE_UNKNOWN
- WINBIO_ANSI_385_FACE_FRONTAL_FULL
- WINBIO_ANSI_385_FACE_FRONTAL_TOKEN
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_ANSI\_385\_FACE Constants

The following constants are **WINBIO\_BIOMETRIC\_SUBTYPE** values that can be used to specify the two types of frontal face images as defined by ANSI INCITS 385-2004: "Face Recognition Format for Data Interchange": full resolution and low resolution. In practice, the biometric framework will use only full resolution images for facial recognition.



| Constant/value                                                                                                                                                                                                                                                                          | Description                                                |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------|
| <span id="WINBIO_ANSI_385_FACE_TYPE_UNKNOWN"></span><span id="winbio_ansi_385_face_type_unknown"></span><dl> <dt>**WINBIO\_ANSI\_385\_FACE\_TYPE\_UNKNOWN**</dt> <dt>0</dt> </dl>    | The frontal face image type is unknown.<br/>         |
| <span id="WINBIO_ANSI_385_FACE_FRONTAL_FULL"></span><span id="winbio_ansi_385_face_frontal_full"></span><dl> <dt>**WINBIO\_ANSI\_385\_FACE\_FRONTAL\_FULL**</dt> <dt>1</dt> </dl>    | The frontal face image type is full resolution.<br/> |
| <span id="WINBIO_ANSI_385_FACE_FRONTAL_TOKEN"></span><span id="winbio_ansi_385_face_frontal_token"></span><dl> <dt>**WINBIO\_ANSI\_385\_FACE\_FRONTAL\_TOKEN**</dt> <dt>2</dt> </dl> | The frontal face image type is low resolution.<br/>  |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



 

 





