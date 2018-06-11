---
title: How to Load a Bitmap from a Resource
description: Shows how to load a Direct2D bitmap stored as an application resource.
ms.assetid: 7285e6ea-ebc7-4693-8a77-99bff0b5d0d1
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to Load a Bitmap from a Resource

As described in [How to Load a Bitmap from a File](how-to-load-a-direct2d-bitmap-from-a-file.md), Direct2D uses the Windows Imaging Component (WIC) to load bitmaps. To load a bitmap from a resource, use WIC objects to load the image and to convert it to a Direct2D-compatible format; then, use the [**CreateBitmapFromWicBitmap**](id2d1rendertarget-createbitmapfromwicbitmap.md) method to create an [**ID2D1Bitmap**](/windows/desktop/api/d2d1/).

1.  In the [application resource definition file](https://msdn.microsoft.com/library/windows/desktop/aa380599), define the resource. The following example defines a resource named "SampleImage".

    ```C++
    // THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
    // ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
    // THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
    // PARTICULAR PURPOSE.
    //
    // Copyright (c) Microsoft Corporation. All rights reserved
    #include "windows.h"

    SampleImage Image "sampleImage.jpg"
    
    ```

    

    This resource will be added to the application's resource file when the application is built.

2.  Load the image from the application resource file.

    ```C++
    HRESULT DemoApp::LoadResourceBitmap(
        ID2D1RenderTarget *pRenderTarget,
        IWICImagingFactory *pIWICFactory,
        PCWSTR resourceName,
        PCWSTR resourceType,
        UINT destinationWidth,
        UINT destinationHeight,
        ID2D1Bitmap **ppBitmap
        )
    {
        IWICBitmapDecoder *pDecoder = NULL;
        IWICBitmapFrameDecode *pSource = NULL;
        IWICStream *pStream = NULL;
        IWICFormatConverter *pConverter = NULL;
        IWICBitmapScaler *pScaler = NULL;

        HRSRC imageResHandle = NULL;
        HGLOBAL imageResDataHandle = NULL;
        void *pImageFile = NULL;
        DWORD imageFileSize = 0;

        // Locate the resource.
        imageResHandle = FindResourceW(HINST_THISCOMPONENT, resourceName, resourceType);
        HRESULT hr = imageResHandle ? S_OK : E_FAIL;
        if (SUCCEEDED(hr))
        {
            // Load the resource.
            imageResDataHandle = LoadResource(HINST_THISCOMPONENT, imageResHandle);

            hr = imageResDataHandle ? S_OK : E_FAIL;
        }
    ```

    

3.  Lock the resource and calculate the image's size.
    ```C++
        if (SUCCEEDED(hr))
        {
            // Lock it to get a system memory pointer.
            pImageFile = LockResource(imageResDataHandle);

            hr = pImageFile ? S_OK : E_FAIL;
        }
        if (SUCCEEDED(hr))
        {
            // Calculate the size.
            imageFileSize = SizeofResource(HINST_THISCOMPONENT, imageResHandle);

            hr = imageFileSize ? S_OK : E_FAIL;
            
        }
    ```

    

4.  Use the [**IWICImagingFactory::CreateStream**](https://msdn.microsoft.com/windows/desktop/1c2ecaf0-5222-4f9b-96fb-5d2da72d11d4) method to create an [**IWICStream**](https://msdn.microsoft.com/windows/desktop/bc398732-037d-4f48-940f-c70975447972) object.
    ```C++
        if (SUCCEEDED(hr))
        {
              // Create a WIC stream to map onto the memory.
            hr = pIWICFactory->CreateStream(&amp;pStream);
        }
        if (SUCCEEDED(hr))
        {
            // Initialize the stream with the memory pointer and size.
            hr = pStream->InitializeFromMemory(
                reinterpret_cast<BYTE*>(pImageFile),
                imageFileSize
                );
        }
    ```

    

5.  Use the [**IWICImagingFactory::CreateDecoderFromStream**](https://msdn.microsoft.com/windows/desktop/b9328715-54a0-4c9a-9977-3252068b7e4b) method to create an [**IWICBitmapDecoder**](https://msdn.microsoft.com/windows/desktop/91dafd5e-e4fb-4691-a3d0-ca8b6ff0aaf7).

    ```C++
        if (SUCCEEDED(hr))
        {
            // Create a decoder for the stream.
            hr = pIWICFactory->CreateDecoderFromStream(
                pStream,
                NULL,
                WICDecodeMetadataCacheOnLoad,
                &amp;pDecoder
                );
        }
    ```

    

6.  Retrieve a frame from the image and store it in an [**IWICBitmapFrameDecode**](https://msdn.microsoft.com/windows/desktop/1498b800-6449-440f-bed7-85891637e559) object.

    ```C++
        if (SUCCEEDED(hr))
        {
            // Create the initial frame.
            hr = pDecoder->GetFrame(0, &amp;pSource);
        }
    ```

    

7.  Before Direct2D can use the image, it must be converted to the 32bppPBGRA pixel format. To convert the image format, use the [**IWICImagingFactory::CreateFormatConverter**](https://msdn.microsoft.com/windows/desktop/50ceabdf-574e-4083-86a4-dddd4da06bbf) method to create an [**IWICFormatConverter**](https://msdn.microsoft.com/windows/desktop/d558aaa7-5962-424c-9e83-363fba09ad50) object, then use the **IWICFormatConverter** object's [**Initialize**](https://msdn.microsoft.com/windows/desktop/ff046b2c-a863-48dd-9cbe-3c559c84b682) method to perform the conversion.
    ```C++
        if (SUCCEEDED(hr))
        {
            // Convert the image format to 32bppPBGRA
            // (DXGI_FORMAT_B8G8R8A8_UNORM + D2D1_ALPHA_MODE_PREMULTIPLIED).
            hr = pIWICFactory->CreateFormatConverter(&amp;pConverter);
        }
    ```

    <span codelanguage="ManagedCPlusPlus"></span>
    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>C++</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><pre><code>    if (SUCCEEDED(hr))
        {</code></pre></td>
    </tr>
    </tbody>
    </table>

    <span codelanguage="ManagedCPlusPlus"></span>
    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>C++</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><pre><code>            
        hr = pConverter-&gt;Initialize(
            pSource,
            GUID_WICPixelFormat32bppPBGRA,
            WICBitmapDitherTypeNone,
            NULL,
            0.f,
            WICBitmapPaletteTypeMedianCut
            );</code></pre></td>
    </tr>
    </tbody>
    </table>

    <span codelanguage="ManagedCPlusPlus"></span>
    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>C++</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><pre><code>    }</code></pre></td>
    </tr>
    </tbody>
    </table>

    

8.  Finally, use the [**CreateBitmapFromWicBitmap**](id2d1rendertarget-createbitmapfromwicbitmap.md) method to create an [**ID2D1Bitmap**](/windows/desktop/api/d2d1/) object that can be drawn by a render target and used with other Direct2D objects.
    ```C++
        if (SUCCEEDED(hr))
        {
            //create a Direct2D bitmap from the WIC bitmap.
            hr = pRenderTarget->CreateBitmapFromWicBitmap(
                pConverter,
                NULL,
                ppBitmap
                );
        
        }

        SafeRelease(&amp;pDecoder);
        SafeRelease(&amp;pSource);
        SafeRelease(&amp;pStream);
        SafeRelease(&amp;pConverter);
        SafeRelease(&amp;pScaler);

        return hr;
    }
    ```

    

Some code has been omitted from this example.

## Related topics

<dl> <dt>

[How to Load a Bitmap from a File](how-to-load-a-direct2d-bitmap-from-a-file.md)
</dt> </dl>

 

 




