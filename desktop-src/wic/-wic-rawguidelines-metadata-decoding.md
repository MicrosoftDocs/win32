---
Description: Decoding
ms.assetid: ff7e5e66-e1ea-49fc-909f-de361214afc3
title: Decoding
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Decoding

To properly support metadata, decoder authors must do the following:

-   Implement [**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master) and [**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master) interfaces.
-   Implement [**IWICMetadataBlockReader**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader?branch=master) on the frame decoder. If the codec supports container-level metadata, this interface must be implemented on the container-level decoder as well as on the frame decoder.
-   While decoding the image stream, call [**IWICComponentFactory**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwiccomponentfactory?branch=master)::[**CreateMetadataReaderFromContainer**](/windows/win32/Wincodecsdk/nf-wincodecsdk-iwiccomponentfactory-createmetadatareaderfromcontainer?branch=master) to instantiate a metadata reader for each metadata block. (Any new metadata readers that the codec implements must be registered with WIC.)

    The decoder should not create metadata readers on its own, but rather use WIC to create them based on the metadata blocks in the stream. The decoder must do this on all blocks that it finds, even if they are not natively known to the docoder, because future metadata readers might be installed on the system that do understand how to handle these metadata blocks.

-   If there is no metadata handler for a block, instantiate the unknown metadata reader by using the metadata creation options.
-   Expose the collection of metadata readers through the [**IWICMetadataBlockReader**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader?branch=master) interface.

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

 

 



