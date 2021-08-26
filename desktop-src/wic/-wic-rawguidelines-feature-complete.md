---
description: 'Feature Completeness: Recommended Interfaces'
ms.assetid: 759bf253-7450-4895-a550-9f81f3498f79
title: 'Feature Completeness: Recommended Interfaces'
ms.topic: article
ms.date: 05/31/2018
---

# Feature Completeness: Recommended Interfaces

The following table lists the Windows Imaging Component (WIC) interfaces RAW codecs should implement.




| Interface | Required for | Description | 
|-----------|--------------|-------------|
| <a href="/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder"><strong>IWICBitmapDecoder</strong></a> | Decoders | Represents the starting point for decoding an image file. Provides access to container-level properties like thumbnails, frames, and palette.<br /> | 
| <a href="/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode"><strong>IWICBitmapFrameDecode</strong></a> | Decoders | Represents a specific image frame within the container that provides access to frame-level properties. This is the interface that decodes the actual image bits.<br /> | 
| <a href="/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader"><strong>IWICMetadataBlockReader</strong></a> | Decoders | Required for enumerating and iterating through metadata blocks and invoking the appropriate metadata readers when reading from an image file. <br /><div class="NOTE"><p>NOTE</p><p>If the RAW container format is TIFF compatible or uses standard IFDs or IRBs to store EXIF or XMP metadata, codec authors can choose to invoke the built-in metadata readers rather than writing their own.</p></div> | 
| <a href="/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsourcetransform"><strong>IWICBitmapSourceTransform</strong></a> | Decoders | Allows the caller to specify desired scaling, cropping, rotation, or pixel format for the decoded image, which can significantly improve decoder performance. For example, Microsoft's JPEG and Wireless Datagram Protocol (WDP) decoders use a pyramid optimization scheme to achieve faster decoding when the target bitmap is smaller than the source bitmap. Windows Vista (and later) will attempt to use this interface to extract a "fast" preview from a RAW image whenever the embedded preview is missing or less than 1,024 pixels in its largest dimension.<br /> | 
| <a href="/windows/desktop/api/Wincodec/nn-wincodec-iwicdevelopraw"><strong>IWICDevelopRaw</strong></a> | Decoders | Required for RAW formats. Exposes parameters that are specific to RAW image processing. RAW codecs should support as many of these parameters as apply to the codec.<br /> | 
| <a href="/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder"><strong>IWICBitmapEncoder</strong></a> | Encoders | Represents the starting point for encoding an image file. This interface is used for setting container-level properties, such as thumbnails, frames, and palette. It is also required to invoke a metadata writer to enable metadata persistence to the image file. For these reasons, this interface is necessary even if encoding the primary bitmap to the RAW format is not supported.<br /> | 
| <a href="/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframeencode"><strong>IWICBitmapFrameEncode</strong></a> | Encoders | Represents a specific image frame within the container. This interface is used to encode the actual image bits and to set per-frame metadata and properties.<br /> | 
| <a href="/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockwriter"><strong>IWICMetadataBlockWriter</strong></a> | Encoders | Required for iterating through metadata blocks and invoking the appropriate metadata writers when serializing an image file.<br /><div class="NOTE"><p>NOTE</p><p>If the RAW container format is TIFF-compatible, codec authors can choose to invoke the built-in metadata writers rather than writing their own.</p></div> | 




 

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

 

 




