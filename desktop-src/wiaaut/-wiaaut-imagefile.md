---
title: ImageFile object
description: Holds images transferred to your computer when you call Transfer or ShowTransfer.
ms.assetid: 35de5260-1c95-4247-8095-994b5084b390
keywords:
- ImageFile object WIA Automation
- ImageFile object WIA Automation , described
topic_type:
- apiref
api_name:
- ImageFile
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ImageFile object

Holds images transferred to your computer when you call [**Transfer**](-wiaaut-iitem-transfer.md) or [**ShowTransfer**](-wiaaut-icommondialog-showtransfer.md). The **ImageFile** object is a container. It also supports image files through LoadFile. An **ImageFile** object can be created using "WIA.ImageFile" as the ProgID in a call to [CreateObject](http://msdn.microsoft.com/library/7t9k08y5(VS.71).aspx).

## Members

The **ImageFile** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ImageFile** object has these methods.



| Method                                          | Description                                                        |
|:------------------------------------------------|:-------------------------------------------------------------------|
| [**LoadFile**](-wiaaut-iimagefile-loadfile.md) | Loads the **ImageFile** object with the specified file.<br/> |
| [**SaveFile**](-wiaaut-iimagefile-savefile.md) | Saves the **ImageFile** object to the specified file.<br/>   |



 

### Properties

The **ImageFile** object has these properties.



| Property                                                                             | Access type           | Description                                                                                       |
|:-------------------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------|
| [**ActiveFrame**](-wiaaut-iimagefile-activeframe.md)<br/>                     | Read/write<br/> | Sets or retrieves the current frame in the image.<br/>                                      |
| [**ARGBData**](-wiaaut-iimagefile-argbdata.md)<br/>                           | Read-only<br/>  | Retrieves the raw image bits as a [**Vector**](-wiaaut-vector.md) of **Long** values.<br/> |
| [**FileData**](-wiaaut-iimagefile-filedata.md)<br/>                           | Read-only<br/>  | Retrieves the raw image file as a [**Vector**](-wiaaut-vector.md) of bytes.<br/>           |
| [**FileExtension**](-wiaaut-iimagefile-fileextension.md)<br/>                 | Read-only<br/>  | Retrieves the file extension for this image file type.<br/>                                 |
| [**FormatID**](-wiaaut-iimagefile-formatid.md)<br/>                           | Read-only<br/>  | Retrieves the FormatID for this file type.<br/>                                             |
| [**FrameCount**](-wiaaut-iimagefile-framecount.md)<br/>                       | Read-only<br/>  | Retrieves the number of frames in the image.<br/>                                           |
| [**Height**](-wiaaut-iimagefile-height.md)<br/>                               | Read-only<br/>  | Retrieves the height of the image in pixels.<br/>                                           |
| [**HorizontalResolution**](-wiaaut-iimagefile-horizontalresolution.md)<br/>   | Read-only<br/>  | Retrieves the horizontal pixels per inch of the image.<br/>                                 |
| [**IsAlphaPixelFormat**](-wiaaut-iimagefile-isalphapixelformat.md)<br/>       | Read-only<br/>  | Specifies whether the pixel format has an alpha component.<br/>                             |
| [**IsAnimated**](-wiaaut-iimagefile-isanimated.md)<br/>                       | Read-only<br/>  | Specifies whether the image is animated.<br/>                                               |
| [**IsExtendedPixelFormat**](-wiaaut-iimagefile-isextendedpixelformat.md)<br/> | Read-only<br/>  | Specifies whether the pixel format is extended (16 bits per channel).<br/>                  |
| [**IsIndexedPixelFormat**](-wiaaut-iimagefile-isindexedpixelformat.md)<br/>   | Read-only<br/>  | Specifies whether the pixel data is an index into a palette or the actual color data.<br/>  |
| [**PixelDepth**](-wiaaut-iimagefile-pixeldepth.md)<br/>                       | Read-only<br/>  | Retrieves the depth of the pixels of the image in BPP.<br/>                                 |
| [**Properties (ImageFile)**](-wiaaut-iimagefile-properties.md)<br/>           | Read-only<br/>  | Retrieves an **ImageFile** collection of all properties for this image.<br/>                |
| [**VerticalResolution**](-wiaaut-iimagefile-verticalresolution.md)<br/>       | Read-only<br/>  | Retrieves the vertical pixels per inch of the image.<br/>                                   |
| [**Width**](-wiaaut-iimagefile-width.md)<br/>                                 | Read-only<br/>  | Retrieves the width of the image in pixels.<br/>                                            |



 

## Remarks

Note that while the **ImageFile** object is intended for use with image files, non-image files support [**FileExtension**](-wiaaut-iimagefile-fileextension.md), [**FileData**](-wiaaut-iimagefile-filedata.md) and [**SaveFile**](-wiaaut-iimagefile-savefile.md).

For example code, see [Display Detailed Image Information](-wiaaut-shared-samples.md#display-detailed-image-information) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**ImageFile (Vector)**](-wiaaut-ivector-imagefile.md)

[**Apply**](-wiaaut-iimageprocess-apply.md)

[**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md)
</dt> <dt>

[**Apply**](-wiaaut-iimageprocess-apply.md)
</dt> <dt>

[**ImageFile (Vector)**](-wiaaut-ivector-imagefile.md)
</dt> </dl>

 

 





