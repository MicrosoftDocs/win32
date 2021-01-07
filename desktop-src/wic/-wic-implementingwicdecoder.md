---
description: "Learn more about: Implementing a WIC-Enabled Decoder"
ms.assetid: a26a592d-42ef-4690-95b4-48a5324be75a
title: Implementing a WIC-Enabled Decoder
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a WIC-Enabled Decoder


Implementing a Windows Imaging Component (WIC) decoder requires writing two classes. The interfaces on these classes correspond directly to the decoder responsibilities outlined in the [Decoding](-wic-howwicworks.md) section of [How The Windows Imaging Component Works](-wic-howwicworks.md).

One of the classes provides container-level services and implements the [IWICBitmapDecoder](-wic-imp-iwicbitmapdecoder.md) interface. If your image format supports container-level metadata, you must also implement the [IWICMetadataBlockReader](-wic-imp-iwicmetadatablockreader.md) interface on this class. It is recommended that you support the [IWICBitmapCodecProgressNotification](-wic-imp-iwicbitmapcodecprogressnotification-decoder.md) interface on both the decoder and encoder to support a better user experience.

The other class you will implement provides frame-level services and does the actual decoding of the image bits for each frame in the container. This class implements the [IWICBitmapFrameDecode](-wic-imp-iwicbitmapframedecode.md) interface and the [IWICMetadataBlockReader](-wic-imp-iwicmetadatablockreader.md) interface. If you are writing a decoder for a raw format, you also implement the [IWICDevelopRaw](-wic-imp-iwicdevelopraw.md) interface on this class. In addition to the required interfaces, it is highly recommended that you implement the [IWICBitmapSourceTransform](-wic-imp-iwicmetadatablockreader.md) interface on this class to enable the best possible performance for your image format.

One of the objects provided by WIC is the [**ImagingFactory**](/windows/desktop/api/Wincodec/nn-wincodec-iwicimagingfactory). You frequently use the [**IWICComponentFactory**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwiccomponentfactory) interface on this object to create various components. Because it is used frequently, you should keep a reference to it as a member property on both your decoder and encoder classes.


```C++
IWICImagingFactory* m_pImagingFactory = NULL;
IWICComponentFactory* m_pComponentFactory = NULL;
HRESULT hr;
      
hr = CoCreateInstance(CLSID_WICImagingFactory, NULL,
  CLSCTX_INPROC_SERVER, IID_IWICImagingFactory,
  (LPVOID*) m_pImagingFactory);

hr = m_pImagingFactory->QueryInterface(
  IID_IWICComponentFactory, (void**)&m_pComponentFactory);
```



## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[How The Windows Imaging Component Works](-wic-howwicworks.md)
</dt> <dt>

[Decoder Interfaces](-wic-decoderinterfaces.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[WIC Metadata Overview](-wic-about-metadata.md)
</dt> <dt>

[Encoding Overview](-wic-creating-encoder.md)
</dt> </dl>

 

 



