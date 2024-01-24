---
description: Implementing a WIC-Enabled Encoder
ms.assetid: 9c1a4fa4-30b9-445f-8aee-46711355ace7
title: Implementing a WIC-Enabled Encoder
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a WIC-Enabled Encoder

## Introduction

Implementing a Windows Imaging Component (WIC) encoder requires writing two classes, as is also true for implementing a WIC decoder. The interfaces on these classes correspond directly to the encoder responsibilities outlined in the [Encoding](-wic-howwicworks.md) section of How The Windows Imaging Component Works.

One of the classes provides container-level services and manages the serialization of the individual image frames within the container. This class implements the [**IWICBitmapEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder) interface. If your image format supports container-level metadata, you must also implement the [**IWICMetadataBlockWriter**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockwriter) interface on this class.

The other class provides frame-level services and does the actual encoding of the image bits for each frame in the container. It also iterates through the metadata blocks for each frame and requests the appropriate metadata writers to serialize the blocks. This class implements the **IWICBitmapFrameEncode** interface and the [**IWICMetadataBlockWriter**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockwriter) interface. This class should have an IStream member that the container-level class initializes on instantiation, into which the **Commit** method will serialize the frame data.

In some cases, such as raw formats, the codec author may not want applications to be able to encode or re-encode to the raw format, because the purpose of a raw file is to contain the sensor data exactly as it came from the camera. In cases where the codec author doesn’t want to enable encoding, it is still necessary to implement a rudimentary encoder just to enable adding metadata. In that case, the encoder need only support those methods necessary for writing metadata, and can copy the image bits untouched from the decoder.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**IWICBitmapEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Implementing IWICDevelopRaw](-wic-imp-iwicdevelopraw.md)
</dt> <dt>

[Encoder Interfaces](-wic-encoderinterfaces.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 



