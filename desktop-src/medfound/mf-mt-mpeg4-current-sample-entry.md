---
description: Specifies the current entry in the sample description box for an MPEG-4 media type.
ms.assetid: c8c36abf-6905-4874-a6d2-90dd0725421b
title: MF_MT_MPEG4_CURRENT_SAMPLE_ENTRY attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_MPEG4\_CURRENT\_SAMPLE\_ENTRY attribute

Specifies the current entry in the sample description box for an MPEG-4 media type.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)

## Remarks

In an MP4 or 3GP file, the sample description box describes the encoding used for a stream in the file. The sample description box can contain multiple entries. This attribute specifies which entry to use. The value is a zero-based index into the list.

Currently, the only supported value is 0. The attribute has been defined for future extensibility.

The MPEG-4 file source always sets the value to 0. The MP4 and 3GP file sinks ignore the value of this attribute if it is present.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[MF\_MT\_MPEG4\_SAMPLE\_DESCRIPTION](mf-mt-mpeg4-sample-description.md)
</dt> </dl>

 

 




