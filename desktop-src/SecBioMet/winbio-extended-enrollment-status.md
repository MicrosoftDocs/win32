---
title: WINBIO_EXTENDED_ENROLLMENT_STATUS structure (Winbio\_types.h)
description: Contains additional information about the status of an enrollment that is in progress.
ms.assetid: 2FDDF4D3-6A3E-4DF5-ACA4-423F893C6F2B
keywords:
- WINBIO_EXTENDED_ENROLLMENT_STATUS structure Windows Biometric Framework API
- PWINBIO_EXTENDED_ENROLLMENT_STATUS structure pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_EXTENDED_ENROLLMENT_STATUS
api_location:
- winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_EXTENDED\_ENROLLMENT\_STATUS structure

Contains additional information about the status of an enrollment that is in progress.

## Syntax


```C++
typedef struct _WINBIO_EXTENDED_ENROLLMENT_STATUS {
  HRESULT                  TemplateStatus;
  WINBIO_REJECT_DETAIL     RejectDetail;
  ULONG                    PercentComplete;
  WINBIO_BIOMETRIC_TYPE    Factor;
  WINBIO_BIOMETRIC_SUBTYPE SubFactor;
  union {
    ULONG32 Null;
    struct {
      RECT BoundingBox;
      LONG Distance;
    } FacialFeatures;
    struct {
      ULONG GeneralSamples;
      ULONG Center;
      ULONG TopEdge;
      ULONG BottomEdge;
      ULONG LeftEdge;
      ULONG RightEdge;
    } Fingerprint;
    struct {
      RECT  EyeBoundingBox_1;
      RECT  EyeBoundingBox_2;
      POINT PupilCenter_1;
      POINT PupilCenter_2;
      LONG  Distance;
    } Iris;
    struct {
      ULONG32 Reserved;
    } Voice;
  } Specific;
} WINBIO_EXTENDED_ENROLLMENT_STATUS, *PWINBIO_EXTENDED_ENROLLMENT_STATUS;
```



## Members

<dl> <dt>

**TemplateStatus**
</dt> <dd>

The status of sample collection for the enrollment template. The following values are possible for this member.



| Value                                                                                                                                                                                                  | Meaning                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="S_OK"></span><span id="s_ok"></span><dl> <dt>**S\_OK**</dt> </dl>                                                                     | The enrollment is ready to be saved.<br/>                |
| <span id="WINBIO_E_INVALID_OPERATION"></span><span id="winbio_e_invalid_operation"></span><dl> <dt>**WINBIO\_E\_INVALID\_OPERATION**</dt> </dl> | No enrollment is in progress.<br/>                       |
| <span id="WINBIO_I_MORE_DATA"></span><span id="winbio_i_more_data"></span><dl> <dt>**WINBIO\_I\_MORE\_DATA**</dt> </dl>                         | More samples are required to complete the template.<br/> |
| <span id="WINBIO_E_BAD_CAPTURE"></span><span id="winbio_e_bad_capture"></span><dl> <dt>**WINBIO\_E\_BAD\_CAPTURE**</dt> </dl>                   | The most recent sample is not usable.<br/>               |



 

</dd> <dt>

**RejectDetail**
</dt> <dd>

The reason that the most recent sample is unusable, if the value of the **TemplateStatus** member is **WINBIO\_E\_BAD\_CAPTURE**.

</dd> <dt>

**PercentComplete**
</dt> <dd>

The best estimate from the engine adapter for the percentage of the template that is complete, as a value from 0 to 100.

</dd> <dt>

**Factor**
</dt> <dd>

The type of biometric unit for which this structure contains information about capabilities and enrollment requirements of the engine adapter. For example, if the value of the **Factor** member is **WINBIO\_TYPE\_FINGERPRINT**, the [**WINBIO\_EXTENDED\_ENGINE\_INFO**](winbio-extended-engine-info.md) structure applies to a fingerprint reader and contains the relevant information in the **Specifc.Fingerprint** structure.

</dd> <dt>

**SubFactor**
</dt> <dd>

A **WINBIO\_BIOMETRIC\_SUBTYPE** value that provides additional information about the enrollment.

</dd> <dt>

**Specific**
</dt> <dd>

Information about the status of an enrollment that is in progress for a specific biometric factor.

<dl> <dt>

**Null**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**FacialFeatures**
</dt> <dd>

Information about the status of an enrollment that is in progress for facial features.

<dl> <dt>

**BoundingBox**
</dt> <dd>

The position within the camera frame of the face of the individual to enroll, in pixels. The size of the camera frame determines the upper limit on the number of pixels for this position. Get the **WINBIO\_PROPERTY\_EXTENDED\_SENSOR\_INFO** property to determine the size of the camera frame. A client that uses the presence monitor must perform the scaling operation to map the position to the camera frame.

</dd> <dt>

**Distance**
</dt> <dd>

The distance between the actual location of the face and the ideal focal distance for the face. This value ranges from -100 to 100. 0 indicates the ideal distance, positive values indicate that the actual location of the face is too far away, and negative values indicate that the actual location is too close.

</dd> </dl> </dd> <dt>

**Fingerprint**
</dt> <dd>

Information about the status of an enrollment that is in progress for fingerprint patterns.

<dl> <dt>

**GeneralSamples**
</dt> <dd>

The total number of samples required to create a new fingerprint template.

</dd> <dt>

**Center**
</dt> <dd>

The number of samples for the center of the fingerprint required to create a new fingerprint template.

</dd> <dt>

**TopEdge**
</dt> <dd>

The number of samples for the top edge of the fingerprint required to create a new fingerprint template.

</dd> <dt>

**BottomEdge**
</dt> <dd>

The number of samples for the bottom edge of the fingerprint required to create a new fingerprint template.

</dd> <dt>

**LeftEdge**
</dt> <dd>

The number of samples for the left edge of the fingerprint required to create a new fingerprint template.

</dd> <dt>

**RightEdge**
</dt> <dd>

The number of samples for the right edge of the fingerprint required to create a new fingerprint template.

</dd> </dl> </dd> <dt>

**Iris**
</dt> <dd>

Information about the status of an enrollment that is in progress for iris patterns.

<dl> <dt>

**EyeBoundingBox\_1**
</dt> <dd>

The position within the camera frame of one of the irises of the individual to enroll, in pixels. If the iris-recognition system is only monitoring one eye, this position is of the iris of that eye. If the iris-recognition system is monitoring both eyes, but only one eye is in the camera frame, this position is of the iris of the eye in the camera frame. If the iris-recognition system is monitoring both eyes, and both eyes are in the camera frame, this position is probably of the iris of the right eye of the individual.

The size of the camera frame determines the upper limit on the number of pixels for this position. Get the **WINBIO\_PROPERTY\_EXTENDED\_SENSOR\_INFO** property to determine the size of the camera frame. A client that uses the presence monitor must perform the scaling operation to map the position to the camera frame.

</dd> <dt>

**EyeBoundingBox\_2**
</dt> <dd>

The position within the camera frame of one of the irises of the individual to enroll, in pixels. If the iris-recognition system is only monitoring one eye, or if only one eye is in the camera frame, this value is empty. If the iris-recognition system is monitoring both eyes, and both eyes are in the camera frame, this position is probably of iris of the left eye of the individual.

The size of the camera frame determines the upper limit on the number of pixels for this position. Get the **WINBIO\_PROPERTY\_EXTENDED\_SENSOR\_INFO** property to determine the size of the camera frame. A client that uses the presence monitor must perform the scaling operation to map the position to the camera frame.

</dd> <dt>

**PupilCenter\_1**
</dt> <dd>

The position of the center of one of the pupils of the individual to enroll. If the iris-recognition system is only monitoring one eye, this position is of the center of the pupil of that eye. If the iris-recognition system is monitoring both eyes, but only one eye is in the camera frame, this position is of the center of the pupil of the eye in the camera frame. If the iris-recognition system is monitoring both eyes, and both eyes are in the camera frame, this position is probably of the center of the pupil of the right eye of the individual.

</dd> <dt>

**PupilCenter\_2**
</dt> <dd>

The position of the center of one of the pupils of the individual to enroll. If the iris-recognition system is only monitoring one eye, or if only one eye is in the camera frame, this value is empty. If the iris-recognition system is monitoring both eyes, and both eyes are in the camera frame, this position is probably of the center of the pupil of the left eye of the individual.

</dd> <dt>

**Distance**
</dt> <dd>

The distance between the actual location of the iris and the ideal focal distance for the iris. This value ranges from -100 to 100. 0 indicates the ideal distance, positive values indicate that the actual location of the iris is too far away, and negative values indicate that the actual location is too close.

</dd> </dl> </dd> <dt>

**Voice**
</dt> <dd>

Information about the status of an enrollment that is in progress for voice patterns.

<dl> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl> </dd> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                                                                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                                                                     |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h for client applications or Winbio\_adapters.h for adapters)</dt> </dl> |



 

 





