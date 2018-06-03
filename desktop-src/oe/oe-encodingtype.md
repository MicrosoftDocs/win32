---
title: ENCODINGTYPE enumeration
description: Do not use. Specifies how something is encoded or intended to be encoded.
ms.assetid: 0f3cfa2c-182c-4133-a792-eacdad81879c
keywords:
- ENCODINGTYPE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# ENCODINGTYPE enumeration

Do not use. Specifies how something is encoded or intended to be encoded.

## Syntax


```C++
typedef enum tagENCODINGTYPE { 
  IET_BINARY    = 0,
  IET_BASE64    = 1,
  IET_UUENCODE  = 2,
  IET_QP        = 3,
  IET_7BIT      = 4,
  IET_8BIT      = 5,
  IET_INETCSET  = 6,
  IET_UNICODE   = 7,
  IET_RFC1522   = 8,
  IET_ENCODED   = 9,
  IET_CURRENT   = 10,
  IET_UNKNOWN   = 11,
  IET_BINHEX40  = 12,
  IET_LAST      = 13
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="IET_BINARY"></span><span id="iet_binary"></span>**IET\_BINARY**
</dt> <dd>

Indicates that the data is in its native format and is not encoded. The value IET\_DECODED can also be used.

</dd> <dt>

<span id="IET_BASE64"></span><span id="iet_base64"></span>**IET\_BASE64**
</dt> <dd>

Indicates MIME Base64 encoding. Base64 should be used for data that contains mostly 8-bit bytes.

</dd> <dt>

<span id="IET_UUENCODE"></span><span id="iet_uuencode"></span>**IET\_UUENCODE**
</dt> <dd>

Indicates uuencode encoding (found mostly in Usenet newsgroups). Uuencode should only be used for attachments in a non-MIME message.

</dd> <dt>

<span id="IET_QP"></span><span id="iet_qp"></span>**IET\_QP**
</dt> <dd>

Indicates MIME Quoted-Printable encoding. Quoted-Printable should be used for text bodies that contain a small amount of 8-bit characters (that is, less than 10%) or for text bodies that have lines longer than 76 characters.

</dd> <dt>

<span id="IET_7BIT"></span><span id="iet_7bit"></span>**IET\_7BIT**
</dt> <dd>

Indicates that the data is not encoded and it does not contain any 8-bit bytes.

</dd> <dt>

<span id="IET_8BIT"></span><span id="iet_8bit"></span>**IET\_8BIT**
</dt> <dd>

Indicates that the data is not encoded and it contains 8-bit bytes.

</dd> <dt>

<span id="IET_INETCSET"></span><span id="iet_inetcset"></span>**IET\_INETCSET**
</dt> <dd>

Indicates that the data is encoded in the Internet code page of a character set.

</dd> <dt>

<span id="IET_UNICODE"></span><span id="iet_unicode"></span>**IET\_UNICODE**
</dt> <dd>

Indicates that the data is in the Windows Unicode format (16-bit characters).

</dd> <dt>

<span id="IET_RFC1522"></span><span id="iet_rfc1522"></span>**IET\_RFC1522**
</dt> <dd>

Indicates that the header property is encoded in [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) format.

</dd> <dt>

<span id="IET_ENCODED"></span><span id="iet_encoded"></span>**IET\_ENCODED**
</dt> <dd>

Indicates that the data is encoded. This is nonspecific and means that the data probably inherits some default encoding format.

</dd> <dt>

<span id="IET_CURRENT"></span><span id="iet_current"></span>**IET\_CURRENT**
</dt> <dd>

Indicates no change in encoding.

</dd> <dt>

<span id="IET_UNKNOWN"></span><span id="iet_unknown"></span>**IET\_UNKNOWN**
</dt> <dd>

Indicates that the encoding type is unknown or invalid. The data can be treated as binary.

</dd> <dt>

<span id="IET_BINHEX40"></span><span id="iet_binhex40"></span>**IET\_BINHEX40**
</dt> <dd>

Indicates Apple Macintosh BinHex encoding.

</dd> <dt>

<span id="IET_LAST"></span><span id="iet_last"></span>**IET\_LAST**
</dt> <dd>

Do not use.

</dd> </dl>

## Remarks

The value -1 is reserved for an [**IMimeSecurity**](oe-imimesecurity.md) default.



| ENCODINGTYPE  | Internet Charset | Internet Encoding | Transmittable |
|---------------|------------------|-------------------|---------------|
| IET\_BINARY   | No               | No                | No            |
| IET\_BASE64   | Yes              | Yes               | Yes           |
| IET\_UUENCODE | Yes              | Yes               | Yes           |
| IET\_QP       | Yes              | Yes               | Yes           |
| IET\_7BIT     | Yes              | No (Dot Stuffed)  | Yes           |
| IET\_8BIT     | Yes              | No (Dot Stuffed)  | Yes           |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





