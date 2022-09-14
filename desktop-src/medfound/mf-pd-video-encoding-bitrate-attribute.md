---
description: Specifies the video encoding bit rate for the presentation, in bits per second. This attribute applies to presentation descriptors.
ms.assetid: 0fe8cf64-2256-4e48-9853-2c734f97f3c7
title: MF_PD_VIDEO_ENCODING_BITRATE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_PD\_VIDEO\_ENCODING\_BITRATE attribute

Specifies the video encoding bit rate for the presentation, in bits per second. This attribute applies to presentation descriptors.

## Data type

**UINT32**

## Remarks

This attribute is optional. Some formats have more complex encoding schemes that cannot be summarized by using this attribute. For Advanced Systems Format (ASF) files, the following attributes collectively describe the encoding bit rate:

-   [**MF\_PD\_ASF\_FILEPROPERTIES\_MAX\_BITRATE**](mf-pd-asf-fileproperties-max-bitrate-attribute.md)
-   [**MF\_SD\_ASF\_EXTSTRMPROP\_AVG\_DATA\_BITRATE**](mf-sd-asf-extstrmprop-avg-data-bitrate-attribute.md)
-   [**MF\_SD\_ASF\_EXTSTRMPROP\_MAX\_DATA\_BITRATE**](mf-sd-asf-extstrmprop-max-data-bitrate-attribute.md)
-   [**MF\_SD\_ASF\_STREAMBITRATES\_BITRATE**](mf-sd-asf-streambitrates-bitrate-attribute.md)

Third-party formats might use other custom attributes.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> </dl>

 

 




