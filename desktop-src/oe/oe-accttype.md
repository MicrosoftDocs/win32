---
title: ACCTTYPE enumeration
description: Defines the various account types.
ms.assetid: 02b46cff-0e81-47eb-ad88-e85c274cb985
keywords:
- ACCTTYPE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
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
ms.topic: enumeration
ms.date: 05/31/2018
---

# ACCTTYPE enumeration

\[**ACCTTYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Defines the various account types.

## Syntax


```C++
typedef enum  { 
  ACCT_NEWS      = 0,
  ACCT_MAIL      = 1,
  ACCT_DIR_SERV  = 2,
  ACCT_LAST      = 3
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="ACCT_NEWS"></span><span id="acct_news"></span>**ACCT\_NEWS**
</dt> <dd>

Indicates a newsgroup account.

</dd> <dt>

<span id="ACCT_MAIL"></span><span id="acct_mail"></span>**ACCT\_MAIL**
</dt> <dd>

Indicates an email account.

</dd> <dt>

<span id="ACCT_DIR_SERV"></span><span id="acct_dir_serv"></span>**ACCT\_DIR\_SERV**
</dt> <dd>

Indicates a directory service.

</dd> <dt>

<span id="ACCT_LAST"></span><span id="acct_last"></span>**ACCT\_LAST**
</dt> <dd>

Indicates the total number of account types in this enumeration.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Product<br/>                  | Outlook Express 6.0<br/>                                                        |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl> |



 

 





