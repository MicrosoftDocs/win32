---
title: HTTPMEMBERERRORLIST structure
description: Contains a list of HTTPMEMBERERROR structures.
ms.assetid: 1889e9d3-b9d1-4abf-8afc-4e6a68315976
keywords:
- HTTPMEMBERERRORLIST structure Windows Mail (formerly Outlook Express)
- LPHTTPMEMBERERRORLIST structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPMEMBERERRORLIST
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

# HTTPMEMBERERRORLIST structure

\[**HTTPMEMBERERRORLIST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains a list of [**HTTPMEMBERERROR**](oe-httpmembererror.md) structures.

## Syntax


```C++
typedef struct tagHTTPMEMBERERRORLIST {
  ULONG             cMemberError;
  LPHTTPMEMBERERROR prgMemberError;
} HTTPMEMBERERRORLIST, *LPHTTPMEMBERERRORLIST;
```



## Members

<dl> <dt>

**cMemberError**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains a **ULONG** that contains the number of elements in **prgMemberError**.

</dd> <dt>

**prgMemberError**
</dt> <dd>

Type: **LPHTTPMEMBERERROR**

</dd> <dd>

Contains a pointer to an array of [**HTTPMEMBERERROR**](oe-httpmembererror.md) structures.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





