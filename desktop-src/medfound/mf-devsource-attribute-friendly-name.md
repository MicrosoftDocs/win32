---
Description: 'Specifies the display name for a device.'
ms.assetid: '3f6c7faf-2ecd-4510-adc2-252c3619d70f'
title: 'MF\_DEVSOURCE\_ATTRIBUTE\_FRIENDLY\_NAME attribute'
---

# MF\_DEVSOURCE\_ATTRIBUTE\_FRIENDLY\_NAME attribute

Specifies the display name for a device. The *display name* is a human-readable string, suitable for display in a user interface.

## Data type

**WCHAR\***

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](imfattributes-getstring.md).

To set this attribute, call [**IMFAttributes::SetString**](imfattributes-setstring.md).

## Remarks

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

 

 




