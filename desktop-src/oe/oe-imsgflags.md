---
title: IMSGFLAGS enumeration
description: Do not use. Describes the contents of an IMimeMessageTree object.
ms.assetid: 7a8cf87d-9a5e-441f-a894-0926b956ef6b
keywords:
- IMSGFLAGS enumeration Windows Mail (formerly Outlook Express)
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

# IMSGFLAGS enumeration

Do not use. Describes the contents of an [**IMimeMessageTree**](oe-imimemessagetree.md) object.

## Syntax


```C++
typedef enum tagIMSGFLAGS { 
  IMF_ATTACHMENTS   = 0x00000001,
  IMF_MULTIPART     = 0x00000002,
  IMF_SUBMULTIPART  = 0x00000004,
  IMF_MIME          = 0x00000008,
  IMF_HTML          = 0x00000010,
  IMF_PLAIN         = 0x00000020,
  IMF_PARTIAL       = 0x00000040,
  IMF_SIGNED        = 0x00000080,
  IMF_ENCRYPTED     = 0x00000100,
  IMF_TNEF          = 0x00000200,
  IMF_MHTML         = 0x00000400,
  IMF_SECURE        = 0x00000800,
  IMF_TEXT          = 0x00001000,
  IMF_CSETTAGGED    = 0x00002000,
  IMF_NEWS          = 0x00004000,
  IMF_VOICEMAIL     = 0x00008000,
  IMF_HASVCARD      = 0x00010000,
  IMF_RFC1154       = 0x00020000
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="IMF_ATTACHMENTS"></span><span id="imf_attachments"></span>**IMF\_ATTACHMENTS**
</dt> <dd>

Indicates that the message has attachments.

</dd> <dt>

<span id="IMF_MULTIPART"></span><span id="imf_multipart"></span>**IMF\_MULTIPART**
</dt> <dd>

Indicates that the message has multipart bodies.

</dd> <dt>

<span id="IMF_SUBMULTIPART"></span><span id="imf_submultipart"></span>**IMF\_SUBMULTIPART**
</dt> <dd>

Indicates that the message has a nested multipart body.

</dd> <dt>

<span id="IMF_MIME"></span><span id="imf_mime"></span>**IMF\_MIME**
</dt> <dd>

Indicates that the message is in [RFC 1521](http://www.ietf.org/rfc/rfc1521.txt) (MIME) format.

</dd> <dt>

<span id="IMF_HTML"></span><span id="imf_html"></span>**IMF\_HTML**
</dt> <dd>

Indicates that the message has a text/html body.

</dd> <dt>

<span id="IMF_PLAIN"></span><span id="imf_plain"></span>**IMF\_PLAIN**
</dt> <dd>

Indicates that the message has a text/plain body.

</dd> <dt>

<span id="IMF_PARTIAL"></span><span id="imf_partial"></span>**IMF\_PARTIAL**
</dt> <dd>

Indicates that the message has a [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) of message/partial.

</dd> <dt>

<span id="IMF_SIGNED"></span><span id="imf_signed"></span>**IMF\_SIGNED**
</dt> <dd>

Indicates that the message is signed.

</dd> <dt>

<span id="IMF_ENCRYPTED"></span><span id="imf_encrypted"></span>**IMF\_ENCRYPTED**
</dt> <dd>

Indicates that the message is encrypted.

</dd> <dt>

<span id="IMF_TNEF"></span><span id="imf_tnef"></span>**IMF\_TNEF**
</dt> <dd>

Indicates that the message has a TNEF attachment.

</dd> <dt>

<span id="IMF_MHTML"></span><span id="imf_mhtml"></span>**IMF\_MHTML**
</dt> <dd>

Indicates that the message has a MIME-HTML multipart/related section.

</dd> <dt>

<span id="IMF_SECURE"></span><span id="imf_secure"></span>**IMF\_SECURE**
</dt> <dd>

Indicates that the message is secure.

</dd> <dt>

<span id="IMF_TEXT"></span><span id="imf_text"></span>**IMF\_TEXT**
</dt> <dd>

Indicates that the message contains text bodies.

</dd> <dt>

<span id="IMF_CSETTAGGED"></span><span id="imf_csettagged"></span>**IMF\_CSETTAGGED**
</dt> <dd>

Indicates that the message was tagged with a character set.

</dd> <dt>

<span id="IMF_NEWS"></span><span id="imf_news"></span>**IMF\_NEWS**
</dt> <dd>

Indicates that the message is a Usenet new article.

</dd> <dt>

<span id="IMF_VOICEMAIL"></span><span id="imf_voicemail"></span>**IMF\_VOICEMAIL**
</dt> <dd>

Indicates that the message contains a voice mail attachment.

</dd> <dt>

<span id="IMF_HASVCARD"></span><span id="imf_hasvcard"></span>**IMF\_HASVCARD**
</dt> <dd>

Indicates that the message has a vCard attachment.

</dd> <dt>

<span id="IMF_RFC1154"></span><span id="imf_rfc1154"></span>**IMF\_RFC1154**
</dt> <dd>

Indicates that the message is formatted using [RFC 1154](http://www.ietf.org/rfc/rfc1154.txt).

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





