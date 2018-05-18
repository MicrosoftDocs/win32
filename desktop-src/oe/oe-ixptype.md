---
title: IXPTYPE enumeration
description: Identifies Internet transport types.
ms.assetid: 'a75416cf-67fe-4f1a-9171-d560c0cd9050'
keywords: ["IXPTYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# IXPTYPE enumeration

\[**IXPTYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Identifies Internet transport types.

## Syntax


```C++
typedef enum tagIXPTYPE { 
  IXP_NNTP      = 0,
  IXP_SMTP      = 1,
  IXP_POP3      = 2,
  IXP_IMAP      = 3,
  IXP_RAS       = 4,
  IXP_HTTPMail  = 5
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="IXP_NNTP"></span><span id="ixp_nntp"></span>**IXP\_NNTP**
</dt> <dd>

Indicates NNTP.

</dd> <dt>

<span id="IXP_SMTP"></span><span id="ixp_smtp"></span>**IXP\_SMTP**
</dt> <dd>

Indicates SMTP.

</dd> <dt>

<span id="IXP_POP3"></span><span id="ixp_pop3"></span>**IXP\_POP3**
</dt> <dd>

Indicates POP3.

</dd> <dt>

<span id="IXP_IMAP"></span><span id="ixp_imap"></span>**IXP\_IMAP**
</dt> <dd>

Indicates IMAP.

</dd> <dt>

<span id="IXP_RAS"></span><span id="ixp_ras"></span>**IXP\_RAS**
</dt> <dd>

Indicates RAS.

</dd> <dt>

<span id="IXP_HTTPMail"></span><span id="ixp_httpmail"></span><span id="IXP_HTTPMAIL"></span>**IXP\_HTTPMail**
</dt> <dd>

Indicates HTTPMail.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





