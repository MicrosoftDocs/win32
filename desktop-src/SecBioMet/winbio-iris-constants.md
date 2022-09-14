---
title: WINBIO_IRIS Constants (Winbio\_types.h)
description: Specify the types for iris recognition.
ms.assetid: B1A594E3-6DEA-4071-B40F-569B8094E801
topic_type:
- apiref
api_name:
- WINBIO_IRIS_TYPE_UNKNOWN
- WINBIO_IRIS_LEFT_EYE
- WINBIO_IRIS_RIGHT_EYE
- WINBIO_IRIS_UNSPECIFIED_POS_01
- WINBIO_IRIS_UNSPECIFIED_POS_02
- WINBIO_IRIS_BOTH_EYES
- WINBIO_IRIS_EITHER_EYE
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_IRIS Constants

The following constants are **WINBIO\_BIOMETRIC\_SUBTYPE** values that can be used to specify the types for iris recognition beyond ANSI INCITS 379-2004: "Iris Image Interchange Format", which does not define any left/right eye values:



| Constant/value                                                                                                                                                                                                                                                                   | Description                                                                                                                                                           |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WINBIO_IRIS_TYPE_UNKNOWN_"></span><span id="winbio_iris_type_unknown_"></span><dl> <dt>**WINBIO\_IRIS\_TYPE\_UNKNOWN** </dt> <dt>0</dt> </dl>                       | The iris type is unknown. <br/>                                                                                                                                 |
| <span id="WINBIO_IRIS_LEFT_EYE_"></span><span id="winbio_iris_left_eye_"></span><dl> <dt>**WINBIO\_IRIS\_LEFT\_EYE** </dt> <dt>0xF5 </dt> </dl>                               | The iris type is the left eye. <br/>                                                                                                                            |
| <span id="WINBIO_IRIS_RIGHT_EYE_"></span><span id="winbio_iris_right_eye_"></span><dl> <dt>**WINBIO\_IRIS\_RIGHT\_EYE** </dt> <dt>0xF6 </dt> </dl>                            | The iris type is the right eye. <br/>                                                                                                                           |
| <span id="WINBIO_IRIS_UNSPECIFIED_POS_01"></span><span id="winbio_iris_unspecified_pos_01"></span><dl> <dt>**WINBIO\_IRIS\_UNSPECIFIED\_POS\_01**</dt> <dt>0xF7</dt> </dl>    | Subtype associated with a user s first template when only one eye is camera frame and it cannot be determined whether it is the user s left or right eye.<br/>  |
| <span id="WINBIO_IRIS_UNSPECIFIED_POS_02_"></span><span id="winbio_iris_unspecified_pos_02_"></span><dl> <dt>**WINBIO\_IRIS\_UNSPECIFIED\_POS\_02** </dt> <dt>0xF8</dt> </dl> | Subtype associated with a user s second template when only one eye is camera frame and it cannot be determined whether it is the user s left or right eye.<br/> |
| <span id="WINBIO_IRIS_BOTH_EYES_"></span><span id="winbio_iris_both_eyes_"></span><dl> <dt>**WINBIO\_IRIS\_BOTH\_EYES** </dt> <dt>0xF9</dt> </dl>                             | The iris type is both eyes. <br/>                                                                                                                               |
| <span id="WINBIO_IRIS_EITHER_EYE_"></span><span id="winbio_iris_either_eye_"></span><dl> <dt>**WINBIO\_IRIS\_EITHER\_EYE** </dt> <dt>0xFA</dt> </dl>                          | The iris type is either eye. <br/>                                                                                                                              |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



 

 





