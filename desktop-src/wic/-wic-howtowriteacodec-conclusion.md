---
description: Building your codec on the Windows Imaging Component (WIC) platform makes it possible for all applications built on WIC to get the same platform support for your image format that they get for the common image formats shipped with the platform.
ms.assetid: 4f25f0f4-246c-4cbd-bd11-d061dbc7de45
title: Conclusion (How to Write a WIC-Enabled Codec)
ms.topic: article
ms.date: 05/31/2018
---

# Conclusion (How to Write a WIC-Enabled Codec)

Building your codec on the Windows Imaging Component (WIC) platform makes it possible for all applications built on WIC to get the same platform support for your image format that they get for the common image formats shipped with the platform. It also enables the Windows Vista Photo Gallery, Windows Explorer, and Photo Viewer to display thumbnails and previews of images in your format using the decoder that you provide. For raw formats, it enables more sophisticated imaging applications to take advantage of your decoder’s raw processing capabilities. Depending on the encoder options you support, you can also expose unique capabilities of your encoder to enable applications to take full advantage of the advanced features of your image format.

Developing a WIC-enabled codec requires you to implement some new interfaces. In many cases, you can write a wrapper for your existing codec that implements these interfaces. When you install your codec, you must make some registry entries to make your codec discoverable by the WIC platform and associate it with the appropriate metadata handlers. You also need to invoke an API to clear the thumbnail cache of any default (empty) thumbnails that may have previously associated with images in your format. If you want, you can enable the Windows Vista Photo Gallery to provide users with a link to download your codec when the Photo Gallery encounters an image with your file name extension. To do this, you must provide Microsoft with information about your codec’s file name extension and the URL for your download site.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[CODEC Installation and Registration](-wic-codecinstallandreg.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 



