---
Description: Implementation Guidelines for Serializing IWICDevelopRaw Settings
ms.assetid: '4ecff5cc-24f3-4b89-b681-85c867b053e7'
title: Implementation Guidelines for Serializing IWICDevelopRaw Settings
---

# Implementation Guidelines for Serializing IWICDevelopRaw Settings

The [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) interface exposes settings that the application can use to modify the processing of the RAW image. The settings should be able to be serialized so that they persist across sessions. Although this can be done in several ways, it is recommended to encode this data in a manner that is consistent with other metadata.

The following are some general implementation guidelines:

-   Any settings made via [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) (such as rotation or white balance) should avoid overwriting camera setting or "as-shot" data unless the tag is commonly used as a "current setting." For example, EXIF orientation tags can be used to persist rotation.
-   It is preferable not to have to save the entire file (including the mosaic pixel data) each time that the [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) settings are asked to be serialized.
-   The process of serializing [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) settings will generally follow this order of events. The application:

    1.  Instantiates an [**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md) on a RAW file.
    2.  Calls [**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md)::[**GetFrame**](-wic-codec-iwicbitmapdecoder-getframe.md) to get an [**IWICBitmapFrameDecode**](-wic-codec-iwicbitmapframedecode.md) for the RAW frame.
    3.  Calls QueryInterface on the IWICBitmapFrameDecode interface for the IWICDevelopRaw interface.
    4.  Calls [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md)::[**GetCurrentParameterSet**](-wic-codec-iwicdevelopraw-getcurrentparameterset.md), which returns an IPropertyBag2 interface with all of the current properties stored in it.

        At this point of the process, the goal is to serialize the settings in the IPropertyBag2 interface into the RAW file. To do so requires spinning up an encoder and so on, which is detailed in the following steps.

    5.  Creates an [**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md) for the RAW file.
    6.  Calls [**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md)::[**Initialize**](-wic-codec-iwicbitmapencoder-initialize.md), passing in a new (blank) stream to encode.
    7.  Calls [**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md)::[**CreateNewFrame**](-wic-codec-iwicbitmapencoder-createnewframe.md) to create a new IWICBitmapFrameEncode for the RAW frame.
    8.  Calls [**IWICBitmapFrameEncode**](-wic-codec-iwicbitmapframeencode.md)::[**Initialize**](-wic-codec-iwicbitmapencoder-initialize.md), and passes in the IPropertyBag2 interface from step 4.
    9.  Calls [**IWICBitmapFrameEncode**](-wic-codec-iwicbitmapframeencode.md)::[**WriteSource**](-wic-codec-iwicbitmapframeencode-writesource.md) with [**IWICBitmapSource**](-wic-codec-iwicbitmapsource.md) from decoder's RAW image frame.
    10. Calls [**IWICBitmapFrameEncode**](-wic-codec-iwicbitmapframeencode.md)::[**Commit**](-wic-codec-iwicbitmapencoder-commit.md). The codec then serializes the properties in the IPropertyBag2 from step 8 into the file. The most common method of serializing the properties is assumed to be by writing them out as metadata in the file.
    11. Calls [**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md)::[**Commit**](-wic-codec-iwicbitmapencoder-commit.md).
    12. Calls IStream::Commit on the stream in step 6.

    The settings are serialized in the file.

    This method does incur the cost of rewriting the entire RAW file each time the settings are serialized. This can be avoided if you implement [**IWICFastMetadataEncoder**](-wic-codec-iwicfastmetadataencoder.md) or if your image file format supports XMP or EXIF, as WIC provides [**IWICFastMetadataEncoder**](-wic-codec-iwicfastmetadataencoder.md) for both of these formats. Also, if your codec writes changes to the end of the image file, then you won't end up rewriting the entire image file.

-   Parameter sets are loaded from the serialized state when the application sets the [**WICRawParameterSet.WICUserAdjustedParameterSet**](-wic-codec-wicrawparameterset.md) enumeration on the [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md)::[**LoadParameterSet**](-wic-codec-iwicdevelopraw-loadparameterset.md) method. The [**WICRawParameterSet.WICUserAdjustedParameterSet**](-wic-codec-wicrawparameterset.md) flag refers to the last-saved parameter set, so a load with this flag should result in restoring parameters to the last-saved state.
-   Upon initial load, the last-saved parameter set should be loaded, if available. If not, then the "as-shot" settings should be used as presets on the [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) interface variables. These as-shot settings can also be loaded by using the [**WICRawParameterSet.WICAsShotParameterSet**](-wic-codec-wicrawparameterset.md) flag.
-   The identifier [**WICRawParameterSet.WICAutoAdjustedParameterSet**](-wic-codec-wicrawparameterset.md) is meant to represent an "Auto" setting. The codec designer can elect any of the following approaches on how to set [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) parameters when this setting is made:

    -   Perform an algorithmic optimization of some parameters, such as exposure or color. This is how Auto functions in typical image editors and is based primarily on pixel data analysis.
    -   Set camera settings similar to how an Auto setting would have behaved. This is useful if the image was shot on a Manual setting and allows the user to override manual settings.
    -   Do nothing. Not all controls need to be set when Auto is selected, and it is OK to leave settings unchanged.

The Windows Vista Photo Gallery and Windows Live Photo Gallery editing tools and other editing applications use the [**IWICDevelopRaw**](-wic-codec-iwicdevelopraw.md) Auto parameter load when the user selects Auto Correct for all normal codec control adjustments such as color and exposure to get the best results.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[WIC Guidelines for Camera RAW Image Formats](-wic-rawguidelines.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> </dl>

 

 



