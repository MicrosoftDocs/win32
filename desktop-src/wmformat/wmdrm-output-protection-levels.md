---
title: WMDRM_OUTPUT_PROTECTION_LEVELS structure (Wmdrmsdk.h)
description: The WMDRM\_OUTPUT\_PROTECTION\_LEVELS structure contains the output protections levels (OPLs) required by a license to perform various actions.
ms.assetid: 6b284180-1033-4c57-b010-6d4ab4bc593a
keywords:
- WMDRM_OUTPUT_PROTECTION_LEVELS structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WMDRM_OUTPUT_PROTECTION_LEVELS
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRM\_OUTPUT\_PROTECTION\_LEVELS structure

The **WMDRM\_OUTPUT\_PROTECTION\_LEVELS** structure contains the output protections levels (OPLs) required by a license to perform various actions.

## Syntax


```C++
typedef struct WMDRM_OUTPUT_PROTECTION_LEVELS {
  WORD wCompressedDigitalVideo;
  WORD wUncompressedDigitalVideo;
  WORD wAnalogVideo;
  WORD wCompressedDigitalAudio;
  WORD wUncompressedDigitalAudio;
  WORD wMinimumCopyProtectionLevel;
} ;
```



## Members

<dl> <dt>

**wCompressedDigitalVideo**
</dt> <dd>

Minimum OPL required to receive compressed digital video.

</dd> <dt>

**wUncompressedDigitalVideo**
</dt> <dd>

Minimum OPL required to receive uncompressed digital video.

</dd> <dt>

**wAnalogVideo**
</dt> <dd>

Minimum OPL required to receive analog video.

</dd> <dt>

**wCompressedDigitalAudio**
</dt> <dd>

Minimum OPL required to receive compressed digital audio.

</dd> <dt>

**wUncompressedDigitalAudio**
</dt> <dd>

Minimum OPL required to receive uncompressed digital audio.

</dd> <dt>

**wMinimumCopyProtectionLevel**
</dt> <dd>

Minimum OPL required to copy the content.

</dd> </dl>

## Remarks

This structure is used by the [**IWMDRMLicense::GetOutputProtectionLevels**](iwmdrmlicense-getoutputprotectionlevels.md) method.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](drm-structures.md)
</dt> </dl>

 

 





