---
Description: Decoding
ms.assetid: 'ff7e5e66-e1ea-49fc-909f-de361214afc3'
title: Decoding
---

# Decoding

To properly support metadata, decoder authors must do the following:

-   Implement [**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md) and [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md) interfaces.
-   Implement [**IWICMetadataBlockReader**](-wic-codec-iwicmetadatablockreader.md) on the frame decoder. If the codec supports container-level metadata, this interface must be implemented on the container-level decoder as well as on the frame decoder.
-   While decoding the image stream, call [**IWICComponentFactory**](-wic-codec-iwiccomponentfactory.md)::[**CreateMetadataReaderFromContainer**](-wic-codec-iwiccomponentfactory-createmetadatareaderfromcontainer.md) to instantiate a metadata reader for each metadata block. (Any new metadata readers that the codec implements must be registered with WIC.)

    The decoder should not create metadata readers on its own, but rather use WIC to create them based on the metadata blocks in the stream. The decoder must do this on all blocks that it finds, even if they are not natively known to the docoder, because future metadata readers might be installed on the system that do understand how to handle these metadata blocks.

-   If there is no metadata handler for a block, instantiate the unknown metadata reader by using the metadata creation options.
-   Expose the collection of metadata readers through the [**IWICMetadataBlockReader**](-wic-codec-iwicmetadatablockreader.md) interface.

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

 

 



