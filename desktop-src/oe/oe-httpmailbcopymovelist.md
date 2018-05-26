---
title: HTTPMAILBCOPYMOVELIST structure
description: Contains a list of HTTPMAILBCOPYMOVE structures.
ms.assetid: 2ba931e8-4a29-42d6-8e36-9d1f0d9f6721
keywords:
- HTTPMAILBCOPYMOVELIST structure Windows Mail (formerly Outlook Express)
- LPHTTPMAILBCOPYMOVELIST structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPMAILBCOPYMOVELIST
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

# HTTPMAILBCOPYMOVELIST structure

\[**HTTPMAILBCOPYMOVELIST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains a list of [**HTTPMAILBCOPYMOVE**](oe-httpmailbcopymove.md) structures.

## Syntax


```C++
typedef struct tagHTTPMAILBCOPYMOVELIST {
  ULONG               cBCopyMove;
  LPHTTPMAILBCOPYMOVE prgBCopyMove;
} HTTPMAILBCOPYMOVELIST, *LPHTTPMAILBCOPYMOVELIST;
```



## Members

<dl> <dt>

**cBCopyMove**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains a **ULONG** that contains the number of elements in **prgBCopyMove**.

</dd> <dt>

**prgBCopyMove**
</dt> <dd>

Type: **LPHTTPMAILBCOPYMOVE**

</dd> <dd>

Contains a pointer to an array of [**HTTPMAILBCOPYMOVE**](oe-httpmailbcopymove.md) structures.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





