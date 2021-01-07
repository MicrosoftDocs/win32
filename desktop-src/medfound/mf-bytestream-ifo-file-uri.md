---
description: 'Contains the URL of the IFO (DVD Information) file specified by the HTTP server in the HTTP header, &\#0034;Pragma: ifoFileURI.dlna.org&\#0034;.'
ms.assetid: 007e0f4d-fb37-4dec-96a7-311df567eb04
title: MF_BYTESTREAM_IFO_FILE_URI attribute (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_BYTESTREAM\_IFO\_FILE\_URI attribute

Contains the URL of the IFO (DVD Information) file specified by the HTTP server in the HTTP header, "Pragma: ifoFileURI.dlna.org".

## Data type

**LPWSTR**

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getstring).

To set this attribute, call [**IMFAttributes::SetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setstring).

## Applies to

[**IMFByteStream**](/windows/desktop/api/mfobjects/nn-mfobjects-imfbytestream)

## Remarks

The HTTP byte stream searches the HTTP header for the "ifoFileURI.dlna.org" string. If the string is found, it is copied to this attribute on the byte stream.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                                           |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Byte Stream Attributes](byte-stream-attributes.md)
</dt> <dt>

[**IMFByteStream**](/windows/desktop/api/mfobjects/nn-mfobjects-imfbytestream)
</dt> </dl>

 

 




