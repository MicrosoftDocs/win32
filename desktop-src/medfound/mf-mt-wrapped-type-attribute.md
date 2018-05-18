---
Description: 'Contains a media type that has been wrapped in another media type.'
ms.assetid: '3bd94523-0206-44d8-83a2-e569e4ab7815'
title: 'MF\_MT\_WRAPPED\_TYPE attribute'
---

# MF\_MT\_WRAPPED\_TYPE attribute

Contains a media type that has been wrapped in another media type.

## Data type

Byte array

## Remarks

This attribute is used in the [**MFWrapMediaType**](mfwrapmediatype.md) function, which wraps a media type inside another media type.

The [**MFWrapMediaType**](mfwrapmediatype.md) function does the following:

1.  Converts the original media type into a binary array.
2.  Sets the **MF\_MT\_WRAPPED\_TYPE** attribute on the new media type. The value of the attribute is the binary array.

Applications typically do not use this attribute directly. To unwrap the original media type, call [**MFUnwrapMediaType**](mfunwrapmediatype.md).

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetBlob**](imfattributes-getblob.md)
</dt> <dt>

[**IMFAttributes::SetBlob**](imfattributes-setblob.md)
</dt> <dt>

[**IMFMediaType**](imfmediatype.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




