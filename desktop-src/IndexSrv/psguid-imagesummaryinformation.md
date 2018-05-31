---
title: PSGUID\_IMAGESUMMARYINFORMATION
description: PSGUID\_IMAGESUMMARYINFORMATION
ms.assetid: 5ad7c1be-affa-4e6d-a4f4-eaa38041346e
keywords:
- PSGUID_IMAGESUMMARYINFORMATION
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PSGUID\_IMAGESUMMARYINFORMATION

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The PSGUID\_IMAGESUMMARYINFORMATION property set defines properties for image files.

``` syntax
#define PSGUID_IMAGESUMMARYINFORMATION {0x6444048fL, 0x4c8b, 0x11d1, \
    0x8b, 0x70, 0x8, 0x00, 0x36, 0xb1, 0x1a, 0x03}
```

### Remarks

The PSGUID\_IMAGESUMMARYINFORMATION property set contains the following property constants:

<dl> <dt>

<span id="PIDISI_FILETYPE"></span><span id="pidisi_filetype"></span>PIDISI\_FILETYPE
</dt> <dd>

Property ID 0x00000002L. Indicates the image file type.

</dd> <dt>

<span id="PIDISI_CX"></span><span id="pidisi_cx"></span>PIDISI\_CX
</dt> <dd>

Property ID 0x00000003L. Indicates the Cx value for the image.

</dd> <dt>

<span id="PIDISI_CY"></span><span id="pidisi_cy"></span>PIDISI\_CY
</dt> <dd>

Property ID 0x00000004L. Indicates the Cy value for the image.

</dd> <dt>

<span id="PIDISI_RESOLUTIONX"></span><span id="pidisi_resolutionx"></span>PIDISI\_RESOLUTIONX
</dt> <dd>

Property ID 0x00000005L. Indicates the x resolution for the image.

</dd> <dt>

<span id="PIDISI_RESOLUTIONY"></span><span id="pidisi_resolutiony"></span>PIDISI\_RESOLUTIONY
</dt> <dd>

Property ID 0x00000006L. Indicates the y resolution for the image.

</dd> <dt>

<span id="PIDISI_BITDEPTH"></span><span id="pidisi_bitdepth"></span>PIDISI\_BITDEPTH
</dt> <dd>

Property ID 0x00000007L. Indicates the bit depth for the image.

</dd> <dt>

<span id="PIDISI_COLORSPACE"></span><span id="pidisi_colorspace"></span>PIDISI\_COLORSPACE
</dt> <dd>

Property ID 0x00000008L. Indicates the color space for the image.

</dd> <dt>

<span id="PIDISI_COMPRESSION"></span><span id="pidisi_compression"></span>PIDISI\_COMPRESSION
</dt> <dd>

Property ID 0x00000009L. Indicates the image compression level.

</dd> <dt>

<span id="PIDISI_TRANSPARENCY"></span><span id="pidisi_transparency"></span>PIDISI\_TRANSPARENCY
</dt> <dd>

Property ID 0x0000000AL. Indicates image transparency.

</dd> <dt>

<span id="PIDISI_GAMMAVALUE"></span><span id="pidisi_gammavalue"></span>PIDISI\_GAMMAVALUE
</dt> <dd>

Property ID 0x0000000BL. Indicates the gamma value for the image.

</dd> <dt>

<span id="PIDISI_FRAMECOUNT"></span><span id="pidisi_framecount"></span>PIDISI\_FRAMECOUNT
</dt> <dd>

Property ID 0x0000000CL. Indicates the frame count for the image.

</dd> <dt>

<span id="PIDISI_DIMENSIONS"></span><span id="pidisi_dimensions"></span>PIDISI\_DIMENSIONS
</dt> <dd>

Property ID 0x0000000DL. Indicates the dimensions of the image.

</dd> </dl>

## Related topics

<dl> <dt>

[PSGUID\_AUDIO](psguid-audio.md)
</dt> <dt>

[PSGUID\_DRM](psguid-drm.md)
</dt> <dt>

[PSGUID\_MUSIC](psguid-music.md)
</dt> <dt>

[PSGUID\_VIDEO](psguid-video.md)
</dt> </dl>

 

 




