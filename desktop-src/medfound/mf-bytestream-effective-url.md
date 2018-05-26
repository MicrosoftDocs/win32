---
Description: Gets the effective URL of a byte stream.
ms.assetid: 0A83CFC0-7EAA-464B-BA39-50DF220AF683
title: MF\_BYTESTREAM\_EFFECTIVE\_URL attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_BYTESTREAM\_EFFECTIVE\_URL attribute

Gets the effective URL of a byte stream.

## Data type

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getstring?branch=master).

To set this attribute, call [**IMFAttributes::SetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setstring?branch=master).

## Applies to

[**IMFByteStream**](/windows/win32/mfobjects/nn-mfobjects-imfbytestream?branch=master)

## Remarks

The effective URL can differ from the original URL if the original URL contains any extra information, such as search strings or anchors, or if the request was redirected.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfobjects.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Byte Stream Attributes](byte-stream-attributes.md)
</dt> <dt>

[**IMFByteStream**](/windows/win32/mfobjects/nn-mfobjects-imfbytestream?branch=master)
</dt> </dl>

 

 




