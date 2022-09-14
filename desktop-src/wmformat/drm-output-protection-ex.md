---
title: DRM_OUTPUT_PROTECTION_EX structure (Wmdrmsdk.h)
description: The DRM\_OUTPUT\_PROTECTION\_EX structure holds information about an output protection technology. This structure extends DRM\_OUTPUT\_PROTECTION by adding a version number.
ms.assetid: eeebf5da-172b-4781-8c44-00504a6961bf
keywords:
- DRM_OUTPUT_PROTECTION_EX structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_OUTPUT_PROTECTION_EX
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_OUTPUT\_PROTECTION\_EX structure

The **DRM\_OUTPUT\_PROTECTION\_EX** structure holds information about an output protection technology. This structure extends **DRM\_OUTPUT\_PROTECTION** by adding a version number.

## Syntax


```C++
typedef struct DRM_OUTPUT_PROTECTION_EX {
  DWORD dwVersion;
  GUID  guidId;
  DWORD dwConfigData;
} ;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

Version number.

</dd> <dt>

**guidId**
</dt> <dd>

GUID identifying the output protection technology.

</dd> <dt>

**dwConfigData**
</dt> <dd>

Configuration data for the technology.

</dd> </dl>

## Remarks

**DRM\_AUDIO\_OUTPUT\_PROTECTION\_EX** and **DRM\_VIDEO\_OUTPUT\_PROTECTION\_EX** are both defined as **DRM\_OUTPUT\_PROTECTION** in **typedef** statements.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**DRM\_OUTPUT\_PROTECTION**](drm-output-protection.md)
</dt> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





