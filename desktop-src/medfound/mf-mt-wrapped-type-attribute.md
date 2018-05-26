---
Description: Contains a media type that has been wrapped in another media type.
ms.assetid: 3bd94523-0206-44d8-83a2-e569e4ab7815
title: MF\_MT\_WRAPPED\_TYPE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_WRAPPED\_TYPE attribute

Contains a media type that has been wrapped in another media type.

## Data type

Byte array

## Remarks

This attribute is used in the [**MFWrapMediaType**](/windows/win32/mfapi/nf-mfapi-mfwrapmediatype?branch=master) function, which wraps a media type inside another media type.

The [**MFWrapMediaType**](/windows/win32/mfapi/nf-mfapi-mfwrapmediatype?branch=master) function does the following:

1.  Converts the original media type into a binary array.
2.  Sets the **MF\_MT\_WRAPPED\_TYPE** attribute on the new media type. The value of the attribute is the binary array.

Applications typically do not use this attribute directly. To unwrap the original media type, call [**MFUnwrapMediaType**](/windows/win32/mfapi/nf-mfapi-mfunwrapmediatype?branch=master).

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

[**IMFAttributes::GetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getblob?branch=master)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setblob?branch=master)
</dt> <dt>

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




