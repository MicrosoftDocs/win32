---
title: HTTPMEMBERINFOLIST structure
description: Contains a list of HTTPMEMBERINFO structures.
ms.assetid: ce412878-159b-47dc-82ba-6b048d2072ba
keywords:
- HTTPMEMBERINFOLIST structure Windows Mail (formerly Outlook Express)
- LPHTTPMEMBERINFOLIST structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPMEMBERINFOLIST
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

# HTTPMEMBERINFOLIST structure

\[**HTTPMEMBERINFOLIST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains a list of [**HTTPMEMBERINFO**](oe-httpmemberinfo.md) structures.

## Syntax


```C++
typedef struct tagHTTPMEMBERINFOLIST {
  ULONG            cMemberInfo;
  LPHTTPMEMBERINFO prgMemberInfo;
  LPSTR            pszRootTimeStamp;
  LPSTR            pszFolderTimeStamp;
} HTTPMEMBERINFOLIST, *LPHTTPMEMBERINFOLIST;
```



## Members

<dl> <dt>

**cMemberInfo**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains a **ULONG** that contains the number of elements in **prgMemberInfo**.

</dd> <dt>

**prgMemberInfo**
</dt> <dd>

Type: **LPHTTPMEMBERINFO**

</dd> <dd>

Contains a pointer to an array of [**HTTPMEMBERINFO**](oe-httpmemberinfo.md) structures.

</dd> <dt>

**pszRootTimeStamp**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the timestamp to log for the root colection resource.

</dd> <dt>

**pszFolderTimeStamp**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the timestamp to log for the collection resource that contains the resources whose properties are returned in **prgMemberInfo**.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





