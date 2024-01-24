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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMDRM\_ANALOG\_VIDEO\_RESTRICTIONS\_EX structure

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





