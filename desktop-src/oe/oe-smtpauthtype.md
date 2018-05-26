---
title: SMTPAUTHTYPE enumeration
description: Do not use. Defines Simple Mail Transport Protocol (SMTP) authentication types.
ms.assetid: 386dd49b-ab0f-4443-b3d8-05efed85999f
keywords:
- SMTPAUTHTYPE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnact.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SMTPAUTHTYPE enumeration

Do not use. Defines Simple Mail Transport Protocol (SMTP) authentication types.

## Syntax


```C++
typedef enum tagSMTPAUTHTYPE { 
  SMTP_AUTH_NONE                     = 0,
  SMTP_AUTH_SICILY                   = 1,
  SMTP_AUTH_USE_POP3ORIMAP_SETTINGS  = 2,
  SMTP_AUTH_USE_SMTP_SETTINGS        = 3
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="SMTP_AUTH_NONE"></span><span id="smtp_auth_none"></span>**SMTP\_AUTH\_NONE**
</dt> <dd>

Indicates using no authentication.

</dd> <dt>

<span id="SMTP_AUTH_SICILY"></span><span id="smtp_auth_sicily"></span>**SMTP\_AUTH\_SICILY**
</dt> <dd>

Indicates using SPA for authentication.

</dd> <dt>

<span id="SMTP_AUTH_USE_POP3ORIMAP_SETTINGS"></span><span id="smtp_auth_use_pop3orimap_settings"></span>**SMTP\_AUTH\_USE\_POP3ORIMAP\_SETTINGS**
</dt> <dd>

Indicates using the POP3 or IMAP authentication settings.

</dd> <dt>

<span id="SMTP_AUTH_USE_SMTP_SETTINGS"></span><span id="smtp_auth_use_smtp_settings"></span>**SMTP\_AUTH\_USE\_SMTP\_SETTINGS**
</dt> <dd>

Indicates using SMTP authentication settings.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Product<br/>                  | Outlook Express 6.0<br/>                                                        |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl> |



 

 





