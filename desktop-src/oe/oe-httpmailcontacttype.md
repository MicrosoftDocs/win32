---
title: HTTPMAILCONTACTTYPE enumeration
description: HTTPMail contact types.
ms.assetid: 238bf07d-6757-439a-a467-60b9bb9d39ef
keywords:
- HTTPMAILCONTACTTYPE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# HTTPMAILCONTACTTYPE enumeration

\[**HTTPMAILCONTACTTYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

HTTPMail contact types.

## Syntax


```C++
typedef enum tagHTTPMAILCONTACTTYPE { 
  HTTPMAIL_CT_CONTACT  = 0,
  HTTPMAIL_CT_GROUP    = 1,
  HTTPMAIL_CT_LAST     = 2
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="HTTPMAIL_CT_CONTACT"></span><span id="httpmail_ct_contact"></span>**HTTPMAIL\_CT\_CONTACT**
</dt> <dd>

A single contact. This is the default type.

</dd> <dt>

<span id="HTTPMAIL_CT_GROUP"></span><span id="httpmail_ct_group"></span>**HTTPMAIL\_CT\_GROUP**
</dt> <dd>

A group of contacts.

</dd> <dt>

<span id="HTTPMAIL_CT_LAST"></span><span id="httpmail_ct_last"></span>**HTTPMAIL\_CT\_LAST**
</dt> <dd>

The last member of this enumeration.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





