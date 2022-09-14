---
description: This topic demonstrates how to scale an IWICBitmapSource using the IWICBitmapScaler component.
ms.assetid: d2c65c9b-6f52-46f7-935d-0c582ca83867
title: How to Scale a Bitmap Source
ms.topic: article
ms.date: 05/31/2018
---

# How to Scale a Bitmap Source

This topic demonstrates how to scale an [**IWICBitmapSource**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapsource) using the [**IWICBitmapScaler**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapscaler) component.

To scale a bitmap source

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
    IWICBitmapScaler *pIScaler = NULL;


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

4.  Create the [**IWICBitmapScaler**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapscaler) to use for the image scaling.

    ```C++
    // Create the scaler.
    if (SUCCEEDED(hr))
    {
       hr = m_pIWICFactory->CreateBitmapScaler(&pIScaler);
    }
    ```

    

5.  Initialize the scaler object with the image data of the bitmap frame at half the size.

    ```C++
    // Initialize the scaler to half the size of the original source.
    if (SUCCEEDED(hr))
    {
       hr = pIScaler->Initialize(
          pIDecoderFrame,                    // Bitmap source to scale.
          uiWidth/2,                         // Scale width to half of original.
          uiHeight/2,                        // Scale height to half of original.
          WICBitmapInterpolationModeFant);   // Use Fant mode interpolation.
    }
    ```

    

6.  Draw or process the scaled bitmap source.

    The following illustration demonstrates imaging scaling. The original image on the left is 200 x 130 pixels. The image on the right is the original image scaled to half the size.

    ![illustration showing scaling an image to a smaller size](graphics/scaledregion.png)

## See Also

[Programming Guide](-wic-programming-guide.md)


[Reference](-wic-codec-reference.md)


[Samples](-wic-samples.md)


 

 



