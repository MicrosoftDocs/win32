---
description: Contains the merit value of a hardware codec.
ms.assetid: 1df40a42-4c02-473f-a87f-2ae2d42e4f4e
title: MFT_CODEC_MERIT_Attribute attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_CODEC\_MERIT\_Attribute attribute

Contains the merit value of a hardware codec.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

This attribute is set on the activation object for a Media Foundation transform (MFT) that represents a hardware codec. The value of the attribute is the codec's merit value.

This attribute controls the order in which the [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex) function enumerates codecs, if the **MFT\_ENUM\_FLAG\_SORTANDFILTER** flag is set. MFTs with a merit value appear higher in the list than other MFTs.

This attribute does not contain a trusted value. To verify the codec's actual merit value, call the [**MFGetMFTMerit**](/windows/desktop/api/mfapi/nf-mfapi-mfgetmftmerit) function.

If the value of the MFT\_CODEC\_MERIT\_Attribute attribute does not match the merit value retrieved by [**MFGetMFTMerit**](/windows/desktop/api/mfapi/nf-mfapi-mfgetmftmerit), the [**IMFActivate::ActivateObject**](/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-activateobject) method fails and returns **MF\_E\_INVALID\_CODEC\_MERIT**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




