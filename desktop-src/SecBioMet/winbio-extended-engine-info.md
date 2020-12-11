---
title: WINBIO_EXTENDED_ENGINE_INFO structure (Winbio\_types.h)
description: Contains information about the capabilities and enrollment requirements of the engine adapter for a biometric unit.
ms.assetid: 83586E04-24CA-4A39-836F-C80DB1508C71
keywords:
- WINBIO_EXTENDED_ENGINE_INFO structure Windows Biometric Framework API
- PWINBIO_EXTENDED_ENGINE_INFO structure pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_EXTENDED_ENGINE_INFO
api_location:
- winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_EXTENDED\_ENGINE\_INFO structure

Contains information about the capabilities and enrollment requirements of the engine adapter for a biometric unit.

## Syntax


```C++
typedef struct _WINBIO_EXTENDED_ENGINE_INFO {
  WINBIO_CAPABILITIES   GenericEngineCapabilities;
  WINBIO_BIOMETRIC_TYPE Factor;
  union {
    ULONG32 Null;
    struct {
      WINBIO_CAPABILITIES Capabilities;
      struct {
        ULONG32 Null;
      } EnrollmentRequirements;
    } FacialFeatures;
    struct {
      WINBIO_CAPABILITIES Capabilities;
      struct {
        ULONG GeneralSamples;
        ULONG Center;
        ULONG TopEdge;
        ULONG BottomEdge;
        ULONG LeftEdge;
        ULONG RightEdge;
      } EnrollmentRequirements;
    } Fingerprint;
    struct {
      WINBIO_CAPABILITIES Capabilities;
      struct {
        ULONG32 Null;
      } EnrollmentRequirements;
    } Iris;
    struct {
      WINBIO_CAPABILITIES Capabilities;
      struct {
        ULONG32 Null;
      } EnrollmentRequirements;
    } Voice;
  } Specific;
} WINBIO_EXTENDED_ENGINE_INFO, *PWINBIO_EXTENDED_ENGINE_INFO;
```



## Members

<dl> <dt>

**GenericEngineCapabilities**
</dt> <dd>

The generic capabilities of the engine component that is connected to a specific biometric unit.

</dd> <dt>

**Factor**
</dt> <dd>

The type of biometric unit for which this structure contains information about capabilities and enrollment requirements of the engine adapter. For example, if the value of the **Factor** member is **WINBIO\_TYPE\_FINGERPRINT**, the **WINBIO\_EXTENDED\_ENGINE\_INFO** structure applies to a fingerprint reader and contains the relevant information in the **Specifc.Fingerprint** structure.

</dd> <dt>

**Specific**
</dt> <dd>

Information about the capabilities and enrollment requirements of the engine adapter for a biometric unit related to a specific biometric factor.

<dl> <dt>

**Null**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**FacialFeatures**
</dt> <dd>

Information about the capabilities and enrollment requirements of the engine adapter for a biometric unit related to facial features.

<dl> <dt>

**Capabilities**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**EnrollmentRequirements**
</dt> <dd> <dl> <dt>

**Null**
</dt> <dd>

Reserved. Must be zero.

</dd> </dl> </dd> </dl> </dd> <dt>

**Fingerprint**
</dt> <dd>

Information about the capabilities and enrollment requirements of the engine adapter for a biometric unit related to fingerprint patterns.

<dl> <dt>

**Capabilities**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**EnrollmentRequirements**
</dt> <dd>

The number of good samples required to create a new fingerprint template.

<dl> <dt>

**GeneralSamples**
</dt> <dd>

The total number of good samples required to create a new fingerprint template.

</dd> <dt>

**Center**
</dt> <dd>

The number of good samples for the center of the fingerprint required to create a new fingerprint template.

</dd> <dt>

**TopEdge**
</dt> <dd>

The number of good samples for the top edge of the fingerprint required to create a new fingerprint template.

</dd> <dt>

**BottomEdge**
</dt> <dd>

The number of good samples for the bottom edge of the fingerprint required to create a new fingerprint template.

</dd> <dt>

**LeftEdge**
</dt> <dd>

The number of good samples for the left edge of the fingerprint required to create a new fingerprint template.

</dd> <dt>

**RightEdge**
</dt> <dd>

The number of good samples for the right edge of the fingerprint required to create a new fingerprint template.

</dd> </dl> </dd> </dl> </dd> <dt>

**Iris**
</dt> <dd>

Information about the capabilities and enrollment requirements of the engine adapter for a biometric unit related to iris patterns.

<dl> <dt>

**Capabilities**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**EnrollmentRequirements**
</dt> <dd> <dl> <dt>

**Null**
</dt> <dd>

Reserved. Must be zero.

</dd> </dl> </dd> </dl> </dd> <dt>

**Voice**
</dt> <dd>

Information about the capabilities and enrollment requirements of the engine adapter for a biometric unit related to voice patterns.

<dl> <dt>

**Capabilities**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**EnrollmentRequirements**
</dt> <dd> <dl> <dt>

**Null**
</dt> <dd>

Reserved. Must be zero.

</dd> </dl> </dd> </dl> </dd> </dl> </dd> </dl>

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
</dt> </dl>

 

 





