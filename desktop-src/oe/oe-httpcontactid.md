---
title: HTTPCONTACTID structure
description: Contains the response information for the ContactInfo, ListContacts, and PatchContact methods.
ms.assetid: 1d7af8e0-2e29-483c-8621-0a3bc21ea276
keywords:
- HTTPCONTACTID structure Windows Mail (formerly Outlook Express)
- LPHTTPCONTACTID structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPCONTACTID
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HTTPCONTACTID structure

\[**HTTPCONTACTID** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the response information for the [**ContactInfo**](oe-ihttpmailtransport-contactinfo.md), [**ListContacts**](oe-ihttpmailtransport-listcontacts.md), and [**PatchContact**](oe-ihttpmailtransport-patchcontact.md) methods.

## Syntax


```C++
typedef struct tagHTTPCONTACTID {
  LPSTR               pszHref;
  LPSTR               pszId;
  HTTPMAILCONTACTTYPE tyContact;
  LPSTR               pszModified;
} HTTPCONTACTID, *LPHTTPCONTACTID;
```



## Members

<dl> <dt>

**pszHref**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the URL to this contact.

</dd> <dt>

**pszId**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the contact ID.

</dd> <dt>

**tyContact**
</dt> <dd>

Type: **[**HTTPMAILCONTACTTYPE**](oe-httpmailcontacttype.md)**

</dd> <dd>

Contains an [**HTTPMAILCONTACTTYPE**](oe-httpmailcontacttype.md) value that indicates the type of contact.

</dd> <dt>

**pszModified**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the date this contact was last updated.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





