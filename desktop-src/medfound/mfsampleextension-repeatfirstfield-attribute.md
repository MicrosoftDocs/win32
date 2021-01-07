---
description: Specifies whether to repeat the first field in an interlaced frame. This attribute applies to media samples.
ms.assetid: c469f418-fa23-443f-8012-0d548ee98c17
title: MFSampleExtension_RepeatFirstField attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_RepeatFirstField attribute

Specifies whether to repeat the first field in an interlaced frame. This attribute applies to media samples.

## Data type

**BOOL** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample)

## Remarks

If the value is **FALSE** or the attribute is not set, the first field is not repeated. If the value is **TRUE**, the first field is repeated. The value **TRUE** is valid only when the following conditions are true:

-   The media type is mixed interlaced and progressive. (The [**MF\_MT\_INTERLACE\_MODE**](mf-mt-interlace-mode-attribute.md) attribute attribute on the media type is **MFVideoInterlace\_MixedInterlaceOrProgressive**.)
-   The frame is progressive and the [**MFSampleExtension\_Interlaced**](mfsampleextension-interlaced-attribute.md) attribute on the sample is **TRUE**.
-   The [**MFSampleExtension\_BottomFieldFirst**](mfsampleextension-bottomfieldfirst-attribute.md) attribute is set on the sample. The value can be **TRUE** or **FALSE**. The ordering of the fields is determined by this attribute.

This attribute is used for 3:2 pulldown. The following table shows the order in which fields are displayed.



| MFSampleExtension\_RepeatFirstField | MFSampleExtension\_BottomFieldFirst | Field order         |
|-------------------------------------|-------------------------------------|---------------------|
| **TRUE**                            | **TRUE**                            | Lower, upper, lower |
| **TRUE**                            | **FALSE**                           | Upper, lower, upper |
| **FALSE**                           | **TRUE**                            | Lower, upper        |
| **FALSE**                           | **FALSE**                           | Upper, lower        |



 

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Sample Attributes](sample-attributes.md)
</dt> <dt>

[Media Samples](media-samples.md)
</dt> <dt>

[Video Interlacing](video-interlacing.md)
</dt> </dl>

 

 




