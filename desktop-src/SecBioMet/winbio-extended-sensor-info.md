---
title: WINBIO_EXTENDED_SENSOR_INFO structure (Winbio\_types.h)
description: Contains information about the capabilities and enrollment requirements of the sensor adapter for a biometric unit.
ms.assetid: 37D8BC57-F68D-487A-98B0-94D62CC091C2
keywords:
- WINBIO_EXTENDED_SENSOR_INFO structure Windows Biometric Framework API
- PWINBIO_EXTENDED_SENSOR_INFO structure pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_EXTENDED_SENSOR_INFO
api_location:
- winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_EXTENDED\_SENSOR\_INFO structure

Contains information about the capabilities and enrollment requirements of the sensor adapter for a biometric unit.

## Syntax


```C++
typedef struct _WINBIO_EXTENDED_SENSOR_INFO {
  WINBIO_CAPABILITIES   GenericSensorCapabilities;
  WINBIO_BIOMETRIC_TYPE Factor;
  union {
    ULONG32 Null;
    struct {
      RECT               FrameSize;
      POINT              FrameOffset;
      WINBIO_ORIENTATION MandatoryOrientation;
    } FacialFeatures;
    struct {
      ULONG32 Reserved;
    } Fingerprint;
    struct {
      RECT               FrameSize;
      POINT              FrameOffset;
      WINBIO_ORIENTATION MandatoryOrientation;
    } Iris;
    struct {
      ULONG32 Reserved;
    } Voice;
  } Specific;
} WINBIO_EXTENDED_SENSOR_INFO, *PWINBIO_EXTENDED_SENSOR_INFO;
```



## Members

<dl> <dt>

**GenericSensorCapabilities**
</dt> <dd>

The generic capabilities of the sensor component that is connected to a specific biometric unit.

</dd> <dt>

**Factor**
</dt> <dd>

The type of biometric unit for which this structure contains information about capabilities and enrollment requirements of the sensor adapter. For example, if the value of the **Factor** member is **WINBIO\_TYPE\_FINGERPRINT**, the **WINBIO\_EXTENDED\_SENSOR\_INFO** structure applies to a fingerprint reader and contains the relevant information in the **Specifc.Fingerprint** structure.

</dd> <dt>

**Specific**
</dt> <dd>

Information about the capabilities and enrollment requirements of the sensor adapter for a biometric unit related to a specific biometric factor.

<dl> <dt>

**Null**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**FacialFeatures**
</dt> <dd>

Information about the capabilities and enrollment requirements of the sensor adapter for a biometric unit related to facial features.

<dl> <dt>

**FrameSize**
</dt> <dd>

The size of the camera frame, indicated as a length and width in pixels by the **right** and **bottom** members of the [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure. The point (0, 0) represents the top-left corner of the frame.

</dd> <dt>

**FrameOffset**
</dt> <dd>

The offset of the camera frame for the face from the video camera, in pixels. A value of (0, 0) indicates that the camera frame for the face and the video camera completely overlap.

</dd> <dt>

**MandatoryOrientation**
</dt> <dd>

The preferred orientation for the camera.

</dd> </dl> </dd> <dt>

**Fingerprint**
</dt> <dd>

Information about the capabilities and enrollment requirements of the sensor adapter for a biometric unit related to fingerprint patterns.

<dl> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

**Iris**
</dt> <dd>

Information about the capabilities and enrollment requirements of the sensor adapter for a biometric unit related to iris patterns.

<dl> <dt>

**FrameSize**
</dt> <dd>

The size of the camera frame, indicated as a length and width in pixels by the **right** and **bottom** members of the [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure. The point (0, 0) represents the top-left corner of the frame.

</dd> <dt>

**FrameOffset**
</dt> <dd>

The offset of the camera frame for the iris from the video camera, in pixels. A value of (0, 0) indicates that the camera frame for the iris and the video camera completely overlap.

</dd> <dt>

**MandatoryOrientation**
</dt> <dd>

The preferred orientation for the camera.

</dd> </dl> </dd> <dt>

**Voice**
</dt> <dd>

Information about the capabilities and enrollment requirements of the sensor adapter for a biometric unit related to voice patterns.

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



## See also

<dl> <dt>

[**WINBIO\_CAPABILITY Constants**](winbio-capability-constants.md)
</dt> <dt>

[**WINBIO\_BIOMETRIC\_TYPE Constants**](winbio-biometric-type-constants.md)
</dt> <dt>

[**WINBIO\_ORIENTATION Constants**](winbio-orientation-constants.md)
</dt> </dl>

 

