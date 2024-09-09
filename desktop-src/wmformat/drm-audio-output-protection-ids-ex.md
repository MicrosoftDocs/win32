---
title: DRM_AUDIO_OUTPUT_PROTECTION_IDS_EX structure (Wmdrmsdk.h)
description: The DRM\_AUDIO\_OUTPUT\_PROTECTION\_IDS\_EX structure contains a list of audio output protection identifiers. This structure extends DRM\_AUDIO\_OUTPUT\_PROTECTION\_IDS by adding a version number.
ms.assetid: e650ddeb-5e41-4ff8-b872-40c85ab519c1
keywords:
- DRM_AUDIO_OUTPUT_PROTECTION_IDS_EX structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_AUDIO_OUTPUT_PROTECTION_IDS_EX
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM\_AUDIO\_OUTPUT\_PROTECTION\_IDS\_EX structure

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_AUDIO\_OUTPUT\_PROTECTION\_IDS\_EX** structure contains a list of audio output protection identifiers. This structure extends **DRM\_AUDIO\_OUTPUT\_PROTECTION\_IDS** by adding a version number.

## Syntax


```C++
typedef struct DRM_AUDIO_OUTPUT_PROTECTION_IDS_EX {
  DWORD                          dwVersion;
  WORD                           cEntries;
  DRM_AUDIO_OUTPUT_PROTECTION_EX *rgAop;
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

Number of entries in the **rgAop** array.

</dd> <dt>

**rgAop**
</dt> <dd>

Array of **DRM\_AUDIO\_OUTPUT\_PROTECTION\_EX** structures. **DRM\_AUDIO\_OUTPUT\_PROTECTION\_EX** is a type defined as [**DRM\_OUTPUT\_PROTECTION\_EX**](drm-output-protection-ex.md).

</dd> </dl>

## Remarks

None.

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

 

 





