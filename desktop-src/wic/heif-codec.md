---
title: HEIF extension codec
description: Info about the HEIF extension codec available through WIC.
ms.topic: reference
ms.date: 01/29/2024
---

# HEIF extension codec

> [!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Info about the High Efficiency Image Format (HEIF) extension codec available through WIC. To download the extension codec from the Microsoft Store, see [HEIF Image Extension](https://apps.microsoft.com/detail/9PMMSR1CGPWG).

Two pixel format GUIDs allow photo viewers to retrieve alternate representations of a HEIF image.

* **Depth-only**
  * GUID\_WICPixelFormat8bppDepth
* **Gain-only**
  * GUID\_WICPixelFormat8bppGain

For more info about those formats, see [Native pixel formats overview](/windows/win32/wic/-wic-codec-native-pixel-formats#heif-native-codec).

The [WICHeifCompressionOption enumeration](/windows/win32/api/wincodec/ne-wincodec-wicheifcompressionoption) of encoding options allows apps to choose which compression format to use when creating a HEIF image file.

## Using the HEIF extension codec

If you have an app that uses WIC, then you can use a pixel format GUID to request how the image is represented. Your app can check whether a WIC decoder supports a specific pixel format by using the [IWICBitmapSourceTransform::GetClosestPixelFormat](/windows/win32/api/wincodec/nf-wincodec-iwicbitmapsourcetransform-getclosestpixelformat) method.

Then, to decode an image into a bitmap that uses a specific pixel format, your app can call [IWICBitmapSourceTransform::CopyPixels](/windows/win32/api/wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels).

For example, if an image is converted into a bitmap that uses the *GUID_WICPixelFormat24bppRGB* pixel format, then that it means that the bitmap contains red, green, and blue color information for each pixel. (8 bits per color component.) GUID_WICPixelFormat32bppRGBA adds *alpha* (transparency) information to each pixel. The pixel format *GUID_WICPixelFormat8bppAlpha* is used for bitmaps that contain only 8-bit *alpha* information for each pixel.

## Depth and gain info for HEIF

For High Efficiency Image Format (HEIF) files, the pixel format *GUID_WICPixelFormat8bppDepth* is relevant. It works similarly to *GUID_WICPixelFormat8bppAlpha*. Except that while *alpha* specifies the transparency of pixels, *depth* specifies the relative distance of pixels from the viewer of the image.

In a bitmap that uses *GUID_WICPixelFormat8bppDepth*, the bitmap contains an 8-bit value with *depth* information per pixel. A value of 0 means that the co-located pixel in the color bitmap representation of the image is located nearest to the viewer; and a value of 255 means that the co-located pixel in the color bitmap is located farthest from the viewer.

Also for HEIF, there's a pixel format named *GUID_WICPixelFormat8bppGain*. Similar to the pixel formats for alpha and depth, *GUID_WICPixelFormat8bppGain* provides an 8-bit value per pixel. The purpose of the *gain* information is to specify a brightness gain that can be applied to the RGB-format pixels: effectively converting a normal RGB image into a High Dynamic Range (HDR) image. Gain information is exposed as-is. Your app can use the Exif or XMP metadata in the HEIF image to determine which camera model has generated the gain. Currently, gain information is included only in HEIF files that were created by recent Apple iOS devices.

There's no *default* depth or gain information for images. Calling [IWICBitmapSourceTransform::CopyPixels](/windows/win32/api/wincodec/nf-wincodec-iwicbitmapsourcetransform-copypixels) requesting a gain or depth representation of an image that doesn't have that information will result in a **WINCODEC_ERR_UNSUPPORTEDPIXELFORMAT** error.

## Compression options

The [WICHeifCompressionOption](/windows/win32/api/wincodec/ne-wincodec-wicheifcompressionoption) enumeration is used to specify an option named *HeifCompressionMethod* when encoding a bitmap into the HEIF format.

HEIF is a container, similar to TIFF, that can use different compression methods. The default compression method is the High-Efficiency Video Codec (HEVC). HEIF files that are compressed with HEVC typically use the `.heic` file extension. With the *WICHeifCompressionAV1* enum value, it will become possible to specify that the AV1 codec should be used instead. HEIF files that use AV1 for compression typically use the `.avif` file extension.  

HEIF will attempt to do certain edits, such as rotation and cropping, without recompressing the image. You can use the *WICHeifCompressionNone* enum value to enforce that the image isn't recompressed. If the image needs to be recompressed, then the *Commit* operation will return **WINCODEC_ERR_UNSUPPORTEDOPERATION** if *WICHeifCompressionNone* has been specified.

The HEVC and AV1 codecs might not be available on all PCs. You can download those codecs from the Microsoft Store. To check whether HEVC or AV1 are installed, you can use the [MFTEnumEx](/windows/win32/api/mfapi/nf-mfapi-mftenumex) function to query for the presence of a video encoder for the formats *MFVideoFormat_HEVC* and *MFVideoFormat_AV1*, respectively.

## Code examples

These code examples use the [Windows Implementation Libraries (WIL)](https://github.com/Microsoft/wil). A convenient way to install WIL is to go to Visual Studio, click **Project** \> **Manage NuGet Packages...** \> **Browse**, type or paste **Microsoft.Windows.ImplementationLibrary** in the search box, select the item in search results, and then click **Install** to install the package for that project.

### Example 1: Depth

This example shows how to check whether depth information is available, and how to retrieve it.

```cpp
using namespace wil;

bool IsPixelFormatSupported(_In_ IWICBitmapSourceTransform* bitmap, 
    REFWICPixelFormatGUID proposedPixelFormat)
{
    WICPixelFormatGUID closestPixelFormat = proposedPixelFormat;
    if (SUCCEEDED(bitmap->GetClosestPixelFormat(&closestPixelFormat)) &&
        closestPixelFormat == proposedPixelFormat)
    {
        return true;
    }
    return false;
}

bool IsDepthAvailable(_In_ IWICBitmapSourceTransform* bitmap)
{
    return IsPixelFormatSupported(bitmap, GUID_WICPixelFormat8bppDepth);
}

HRESULT GetDepthBitmap(_In_ IWICBitmapFrameDecode* frame, unique_cotaskmem_ptr<BYTE[]>& bitmap)
{
    bitmap.reset();

    com_ptr_nothrow<IWICBitmapSourceTransform> frameTransform;
    RETURN_IF_FAILED(com_query_to_nothrow(frame, &frameTransform));

    // Check whether depth information is available for this image. If there's no depth
    // information, then just return an empty bitmap.
    if (IsDepthAvailable(frameTransform.get()))
    {
        UINT width;
        UINT height;
        RETURN_IF_FAILED(frame->GetSize(&width, &height));

        size_t bitmapSize;
        RETURN_IF_FAILED(SizeTMult(width, height, &bitmapSize));

        bitmap = make_unique_cotaskmem_nothrow<BYTE[]>(bitmapSize);
        RETURN_IF_NULL_ALLOC(bitmap);

        WICPixelFormatGUID pixelFormat = GUID_WICPixelFormat8bppDepth;
        RETURN_IF_FAILED(frameTransform->CopyPixels(nullptr, width, height,
            &pixelFormat, WICBitmapTransformRotate0, width, bitmapSize, bitmap.get()));
    }
    return S_OK;
}
```

### Example 2: Gain

This example shows how to check whether *gain* information is available, and how to retrieve it. This example reuses the **IsPixelFormatSupported** function shown in Example 1.

```cpp
using namespace wil;

bool IsGainAvailable(_In_ IWICBitmapSourceTransform* bitmap)
{
    return IsPixelFormatSupported(bitmap, GUID_WICPixelFormat8bppGain);
}

HRESULT GetGainBitmap(_In_ IWICBitmapFrameDecode* frame, unique_cotaskmem_ptr<BYTE[]>& bitmap)
{
    bitmap.reset();

    com_ptr_nothrow<IWICBitmapSourceTransform> frameTransform;
    RETURN_IF_FAILED(com_query_to_nothrow(frame, &frameTransform));

    // Check whether gain information is available for this image. If there's no gain
    // information, then just return an empty bitmap.
    if (IsGainAvailable(frameTransform.get()))
    {
        UINT width;
        UINT height;
        RETURN_IF_FAILED(frame->GetSize(&width, &height));

        size_t bitmapSize;
        RETURN_IF_FAILED(SizeTMult(width, height, &bitmapSize));

        bitmap = make_unique_cotaskmem_nothrow<BYTE[]>(bitmapSize);
        RETURN_IF_NULL_ALLOC(bitmap);

        WICPixelFormatGUID pixelFormat = GUID_WICPixelFormat8bppGain;
        RETURN_IF_FAILED(frameTransform->CopyPixels(nullptr, width, height,
            &pixelFormat, WICBitmapTransformRotate0, width, bitmapSize, bitmap.get()));
    }
    return S_OK;
}
```

### Example 3: Specifying that AV1 compression must be used

This example shows how to use AV1 compression to encode a HEIF file, creating an `.avif` file.

```cpp
using namespace wil;

HRESULT EncodeSourceAsAvif(IWICBitmapSource* source, IWICStream* outputStream, IWICImagingFactory* factory)
{
    com_ptr_nothrow<IWICBitmapEncoder> encoder;
    RETURN_IF_FAILED(factory->CreateEncoder(GUID_ContainerFormatHeif, nullptr, &encoder));
    RETURN_IF_FAILED(encoder->Initialize(outputStream, WICBitmapEncoderCacheInMemory));

    com_ptr_nothrow<IWICBitmapFrameEncode> outputFrame;
    com_ptr_nothrow<IPropertyBag2> encoderOptions;
    RETURN_IF_FAILED(encoder->CreateNewFrame(&outputFrame, &encoderOptions));

    // Configure the output frame to compress the source image using the AV1 encoder.
    PROPBAG2 option{};
    option.pstrName = L"HeifCompressionMethod";

    VARIANT propertyValue{};
    propertyValue.vt = VT_UI1;
    propertyValue.bVal = static_cast<BYTE>(WICHeifCompressionAV1);

    RETURN_IF_FAILED(encoderOptions->Write(1, &option, &propertyValue));
    RETURN_IF_FAILED(outputFrame->Initialize(encoderOptions.get()));
    RETURN_IF_FAILED(outputFrame->WriteSource(source, nullptr));

    // Do the actual encoding of the source image. If the AV1 encoder is missing,
    // then this call fails.
    RETURN_IF_FAILED(outputFrame->Commit());
    RETURN_IF_FAILED(encoder->Commit());
    return S_OK;
}
```

### Example 4: Specifying that compression is not allowed

This example shows how to save an image in a HEIF container and apply rotation and cropping to the image; but enforcing that the image is not getting compressed. If the source is already in HEVC or AV1 format, then that will succeed. But if the source is a raw bitmap or in some other format, then the function will return an error if encoding is not allowed.

```cpp
using namespace wil;

// Rotate and optionally crop the source image, and produce a HEIF image file as output.
// If the input parameter allowEncoding is false, and the image needs to be encoded,
// then this function will return WINCODEC_ERR_UNSUPPORTEDOPERATION.
HRESULT RotateAndCropSource(
    IWICBitmapSource* source,
    IWICStream* outputStream,
    IWICImagingFactory* factory,
    bool allowCompression,
    WICBitmapTransformOptions transformOptions,
    WICRect* cropRectangle = nullptr)
{
    com_ptr_nothrow<IWICBitmapEncoder> encoder;
    RETURN_IF_FAILED(factory->CreateEncoder(GUID_ContainerFormatHeif, NULL, &encoder));
    RETURN_IF_FAILED(encoder->Initialize(outputStream, WICBitmapEncoderCacheInMemory));

    com_ptr_nothrow<IWICBitmapFrameEncode> outputFrame;
    com_ptr_nothrow<IPropertyBag2> encoderOptions;
    RETURN_IF_FAILED(encoder->CreateNewFrame(&outputFrame, &encoderOptions));

    VARIANT propertyValue{};

    if (!allowCompression)
    {
        // Specify that compression of the image is not allowed.
        PROPBAG2 option{};
        option.pstrName = L"HeifCompressionMethod";

        propertyValue.vt = VT_UI1;
        propertyValue.bVal = static_cast<BYTE>(WICHeifCompressionNone);
        RETURN_IF_FAILED(encoderOptions->Write(1, &option, &propertyValue));
    }

    if (transformOptions != WICBitmapTransformRotate0)
    {
        PROPBAG2 option{};
        option.pstrName = L"BitmapTransform";

        propertyValue.vt = VT_UI1;
        propertyValue.bVal = static_cast<BYTE>(transformOptions);
        RETURN_IF_FAILED(encoderOptions->Write(1, &option, &propertyValue));
    }

    RETURN_IF_FAILED(outputFrame->Initialize(encoderOptions.get()));
    RETURN_IF_FAILED(outputFrame->WriteSource(source, cropRectangle));

    // Generate the HEIF file. If the image needs to be compressed, this call fails.
    RETURN_IF_FAILED(outputFrame->Commit());
    RETURN_IF_FAILED(encoder->Commit());
    return S_OK;
}
```
