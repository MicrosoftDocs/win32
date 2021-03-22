---
title: DRM_OUTPUT_PROTECTION structure (Wmdrmsdk.h)
description: The DRM\_OUTPUT\_PROTECTION structure holds information about an output protection technology.
ms.assetid: e458013d-b77e-4e03-bff9-e3ecfc72ebdb
keywords:
- DRM_OUTPUT_PROTECTION structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_OUTPUT_PROTECTION
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_OUTPUT\_PROTECTION structure

The **DRM\_OUTPUT\_PROTECTION** structure holds information about an output protection technology.

## Syntax


```C++
typedef struct DRM_OUTPUT_PROTECTION {
  GUID guidId;
  BYTE bConfigData;
} ;
```



## Members

<dl> <dt>

**guidId**
</dt> <dd>

GUID identifying the output protection technology.

</dd> <dt>

**bConfigData**
</dt> <dd>

Configuration data for the technology.

</dd> </dl>

## Remarks

**DRM\_AUDIO\_OUTPUT\_PROTECTION** and **DRM\_VIDEO\_OUTPUT\_PROTECTION** are both defined as **DRM\_OUTPUT\_PROTECTION** in **typedef** statements.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**DRM\_OUTPUT\_PROTECTION\_EX**](drm-output-protection-ex.md)
</dt> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





