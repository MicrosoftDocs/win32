---
title: DRM_AUDIO_OUTPUT_PROTECTION_IDS structure (Wmdrmsdk.h)
description: The DRM\_AUDIO\_OUTPUT\_PROTECTION\_IDS structure contains a list of audio output protection identifiers.
ms.assetid: 21972b18-334b-4a4d-812d-21cbfaf7cc58
keywords:
- DRM_AUDIO_OUTPUT_PROTECTION_IDS structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_AUDIO_OUTPUT_PROTECTION_IDS
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_AUDIO\_OUTPUT\_PROTECTION\_IDS structure

The **DRM\_AUDIO\_OUTPUT\_PROTECTION\_IDS** structure contains a list of audio output protection identifiers.

## Syntax


```C++
typedef struct DRM_AUDIO_OUTPUT_PROTECTION_IDS {
  WORD                        cEntries;
  DRM_AUDIO_OUTPUT_PROTECTION *rgAop;
} ;
```



## Members

<dl> <dt>

**cEntries**
</dt> <dd>

Number of entries in the **rgAop** array.

</dd> <dt>

**rgAop**
</dt> <dd>

Array of **DRM\_AUDIO\_OUTPUT\_PROTECTION** structures. **DRM\_AUDIO\_OUTPUT\_PROTECTION** is a type defined as [**DRM\_OUTPUT\_PROTECTION**](drm-output-protection.md).

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

 

 





