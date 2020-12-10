---
title: WINBIO_PRESENCE_PROPERTIES union (Winbio\_types.h)
description: Contains biometric values that the Windows Biometric Framework used to determine that an individual was present.
ms.assetid: 596CAA7F-35D2-442A-8041-BA1010DF5BAD
keywords:
- WINBIO_PRESENCE_PROPERTIES union Windows Biometric Framework API
- PWINBIO_PRESENCE_PROPERTIES union pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_PRESENCE_PROPERTIES
api_location:
- winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_PRESENCE\_PROPERTIES union

Contains biometric values that the Windows Biometric Framework used to determine that an individual was present.

## Syntax


```C++
typedef union _WINBIO_PRESENCE_PROPERTIES {
  struct {
    RECT BoundingBox;
    LONG Distance;
  } FacialFeatures;
  struct {
    RECT  EyeBoundingBox_1;
    RECT  EyeBoundingBox_2;
    POINT PupilCenter_1;
    POINT PupilCenter_2;
    LONG  Distance;
  } Iris;
} WINBIO_PRESENCE_PROPERTIES, *PWINBIO_PRESENCE_PROPERTIES;
```



## Members

<dl> <dt>

**FacialFeatures**
</dt> <dd>

Values for the location of facial features that the Windows Biometric Framework used to determine that an individual was present.

<dl> <dt>

**BoundingBox**
</dt> <dd>

The position within the camera frame of the face of the individual, in pixels. The size of the camera frame determines the upper limit on the number of pixels for this position. Get the **WINBIO\_PROPERTY\_EXTENDED\_SENSOR\_INFO** property to determine the size of the camera frame. A client that uses the presence monitor must perform the scaling operation to map the position to the camera frame .

</dd> <dt>

**Distance**
</dt> <dd>

The distance between the actual location of the face and the ideal focal distance for the face. This value ranges from -100 to 100. 0 indicates the ideal distance, positive values indicate that the actual location of the face is too far away, and negative values indicate that the actual location is too close.

</dd> </dl> </dd> <dt>

**Iris**
</dt> <dd>

Values for iris location that the Windows Biometric Framework used to determine that an individual was present.

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

</dd> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                                                                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                                                                     |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h for client applications or Winbio\_adapters.h for adapters)</dt> </dl> |



 

 





