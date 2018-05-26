---
title: LDAP Authentication Types
description: Do not use. Lightweight Directory Access Protocol (LDAP) authentication type values that can be set, and their meaning.
ms.assetid: 037ea4d3-0e7b-454f-b0e3-129aebcfe5ab
topic_type:
- apiref
api_name:
- LDAP_AUTH_ANONYMOUS
- LDAP_AUTH_PASSWORD
- LDAP_AUTH_MEMBER_SYSTEM
- LDAP_AUTH_MAX
api_location:
- Imnact.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LDAP Authentication Types

Do not use. Lightweight Directory Access Protocol (LDAP) authentication type values that can be set, and their meaning.



| Constant/value                                                                                                                                                                                                                                            | Description                                                   |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------|
| <span id="LDAP_AUTH_ANONYMOUS"></span><span id="ldap_auth_anonymous"></span><dl> <dt>**LDAP\_AUTH\_ANONYMOUS**</dt> <dt>0x0000</dt> </dl>              | Indicates server does not require logon.<br/>           |
| <span id="LDAP_AUTH_PASSWORD"></span><span id="ldap_auth_password"></span><dl> <dt>**LDAP\_AUTH\_PASSWORD**</dt> <dt>0x0001</dt> </dl>                 | Indicates server requires logon.<br/>                   |
| <span id="LDAP_AUTH_MEMBER_SYSTEM"></span><span id="ldap_auth_member_system"></span><dl> <dt>**LDAP\_AUTH\_MEMBER\_SYSTEM**</dt> <dt>0x0002</dt> </dl> | Indicates server requires logon using SPA.<br/>         |
| <span id="LDAP_AUTH_MAX"></span><span id="ldap_auth_max"></span><dl> <dt>**LDAP\_AUTH\_MAX**</dt> <dt>0x0002</dt> </dl>                                | Indicates maximum valid authentication type value.<br/> |



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Product<br/>                  | Outlook Express 6.0<br/>                                                        |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl> |



 

 





