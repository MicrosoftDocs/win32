---
title: LDAP Paged Result Support Types
description: Do not use.
ms.assetid: 51001afd-075e-45b2-a80d-21119d69726d
topic_type:
- apiref
api_name:
- LDAP_PRESULT_UNKNOWN
- LDAP_PRESULT_SUPPORTED
- LDAP_PRESULT_NOTSUPPORTED
- LDAP_PRESULT_MAX
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

# LDAP Paged Result Support Types

Do not use. For convenience, query results may be broken into pages. The following Lightweight Directory Access Protocol (LDAP) paged result support types are defined:



| Constant/value                                                                                                                                                                                                                                                 | Description                                                |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------|
| <span id="LDAP_PRESULT_UNKNOWN"></span><span id="ldap_presult_unknown"></span><dl> <dt>**LDAP\_PRESULT\_UNKNOWN**</dt> <dt>0x0000</dt> </dl>                | Indicates support for paged results is unknown.<br/> |
| <span id="LDAP_PRESULT_SUPPORTED"></span><span id="ldap_presult_supported"></span><dl> <dt>**LDAP\_PRESULT\_SUPPORTED**</dt> <dt>0x0001</dt> </dl>          | Indicates paged results is supported.<br/>           |
| <span id="LDAP_PRESULT_NOTSUPPORTED"></span><span id="ldap_presult_notsupported"></span><dl> <dt>**LDAP\_PRESULT\_NOTSUPPORTED**</dt> <dt>0x0002</dt> </dl> | Indicates paged results is not supported.<br/>       |
| <span id="LDAP_PRESULT_MAX"></span><span id="ldap_presult_max"></span><dl> <dt>**LDAP\_PRESULT\_MAX**</dt> <dt>0x0002</dt> </dl>                            | Indicates maximum valid constant value.<br/>         |



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Product<br/>                  | Outlook Express 6.0<br/>                                                        |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl> |



 

 





