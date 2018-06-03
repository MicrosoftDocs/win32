---
title: ACTX structure
description: Do not use. Contains account information.
ms.assetid: ee983cdc-f5d6-4a81-8d48-3fc0ccd27899
keywords:
- ACTX structure Windows Mail (formerly Outlook Express)
- ACCESSTYPE structure Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnact.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ACTX structure

Do not use. Contains account information.

## Syntax


```C++
typedef struct tagAccountContext {
  ACCTTYPE AcctType;
  LPSTR    pszAccountID;
  LPSTR    pszOldName;
  DWORD    dwServerType;
} ACCESSTYPE;
```



## Members

<dl> <dt>

**AcctType**
</dt> <dd>

Type: **[**ACCTTYPE**](oe-accttype.md)**

</dd> <dd>

Contains an [**ACCTTYPE**](oe-accttype.md) value that indicates the account type.

</dd> <dt>

**pszAccountID**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the account ID.

</dd> <dt>

**pszOldName**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the account name before it was changed or the account was deleted.

</dd> <dt>

**dwServerType**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that indicates the server type.



| Value                                                                                                                                                      | Meaning                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| <span id="SRV_NNTP"></span><span id="srv_nntp"></span><dl> <dt>**SRV\_NNTP**</dt> </dl>             | Indicates a NNTP server. <br/>      |
| <span id="SRV_SMTP"></span><span id="srv_smtp"></span><dl> <dt>**SRV\_SMTP**</dt> </dl>             | Indicates a SMTP server. <br/>      |
| <span id="SRV_POP3"></span><span id="srv_pop3"></span><dl> <dt>**SRV\_POP3**</dt> </dl>             | Indicates a POP3 server. <br/>      |
| <span id="SRV_IMAP"></span><span id="srv_imap"></span><dl> <dt>**SRV\_IMAP**</dt> </dl>             | Indicates an IMAP server. <br/>     |
| <span id="SRV_HTTPMAIL"></span><span id="srv_httpmail"></span><dl> <dt>**SRV\_HTTPMAIL**</dt> </dl> | Indicates an HTTPMail server. <br/> |
| <span id="SRV_LDAP"></span><span id="srv_ldap"></span><dl> <dt>**SRV\_LDAP**</dt> </dl>             | Indicates a LDAP server. <br/>      |



 

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Product<br/>                  | Outlook Express 6.0<br/>                                                        |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl> |



 

 





