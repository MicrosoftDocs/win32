---
title: WIC constants, enumerations, and flags
description: This section contains information about the Windows Imaging Component (WIC) constants, enumerations, and flags.
ms.assetid: a3f44919-bd55-48cf-9dc6-37de0059a639
ms.topic: reference
ms.date: 01/11/2024
---

# WIC constants, enumerations, and flags

This section contains information about the Windows Imaging Component (WIC) constants, enumerations, and flags.

## In this section

| Topic | Description |
|-|-|
| [WIC GUIDs and CLSIDs](-wic-guids-clsids.md) | |
| [Codec Error Codes](-wic-codec-error-codes.md) | |
| [Native Pixel Formats](-wic-codec-native-pixel-formats.md) | This topic introduces the pixel formats provided by the WIC |
| [Native WIC Codecs](native-wic-codecs.md) | This section contains information about the native imaging codecs available in WIC. |
| [**IWICDevelopRawNotificationCallback Constants**](-wic-codec-iwicdeveloprawnotification-constants.md) | Flags used to by [**IWICDevelopRawNotificationCallback**](/windows/win32/api/wincodec/nn-wincodec-iwicdeveloprawnotificationcallback) to indicate which members have changed. |
| [**IWICJpegFrameDecode Constants**](iwicjpegframedecode-constants.md) | Flags used by the [**WICJpegScanHeader**](/windows/win32/api/wincodec/ns-wincodec-wicjpegscanheader) and [**WICJpegFrameHeader**](/windows/win32/api/wincodec/ns-wincodec-wicjpegframeheader). |
| [**WIC8BIMIptcDigestProperties**](/windows/win32/api/wincodec/ne-wincodec-wic8bimiptcdigestproperties) | Specifies the identifiers of the metadata items in an 8BIM IPTC digest metadata block. |
| [**WIC8BIMIptcProperties**](/windows/win32/api/wincodec/ne-wincodec-wic8bimiptcproperties) | Specifies the identifiers of the metadata items in an 8BIM IPTC block. |
| [**WIC8BIMResolutionInfoProperties**](/windows/win32/api/wincodec/ne-wincodec-wic8bimresolutioninfoproperties) | Specifies the identifiers of the metadata items in an 8BIMResolutionInfo block. |
| [**WICBitmapAlphaChannelOption**](/windows/win32/api/wincodec/ne-wincodec-wicbitmapalphachanneloption) | Specifies the desired alpha channel usage. |
| [**WICBitmapCreateCacheOption**](/windows/win32/api/wincodec/ne-wincodec-wicbitmapcreatecacheoption) | Specifies the desired cache usage. |
| [**WICBitmapDecoderCapabilities**](/windows/win32/api/wincodec/ne-wincodec-wicbitmapdecodercapabilities) | Specifies the capabilities of the decoder. |
| [**WICBitmapDitherType**](/windows/win32/api/wincodec/ne-wincodec-wicbitmapdithertype) | Specifies the type of [dither](/windows) algorithm to apply when converting between image formats. |
| [**WICBitmapEncoderCacheOption**](/windows/win32/api/wincodec/ne-wincodec-wicbitmapencodercacheoption) | Specifies the cache options available for an encoder. |
| [**WICBitmapInterpolationMode**](/windows/win32/api/wincodec/ne-wincodec-wicbitmapinterpolationmode) | Specifies the sampling or filtering mode to use when scaling an image. |
| [**WICBitmapLockFlags**](/windows/win32/api/wincodec/ne-wincodec-wicbitmaplockflags) | Specifies access to an [**IWICBitmap**](/windows/win32/api/wincodec/nn-wincodec-iwicbitmap). |
| [**WICBitmapPaletteType**](/windows/win32/api/wincodec/ne-wincodec-wicbitmappalettetype) | Specifies the type of palette used for an indexed image format. |
| [**WICBitmapTransformOptions**](/windows/win32/api/wincodec/ne-wincodec-wicbitmaptransformoptions) | Specifies the flip and rotation transforms. |
| [**WICColorContextType**](/windows/win32/api/wincodec/ne-wincodec-wiccolorcontexttype) | Specifies the color context types. |
| [**WICComponentEnumerateOptions**](/windows/win32/api/wincodec/ne-wincodec-wiccomponentenumerateoptions) | Specifies component enumeration options. |
| [**WICComponentSigning**](/windows/win32/api/wincodec/ne-wincodec-wiccomponentsigning) | Specifies the component signing status. |
| [**WICComponentType**](/windows/win32/api/wincodec/ne-wincodec-wiccomponenttype) | Specifies the type of WIC component. |
| [**WICDecodeOptions**](/windows/win32/api/wincodec/ne-wincodec-wicdecodeoptions) | Specifies decode options. |
| [**WICDdsDimension**](/windows/win32/api/wincodec/ne-wincodec-wicddsdimension) | Specifies the dimension type of the data contained in DDS image. |
| [**WICDdsAlphaMode**](/windows/win32/api/wincodec/ne-wincodec-wicddsalphamode) | Specifies the meaning of pixel color component values contained in the DDS image. |
| [**WICGifApplicationExtensionProperties**](/windows/win32/api/wincodec/ne-wincodec-wicgifapplicationextensionproperties) | Specifies the application extension metadata properties for a Graphics Interchange Format (GIF) image. |
| [**WICGifCommentExtensionProperties**](/windows/win32/api/wincodec/ne-wincodec-wicgifcommentextensionproperties) | Specifies the comment extension metadata properties for a GIF image. |
| [**WICGifGraphicControlExtensionProperties**](/windows/win32/api/wincodec/ne-wincodec-wicgifgraphiccontrolextensionproperties) | Specifies the graphic control extension metadata properties that define the transitions between each frame animation for GIF images. |
| [**WICGifImageDescriptorProperties**](/windows/win32/api/wincodec/ne-wincodec-wicgifimagedescriptorproperties) | Specifies the image descriptor metadata properties for GIF frames. |
| [**WICGifLogicalScreenDescriptorProperties**](/windows/win32/api/wincodec/ne-wincodec-wicgiflogicalscreendescriptorproperties) | Specifies the logical screen descriptor properties for GIF metadata. |
| [**WICHeifCompressionOption**](/windows/win32/api/wincodec/ne-wincodec-wicheifcompressionoption) | Defines constants that specify High Efficiency Image Format (HEIF) compression options. Allows you to choose which compression format to use when creating a HEIF image file. |
| [**WICJpegCommentProperties**](/windows/win32/api/wincodec/ne-wincodec-wicjpegcommentproperties) | Specifies the JPEG comment properties. |
| [**WICJpegChrominanceProperties**](/windows/win32/api/wincodec/ne-wincodec-wicjpegchrominanceproperties) | Specifies the JPEG chrominance table property. |
| [**WICJpegIndexingOptions**](/windows/win32/api/wincodec/ne-wincodec-wicjpegindexingoptions) | Specifies the options for indexing a JPEG image.  |
| [**WICJpegLuminanceProperties**](/windows/win32/api/wincodec/ne-wincodec-wicjpegluminanceproperties) | Specifies the JPEG luminance table property. |
| [**WICJpegScanType**](/windows/win32/api/wincodec/ne-wincodec-wicjpegscantype) | Specifies the memory layout of pixel data in a JPEG image scan.  |
| [**WICJpegTransferMatrix**](/windows/win32/api/wincodec/ne-wincodec-wicjpegtransfermatrix) | Specifies conversion matrix from Y'Cb'Cr' to R'G'B'.  |
| [**WICJpegYCrCbSubsamplingOption**](/windows/win32/api/wincodec/ne-wincodec-wicjpegycrcbsubsamplingoption) | Specifies the JPEG YCrCB subsampling options.  |
| [**WICMetadataCreationOptions**](/windows/win32/api/Wincodecsdk/ne-wincodecsdk-wicmetadatacreationoptions) | Specifies metadata creation options. |
| [**WICNamedWhitePoint**](/windows/win32/api/wincodec/ne-wincodec-wicnamedwhitepoint) | Specifies named white balances for raw images. |
| [**WICPersistOptions**](/windows/win32/api/Wincodecsdk/ne-wincodecsdk-wicpersistoptions) | Specifies WIC options that are used when initializing a component with a stream. |
| [**WICPixelFormatNumericRepresentation**](/windows/win32/api/wincodec/ne-wincodec-wicpixelformatnumericrepresentation) | |
| [**WICPlanarOptions**](/windows/win32/api/wincodec/ne-wincodec-wicplanaroptions) | Specifies additional options to an [**IWICPlanarBitmapSourceTransform**](/windows/win32/api/wincodec/nn-wincodec-iwicplanarbitmapsourcetransform) implementation.  |
| [**WICProgressOperation**](/windows/win32/api/wincodec/ne-wincodec-wicprogressoperation) | Specifies the progress operations to receive notifications for. |
| [**WICPngBkgdProperties**](/windows/win32/api/wincodec/ne-wincodec-wicpngbkgdproperties) | Specifies the Portable Network Graphics (PNG) background (bKGD) chunk metadata properties. |
| [**WICPngChrmProperties**](/windows/win32/api/wincodec/ne-wincodec-wicpngchrmproperties) | Specifies the PNG cHRM chunk metadata properties for CIE XYZ chromaticity. |
| [**WICPngFilterOption**](/windows/win32/api/wincodec/ne-wincodec-wicpngfilteroption) | Specifies the PNG filters available for compression optimization. |
| [**WICPngGamaProperties**](/windows/win32/api/wincodec/ne-wincodec-wicpnggamaproperties) | Specifies the PNG gAMA chunk metadata properties. |
| [**WICPngHistProperties**](/windows/win32/api/wincodec/ne-wincodec-wicpnghistproperties) | Specifies the PNG hIST chunk metadata properties. |
| [**WICPngIccpProperties**](/windows/win32/api/wincodec/ne-wincodec-wicpngiccpproperties) | Specifies the PNG iCCP chunk metadata properties. |
| [**WICPngItxtProperties**](/windows/win32/api/wincodec/ne-wincodec-wicpngitxtproperties) | Specifies the PNG iTXT chunk metadata properties. |
| [**WICPngSrgbProperties**](/windows/win32/api/wincodec/ne-wincodec-wicpngsrgbproperties) | Specifies the PNG sRGB chunk metadata properties. |
| [**WICPngTimeProperties**](/windows/win32/api/wincodec/ne-wincodec-wicpngtimeproperties) | Specifies the PNG tIME chunk metadata properties. |
| [**WICProgressNotification**](/windows/win32/api/wincodec/ne-wincodec-wicprogressnotification) | Specifies when the progress notification callback should be called. |
| [**WICRawCapabilities**](/windows/win32/api/wincodec/ne-wincodec-wicrawcapabilities) | Specifies the capability support of a raw image. |
| [**WICRawParameterSet**](/windows/win32/api/wincodec/ne-wincodec-wicrawparameterset) | Specifies the parameter set used by a raw codec. |
| [**WICRawRenderMode**](/windows/win32/api/wincodec/ne-wincodec-wicrawrendermode) | Specifies the render intent of the next [**CopyPixels**](/windows/win32/api/wincodec/nf-wincodec-iwicbitmapsource-copypixels) call.  |
| [**WICRawRotationCapabilities**](/windows/win32/api/wincodec/ne-wincodec-wicrawrotationcapabilities) | Specifies the rotation capabilities of the codec. |
| [**WICSectionAccessLevel**](/windows/win32/api/wincodec/ne-wincodec-wicsectionaccesslevel) | Specifies the access level of a Windows Graphics Device Interface (GDI) section. |
| [**WICTiffCompressionOption**](/windows/win32/api/wincodec/ne-wincodec-wictiffcompressionoption) | Specifies the Tagged Image File Format (TIFF) compression options. |
