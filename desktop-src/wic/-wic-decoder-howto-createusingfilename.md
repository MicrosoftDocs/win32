---
description: This topic describes how to create a bitmap decoder by using an image filename.
ms.assetid: b384861d-4e71-4e07-8b44-5c1cbcb3a70f
title: How to Create a Decoder Using an Image Filename
ms.topic: article
ms.date: 05/31/2018
---

# How to Create a Decoder Using an Image Filename

This topic describes how to create a bitmap decoder by using an image filename.

To create a bitmap decoder by using an image filename

1.  Create an [**IWICImagingFactory**](/windows/desktop/api/Wincodec/nn-wincodec-iwicimagingfactory) object to create Windows Imaging Component (WIC) objects.

    ```C++
    // Create WIC factory
    hr = CoCreateInstance(
        CLSID_WICImagingFactory,
        NULL,
        CLSCTX_INPROC_SERVER,
        IID_PPV_ARGS(&m_pIWICFactory)
        );
    ```

    

2.  Use the [**CreateDecoderFromFilename**](/windows/desktop/api/Wincodec/nf-wincodec-iwicimagingfactory-createdecoderfromfilename) method to create an [**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder) from an image file.

    ```C++
    HRESULT hr = S_OK;

    IWICBitmapDecoder *pIDecoder = NULL;
    IWICBitmapFrameDecode *pIDecoderFrame  = NULL;

    hr = m_pIWICFactory->CreateDecoderFromFilename(
       L"turtle.jpg",                  // Image to be decoded
       NULL,                           // Do not prefer a particular vendor
       GENERIC_READ,                   // Desired read access to the file
       WICDecodeMetadataCacheOnDemand, // Cache metadata when needed
       &pIDecoder                      // Pointer to the decoder
       );
    ```

    

3.  Get the first [**IWICBitmapFrameDecode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframedecode) of the image.

    ```C++
    // Retrieve the first bitmap frame.
    if (SUCCEEDED(hr))
    {
       hr = pIDecoder->GetFrame(0, &pIDecoderFrame);
    }
    ```

    

    The JPEG file format only supports a single frame. Because the file in this example is a JPEG file, the first frame (`0`) is used. For image formats that have multiple frames, see [How to Retrieve the Frames of an Image](-wic-bitmapsources-howto-retrieveimageframes.md) for accessing each frame of the image.

4.  Process the image frame. For additional information about [**IWICBitmapSource**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsource) objects, see the [Bitmap Sources Overview](-wic-bitmapsources.md).

## See Also

[Programming Guide](-wic-programming-guide.md)


[Reference](-wic-codec-reference.md)


[Samples](-wic-samples.md)


 

 



