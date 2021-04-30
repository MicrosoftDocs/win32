---
description: The Media Foundation DV video decoder is a Media Foundation Transform that decodes DV video.
ms.assetid: 97e5ba52-92fc-49e4-9c22-6f61bfda2003
title: DV Video Decoder
ms.topic: reference
ms.date: 05/31/2018
---

# DV Video Decoder

The Media Foundation DV video decoder is a [Media Foundation Transform](media-foundation-transforms.md) that decodes DV video.

The DV video decoder supports the following input types:



| Subtype                 | Description                  |
|-------------------------|------------------------------|
| **MFVideoFormat\_DVC**  | DVC/DV Video                 |
| **MFVideoFormat\_DVHD** | HD-DVCR (1125-60 or 1250-50) |
| **MFVideoFormat\_DVSD** | SDL-DVCR (525-60 or 625-50)  |
| **MFVideoFormat\_DVSL** | SD-DVCR (525-60 or 625-50)   |



 

It supports a single output type:



| Subtype             | Description |
|---------------------|-------------|
| MFVideoFormat\_YUY2 | YUY2 video  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| DLL<br/>                      | <dl> <dt>Mfdvdec.dll</dt> </dl> |



## See also

<dl> <dt>

[Codec Objects](codecobjects.md)
</dt> <dt>

[Supported Media Formats in Media Foundation](supported-media-formats-in-media-foundation.md)
</dt> <dt>

[Video Media Types](video-media-types.md)
</dt> </dl>

 

 




