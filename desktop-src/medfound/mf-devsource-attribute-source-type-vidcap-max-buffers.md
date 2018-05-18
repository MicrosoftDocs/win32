---
Description: 'Specifies the maximum number of frames that the video capture source will buffer.'
ms.assetid: 'af30606b-f1a0-4fbf-a831-05ed891f5d53'
title: 'MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_MAX\_BUFFERS attribute'
---

# MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_MAX\_BUFFERS attribute

Specifies the maximum number of frames that the video capture source will buffer.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Remarks

By default, the video capture source buffers a maximum of one frame at a time. You can increase the buffer limit by setting this attribute.

The correct way to set this attribute depends on the function used to create the media source:

-   [**MFCreateDeviceSource**](mfcreatedevicesource.md): Set the attribute through the *pAttributes* parameter of the function.
-   [**MFCreateDeviceSourceActivate**](mfcreatedevicesourceactivate.md): Set the attribute through the *pAttributes* parameter of the function.
-   [**MFEnumDeviceSources**](mfenumdevicesources.md): Set the attribute on the [**IMFActivate**](imfactivate.md) pointer returned by the function. Set the attribute before calling [**IMFActivate::ActivateObject**](imfactivate-activateobject.md).

The attribute applies only to video capture devices.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Audio/Video Capture](audio-video-capture.md)
</dt> <dt>

[Capture Device Attributes](capture-device-attributes.md)
</dt> </dl>

 

 




