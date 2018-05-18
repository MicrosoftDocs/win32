---
title: RFC1522INFO structure
description: Do not use. Holds information about RFC 1522 encoding. Various members of this structure are used in calls to DecodeHeader and EncodeHeader.
ms.assetid: '4d6c1416-f4bb-4dfe-9eda-831c085c206e'
keywords: ["RFC1522INFO structure Windows Mail (formerly Outlook Express)", "LPRFC1522INFO structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- RFC1522INFO
api_location:
- Mimeole.h
api_type:
- HeaderDef
---

# RFC1522INFO structure

Do not use. Holds information about [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding. Various members of this structure are used in calls to [**DecodeHeader**](oe-imimeinternational-decodeheader.md) and [**EncodeHeader**](oe-imimeinternational-encodeheader.md).

## Syntax


```C++
typedef struct tagRFC1522INFO {
  BOOL     fRfc1522Allowed;
  BOOL     fRfc1522Used;
  BOOL     fAllow8bit;
  HCHARSET hRfc1522Cset;
} RFC1522INFO, *LPRFC1522INFO;
```



## Members

<dl> <dt>

**fRfc1522Allowed**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Indicates whether [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding can be used. The [**EncodeHeader**](oe-imimeinternational-encodeheader.md) method uses this member.



| Value                                                                                                                                | Meaning                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding cannot be used. [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding should not be used on non-MIME messages. <br/> |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding can be used.<br/>                                                                                                       |



 

</dd> <dt>

**fRfc1522Used**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Indicates whether [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding was used to encode or decode the header. The [**EncodeHeader**](oe-imimeinternational-encodeheader.md) and [**DecodeHeader**](oe-imimeinternational-decodeheader.md) methods use this member.



| Value                                                                                                                                | Meaning                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding was removed. <br/> |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding was applied. <br/> |



 

</dd> <dt>

**fAllow8bit**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Indicates whether the client has specified permission to transmit 8-bit characters. The [**EncodeHeader**](oe-imimeinternational-encodeheader.md) method uses this member.



| Value                                                                                                                                | Meaning                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | Use [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding. <br/>        |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | Do not use [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding. <br/> |



 

</dd> <dt>

**hRfc1522Cset**
</dt> <dd>

Type: **HCHARSET**

</dd> <dd>

Contains the handle to the character set that was contained in the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding. The [**DecodeHeader**](oe-imimeinternational-decodeheader.md) method uses this member.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





