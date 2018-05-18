---
Description: 'This topic demonstrates how to rotate an IWICBitmapSource by using an IWICBitmapFlipRotator component.'
ms.assetid: '371c7759-0165-4a2a-b2ff-f9c8a31053a4'
title: How to Flip and Rotate a Bitmap Source
---

# How to Flip and Rotate a Bitmap Source

This topic demonstrates how to rotate an [**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md) by using an [**IWICBitmapFlipRotator**](-wic-codec-iwicbitmapfliprotator.md) component.

To flip and rotate a bitmap source

1.  Create an [**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md) object to create Windows Imaging Component (WIC) objects.

    ```C++
    // Create WIC factory
    hr = CoCreateInstance(
        CLSID_WICImagingFactory,
        NULL,
        CLSCTX_INPROC_SERVER,
        IID_PPV_ARGS(&amp;m_pIWICFactory)
        );
    ```

    

2.  Use the [**CreateDecoderFromFilename**](-wic-codec-iwicimagingfactory-createdecoderfromfilename.md) method to create an [**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md) from an image file.

    ```C++
    HRESULT hr = S_OK;

    IWICBitmapDecoder *pIDecoder = NULL;
    IWICBitmapFrameDecode *pIDecoderFrame  = NULL;
    IWICBitmapFlipRotator *pIFlipRotator = NULL;

    hr = m_pIWICFactory->CreateDecoderFromFilename(
       L"turtle.jpg",                  // Image to be decoded
       NULL,                           // Do not prefer a particular vendor
       GENERIC_READ,                   // Desired read access to the file
       WICDecodeMetadataCacheOnDemand, // Cache metadata when needed
       &amp;pIDecoder                      // Pointer to the decoder
       );
    ```

    

3.  Get the first [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md) of the image.

    ```C++
    // Retrieve the first bitmap frame.
    if (SUCCEEDED(hr))
    {
       hr = pIDecoder->GetFrame(0, &amp;pIDecoderFrame);
    }
    ```

    

    The JPEG file format only supports a single frame. Because the file in this example is a JPEG file, the first frame (`0`) is used. For image formats that have multiple frames, see [How to Retrieve the Frames of an Image](-wic-bitmapsources-howto-retrieveimageframes.md) for accessing each frame of the image.

4.  Create the [**IWICBitmapFlipRotator**](-wic-codec-iwicbitmapfliprotator.md) to use for flipping the image.

    ```C++
    // Create the flip/rotator.
    if (SUCCEEDED(hr))
    {
       hr = m_pIWICFactory->CreateBitmapFlipRotator(&amp;pIFlipRotator);
    }
    ```

    

5.  Initialize the flip/rotator object with the image data of the bitmap frame flipped horizontally (along the vertical y-axis).

    ```C++
    // Initialize the flip/rotator to flip the original source horizontally.
    if (SUCCEEDED(hr))
    {
       hr = pIFlipRotator->Initialize(
          pIDecoderFrame,                     // Bitmap source to flip.
          WICBitmapTransformFlipHorizontal);  // Flip the pixels along the 
                                              //  vertical y-axis.
    }
    ```

    

    See [**WICBitmapTransformOptions**](-wic-codec-wicbitmaptransformoptions.md) for additional rotations and flipping options.

6.  Draw or process the flipped bitmap source.

    > [!Note]  
    > The [**IWICBitmapFlipRotator**](-wic-codec-iwicbitmapfliprotator.md) interface inherits from the [**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md) interface, so you can use the initialized flip/rotator object anywhere that accepts a **IWICBitmapSource**.

     

    The following illustration demonstrates flipping an imaging horizontally (along the vertical x-axis).

    ![illustration showing a horizontal flip (along the verital x-axis) of an image](graphics/fliphorizontal.png)

## See Also

[Programming Guide](-wic-programming-guide.md)


[Reference](-wic-codec-reference.md)


[Samples](-wic-samples.md)


 

 



