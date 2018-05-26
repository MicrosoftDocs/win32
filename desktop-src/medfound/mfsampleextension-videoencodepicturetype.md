---
Description: Specifies the type of picture that is output by a video encoder.
ms.assetid: 18A47033-3EAC-46C3-94AB-6ED20732F63C
title: MFSampleExtension\_VideoEncodePictureType attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFSampleExtension\_VideoEncodePictureType attribute

Specifies the type of picture that is output by a video encoder.

## Data type

**eAVEncH264PictureType\_B** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Applies to

[**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master)

## Remarks

The [**H.264 Video Encoder**](h-264-video-encoder.md) sets this attribute on the output samples that it generates. The value of the attribute is a member of the [**eAVEncH264PictureType**](/windows/win32/codecapi/ne-codecapi-eavench264picturetype?branch=master) enumeration.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**H.264 Video Encoder**](h-264-video-encoder.md)
</dt> <dt>

[Sample Attributes](sample-attributes.md)
</dt> <dt>

[Media Samples](media-samples.md)
</dt> </dl>

 

 




