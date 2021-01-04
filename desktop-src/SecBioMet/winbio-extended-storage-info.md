---
title: WINBIO_EXTENDED_STORAGE_INFO structure (Winbio\_types.h)
description: Contains information about the capabilities and enrollment requirements of the storage adapter for a biometric unit.
ms.assetid: 7A648610-E947-4967-A9AF-C8A9C0B81D92
keywords:
- WINBIO_EXTENDED_STORAGE_INFO structure Windows Biometric Framework API
- PWINBIO_EXTENDED_STORAGE_INFO structure pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_EXTENDED_STORAGE_INFO
api_location:
- winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_EXTENDED\_STORAGE\_INFO structure

Contains information about the capabilities and enrollment requirements of the storage adapter for a biometric unit.

## Syntax


```C++
typedef struct _WINBIO_EXTENDED_STORAGE_INFO {
  WINBIO_CAPABILITIES   GenericStorageCapabilities;
  WINBIO_BIOMETRIC_TYPE Factor;
  union {
    ULONG32 Null;
    struct {
      WINBIO_CAPABILITIES Capabilities;
    } FacialFeatures;
    struct {
      WINBIO_CAPABILITIES Capabilities;
    } Fingerprint;
    struct {
      WINBIO_CAPABILITIES Capabilities;
    } Iris;
    struct {
      WINBIO_CAPABILITIES Capabilities;
    } Voice;
  } Specific;
} WINBIO_EXTENDED_STORAGE_INFO, *PWINBIO_EXTENDED_STORAGE_INFO;
```



## Members

<dl> <dt>

**GenericStorageCapabilities**
</dt> <dd>

The generic capabilities of the storage component that is connected to a specific biometric unit.

</dd> <dt>

**Factor**
</dt> <dd>

The type of biometric unit for which this structure contains information about capabilities and enrollment requirements of the storage adapter. For example, if the value of the **Factor** member is **WINBIO\_TYPE\_FINGERPRINT**, the **WINBIO\_EXTENDED\_STORAGE\_INFO** structure applies to a fingerprint reader and contains the relevant information in the **Specifc.Fingerprint** structure.

</dd> <dt>

**Specific**
</dt> <dd>

Information about the capabilities and enrollment requirements of the storage adapter for a biometric unit related to a specific biometric factor.

<dl> <dt>

**Null**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**FacialFeatures**
</dt> <dd>

Information about the capabilities and enrollment requirements of the storage adapter for a biometric unit related to facial features.

<dl> <dt>

**Capabilities**
</dt> <dd>

The facial recognition capabilities of the storage component that is connected to a specific biometric unit.

</dd> </dl> </dd> <dt>

**Fingerprint**
</dt> <dd>

Information about the capabilities and enrollment requirements of the storage adapter for a biometric unit related to fingerprint patterns.

<dl> <dt>

**Capabilities**
</dt> <dd>

The fingerprint recognition capabilities of the storage component that is connected to a specific biometric unit

</dd> </dl> </dd> <dt>

**Iris**
</dt> <dd>

Information about the capabilities and enrollment requirements of the storage adapter for a biometric unit related to iris patterns.

<dl> <dt>

**Capabilities**
</dt> <dd>

The iris recognition capabilities of the storage component that is connected to a specific biometric unit

</dd> </dl> </dd> <dt>

**Voice**
</dt> <dd>

Information about the capabilities and enrollment requirements of the storage adapter for a biometric unit related to voice patterns.

<dl> <dt>

**Capabilities**
</dt> <dd>

The voice recognition capabilities of the storage component that is connected to a specific biometric unit

</dd> </dl> </dd> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                                                                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                                                                     |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h for client applications or Winbio\_adapters.h for adapters)</dt> </dl> |



## See also

<dl> <dt>

[**WINBIO\_BIOMETRIC\_TYPE Constants**](winbio-biometric-type-constants.md)
</dt> <dt>

[**WINBIO\_CAPABILITY Constants**](winbio-capability-constants.md)
</dt> </dl>

 

 





