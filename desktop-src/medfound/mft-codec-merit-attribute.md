---
Description: 'Contains the merit value of a hardware codec.'
ms.assetid: '1df40a42-4c02-473f-a87f-2ae2d42e4f4e'
title: 'MFT\_CODEC\_MERIT\_Attribute attribute'
---

# MFT\_CODEC\_MERIT\_Attribute attribute

Contains the merit value of a hardware codec.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Remarks

This attribute is set on the activation object for a Media Foundation transform (MFT) that represents a hardware codec. The value of the attribute is the codec's merit value.

This attribute controls the order in which the [**MFTEnumEx**](mftenumex.md) function enumerates codecs, if the **MFT\_ENUM\_FLAG\_SORTANDFILTER** flag is set. MFTs with a merit value appear higher in the list than other MFTs.

This attribute does not contain a trusted value. To verify the codec's actual merit value, call the [**MFGetMFTMerit**](mfgetmftmerit.md) function.

If the value of the MFT\_CODEC\_MERIT\_Attribute attribute does not match the merit value retrieved by [**MFGetMFTMerit**](mfgetmftmerit.md), the [**IMFActivate::ActivateObject**](imfactivate-activateobject.md) method fails and returns **MF\_E\_INVALID\_CODEC\_MERIT**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                          |
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

 

 




