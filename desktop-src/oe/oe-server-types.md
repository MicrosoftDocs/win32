---
title: Server Types
description: Do not use. Server type values that can be set and their meaning.
ms.assetid: d97e83f4-1843-4921-ba0b-833f91b9c7c1
topic_type:
- apiref
api_name:
- SRV_NNTP
- SRV_IMAP
- SRV_POP3
- SRV_SMTP
- SRV_LDAP
- SRV_HTTPMAIL
- SRV_MAIL
- SRV_ALL
api_location:
- Imnact.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Server Types

Do not use. Server type values that can be set and their meaning.



| Constant/value                                                                                                                                                                                                                                                                             | Description                              |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------|
| <span id="SRV_NNTP"></span><span id="srv_nntp"></span><dl> <dt>**SRV\_NNTP**</dt> <dt>0x0001</dt> </dl>                                                                                 | Indicates a NNTP server.<br/>      |
| <span id="SRV_IMAP"></span><span id="srv_imap"></span><dl> <dt>**SRV\_IMAP**</dt> <dt>0x0002</dt> </dl>                                                                                 | Indicates a IMAP server.<br/>      |
| <span id="SRV_POP3"></span><span id="srv_pop3"></span><dl> <dt>**SRV\_POP3**</dt> <dt>0x0004</dt> </dl>                                                                                 | Indicates a POP3 server.<br/>      |
| <span id="SRV_SMTP"></span><span id="srv_smtp"></span><dl> <dt>**SRV\_SMTP**</dt> <dt>0x0008</dt> </dl>                                                                                 | Indicates a SMTP server.<br/>      |
| <span id="SRV_LDAP"></span><span id="srv_ldap"></span><dl> <dt>**SRV\_LDAP**</dt> <dt>0x0010</dt> </dl>                                                                                 | Indicates a LDAP server.<br/>      |
| <span id="SRV_HTTPMAIL"></span><span id="srv_httpmail"></span><dl> <dt>**SRV\_HTTPMAIL**</dt> <dt>0x0020</dt> </dl>                                                                     | Indicates an HTTPMail server.<br/> |
| <span id="SRV_MAIL"></span><span id="srv_mail"></span><dl> <dt>**SRV\_MAIL**</dt> <dt>((DWORD)(SRV\_IMAP \| SRV\_POP3 \| SRV\_SMTP \| SRV\_HTTPMAIL))</dt> </dl>                        | Indicates all mail servers.<br/>   |
| <span id="SRV_ALL"></span><span id="srv_all"></span><dl> <dt>**SRV\_ALL**</dt> <dt>((DWORD)(SRV\_NNTP \| SRV\_IMAP \| SRV\_POP3 \| SRV\_SMTP \| SRV\_LDAP \| SRV\_HTTPMAIL))</dt> </dl> | Indicates all servers.<br/>        |



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Product<br/>                  | Outlook Express 6.0<br/>                                                        |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl> |



 

 





