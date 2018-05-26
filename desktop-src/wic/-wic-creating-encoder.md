---
Description: An encoder writes image data to a stream. Encoders can compress, encrypt, and alter the image pixels in a number of ways prior to writing them to the stream.
ms.assetid: e1e3a9d9-209b-46a6-92da-5570476507cf
title: Encoding Overview
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Encoding Overview

An encoder writes image data to a stream. Encoders can compress, encrypt, and alter the image pixels in a number of ways prior to writing them to the stream. Using some encoders results in tradeoffs—for example, JPEG, which trades off color information for better compression. Other encoders do not result in such losses—for example, bitmap (BMP). Because many codecs use proprietary technology to achieve better compression and image fidelity, the details on how an image gets encoded are up to the codec developer.

This topic includes the following sections.

-   [IWICBitmapEncoder](#iwicbitmapencoder)
-   [IWICBitmapFrameEncode](#iwicbitmapframeencode)
-   [TIFF Encoding Example](#tiff-encoding-example)
-   [Encoder Options Usage](#encoder-options-usage)
-   [Encoder Options](#encoder-options-usage)
-   [Encoder Options Examples](#encoder-options-examples)
-   [Related topics](#related-topics)

## IWICBitmapEncoder

[**IWICBitmapEncoder**](/windows/win32/wincodec/nn-wincodec-iwicbitmapencoder?branch=master) is the main interface for encoding an image to the target format and used to serialize an image's components, such as thumbnail ([**SetThumbnail**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-setthumbnail?branch=master)) and frames ([**CreateNewFrame**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-createnewframe?branch=master)), to the image file.

How and when serialization occurs is left up to the codec developer. Each individual block of data within the target file format should be able to set independent of order, but again, this is the codec developer's decision. Once the [**Commit**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-commit?branch=master) method is called however, changes to the image should not be allowed and the stream should be closed.

## IWICBitmapFrameEncode

[**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master) is the interface for encoding the individual frames of an image. It provides methods for setting individual frame imaging components, such as thumbnails and frames, as well as image dimensions, DPI, and pixel formats.

Individual frames may be encoded with frame-specific metadata so [**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master) provides access to a metadata writer through the [**GetMetadataQueryWriter**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-getmetadataquerywriter?branch=master) method.

The frame's [**Commit**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-commit?branch=master) method commits all changes to the individual frame and indicates that changes to that frame should no longer be accepted.

## TIFF Encoding Example

In the following example, a Tagged Image File Format (TIFF) image is encoded using [**IWICBitmapEncoder**](/windows/win32/wincodec/nn-wincodec-iwicbitmapencoder?branch=master) and an [**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master). The TIFF output is customized using the [**WICTiffCompressionOption**](/windows/win32/Wincodec/ne-wincodec-wictiffcompressionoption?branch=master) and the bitmap frame is initialized using the given options. Once the image has been created using [**WritePixels**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-writepixels?branch=master), the frame is committed by way of [**Commit**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-commit?branch=master) and the image is saved using [**Commit**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-commit?branch=master).


```C++
IWICImagingFactory *piFactory = NULL;
IWICBitmapEncoder *piEncoder = NULL;
IWICBitmapFrameEncode *piBitmapFrame = NULL;
IPropertyBag2 *pPropertybag = NULL;

IWICStream *piStream = NULL;
UINT uiWidth = 640;
UINT uiHeight = 480;

HRESULT hr = CoCreateInstance(
                CLSID_WICImagingFactory,
                NULL,
                CLSCTX_INPROC_SERVER,
                IID_IWICImagingFactory,
                (LPVOID*) &amp;piFactory);

if (SUCCEEDED(hr))
{
    hr = piFactory->CreateStream(&amp;piStream);
}

if (SUCCEEDED(hr))
{
    hr = piStream->InitializeFromFilename(L"output.tif", GENERIC_WRITE);
}

if (SUCCEEDED(hr))
{
   hr = piFactory->CreateEncoder(GUID_ContainerFormatTiff, NULL, &amp;piEncoder);
}

if (SUCCEEDED(hr))
{
    hr = piEncoder->Initialize(piStream, WICBitmapEncoderNoCache);
}

if (SUCCEEDED(hr))
{
    hr = piEncoder->CreateNewFrame(&amp;piBitmapFrame, &amp;pPropertybag);
}

if (SUCCEEDED(hr))
{        
    // This is how you customize the TIFF output.
    PROPBAG2 option = { 0 };
    option.pstrName = L"TiffCompressionMethod";
    VARIANT varValue;    
    VariantInit(&amp;varValue);
    varValue.vt = VT_UI1;
    varValue.bVal = WICTiffCompressionZIP;      
    hr = pPropertybag->Write(1, &amp;option, &amp;varValue);        
    if (SUCCEEDED(hr))
    {
        hr = piBitmapFrame->Initialize(pPropertybag);
    }
}

if (SUCCEEDED(hr))
{
    hr = piBitmapFrame->SetSize(uiWidth, uiHeight);
}

WICPixelFormatGUID formatGUID = GUID_WICPixelFormat24bppBGR;
if (SUCCEEDED(hr))
{
    hr = piBitmapFrame->SetPixelFormat(&amp;formatGUID);
}

if (SUCCEEDED(hr))
{
    // We're expecting to write out 24bppRGB. Fail if the encoder cannot do it.
    hr = IsEqualGUID(formatGUID, GUID_WICPixelFormat24bppBGR) ? S_OK : E_FAIL;
}

if (SUCCEEDED(hr))
{
    UINT cbStride = (uiWidth * 24 + 7)/8/***WICGetStride***/;
    UINT cbBufferSize = uiHeight * cbStride;

    BYTE *pbBuffer = new BYTE[cbBufferSize];

    if (pbBuffer != NULL)
    {
        for (UINT i = 0; i < cbBufferSize; i++)
        {
            pbBuffer[i] = static_cast<BYTE>(rand());
        }

        hr = piBitmapFrame->WritePixels(uiHeight, cbStride, cbBufferSize, pbBuffer);

        delete[] pbBuffer;
    }
    else
    {
        hr = E_OUTOFMEMORY;
    }
}

if (SUCCEEDED(hr))
{
    hr = piBitmapFrame->Commit();
}    

if (SUCCEEDED(hr))
{
    hr = piEncoder->Commit();
}

if (piFactory)
    piFactory->Release();

if (piBitmapFrame)
    piBitmapFrame->Release();

if (piEncoder)
    piEncoder->Release();

if (piStream)
    piStream->Release();

return hr;
```



## Encoder Options Usage

Different encoders for different formats need to expose different options for how an image is encoded. Windows Imaging Component (WIC) provides a consistent mechanism for expressing whether encoding options are required while still enabling applications to work with multiple encoders without requiring knowledge of a particular format. This is accomplished by providing an [IPropertyBag](http://msdn.microsoft.com/en-us/library/Aa768196(VS.85).aspx) parameter on the [**CreateNewFrame**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-createnewframe?branch=master) method and the [**Initialize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-initialize?branch=master) method.

The component factory provides an easy creation point for creating an encoder options property bag. Codecs can use this service if they need to provide a simple, intuitive and non-conflicting set of encoder options. The imaging property bag must be initialized during creation with all the encoder options relevant to that codec. For encoder options from the canonical set, the value range will be enforced on Write. For more advanced needs, codecs should write their own property bag implementation.

An application is given the encoder options bag during frame creation and must configure any values prior to initializing the encoder frame. For a UI-driven application, it can offer a fixed UI for the canonical encoder options and an advanced view for remaining options. Changes can be made one at a time through the Write method and any error will be reported through IErrorLog. The UI application should always re-read and display all options after making a change in case the change caused a cascade effect. An application should be prepared to handle failed frame initialization for codecs that only provide minimal error reporting through their property bag.

## Encoder Options

An application can expect to encounter the following set of encoder options. Encoder options reflect the capabilities of an encoder and the underlying container format, and therefore are by their nature not really codec-agnostic. When possible, new options should be normalized so they can be applied to new codecs that emerge.



| Property Name      | VARTYPE  | Value                                                                     | Applicable Codecs |
|--------------------|----------|---------------------------------------------------------------------------|-------------------|
| ImageQuality       | VT\_R4   | 0-1.0                                                                     | JPEG, HDPhoto     |
| CompressionQuality | VT\_R4   | 0-1.0                                                                     | TIFF              |
| Lossless           | VT\_BOOL | **TRUE**, **FALSE**                                                       | HDPhoto           |
| BitmapTransform    | VT\_UI1  | [**WICBitmapTransformOptions**](/windows/win32/Wincodec/ne-wincodec-wicbitmaptransformoptions?branch=master) | JPEG              |



 

ImageQualty of 0.0 means the lowest possible fidelity rendition and 1.0 means the highest fidelity, which may also imply lossless depending on the codec.

CompressionQuality of 0.0 means the least efficient compression scheme available, typically resulting in a fast encode but larger output. A value of 1.0 means the most efficient scheme available, typically taking more time to encode but producing smaller output. Depending on the capabilities of the codec, this range may be mapped onto a discrete set of available compression methods.

Lossless means that the codec encodes the image as lossless with no image data loss. If Lossless is enabled, ImageQuality is ignored.

In addition to the above generic encoder options, codecs supplied with WIC support the following options. If a codec has a need to support an option that is consistent with the usage in these supplied codecs, it is encouraged to do so.



| Property Name           | VARTYPE           | Value                                                                             | Applicable Codecs |
|-------------------------|-------------------|-----------------------------------------------------------------------------------|-------------------|
| InterlaceOption         | VT\_BOOL          | On/Off                                                                            | PNG               |
| FilterOption            | VT\_UI1           | [**WICPngFilterOption**](/windows/win32/Wincodec/ne-wincodec-wicpngfilteroption?branch=master)                       | PNG               |
| TiffCompressionMethod   | VT\_UI1           | [**WICTiffCompressionOption**](/windows/win32/Wincodec/ne-wincodec-wictiffcompressionoption?branch=master)           | TIFF              |
| Luminance               | VT\_UI4/VT\_ARRAY | 64 Entries (DCT)                                                                  | JPEG              |
| Chrominance             | VT\_UI4/VT\_ARRAY | 64 Entries (DCT)                                                                  | JPEG              |
| JpegYCrCbSubsampling    | VT\_UI1           | [**WICJpegYCrCbSubsamplingOption**](/windows/win32/Wincodec/ne-wincodec-wicjpegycrcbsubsamplingoption?branch=master) | JPEG              |
| SuppressApp0            | VT\_BOOL          |                                                                                   | JPEG              |
| EnableV5Header32bppBGRA | VT\_BOOL          | On/Off                                                                            | BMP               |



 

Use **VT\_EMPTY** to indicate **\*not set\*** as the default. If additional properties are set but not supported, the encoder should ignore them; this allows applications to code less logic if they want a capability that may or may not be present.

## Encoder Options Examples

In the [TIFF Encoding Example](#tiff-encoding-example) above, a specific encoder option is set. The *pstrName* member of the PROPBAG2 structure is set to the appropriate property name, and the VARIANT is set to the corresponding VARTYPE and the desired value—in this case, a member of the [**WICTiffCompressionOption**](/windows/win32/Wincodec/ne-wincodec-wictiffcompressionoption?branch=master) enumeration.


```C++
if (SUCCEEDED(hr))
{
    hr = piEncoder->CreateNewFrame(&amp;piBitmapFrame, &amp;pPropertybag);
}

if (SUCCEEDED(hr))
{        
    // This is how you customize the TIFF output.
    PROPBAG2 option = { 0 };
    option.pstrName = L"TiffCompressionMethod";
    VARIANT varValue;    
    VariantInit(&amp;varValue);
    varValue.vt = VT_UI1;
    varValue.bVal = WICTiffCompressionZIP;      
    hr = pPropertybag->Write(1, &amp;option, &amp;varValue);        
    if (SUCCEEDED(hr))
    {
        hr = piBitmapFrame->Initialize(pPropertybag);
    }
}
```



To use the default encoder options, simply initialize the bitmap frame with the property bag returned when the frame was created.


```C++
if (SUCCEEDED(hr))
{
    hr = piEncoder->CreateNewFrame(&amp;piBitmapFrame, &amp;pPropertybag);
}

if (SUCCEEDED(hr))
{        
    // Accept the default encoder options.
    if (SUCCEEDED(hr))
    {
        hr = piBitmapFrame->Initialize(pPropertybag);
    }
}
```



It is also possible to eliminate the property bag when no encoder options are being considered.


```C++
if (SUCCEEDED(hr))
{
    hr = piEncoder->CreateNewFrame(&amp;piBitmapFrame, 0);
}

if (SUCCEEDED(hr))
{        
    // No encoder options.
    if (SUCCEEDED(hr))
    {
        hr = piBitmapFrame->Initialize(0);
    }
}
```



## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[Decoding Overview](-wic-creating-decoder.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> </dl>

 

 



