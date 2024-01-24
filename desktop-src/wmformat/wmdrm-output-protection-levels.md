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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMDRM\_OUTPUT\_PROTECTION\_LEVELS structure

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





