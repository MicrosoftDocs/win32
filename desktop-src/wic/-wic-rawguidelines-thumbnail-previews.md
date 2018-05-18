---
Description: Thumbnails and Previews
ms.assetid: 'e45f025e-a1ac-47c8-b794-ab1402ab35fb'
title: Thumbnails and Previews
---

# Thumbnails and Previews

Windows Vista and the Windows Photo Gallery rely on Windows Imaging Component (WIC) to render fast thumbnails and previews of images. To support fast thumbnail and preview rendering, RAW codecs must implement the WIC[**GetThumbnail**](-wic-codec-iwicbitmapdecoder-getthumbnail.md) and [**GetPreview**](-wic-codec-iwicbitmapdecoder-getpreview.md) interfaces. To support a responsive user experience, it is highly desirable that these interfaces return an [**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md) to the caller in 200 milliseconds or less.

Microsoft strongly recommends that RAW file format owners generate a prerendered preview and cache this in the image file. For an in-device format, this is usually done at capture time. However, previews could also be regenerated and stored in the image file whenever [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) interface properties are changed-if it does not take too much work to do so.

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

 

 



