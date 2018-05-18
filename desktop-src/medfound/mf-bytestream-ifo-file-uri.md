---
Description: 'Contains the URL of the IFO (DVD Information) file specified by the HTTP server in the HTTP header, &\#0034;Pragma: ifoFileURI.dlna.org&\#0034;.'
ms.assetid: '007e0f4d-fb37-4dec-96a7-311df567eb04'
title: 'MF\_BYTESTREAM\_IFO\_FILE\_URI attribute'
---

# MF\_BYTESTREAM\_IFO\_FILE\_URI attribute

Contains the URL of the IFO (DVD Information) file specified by the HTTP server in the HTTP header, "Pragma: ifoFileURI.dlna.org".

## Data type

**LPWSTR**

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](imfattributes-getstring.md).

To set this attribute, call [**IMFAttributes::SetString**](imfattributes-setstring.md).

## Applies to

[**IMFByteStream**](imfbytestream.md)

## Remarks

The HTTP byte stream searches the HTTP header for the "ifoFileURI.dlna.org" string. If the string is found, it is copied to this attribute on the byte stream.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                                          |
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

[**IMFByteStream**](imfbytestream.md)
</dt> </dl>

 

 




