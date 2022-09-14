---
title: DRM_PLAY_OPL_EX structure (Wmdrmsdk.h)
description: The DRM\_PLAY\_OPL\_EX structure holds information about the output protection levels (OPLs) specified in a license for play actions.
ms.assetid: 287f6681-f12e-4ef3-b802-24ee7b94bc7f
keywords:
- DRM_PLAY_OPL_EX structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_PLAY_OPL_EX
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_PLAY\_OPL\_EX structure

The **DRM\_PLAY\_OPL\_EX** structure holds information about the output protection levels (OPLs) specified in a license for play actions.

## Syntax


```C++
typedef struct DRM_PLAY_OPL_EX {
  DWORD                                dwVersion;
  DRM_MINIMUM_OUTPUT_PROTECTION_LEVELS minOPL;
  DRM_OPL_OUTPUT_IDS                   oplIdReserved;
  DRM_VIDEO_OUTPUT_PROTECTION_IDS_EX   vopi;
} ;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

Version number.

</dd> <dt>

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

## Remarks

This structure is identical to the **DRM\_PLAY\_OPL** structure, except that it includes a version number.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**DRM\_PLAY\_OPL**](drmdrm-play-opl.md)
</dt> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





