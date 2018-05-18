---
title: HTTPCONTACTINFOLIST structure
description: Contains a list of HTTPCONTACTINFO structures.
ms.assetid: 'bc5133e6-06aa-41a2-a9de-b0b2ffd009ab'
keywords: ["HTTPCONTACTINFOLIST structure Windows Mail (formerly Outlook Express)", "LPHTTPCONTACTINFOLIST structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- HTTPCONTACTINFOLIST
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# HTTPCONTACTINFOLIST structure

\[**HTTPCONTACTINFOLIST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains a list of [**HTTPCONTACTINFO**](oe-httpcontactinfo.md) structures.

## Syntax


```C++
typedef struct tagHTTPCONTACTINFOLIST {
  ULONG             cContactInfo;
  LPHTTPCONTACTINFO prgContactInfo;
} HTTPCONTACTINFOLIST, *LPHTTPCONTACTINFOLIST;
```



## Members

<dl> <dt>

**cContactInfo**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains a **ULONG** that contains the number of elements in **prgContactInfo**.

</dd> <dt>

**prgContactInfo**
</dt> <dd>

Type: **LPHTTPCONTACTINFO**

</dd> <dd>

Contains a pointer to an array of [**HTTPCONTACTINFO**](oe-httpcontactinfo.md) structures.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





