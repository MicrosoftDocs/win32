---
Description: 'Specifies the preferred output format for an encoder.'
ms.assetid: '36a09696-3fe7-41a0-93f1-712220f88b04'
title: 'MFT\_PREFERRED\_OUTPUTTYPE\_Attribute attribute'
---

# MFT\_PREFERRED\_OUTPUTTYPE\_Attribute attribute

Specifies the preferred output format for an encoder.

## Data type

**[**IMFAttributes**](imfattributes.md)\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](imfattributes-getunknown.md).

To set this attribute, call [**IMFAttributes::SetUnknown**](imfattributes-setunknown.md).

## Applies to

[**IMFActivate**](imfactivate.md)

## Remarks

This attribute can be set on the activation object returned by the [**MFCreateTransformActivate**](mfcreatetransformactivate.md) function. The attribute applies only when the activation object is configured to create an encoder. The value of the attribute is a media type. The activation object sets this output type on the encoder.

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

[**MFCreateTransformActivate**](mfcreatetransformactivate.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




