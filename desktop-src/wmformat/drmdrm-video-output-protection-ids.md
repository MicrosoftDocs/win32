---
title: DRM_VIDEO_OUTPUT_PROTECTION_IDS structure (Wmdrmsdk.h)
description: The DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS structure holds an array of DRM\_VIDEO\_OUTPUT\_PROTECTION structures.
ms.assetid: 9f206a7e-c92b-4f29-a591-72784086d1db
keywords:
- DRM_VIDEO_OUTPUT_PROTECTION_IDS structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_VIDEO_OUTPUT_PROTECTION_IDS
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS structure

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS** structure holds an array of **DRM\_VIDEO\_OUTPUT\_PROTECTION** structures.

## Syntax


```C++
typedef struct DRM_VIDEO_OUTPUT_PROTECTION_IDS {
  WORD                        cEntries;
  DRM_VIDEO_OUTPUT_PROTECTION *rgVop;
} ;
```



## Members

<dl> <dt>

**cEntries**
</dt> <dd>

Number of elements in the array referenced by **rgVop**.

</dd> <dt>

**rgVop**
</dt> <dd>

Address of an array of **DRM\_VIDEO\_OUTPUT\_PROTECTION** structures. **DRM\_VIDEO\_OUTPUT\_PROTECTION** is a type defined as [**DRM\_OUTPUT\_PROTECTION**](drm-output-protection.md).

</dd> </dl>

## Remarks

This structure is used as a member of the [**DRM\_PLAY\_OPL**](drmdrm-play-opl.md) structure.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**DRM\_AUDIO\_OUTPUT\_PROTECTION\_IDS**](drm-audio-output-protection-ids.md)
</dt> <dt>

[**DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS\_EX**](drm-video-output-protection-ids-ex.md)
</dt> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





