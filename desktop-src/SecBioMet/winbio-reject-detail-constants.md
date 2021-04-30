---
title: WINBIO_REJECT_DETAIL Constants (Winbio\_types.h)
description: Specify the reason a biometric fingerprint capture or identification procedure did not succeed.
ms.assetid: b1ae4e65-9e53-42dd-99ba-1910b72688dd
topic_type:
- apiref
api_name:
- WINBIO_FP_TOO_HIGH
- WINBIO_FP_TOO_LOW
- WINBIO_FP_TOO_LEFT
- WINBIO_FP_TOO_RIGHT
- WINBIO_FP_TOO_FAST
- WINBIO_FP_TOO_SLOW
- WINBIO_FP_POOR_QUALITY
- WINBIO_FP_TOO_SKEWED
- WINBIO_FP_TOO_SHORT
- WINBIO_FP_MERGE_FAILURE
- WINBIO_REJECT_DETAIL_ANTI_SPOOF_MASK
- WINBIO_REJECT_DETAIL_POSITION_MASK
- WINBIO_REJECT_DETAIL_REASON_MASK
- WINBIO_IRIS_POOR_QUALITY
- WINBIO_IRIS_TOO_BRIGHT
- WINBIO_IRIS_TOO_DARK
- WINBIO_IRIS_SPOOF_DETECTED
- WINBIO_IRIS_TOO_SKEWED
- WINBIO_IRIS_TOO_CLOSED
- WINBIO_IRIS_GLARE
- WINBIO_IRIS_DIRTY_LENS
- WINBIO_IRIS_POOR_FOCUS
- WINBIO_IRIS_WRONG_ORIENTATION
- WINBIO_IRIS_TOO_HIGH
- WINBIO_IRIS_TOO_LOW
- WINBIO_IRIS_TOO_LEFT
- WINBIO_IRIS_TOO_RIGHT
- WINBIO_IRIS_TOO_NEAR
- WINBIO_IRIS_TOO_FAR
- WINBIO_FACE_POOR_QUALITY
- WINBIO_FACE_TOO_BRIGHT
- WINBIO_FACE_TOO_DARK
- WINBIO_FACE_SPOOF_DETECTED
- WINBIO_FACE_AMBIGUOUS_TARGET
- WINBIO_FACE_EYES_OCCLUDED
- WINBIO_FACE_WRONG_ORIENTATION
- WINBIO_FACE_TOO_HIGH
- WINBIO_FACE_TOO_LOW
- WINBIO_FACE_TOO_LEFT
- WINBIO_FACE_TOO_RIGHT
- WINBIO_FACE_TOO_NEAR
- WINBIO_FACE_TOO_FAR
api_location:
- winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_REJECT\_DETAIL Constants

The following constants can be used to specify the reason a biometric fingerprint capture or identification procedure did not succeed.



| Constant                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                       |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WINBIO_FP_TOO_HIGH"></span><span id="winbio_fp_too_high"></span><dl> <dt>**WINBIO\_FP\_TOO\_HIGH**</dt> </dl>                                                                  | The finger scan began too high on the finger.<br/>                                                                                                                                                                                                                                          |
| <span id="WINBIO_FP_TOO_LOW"></span><span id="winbio_fp_too_low"></span><dl> <dt>**WINBIO\_FP\_TOO\_LOW**</dt> </dl>                                                                     | The finger scan began too low on the finger.<br/>                                                                                                                                                                                                                                           |
| <span id="WINBIO_FP_TOO_LEFT"></span><span id="winbio_fp_too_left"></span><dl> <dt>**WINBIO\_FP\_TOO\_LEFT**</dt> </dl>                                                                  | The finger was too far left during scanning.<br/>                                                                                                                                                                                                                                           |
| <span id="WINBIO_FP_TOO_RIGHT"></span><span id="winbio_fp_too_right"></span><dl> <dt>**WINBIO\_FP\_TOO\_RIGHT**</dt> </dl>                                                               | The finger was too far right during scanning.<br/>                                                                                                                                                                                                                                          |
| <span id="WINBIO_FP_TOO_FAST"></span><span id="winbio_fp_too_fast"></span><dl> <dt>**WINBIO\_FP\_TOO\_FAST**</dt> </dl>                                                                  | The finger was swiped too quickly on the sensor.<br/>                                                                                                                                                                                                                                       |
| <span id="WINBIO_FP_TOO_SLOW"></span><span id="winbio_fp_too_slow"></span><dl> <dt>**WINBIO\_FP\_TOO\_SLOW**</dt> </dl>                                                                  | The finger was swiped too slowly on the sensor.<br/>                                                                                                                                                                                                                                        |
| <span id="WINBIO_FP_POOR_QUALITY"></span><span id="winbio_fp_poor_quality"></span><dl> <dt>**WINBIO\_FP\_POOR\_QUALITY**</dt> </dl>                                                      | The scan quality was too poor.<br/>                                                                                                                                                                                                                                                         |
| <span id="WINBIO_FP_TOO_SKEWED"></span><span id="winbio_fp_too_skewed"></span><dl> <dt>**WINBIO\_FP\_TOO\_SKEWED**</dt> </dl>                                                            | The finger did not pass straight across the sensor.<br/>                                                                                                                                                                                                                                    |
| <span id="WINBIO_FP_TOO_SHORT"></span><span id="winbio_fp_too_short"></span><dl> <dt>**WINBIO\_FP\_TOO\_SHORT**</dt> </dl>                                                               | Not enough of the finger was scanned.<br/>                                                                                                                                                                                                                                                  |
| <span id="WINBIO_FP_MERGE_FAILURE"></span><span id="winbio_fp_merge_failure"></span><dl> <dt>**WINBIO\_FP\_MERGE\_FAILURE**</dt> </dl>                                                   | The fingerprint captures could not be combined.<br/>                                                                                                                                                                                                                                        |
| <span id="WINBIO_REJECT_DETAIL_ANTI_SPOOF_MASK____"></span><span id="winbio_reject_detail_anti_spoof_mask____"></span><dl> <dt>**WINBIO\_REJECT\_DETAIL\_ANTI\_SPOOF\_MASK** </dt> </dl> | This mask covers the upper 8 bits of the reject detail value where the proof-of-liveness behaviors are located. This value is supported starting in Windows 10.<br/>                                                                                                                        |
| <span id="WINBIO_REJECT_DETAIL_POSITION_MASK______"></span><span id="winbio_reject_detail_position_mask______"></span><dl> <dt>**WINBIO\_REJECT\_DETAIL\_POSITION\_MASK** </dt> </dl>    | This mask covers the range of bits devoted to position errors. This value is supported starting in Windows 10.<br/>                                                                                                                                                                         |
| <span id="WINBIO_REJECT_DETAIL_REASON_MASK"></span><span id="winbio_reject_detail_reason_mask"></span><dl> <dt>**WINBIO\_REJECT\_DETAIL\_REASON\_MASK**</dt> </dl>                       | This mask covers the lower 16 bits where the enumerated reason for the rejection is located. This value is supported starting in Windows 10.<br/>                                                                                                                                           |
| <span id="WINBIO_IRIS_POOR_QUALITY"></span><span id="winbio_iris_poor_quality"></span><dl> <dt>**WINBIO\_IRIS\_POOR\_QUALITY**</dt> </dl>                                                | The conditions caused the camera to capture a poor image. Instruct the user to clean the sensor and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                        |
| <span id="WINBIO_IRIS_TOO_BRIGHT"></span><span id="winbio_iris_too_bright"></span><dl> <dt>**WINBIO\_IRIS\_TOO\_BRIGHT**</dt> </dl>                                                      | The image includes too much ambient light to get a good match. Instruct the user to ensure that they are no facing another bright light source. This value is supported starting in Windows 10.<br/>                                                                                        |
| <span id="WINBIO_IRIS_TOO_DARK"></span><span id="winbio_iris_too_dark"></span><dl> <dt>**WINBIO\_IRIS\_TOO\_DARK**</dt> </dl>                                                            | The image is too dark to get a good match. Instruct the user to ensure that their iris is not obscured by items such as a veil, dark glasses, or colored contacts. This value is supported starting in Windows 10.<br/>                                                                     |
| <span id="WINBIO_IRIS_SPOOF_DETECTED"></span><span id="winbio_iris_spoof_detected"></span><dl> <dt>**WINBIO\_IRIS\_SPOOF\_DETECTED**</dt> </dl>                                          | The recognition component believes that the iris is not live, but is coming from a replayed video feed, a photo, or a 3-D sculpture. This value is supported starting in Windows 10.<br/>                                                                                                   |
| <span id="WINBIO_IRIS_TOO_SKEWED"></span><span id="winbio_iris_too_skewed"></span><dl> <dt>**WINBIO\_IRIS\_TOO\_SKEWED**</dt> </dl>                                                      | The user is not looking directly at the camera. Instruct the user to look directly at the camera and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                       |
| <span id="WINBIO_IRIS_TOO_CLOSED"></span><span id="winbio_iris_too_closed"></span><dl> <dt>**WINBIO\_IRIS\_TOO\_CLOSED**</dt> </dl>                                                      | The user's eyelids are obscuring the iris. Instruct the user to open their eyes a little more and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                          |
| <span id="WINBIO_IRIS_GLARE"></span><span id="winbio_iris_glare"></span><dl> <dt>**WINBIO\_IRIS\_GLARE**</dt> </dl>                                                                      | The image includes lens glare. Instruct the user to remove their glasses and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                               |
| <span id="WINBIO_IRIS_DIRTY_LENS"></span><span id="winbio_iris_dirty_lens"></span><dl> <dt>**WINBIO\_IRIS\_DIRTY\_LENS**</dt> </dl>                                                      | The camera lens was dirty. Instruct the user to clean the lens and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                                         |
| <span id="WINBIO_IRIS_POOR_FOCUS"></span><span id="winbio_iris_poor_focus"></span><dl> <dt>**WINBIO\_IRIS\_POOR\_FOCUS**</dt> </dl>                                                      | This iris is out of focus. This value is supported starting in Windows 10.<br/>                                                                                                                                                                                                             |
| <span id="WINBIO_IRIS_WRONG_ORIENTATION"></span><span id="winbio_iris_wrong_orientation"></span><dl> <dt>**WINBIO\_IRIS\_WRONG\_ORIENTATION**</dt> </dl>                                 | The camera orientation does not match the mandatory orientation that the [**WINBIO\_EXTENDED\_SENSOR\_INFO**](winbio-extended-sensor-info.md) structure specifies. Instruct the user to change the camera orientation and scan again. This value is supported starting in Windows 10.<br/> |
| <span id="WINBIO_IRIS_TOO_HIGH"></span><span id="winbio_iris_too_high"></span><dl> <dt>**WINBIO\_IRIS\_TOO\_HIGH**</dt> </dl>                                                            | The iris is facing up. Instruct the user to look down a little bit and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                                     |
| <span id="WINBIO_IRIS_TOO_LOW"></span><span id="winbio_iris_too_low"></span><dl> <dt>**WINBIO\_IRIS\_TOO\_LOW**</dt> </dl>                                                               | The iris is facing down. Instruct the user to look up a little bit and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                                     |
| <span id="WINBIO_IRIS_TOO_LEFT"></span><span id="winbio_iris_too_left"></span><dl> <dt>**WINBIO\_IRIS\_TOO\_LEFT**</dt> </dl>                                                            | The iris is too far to the left. Instruct the user to look a little more to the right and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                  |
| <span id="WINBIO_IRIS_TOO_RIGHT"></span><span id="winbio_iris_too_right"></span><dl> <dt>**WINBIO\_IRIS\_TOO\_RIGHT**</dt> </dl>                                                         | The iris is too far to the right. Instruct the user to look a little more to the left and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                  |
| <span id="WINBIO_IRIS_TOO_NEAR"></span><span id="winbio_iris_too_near"></span><dl> <dt>**WINBIO\_IRIS\_TOO\_NEAR**</dt> </dl>                                                            | The iris is too close to the camera. Instruct the user to move a little further away and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                   |
| <span id="WINBIO_IRIS_TOO_FAR"></span><span id="winbio_iris_too_far"></span><dl> <dt>**WINBIO\_IRIS\_TOO\_FAR**</dt> </dl>                                                               | The iris is too far from the camera. Instruct the user to move a little closer and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                         |
| <span id="WINBIO_FACE_POOR_QUALITY"></span><span id="winbio_face_poor_quality"></span><dl> <dt>**WINBIO\_FACE\_POOR\_QUALITY**</dt> </dl>                                                | The conditions caused the camera to capture a poor image. Instruct the user to clean the sensor and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                        |
| <span id="WINBIO_FACE_TOO_BRIGHT"></span><span id="winbio_face_too_bright"></span><dl> <dt>**WINBIO\_FACE\_TOO\_BRIGHT**</dt> </dl>                                                      | The image includes too much ambient light to get a good match. Instruct the user to ensure that they are no facing another bright light source. This value is supported starting in Windows 10.<br/>                                                                                        |
| <span id="WINBIO_FACE_TOO_DARK"></span><span id="winbio_face_too_dark"></span><dl> <dt>**WINBIO\_FACE\_TOO\_DARK**</dt> </dl>                                                            | The image is too dark to get a good match. This value is supported starting in Windows 10.<br/>                                                                                                                                                                                             |
| <span id="WINBIO_FACE_SPOOF_DETECTED"></span><span id="winbio_face_spoof_detected"></span><dl> <dt>**WINBIO\_FACE\_SPOOF\_DETECTED**</dt> </dl>                                          | The recognition component believes that the face is not live, but is coming from a replayed video feed, a photo, or a 3-D sculpture. This value is supported starting in Windows 10.<br/>                                                                                                   |
| <span id="WINBIO_FACE_AMBIGUOUS_TARGET"></span><span id="winbio_face_ambiguous_target"></span><dl> <dt>**WINBIO\_FACE\_AMBIGUOUS\_TARGET**</dt> </dl>                                    | Two or more faces are overlapping in camera frame. This value is supported starting in Windows 10.<br/>                                                                                                                                                                                     |
| <span id="WINBIO_FACE_EYES_OCCLUDED"></span><span id="winbio_face_eyes_occluded"></span><dl> <dt>**WINBIO\_FACE\_EYES\_OCCLUDED**</dt> </dl>                                             | The user's eyes are occluded. Instruct the user to ensure that their eyes are not obscured by items such as a veil, dark glasses, or colored contacts. This value is supported starting in Windows 10.<br/>                                                                                 |
| <span id="WINBIO_FACE_WRONG_ORIENTATION"></span><span id="winbio_face_wrong_orientation"></span><dl> <dt>**WINBIO\_FACE\_WRONG\_ORIENTATION**</dt> </dl>                                 | The camera orientation does not match the mandatory orientation that the [**WINBIO\_EXTENDED\_SENSOR\_INFO**](winbio-extended-sensor-info.md) structure specifies. Instruct the user to change the camera orientation and scan again. This value is supported starting in Windows 10.<br/> |
| <span id="WINBIO_FACE_TOO_HIGH"></span><span id="winbio_face_too_high"></span><dl> <dt>**WINBIO\_FACE\_TOO\_HIGH**</dt> </dl>                                                            | The face is facing up. Instruct the user to look down a little bit and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                                     |
| <span id="WINBIO_FACE_TOO_LOW"></span><span id="winbio_face_too_low"></span><dl> <dt>**WINBIO\_FACE\_TOO\_LOW**</dt> </dl>                                                               | The face is facing down. Instruct the user to look up a little bit and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                                     |
| <span id="WINBIO_FACE_TOO_LEFT"></span><span id="winbio_face_too_left"></span><dl> <dt>**WINBIO\_FACE\_TOO\_LEFT**</dt> </dl>                                                            | The face is too far to the left. Instruct the user to move a little more to the right and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                  |
| <span id="WINBIO_FACE_TOO_RIGHT"></span><span id="winbio_face_too_right"></span><dl> <dt>**WINBIO\_FACE\_TOO\_RIGHT**</dt> </dl>                                                         | The face is too far to the right. Instruct the user to move a little more to the left and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                  |
| <span id="WINBIO_FACE_TOO_NEAR"></span><span id="winbio_face_too_near"></span><dl> <dt>**WINBIO\_FACE\_TOO\_NEAR**</dt> </dl>                                                            | The face is too close to the camera. Instruct the user to move a little further away and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                   |
| <span id="WINBIO_FACE_TOO_FAR"></span><span id="winbio_face_too_far"></span><dl> <dt>**WINBIO\_FACE\_TOO\_FAR**</dt> </dl>                                                               | The face is too far from the camera. Instruct the user to move a little closer and scan again. This value is supported starting in Windows 10.<br/>                                                                                                                                         |



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

 

 





