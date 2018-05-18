---
Description: 'This topic demonstrates how to modify the pixels of a bitmap source using the IWICBitmap and IWICBitmapLock components.'
ms.assetid: 'a08af015-bc42-4a31-af03-106714b08d08'
title: How to Modify the Pixels of a Bitmap Source
---

# How to Modify the Pixels of a Bitmap Source

This topic demonstrates how to modify the pixels of a bitmap source using the [**IWICBitmap**](-wic-codec-iwicbitmap.md) and [**IWICBitmapLock**](-wic-codec-iwicbitmaplock.md) components.

To modify the pixels of a bitmap source

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

4.  Create an [**IWICBitmap**](-wic-codec-iwicbitmap.md) from the previously obtained image frame.

    ```C++
    IWICBitmap *pIBitmap = NULL;
    IWICBitmapLock *pILock = NULL;

    UINT uiWidth = 10;
    UINT uiHeight = 10;

    WICRect rcLock = { 0, 0, uiWidth, uiHeight };

    // Create the bitmap from the image frame.
    if (SUCCEEDED(hr))
    {
       hr = m_pIWICFactory->CreateBitmapFromSource(
          pIDecoderFrame,          // Create a bitmap from the image frame
          WICBitmapCacheOnDemand,  // Cache metadata when needed
          &amp;pIBitmap);              // Pointer to the bitmap
    }
    ```

    

5.  Obtain an [**IWICBitmapLock**](-wic-codec-iwicbitmaplock.md) for a specified rectangle of the [**IWICBitmap**](-wic-codec-iwicbitmap.md).

    ```C++
    if (SUCCEEDED(hr))
    {
       // Obtain a bitmap lock for exclusive write.
       // The lock is for a 10x10 rectangle starting at the top left of the
       // bitmap.
       hr = pIBitmap->Lock(&amp;rcLock, WICBitmapLockWrite, &amp;pILock);
    ```

    

6.  Process the pixel data that is now locked by the [**IWICBitmapLock**](-wic-codec-iwicbitmaplock.md) object.

    ```C++
       if (SUCCEEDED(hr))
       {
          UINT cbBufferSize = 0;
          BYTE *pv = NULL;

          // Retrieve a pointer to the pixel data.
          if (SUCCEEDED(hr))
          {
             hr = pILock->GetDataPointer(&amp;cbBufferSize, &amp;pv);
          }
          
          // Pixel manipulation using the image data pointer pv.
          // ...

          // Release the bitmap lock.
          SafeRelease(&amp;pILock);
       }
    }
    ```

    

    To unlock the [**IWICBitmap**](-wic-codec-iwicbitmap.md), call [IUnknown::Release](http://msdn.microsoft.com/en-us/library/ms682317(VS.85).aspx) on all [**IWICBitmapLock**](-wic-codec-iwicbitmaplock.md) objects associated with the **IWICBitmap**.

7.  Clean up created objects.

    ```C++
    SafeRelease(&amp;pIBitmap);
    SafeRelease(&amp;pIDecoder);
    SafeRelease(&amp;pIDecoderFrame);
    ```

    

## See Also

[Programming Guide](-wic-programming-guide.md)


[Reference](-wic-codec-reference.md)


[Samples](-wic-samples.md)


 

 



