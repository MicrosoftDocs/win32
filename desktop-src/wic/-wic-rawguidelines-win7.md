---
description: RAW Codec Requirements for Windows 7
ms.assetid: 3f8bd336-ba03-4ffb-9aa2-ea55a276e3bc
title: RAW Codec Requirements for Windows 7
ms.topic: article
ms.date: 05/31/2018
---

# RAW Codec Requirements for Windows 7

The following codec features are required at a minimum:

All functionality that is required for Windows Vista shell and Photo Gallery support: thumbnail, preview, and (persisted) rotation. RAW processing should default to appropriate as-shot settings.

Support for core metadata (both read and write), Non-EXIF metadata, as well as EXIF metadata, should be persisted inside RAW file formats without use of sidecar files.

Support for the [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw) interface. For Windows 7, Windows Imaging Component (WIC)WIC requires that all parameter interfaces exposed by [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw) be implemented.

Orientation state support:

-   90 degree-step Image rotations should be applied by using the [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw)::[**SetRotation**](/windows/desktop/api/Wincodec/nf-wincodec-iwicdevelopraw-setrotation) method. Applications and Windows use this method to rotate the images (and cached thumbnails and previews).
-   Application of rotation by using this API should also be persisted by the codec (see earlier in this paper).
-   Applications can use the rotation capabilities of the [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform) API, but the codec will not serialize any rotation settings on this API, so rotations done using [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform) will not be persisted.

High-speed thumbnail and preview extraction support. If the preview maximum pixel dimension (width or height) is less than 1024 pixels in size, Windows Vista will request a render for screen preview:

-   The [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw)::[**SetRenderMode**](/windows/desktop/api/Wincodec/nf-wincodec-iwicdevelopraw-setrendermode) method should support at least the [**WICRawRenderQualityDraftMode**](/windows/desktop/api/Wincodec/ne-wincodec-wicrawrendermode) and [**WICRawRenderQualityBestQuality**](/windows/desktop/api/Wincodec/ne-wincodec-wicrawrendermode) modes to allow faster rendering of thumbnails and previews than the full-quality mode.
-   Windows will call [**IWICBitmapSourceTransform**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform)::[**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels) with the requested screen resolution size.
-   Screen resolution sizes must be supported in the above API.
-   Consistent image processing of thumbnail, preview, and full-image bits from [**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels) is required.

High dynamic range (HDR) pixel formats.

XML Paper Specification (XPS) printing.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[WIC Guidelines for Camera RAW Image Formats](-wic-rawguidelines.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> </dl>

 

 



