---
title: DRM_PLAY_OPL structure (Wmdrmsdk.h)
description: The DRM\_PLAY\_OPL structure holds information about the output protection levels (OPLs) specified in a license for play actions.
ms.assetid: 10703893-630c-4cbe-a0b0-d2890905daba
keywords:
- DRM_PLAY_OPL structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_PLAY_OPL
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_PLAY\_OPL structure

The **DRM\_PLAY\_OPL** structure holds information about the output protection levels (OPLs) specified in a license for play actions.

## Syntax


```C++
typedef struct DRM_PLAY_OPL {
  DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS minOPL;
  DRM_OPL_OUTPUT_IDS                   oplIdReserved;
  DRM_VIDEO_OUTPUT_PROTECTION_IDS      vopi;
} ;
```



## Members

<dl> <dt>

**minOPL**
</dt> <dd>

[**DRM\_MINIMUM\_OUTPUT\_PROTECTION\_LEVELS**](drmdrm-minimum-output-protection-levels.md) structure containing the minimum OPL required to play content in different formats.

</dd> <dt>

**oplIdReserved**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**vopi**
</dt> <dd>

[**DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS**](drmdrm-video-output-protection-ids.md) structure containing the video output protection identifiers that apply to playback of the content.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**DRM\_COPY\_OPL**](drmdrm-copy-opl.md)
</dt> <dt>

[**DRM\_PLAY\_OPL\_EX**](drm-play-opl-ex.md)
</dt> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





