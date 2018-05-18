---
Description: 'This section of topics provide developers with guidance on how to implement image file format codecs that will function within the Windows Imaging Component (WIC) framework.'
ms.assetid: '58f03dc2-cc31-4d76-b75a-f332da1f900f'
title: 'How to Write a WIC-Enabled Codec'
---

# How to Write a WIC-Enabled Codec

This section of topics provide developers with guidance on how to implement image file format codecs that will function within the Windows Imaging Component (WIC) framework.

<dl>

[Introduction](-wic-howtowriteacodec-intro.md)  
[How The Windows Imaging Component (WIC) Works](-wic-howwicworks.md)  
<dl>

[Discovery and Arbitration](-wic-howwicworks.md)  
[Decoding](-wic-howwicworks.md)  
[Encoding](-wic-howwicworks.md)  
[The Lifetime of a Codec](-wic-howwicworks.md)  
[How to WIC-enable a Codec](-wic-howwicworks.md)  
[Multi-Threaded Apartment Support in WIC](-wic-howwicworks.md)  
</dl> </dd> [Implementing a WIC-Enabled Decoder](-wic-implementingwicdecoder.md)<dl>

[Decoder Interfaces](-wic-decoderinterfaces.md)<dl>

[IWICBitmapDecoder](-wic-imp-iwicbitmapdecoder.md)  
[IWICBitmapCodecProgressNotification](-wic-imp-iwicbitmapcodecprogressnotification-decoder.md)  
[IWICBitmapSource](-wic-imp-iwicbitmapsource.md)  
[IWICBitmapFrameDecode](-wic-imp-iwicbitmapframedecode.md)  
[IWICMetadataBlockReader](-wic-imp-iwicmetadatablockreader.md)  
[IWICBitmapSourceTransform](-wic-imp-iwicbitmapsourcetransform.md)  
[IWICDevelopRaw](-wic-imp-iwicdevelopraw.md)  
</dl> </dd> </dl> </dd> [Implementing a WIC-Enabled Encoder](-wic-implementingwicencoder.md)  
<dl>

[Encoder Interfaces](-wic-encoderinterfaces.md)  
<dl>

[IWICBitmapEncoder](-wic-imp-iwicbitmapencoder.md)  
[IWICBitmapCodecProgressNotification](-wic-imp-iwicbitmapcodecprogressnotification-encoder.md)  
[IWICBitmapFrameEncode](-wic-imp-iwicbitmapframeencode.md)  
[IWICMetadataBlockWriter](-wic-imp-iwicmetadatablockwriter.md)  
</dl> </dd> </dl> </dd> [Codec Installation and Registration](-wic-codecinstallandreg.md)  
<dl>

[Registering a Codec](-wic-codecinstallandreg.md)  
<dl>

[General Register Entries](-wic-generalregentries.md)  
[Encoder-Specific Registry Entries](-wic-encoderregentries.md)  
<dl>

[Registering a Container Format with Metadata Writers](-wic-encoderregentries.md)  
</dl> </dd> [Encoder-Specific Registry Entries](-wic-decoderregentries.md)  
<dl>

[Registering a New Container Format with Metadata Readers](-wic-decoderregentries.md)  
</dl> </dd> [Integration with Windows Vista PhotoGallery and Explorer](-wic-integrationregentries.md)  
<dl>

[Windows Property Store](-wic-integrationregentries.md)  
[Windows Vista Photo Gallery](-wic-integrationregentries.md)  
[Windows Vista Thumbnail Cache](-wic-integrationregentries.md)  
</dl> </dd> </dl> </dd> [Updating the Thumbnail Cache when Installing a Codec](-wic-codecinstallandreg.md)  
[Making Your WIC-Enabled Codec Available to Users](-wic-codecinstallandreg.md)  
</dl> </dd> [Conclusion](-wic-howtowriteacodec-conclusion.md)  
</dl>

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Introduction (How to Write a WIC-Enabled CODEC)](-wic-howtowriteacodec-intro.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 



