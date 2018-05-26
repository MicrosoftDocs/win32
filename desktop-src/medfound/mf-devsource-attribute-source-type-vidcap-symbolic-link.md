---
Description: Contains the symbolic link for a video capture driver.
ms.assetid: 3d256dec-ec8c-4c62-883b-e2c292fd90eb
title: MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_SYMBOLIC\_LINK attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_SYMBOLIC\_LINK attribute

Contains the symbolic link for a video capture driver.

## Data type

**WCHAR\***

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getstring?branch=master).

To set this attribute, call [**IMFAttributes::SetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setstring?branch=master).

## Remarks

Use this attribute as input to the [**MFCreateDeviceSourceActivate**](/windows/win32/mfidl/nf-mfidl-mfcreatedevicesourceactivate?branch=master) function.

In addition, this attribute is set on the activation objects returned by the following functions:

-   [**MFCreateDeviceSourceActivate**](/windows/win32/mfidl/nf-mfidl-mfcreatedevicesourceactivate?branch=master)
-   [**MFEnumDeviceSources**](/windows/win32/mfidl/nf-mfidl-mfenumdevicesources?branch=master)

The symbolic link should be considered an opaque string. The human-readable display name for a device is contained in the [MF\_DEVSOURCE\_ATTRIBUTE\_FRIENDLY\_NAME](mf-devsource-attribute-friendly-name.md) attribute.

The MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_SYMBOLIC\_LINK attribute can be passed in as the value of the DevicePath argument of the [**SetupDiOpenDeviceInterface**](devinst.setupdiopendeviceinterface) function.

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

 

 




