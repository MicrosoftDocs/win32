---
title: ADDRESSLIST structure
description: Do not use. Holds a list of ADDRESSPROPS structures.
ms.assetid: 0a1ffc78-e89c-4790-9c83-b98428df2141
keywords:
- ADDRESSLIST structure Windows Mail (formerly Outlook Express)
- LPADDRESSLIST structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ADDRESSLIST
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ADDRESSLIST structure

Do not use. Holds a list of [**ADDRESSPROPS**](oe-addressprops.md) structures.

## Syntax


```C++
typedef struct tagADDRESSLIST {
  ULONG          cAdrs;
  LPADDRESSPROPS prgAdr;
} ADDRESSLIST, *LPADDRESSLIST;
```



## Members

<dl> <dt>

**cAdrs**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains the number of valid elements in **prgAdr**.

</dd> <dt>

**prgAdr**
</dt> <dd>

Type: **LPADDRESSPROPS**

</dd> <dd>

Contains a pointer to an array of [**ADDRESSPROPS**](oe-addressprops.md) structures.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





