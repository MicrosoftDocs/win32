---
Description: Specifies the device category for a video capture device.
ms.assetid: 008ff9df-ebe0-4efd-a62c-24f4a4239ebd
title: MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_CATEGORY attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_CATEGORY attribute

Specifies the device category for a video capture device.

## Data type

**GUID**

The following value is defined.



| Value                                                                                                                                                                                                                                                             | Meaning                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| <span id="CLSID_VideoInputDeviceCategory"></span><span id="clsid_videoinputdevicecategory"></span><span id="CLSID_VIDEOINPUTDEVICECATEGORY"></span><dl> <dt>**CLSID\_VideoInputDeviceCategory**</dt> </dl> | Video capture device.<br/> |



 

## Get/set

To get this attribute, call [**IMFAttributes::GetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getguid?branch=master).

To set this attribute, call [**IMFAttributes::SetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setguid?branch=master).

## Remarks

Use this attribute as input to the [**MFEnumDeviceSources**](/windows/win32/mfidl/nf-mfidl-mfenumdevicesources?branch=master) function when enumerating video capture devices.

In addition, this attribute is set on the activation objects returned by the following functions:

-   [**MFCreateDeviceSourceActivate**](/windows/win32/mfidl/nf-mfidl-mfcreatedevicesourceactivate?branch=master)
-   [**MFEnumDeviceSources**](/windows/win32/mfidl/nf-mfidl-mfenumdevicesources?branch=master)

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

 

 




