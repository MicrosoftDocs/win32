---
title: DRM_OPL_OUTPUT_IDS structure (Wmdrmsdk.h)
description: The DRM\_OPL\_OUTPUT\_IDS structure holds a number of output protection level (OPL) output identifiers.
ms.assetid: 3627f2a7-1cea-400b-82e7-678898ccc386
keywords:
- DRM_OPL_OUTPUT_IDS structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_OPL_OUTPUT_IDS
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_OPL\_OUTPUT\_IDS structure

The **DRM\_OPL\_OUTPUT\_IDS** structure holds a number of output protection level (OPL) output identifiers.

## Syntax


```C++
typedef struct DRM_OPL_OUTPUT_IDS {
  WORD cIds;
  GUID *rgIds;
} ;
```



## Members

<dl> <dt>

**cIds**
</dt> <dd>

Number of identifiers in the array referenced by **rgIds**.

</dd> <dt>

**rgIds**
</dt> <dd>

Address of an array of GUIDs. Each member of the array contains an OPL output identifier.

</dd> </dl>

## Remarks

This structure is used as a member of the [**DRM\_COPY\_OPL**](drmdrm-copy-opl.md) and [**DRM\_PLAY\_OPL**](drmdrm-play-opl.md) structures to identify groups of output identifiers.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





