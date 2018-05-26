---
Description: Contains the photo thumbnail of a IMFSample.
ms.assetid: 510706A3-92FB-4188-97B9-6E8E0B4B175F
title: MFSampleExtension\_PhotoThumbnail attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFSampleExtension\_PhotoThumbnail attribute

Contains the photo thumbnail of a [**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master).

## Data type

**IUnknown** stored as **IMFMediaBuffer**

The thumbnail is configured using the **KSPROPERTYSETID\_ExtendedCameraControl**.

## Remarks

This attribute is set on the [**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master) provided by the MFT0 and is the [**IUnknown**](com.iunknown) interface of the [**IMFMediaBuffer**](/windows/win32/mfobjects/nn-mfobjects-imfmediabuffer?branch=master) associated with the photo thumbnail.

The format of the photo thumbnail can be JPEG (major type image), NV12 or ARGB32.

The [MFSampleExtension\_PhotoThumbnailMediaType](mfsampleextension-photothumbnailmediatype.md) is required for thumbnails to describe the media type.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master)
</dt> </dl>

 

 




