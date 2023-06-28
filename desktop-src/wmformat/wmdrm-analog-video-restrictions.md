---
title: WMDRM_ANALOG_VIDEO_RESTRICTIONS structure (Wmdrmsdk.h)
description: The WMDRM\_ANALOG\_VIDEO\_RESTRICTIONS structure holds information about a restriction for playing back content as analog video.
ms.assetid: 13b38115-bd18-45b9-a1d5-542e043a4bde
keywords:
- WMDRM_ANALOG_VIDEO_RESTRICTIONS structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WMDRM_ANALOG_VIDEO_RESTRICTIONS
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMDRM\_ANALOG\_VIDEO\_RESTRICTIONS structure

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WMDRM\_ANALOG\_VIDEO\_RESTRICTIONS** structure holds information about a restriction for playing back content as analog video.

## Syntax


```C++
typedef struct WMDRM_ANALOG_VIDEO_RESTRICTIONS {
  GUID  guidRestrictionID;
  DWORD dwRestrictionData;
} ;
```



## Members

<dl> <dt>

**guidRestrictionID**
</dt> <dd>

Restriction identifier.

</dd> <dt>

**dwRestrictionData**
</dt> <dd>

Restriction data.

</dd> </dl>

## Remarks

This structure is received when you call [**IWMDRMLicense::GetAnalogVideoRestrictionLevels**](iwmdrmlicense-getanalogvideorestrictionlevels.md).

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](drm-structures.md)
</dt> <dt>

[**WMDRM\_ANALOG\_VIDEO\_RESTRICTIONS\_EX**](wmdrm-analog-video-restrictions-ex.md)
</dt> </dl>

 

 





