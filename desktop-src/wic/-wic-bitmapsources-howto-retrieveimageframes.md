---
Description: 'This topic demonstrates how to decode a multi-frame image and retrieve each frame for processing.'
ms.assetid: 'e4f69608-7bf1-4d54-b586-b749526700c9'
title: How to Retrieve the Frames from an Image
---

# How to Retrieve the Frames from an Image

This topic demonstrates how to decode a multi-frame image and retrieve each frame for processing.

To retrieve the frames of an image

1.  Create an [**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md) to create Windows Imaging Component (WIC) objects.

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
    UINT nFrameCount = 0;
    UINT uiWidth, uiHeight;

    // Create decoder for an image.
    hr = m_pIWICFactory->CreateDecoderFromFilename(
       L"creek.tiff",                  // Image to be decoded
       NULL,                           // Do not prefer a particular vendor
       GENERIC_READ,                   // Desired read access to the file
       WICDecodeMetadataCacheOnDemand, // Cache metadata when needed
       &amp;pIDecoder                      // Pointer to the decoder
       );
    ```

    

3.  Retrieve the number of frames in the images.

    ```C++
    // Retrieve the frame count of the image.
    if (SUCCEEDED(hr))
    {
       hr = pIDecoder->GetFrameCount(&amp;nFrameCount);
    }
    ```

    

4.  Process each frame by obtaining an [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md) for each frame in the image.

    ```C++
    // Process each frame in the image.
    for (UINT i=0; i < nFrameCount; i++)
    {
       // Retrieve the next bitmap frame.
       if (SUCCEEDED(hr))
       {
          hr = pIDecoder->GetFrame(i, &amp;pIDecoderFrame);
       }

       // Retrieve the size of the bitmap frame.
       if (SUCCEEDED(hr))
       {
          hr = pIDecoderFrame->GetSize(&amp;uiWidth, &amp;uiHeight);
       }

       // Additional frame processing.
       // ...

       SafeRelease(&amp;pIDecoderFrame);
    }
    ```

    

## See Also

[Programming Guide](-wic-programming-guide.md)


[Reference](-wic-codec-reference.md)


[Samples](-wic-samples.md)


 

 



