---
title: WMDRM_ANALOG_VIDEO_RESTRICTIONS_EX structure (Wmdrmsdk.h)
description: The WMDRM\_ANALOG\_VIDEO\_RESTRICTIONS\_EX structure holds extended information about a restriction for playing back content as analog video.
ms.assetid: fe9092fe-a717-4377-9653-1cc07795319f
keywords:
- WMDRM_ANALOG_VIDEO_RESTRICTIONS_EX structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WMDRM_ANALOG_VIDEO_RESTRICTIONS_EX
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRM\_ANALOG\_VIDEO\_RESTRICTIONS\_EX structure

The **WMDRM\_ANALOG\_VIDEO\_RESTRICTIONS\_EX** structure holds extended information about a restriction for playing back content as analog video.

## Syntax


```C++
typedef struct WMDRM_ANALOG_VIDEO_RESTRICTIONS_EX {
  DWORD dwVersion;
  GUID  guidRestrictionID;
  DWORD cbRestrictionData;
  BYTE  *pbRestrictionData;
} ;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

Version number.

</dd> <dt>

**guidRestrictionID**
</dt> <dd>

Restriction ID.

</dd> <dt>

**cbRestrictionData**
</dt> <dd>

Size of restriction data in bytes.

</dd> <dt>

**pbRestrictionData**
</dt> <dd>

Restriction data.

</dd> </dl>

## Remarks

None.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](drm-structures.md)
</dt> <dt>

[**WMDRM\_ANALOG\_VIDEO\_RESTRICTIONS**](wmdrm-analog-video-restrictions.md)
</dt> </dl>

 

 





