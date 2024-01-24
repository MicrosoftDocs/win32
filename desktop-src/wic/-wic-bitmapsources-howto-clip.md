---
description: This topic demonstrates how to obtain a rectangular portion of an IWICBitmapSource using an IWICBitmapClipper component.
ms.assetid: c9834827-8e1d-436d-be82-c1a2a2f7ca5c
title: How to Clip a Bitmap Source
ms.topic: article
ms.date: 05/31/2018
---

# How to Clip a Bitmap Source

This topic demonstrates how to obtain a rectangular portion of an [**IWICBitmapSource**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsource) using an [**IWICBitmapClipper**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapclipper) component.

To clip a bitmap source

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

4.  Create the [**IWICBitmapClipper**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapclipper) to use for the image clipping.

    ```C++
    IWICBitmapClipper *pIClipper = NULL;

    if (SUCCEEDED(hr))
    {
       hr = m_pIWICFactory->CreateBitmapClipper(&pIClipper);
    }
    ```

    

5.  Initialize the clipper object with the image data within the given rectangle of the bitmap frame.

    ```C++
    // Create the clipping rectangle.
    WICRect rcClip = { 0, 0, uiWidth/2, uiHeight/2 };

    // Initialize the clipper with the given rectangle of the frame's image data.
    if (SUCCEEDED(hr))
    {
       hr = pIClipper->Initialize(pIDecoderFrame, &rcClip);
    }
    ```

    

6.  Draw or process the clipped image.

    The following illustration demonstrates imaging clipping. The original image on the left is 200 x 130 pixels. The image on the right is the original image clipped to a rectangle defined as `{20,20,100,100}`.

    ![illustration of imaging clipping](graphics/cliparegion_axisalignedclip.png)

## See Also

[Programming Guide](-wic-programming-guide.md)


[Reference](-wic-codec-reference.md)


[Samples](-wic-samples.md)


 

 



