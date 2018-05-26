---
title: MIMEPROPFLAGS enumeration
description: Do not use. Defines aspects of a MimeOLE property.
ms.assetid: 68d8e2e1-5553-4377-a34e-689025ce277c
keywords:
- MIMEPROPFLAGS enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MIMEPROPFLAGS enumeration

Do not use. Defines aspects of a MimeOLE property.

## Syntax


```C++
typedef enum tagMIMEPROPFLAGS { 
  MPF_INETCSET   = 0x00000001,
  MPF_RFC1522    = 0x00000002,
  MPF_ADDRESS    = 0x00000004,
  MPF_HASPARAMS  = 0x00000008,
  MPF_MIME       = 0x00000010,
  MPF_READONLY   = 0x00000020
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="MPF_INETCSET"></span><span id="mpf_inetcset"></span>**MPF\_INETCSET**
</dt> <dd>

Indicates that the property can be encoded in an Internet code page before transmission.

</dd> <dt>

<span id="MPF_RFC1522"></span><span id="mpf_rfc1522"></span>**MPF\_RFC1522**
</dt> <dd>

Indicates that the property can be encoded using [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) to try to remove 8-bit characters.

</dd> <dt>

<span id="MPF_ADDRESS"></span><span id="mpf_address"></span>**MPF\_ADDRESS**
</dt> <dd>

Indicates that the property contains a set of Internet addresses.

</dd> <dt>

<span id="MPF_HASPARAMS"></span><span id="mpf_hasparams"></span>**MPF\_HASPARAMS**
</dt> <dd>

Indicates that the property contains parameters.

</dd> <dt>

<span id="MPF_MIME"></span><span id="mpf_mime"></span>**MPF\_MIME**
</dt> <dd>

Indicates that the property is MIME specific.

</dd> <dt>

<span id="MPF_READONLY"></span><span id="mpf_readonly"></span>**MPF\_READONLY**
</dt> <dd>

Indicates that the property is read-only.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





