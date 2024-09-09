---
title: DRM_VIDEO_OUTPUT_PROTECTION_IDS_EX structure (Wmdrmsdk.h)
description: The DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS\_EX structure holds an array of DRM\_VIDEO\_OUTPUT\_PROTECTION structures.
ms.assetid: 89de0ade-fa86-4081-b65b-9c84fb68cf3d
keywords:
- DRM_VIDEO_OUTPUT_PROTECTION_IDS_EX structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_VIDEO_OUTPUT_PROTECTION_IDS_EX
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS\_EX structure

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS\_EX** structure holds an array of **DRM\_VIDEO\_OUTPUT\_PROTECTION** structures.

## Syntax


```C++
typedef struct DRM_VIDEO_OUTPUT_PROTECTION_IDS_EX {
  DWORD                          dwVersion;
  WORD                           cEntries;
  DRM_VIDEO_OUTPUT_PROTECTION_EX *rgVop;
} ;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

Version number.

</dd> <dt>

**cEntries**
</dt> <dd>

Number of elements in the array referenced by **rgVop**.

</dd> <dt>

**rgVop**
</dt> <dd>

Address of an array of **DRM\_VIDEO\_OUTPUT\_PROTECTION\_EX** structures. **DRM\_VIDEO\_OUTPUT\_PROTECTION\_EX** is a type defined as [**DRM\_OUTPUT\_PROTECTION\_EX**](drm-output-protection-ex.md).

</dd> </dl>

## Remarks

None.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**DRM\_AUDIO\_OUTPUT\_PROTECTION\_IDS\_EX**](drm-audio-output-protection-ids-ex.md)
</dt> <dt>

[**DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS**](drmdrm-video-output-protection-ids.md)
</dt> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





