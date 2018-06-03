---
title: HTTPTARGETLIST structure
description: Contains an array of target resource URLs.
ms.assetid: 9d6b5f01-527e-40aa-938a-585803c8abaf
keywords:
- HTTPTARGETLIST structure Windows Mail (formerly Outlook Express)
- LPHTTPTARGETLIST structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPTARGETLIST
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

# HTTPTARGETLIST structure

\[**HTTPTARGETLIST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains an array of target resource URLs.

## Syntax


```C++
typedef struct tagHTTPTARGETLIST {
  ULONG  cTarget;
  LPCSTR *prgTarget;
} HTTPTARGETLIST, *LPHTTPTARGETLIST;
```



## Members

<dl> <dt>

**cTarget**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains a **ULONG** that contains the number of strings in the array pointed to by **prgTarget**.

</dd> <dt>

**prgTarget**
</dt> <dd>

Type: **LPCSTR\***

</dd> <dd>

Contains a pointer to an array of null-terminated **LPCSTR** strings, each of which contains the URL of a resource, for example, "message1234.html".

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





