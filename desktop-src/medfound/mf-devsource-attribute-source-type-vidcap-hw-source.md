---
Description: 'Specifies whether a video capture source is a hardware device or a software device.'
ms.assetid: '4a886124-54f1-4cd1-a22b-552e8c8d556f'
title: 'MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_HW\_SOURCE attribute'
---

# MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_HW\_SOURCE attribute

Specifies whether a video capture source is a hardware device or a software device.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Remarks

If the value is **TRUE**, the capture source is a hardware device. If the value is **FALSE**, it is a software device. The default value is **FALSE**.

This attribute is set on the activation objects returned by the following functions:

-   [**MFCreateDeviceSourceActivate**](mfcreatedevicesourceactivate.md)
-   [**MFEnumDeviceSources**](mfenumdevicesources.md)

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

 

 




