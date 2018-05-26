---
Description: Encoding
ms.assetid: 501e63bf-26ef-42fb-b181-f1a8b26c122c
title: Encoding
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Encoding

The encoder author must do the following:

-   Implement [**IWICBitmapEncoder**](/windows/win32/wincodec/nn-wincodec-iwicbitmapencoder?branch=master) and [**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master) interfaces.
-   Implement [**IWICMetadataBlockWriter**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockwriter?branch=master) on the frame encoder. If the codec supports container-level metadata, this interface must be implemented on the container-level encoder as well as on the frame encoder.
-   If the container format implicitly contains any mandatory metadata blocks, instantiate a metadata writer for each such block. For example, the TIFF format requires an interface device (IFD) for each frame, so the IFD writer must always be exposed.
-   Implement support for managing the collection of metadata writers. The block writer manages any order requirements or container restrictions on the kinds of metadata blocks that can be encoded. The block writer must verify that any new metadata writers can be embedded within the container format.
-   When encoding the image stream, call [**WICSerializeMetadataContent**](/windows/win32/wincodecsdk/nf-wincodecsdk-wicserializemetadatacontent?branch=master) to serialize each metadata writer’s content into the stream. If the metadata block contains "critical" metadata the encoder must set the critical metadata items before asking the metadata writer to serialize content.
-   Check for any unknown metadata handlers to ensure that redundant metadata blocks are not present. This is important because, while preserving metadata in a decode or encode scenario, unknown blocks might be a duplicate of mandatory metadata blocks.

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

 

 



