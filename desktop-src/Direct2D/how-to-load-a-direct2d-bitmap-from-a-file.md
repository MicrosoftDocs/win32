---
title: How to Load a Bitmap from a File
description: Shows how to load a Direct2D bitmap from an image file.
ms.assetid: 4abfbc2b-2730-4d96-897e-1e2232383a72
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to Load a Bitmap from a File

Direct2D uses the Windows Imaging Component (WIC) to load bitmaps. To load a bitmap from a file, first use WIC objects to load the image and to convert it to a Direct2D-compatible format, then use the [**CreateBitmapFromWicBitmap**](id2d1rendertarget-createbitmapfromwicbitmap.md) method to create an [**ID2D1Bitmap**](/windows/desktop/api/d2d1/).

1.  Create an [**IWICBitmapDecoder**](https://msdn.microsoft.com/windows/desktop/91dafd5e-e4fb-4691-a3d0-ca8b6ff0aaf7) by using the [**IWICImagingFactory::CreateDecoderFromFileName**](https://msdn.microsoft.com/windows/desktop/100c54c7-bb10-47dd-8436-04282ec6b110) method.

    ```C++
    HRESULT DemoApp::LoadBitmapFromFile(
        ID2D1RenderTarget *pRenderTarget,
        IWICImagingFactory *pIWICFactory,
        PCWSTR uri,
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

        HRESULT hr = pIWICFactory->CreateDecoderFromFilename(
            uri,
            NULL,
            GENERIC_READ,
            WICDecodeMetadataCacheOnLoad,
            &amp;pDecoder
            );
            
    ```

    

2.  Retrieve a frame from the image and store the frame in an [**IWICBitmapFrameDecode**](https://msdn.microsoft.com/windows/desktop/1498b800-6449-440f-bed7-85891637e559) object.

    ```C++
        if (SUCCEEDED(hr))
        {
            // Create the initial frame.
            hr = pDecoder->GetFrame(0, &amp;pSource);
        }
    ```

    

3.  The bitmap must be converted to a format that Direct2D can use, so convert the image's pixel format to 32bppPBGRA. (For a list of supported formats, see [Pixel Formats and Alpha Modes](supported-pixel-formats-and-alpha-modes.md).). Call the [**IWICImagingFactory::CreateFormatConverter**](https://msdn.microsoft.com/windows/desktop/50ceabdf-574e-4083-86a4-dddd4da06bbf) method to create an [**IWICFormatConverter**](https://msdn.microsoft.com/windows/desktop/d558aaa7-5962-424c-9e83-363fba09ad50) object, then call the **IWICFormatConverter** object's [**Initialize**](https://msdn.microsoft.com/windows/desktop/ff046b2c-a863-48dd-9cbe-3c559c84b682) method to perform the conversion.
    ```C++
        if (SUCCEEDED(hr))
        {

            // Convert the image format to 32bppPBGRA
            // (DXGI_FORMAT_B8G8R8A8_UNORM + D2D1_ALPHA_MODE_PREMULTIPLIED).
            hr = pIWICFactory->CreateFormatConverter(&amp;pConverter);

        }
     
     
        if (SUCCEEDED(hr))
        {
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
    <td><pre><code>        hr = pConverter-&gt;Initialize(
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

    

4.  Call the [**CreateBitmapFromWicBitmap**](id2d1rendertarget-createbitmapfromwicbitmap.md) method to create an [**ID2D1Bitmap**](/windows/desktop/api/d2d1/) object that can be drawn by a render target and used with other Direct2D objects.
    ```C++
        if (SUCCEEDED(hr))
        {
        
            // Create a Direct2D bitmap from the WIC bitmap.
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

[**ID2D1Bitmap**](/windows/desktop/api/d2d1/)
</dt> <dt>

[**CreateBitmapFromWicBitmap**](id2d1rendertarget-createbitmapfromwicbitmap.md)
</dt> <dt>

[How to Load a Bitmap from a Resource](how-to-load-a-bitmap-from-a-resource.md)
</dt> </dl>

 

 




