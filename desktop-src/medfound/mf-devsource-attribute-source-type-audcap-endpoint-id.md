---
Description: 'Specifies the endpoint ID for an audio capture device.'
ms.assetid: 'a0d8b54b-7a05-4307-a756-a34bb22f1afd'
title: 'MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_AUDCAP\_ENDPOINT\_ID attribute'
---

# MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_AUDCAP\_ENDPOINT\_ID attribute

Specifies the endpoint ID for an audio capture device.

## Data type

**WCHAR\***

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](imfattributes-getstring.md).

To set this attribute, call [**IMFAttributes::SetString**](imfattributes-setstring.md).

## Remarks

The value of the attribute is an endpoint ID. This attribute is used with the following functions:

-   It can be used as input to the [**MFCreateDeviceSource**](mfcreatedevicesource.md) and [**MFCreateDeviceSourceActivate**](mfcreatedevicesourceactivate.md) functions. In this context, the attribute specifies the audio capture device for the function. You can get the endpoint ID for a given device by calling the [**IMMDevice::GetId**](coreaudio.immdevice_getid) method. See the Core Audio API documentation for more information.
-   When the [**MFEnumDeviceSources**](mfenumdevicesources.md) function enumerates audio devices, the returned activation objects contain this attribute. The attribute is used internally by the activation object when it creates the media source.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                   |                                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Audio/Video Capture](audio-video-capture.md)
</dt> <dt>

[Capture Device Attributes](capture-device-attributes.md)
</dt> </dl>

 

 




