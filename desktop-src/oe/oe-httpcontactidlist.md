---
title: HTTPCONTACTIDLIST structure
description: Contains a list of HTTPCONTACTID structures.
ms.assetid: 9c1f30ea-a501-41c7-9a77-57d8c38390f1
keywords:
- HTTPCONTACTIDLIST structure Windows Mail (formerly Outlook Express)
- LPHTTPCONTACTIDLIST structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPCONTACTIDLIST
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# HTTPCONTACTIDLIST structure

\[**HTTPCONTACTIDLIST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains a list of [**HTTPCONTACTID**](oe-httpcontactid.md) structures.

## Syntax


```C++
typedef struct tagHTTPCONTACTIDLIST {
  ULONG           cContactId;
  LPHTTPCONTACTID prgContactId;
} HTTPCONTACTIDLIST, *LPHTTPCONTACTIDLIST;
```



## Members

<dl> <dt>

**cContactId**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains a **ULONG** that contains the number of elements in **prgContactId**.

</dd> <dt>

**prgContactId**
</dt> <dd>

Type: **LPHTTPCONTACTID**

</dd> <dd>

Contains a pointer to an array of [**HTTPCONTACTID**](oe-httpcontactid.md) structures.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





