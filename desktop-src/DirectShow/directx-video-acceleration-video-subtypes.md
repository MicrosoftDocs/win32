---
description: The following subtypes are used by decoders that are using DirectX Video Acceleration (DXVA).
ms.assetid: 031b076b-cdfa-407f-8efa-391bce3075ef
title: DirectX Video Acceleration Video Subtypes (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# DirectX Video Acceleration Video Subtypes

The following subtypes are used by decoders that are using DirectX Video Acceleration (DXVA). AI44 and IA44 are surfaces with a bits-per-pixel value of 8. There are 4 bits of I and 4 bits of *A*. *I* represents an index into a 16-entry YUV palette. *A* represents 4 bits of transparency information (also known as per-pixel-alpha). Therefore, AI44 and IA44 surfaces allow for 16 different colors at 16 different transparency values, or 256 different pixel representations. With AI44 the alpha is stored in the hi-nibble, in IA44 the alpha is stored in the lo-nibble. Both formats are very useful for DVD sub-picture images and Line21 and Teletext images. Microsoft prefers the AI44 version because it is slightly easier to generate text using this format.

| Subtype            | Description                                                 |
|--------------------|-------------------------------------------------------------|
| MEDIASUBTYPE\_AI44 | For subpicture and text overlays. See previous description. |
| MEDIASUBTYPE\_IA44 | For subpicture and text overlays. See previous description. |



 

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Video Subtypes](video-subtypes.md)
</dt> </dl>

 

 




