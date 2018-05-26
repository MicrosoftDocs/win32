---
Description: Specifies the device role for an audio capture device.
ms.assetid: 4f2885b6-c771-4577-880d-5feea671432e
title: MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_AUDCAP\_ROLE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_AUDCAP\_ROLE attribute

Specifies the device role for an audio capture device.

## Data type

**ERole** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Remarks

The **eRole** enumeration type is documented in the Core Audio API documentation.

The value of the attribute specifies a device role. This attribute is used with the following functions.

This attribute can be used as input to the [**MFCreateDeviceSource**](/windows/win32/mfidl/nf-mfidl-mfcreatedevicesource?branch=master) and [**MFCreateDeviceSourceActivate**](/windows/win32/mfidl/nf-mfidl-mfcreatedevicesourceactivate?branch=master) functions. If the attribute is specified, the function creates a media source that uses the default audio capture device for the specified device role.

This attribute can also be used as input to the [**MFEnumDeviceSources**](/windows/win32/mfidl/nf-mfidl-mfenumdevicesources?branch=master) function. If the attribute is specified, the enumeration is restricted to the specified device role. In addition, each activation object returned by the **MFEnumDeviceSources** function contains this attribute. The attribute is then used internally by the activation object when it creates the media source.

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

 

 




