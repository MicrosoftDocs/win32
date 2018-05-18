---
Description: 'Specifies the output format of a device.'
ms.assetid: '33a1b546-ece2-44ef-a1c0-5579c32be0bc'
title: 'MF\_DEVSOURCE\_ATTRIBUTE\_MEDIA\_TYPE attribute'
---

# MF\_DEVSOURCE\_ATTRIBUTE\_MEDIA\_TYPE attribute

Specifies the output format of a device.

## Data type

**[**MFT\_REGISTER\_TYPE\_INFO**](mft-register-type-info.md)** stored as **BYTE\[\]**

## Get/set

To get this attribute, call [**IMFAttributes::GetBlob**](imfattributes-getblob.md).

To set this attribute, call [**IMFAttributes::SetBlob**](imfattributes-setblob.md).

## Remarks

This attribute contains a pair of GUIDs: a major type and a subtype. These GUIDs describe the default output format of the device. The device might support additional output formats.

For example, if a video capture device outputs RGB-32 video, the value of this attribute is `{ MFMediaType_Video, MFVideoFormat_RGB32 }`.

This attribute is a hint to the application. To get the exact output format, create the media source for the device and get the media source's presentation descriptor.

This attribute is set on the activation objects returned by the following functions:

-   [**MFCreateDeviceSourceActivate**](mfcreatedevicesourceactivate.md)
-   [**MFEnumDeviceSources**](mfenumdevicesources.md)

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

 

 




