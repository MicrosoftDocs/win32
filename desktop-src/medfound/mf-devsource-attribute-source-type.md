---
Description: Specifies a devices type, such as audio capture or video capture.
ms.assetid: c6c05267-1c93-48e2-b463-b5a1514f1b7b
title: MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE attribute

Specifies a device's type, such as audio capture or video capture.

## Data type

**GUID**

The following values are defined for this attribute:



| Value                                                                                                                                                                                                                                                                 | Meaning                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| <span id="MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_AUDCAP_GUID"></span><span id="mf_devsource_attribute_source_type_audcap_guid"></span><dl> <dt>**MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_AUDCAP\_GUID**</dt> </dl> | Audio capture device.<br/> |
| <span id="MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_GUID"></span><span id="mf_devsource_attribute_source_type_vidcap_guid"></span><dl> <dt>**MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_GUID**</dt> </dl> | Video capture device.<br/> |



 

## Get/set

To get this attribute, call [**IMFAttributes::GetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getguid?branch=master).

To set this attribute, call [**IMFAttributes::SetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setguid?branch=master).

## Remarks

Use this attribute as input to the following functions:

-   [**MFCreateDeviceSource**](/windows/win32/mfidl/nf-mfidl-mfcreatedevicesource?branch=master)
-   [**MFCreateDeviceSourceActivate**](/windows/win32/mfidl/nf-mfidl-mfcreatedevicesourceactivate?branch=master)
-   [**MFEnumDeviceSources**](/windows/win32/mfidl/nf-mfidl-mfenumdevicesources?branch=master)

In addition, this attribute is set on the activation objects returned by the [**MFEnumDeviceSources**](/windows/win32/mfidl/nf-mfidl-mfenumdevicesources?branch=master) function.

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

 

 




