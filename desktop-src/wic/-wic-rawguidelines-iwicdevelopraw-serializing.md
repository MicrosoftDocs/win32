---
Description: Implementation Guidelines for Serializing IWICDevelopRaw Settings
ms.assetid: 4ecff5cc-24f3-4b89-b681-85c867b053e7
title: Implementation Guidelines for Serializing IWICDevelopRaw Settings
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementation Guidelines for Serializing IWICDevelopRaw Settings

The [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master) interface exposes settings that the application can use to modify the processing of the RAW image. The settings should be able to be serialized so that they persist across sessions. Although this can be done in several ways, it is recommended to encode this data in a manner that is consistent with other metadata.

The following are some general implementation guidelines:

-   Any settings made via [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master) (such as rotation or white balance) should avoid overwriting camera setting or "as-shot" data unless the tag is commonly used as a "current setting." For example, EXIF orientation tags can be used to persist rotation.
-   It is preferable not to have to save the entire file (including the mosaic pixel data) each time that the [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master) settings are asked to be serialized.
-   The process of serializing [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master) settings will generally follow this order of events. The application:

    1.  Instantiates an [**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master) on a RAW file.
    2.  Calls [**IWICBitmapDecoder**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapdecoder?branch=master)::[**GetFrame**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapdecoder-getframe?branch=master) to get an [**IWICBitmapFrameDecode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframedecode?branch=master) for the RAW frame.
    3.  Calls QueryInterface on the IWICBitmapFrameDecode interface for the IWICDevelopRaw interface.
    4.  Calls [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master)::[**GetCurrentParameterSet**](/windows/win32/Wincodec/nf-wincodec-iwicdevelopraw-getcurrentparameterset?branch=master), which returns an IPropertyBag2 interface with all of the current properties stored in it.

        At this point of the process, the goal is to serialize the settings in the IPropertyBag2 interface into the RAW file. To do so requires spinning up an encoder and so on, which is detailed in the following steps.

    5.  Creates an [**IWICBitmapEncoder**](/windows/win32/wincodec/nn-wincodec-iwicbitmapencoder?branch=master) for the RAW file.
    6.  Calls [**IWICBitmapEncoder**](/windows/win32/wincodec/nn-wincodec-iwicbitmapencoder?branch=master)::[**Initialize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-initialize?branch=master), passing in a new (blank) stream to encode.
    7.  Calls [**IWICBitmapEncoder**](/windows/win32/wincodec/nn-wincodec-iwicbitmapencoder?branch=master)::[**CreateNewFrame**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-createnewframe?branch=master) to create a new IWICBitmapFrameEncode for the RAW frame.
    8.  Calls [**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master)::[**Initialize**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-initialize?branch=master), and passes in the IPropertyBag2 interface from step 4.
    9.  Calls [**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master)::[**WriteSource**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapframeencode-writesource?branch=master) with [**IWICBitmapSource**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapsource?branch=master) from decoder's RAW image frame.
    10. Calls [**IWICBitmapFrameEncode**](/windows/win32/Wincodec/nn-wincodec-iwicbitmapframeencode?branch=master)::[**Commit**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-commit?branch=master). The codec then serializes the properties in the IPropertyBag2 from step 8 into the file. The most common method of serializing the properties is assumed to be by writing them out as metadata in the file.
    11. Calls [**IWICBitmapEncoder**](/windows/win32/wincodec/nn-wincodec-iwicbitmapencoder?branch=master)::[**Commit**](/windows/win32/Wincodec/nf-wincodec-iwicbitmapencoder-commit?branch=master).
    12. Calls IStream::Commit on the stream in step 6.

    The settings are serialized in the file.

    This method does incur the cost of rewriting the entire RAW file each time the settings are serialized. This can be avoided if you implement [**IWICFastMetadataEncoder**](/windows/win32/Wincodec/nn-wincodec-iwicfastmetadataencoder?branch=master) or if your image file format supports XMP or EXIF, as WIC provides [**IWICFastMetadataEncoder**](/windows/win32/Wincodec/nn-wincodec-iwicfastmetadataencoder?branch=master) for both of these formats. Also, if your codec writes changes to the end of the image file, then you won't end up rewriting the entire image file.

-   Parameter sets are loaded from the serialized state when the application sets the [**WICRawParameterSet.WICUserAdjustedParameterSet**](/windows/win32/Wincodec/ne-wincodec-wicrawparameterset?branch=master) enumeration on the [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master)::[**LoadParameterSet**](/windows/win32/Wincodec/nf-wincodec-iwicdevelopraw-loadparameterset?branch=master) method. The [**WICRawParameterSet.WICUserAdjustedParameterSet**](/windows/win32/Wincodec/ne-wincodec-wicrawparameterset?branch=master) flag refers to the last-saved parameter set, so a load with this flag should result in restoring parameters to the last-saved state.
-   Upon initial load, the last-saved parameter set should be loaded, if available. If not, then the "as-shot" settings should be used as presets on the [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master) interface variables. These as-shot settings can also be loaded by using the [**WICRawParameterSet.WICAsShotParameterSet**](/windows/win32/Wincodec/ne-wincodec-wicrawparameterset?branch=master) flag.
-   The identifier [**WICRawParameterSet.WICAutoAdjustedParameterSet**](/windows/win32/Wincodec/ne-wincodec-wicrawparameterset?branch=master) is meant to represent an "Auto" setting. The codec designer can elect any of the following approaches on how to set [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master) parameters when this setting is made:

    -   Perform an algorithmic optimization of some parameters, such as exposure or color. This is how Auto functions in typical image editors and is based primarily on pixel data analysis.
    -   Set camera settings similar to how an Auto setting would have behaved. This is useful if the image was shot on a Manual setting and allows the user to override manual settings.
    -   Do nothing. Not all controls need to be set when Auto is selected, and it is OK to leave settings unchanged.

The Windows Vista Photo Gallery and Windows Live Photo Gallery editing tools and other editing applications use the [**IWICDevelopRaw**](/windows/win32/Wincodec/nn-wincodec-iwicdevelopraw?branch=master) Auto parameter load when the user selects Auto Correct for all normal codec control adjustments such as color and exposure to get the best results.

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

 

 



