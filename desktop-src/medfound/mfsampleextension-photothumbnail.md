---
Description: Contains the photo thumbnail of a IMFSample.
ms.assetid: 510706A3-92FB-4188-97B9-6E8E0B4B175F
title: MFSampleExtension\_PhotoThumbnail attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFSampleExtension\_PhotoThumbnail attribute

Contains the photo thumbnail of a [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample).

## Data type

**IUnknown** stored as **IMFMediaBuffer**

The thumbnail is configured using the **KSPROPERTYSETID\_ExtendedCameraControl**.

## Remarks

This attribute is set on the [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) provided by the MFT0 and is the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface of the [**IMFMediaBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer) associated with the photo thumbnail.

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

[**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample)
</dt> </dl>

 

 




