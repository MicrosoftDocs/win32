---
Description: 'Contains the registered input types for a Media Foundation transform (MFT).'
ms.assetid: '0fb1d9f2-2b57-41bc-8365-0b88bd5a2f3d'
title: 'MFT\_INPUT\_TYPES\_Attributes attribute'
---

# MFT\_INPUT\_TYPES\_Attributes attribute

Contains the registered input types for a Media Foundation transform (MFT).

## Data type

**MFT\_REGISTER\_TYPE\_INFO\[\]** stored as **BYTE\[\]**

## Get/set

To get this attribute, call [**IMFAttributes::GetBlob**](imfattributes-getblob.md).

To set this attribute, call [**IMFAttributes::SetBlob**](imfattributes-setblob.md).

## Remarks

This attribute is set on the [**IMFActivate**](imfactivate.md) pointers returned by the [**MFTEnumEx**](mftenumex.md) function.

This attribute contains an array of [**MFT\_REGISTER\_TYPE\_INFO**](mft-register-type-info.md) structures that describe one or more input formats supported by the MFT. These values are taken from the registry and are intended as a hint to the application. The MFT might support additional formats. To set the actual input format, you must create the MFT and call [**IMFTransform::SetInputType**](imftransform-setinputtype.md).

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

 

 




