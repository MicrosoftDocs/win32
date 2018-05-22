---
Description: 'Specifies a device's type, such as audio capture or video capture.'
ms.assetid: 'c6c05267-1c93-48e2-b463-b5a1514f1b7b'
title: 'MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE attribute'
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

To get this attribute, call [**IMFAttributes::GetGUID**](imfattributes-getguid.md).

To set this attribute, call [**IMFAttributes::SetGUID**](imfattributes-setguid.md).

## Remarks

Use this attribute as input to the following functions:

-   [**MFCreateDeviceSource**](mfcreatedevicesource.md)
-   [**MFCreateDeviceSourceActivate**](mfcreatedevicesourceactivate.md)
-   [**MFEnumDeviceSources**](mfenumdevicesources.md)

In addition, this attribute is set on the activation objects returned by the [**MFEnumDeviceSources**](mfenumdevicesources.md) function.

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

 

 




