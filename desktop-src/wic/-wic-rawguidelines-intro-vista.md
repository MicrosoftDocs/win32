---
description: RAW Image Formats in Windows Vista
ms.assetid: e28b642c-03c8-4ecc-b5f5-e3911b8003a7
title: RAW Image Formats in Windows Vista
ms.topic: article
ms.date: 05/31/2018
---

# RAW Image Formats in Windows Vista

Windows Vista Explorer , Windows Vista Photo Gallery, Window Live Photo Gallery, and the Windows 7 Photo Viewer all use Windows Imaging Component (WIC) and therefore support RAW image formats when appropriate codecs are installed on the computer.

Because WIC is an extensible imaging architecture, any WIC application can consume new image formats as soon as new codecs are installed on the system. This makes WIC ideal as a Plug and Play solution for the RAW image formats that digital cameras produce. Through WIC, Windows applications can gain support for new camera models whenever updated codecs are made available (ideally in-box with new cameras). Codec authors can support these scenarios by implementing WIC interfaces that are common to all image types, as described in more detail in this document.

Today, most mainstream consumer applications have no special knowledge of RAW image formats and do not expose a user interface for adjusting RAW processing settings.

However, to support specialized imaging applications, RAW codec authors must also implement the [**IWICDevelopRaw**](/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw) interface. This interface exposes special features for RAW images, such as the ability to make common image adjustments and to process (develop) RAW images into specified red-green-blue (RGB) color spaces.

Several other WIC interfaces are important for RAW codec authors to implement. These are discussed in more detail in this series of topics.

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

 

 



