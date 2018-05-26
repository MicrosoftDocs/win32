---
Description: Sets the processing mode of the Video Stabilization MFT.
ms.assetid: 0D49892A-8628-4F2B-B41B-51160A19DC9B
title: MF\_VIDEODSP\_MODE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_VIDEODSP\_MODE attribute

Sets the processing mode of the [**Video Stabilization MFT**](video-stabilization-mft.md).

## Data type

**MFVideoDSPMode** stored as **UIINT32**

## Remarks

The value of this attribute is an [**MFVideoDSPMode**](/windows/win32/wmcodecdsp/ne-wmcodecdsp-_mfvideodspmode?branch=master) enumeration value. This attribute can be used to enable or disable the image stabilization, and can be updated for each output sample.

To set this attribute:

1.  Call [**IMFTransform::GetAttributes**](/windows/win32/mftransform/nf-mftransform-imftransform-getattributes?branch=master) on the video stabilization MFT to get an [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) pointer.
2.  Call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master) to set the attribute.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**Video Stabilization MFT**](video-stabilization-mft.md)
</dt> </dl>

 

 




