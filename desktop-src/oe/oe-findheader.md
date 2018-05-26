---
title: FINDHEADER structure
description: Do not use. Defines how an IMimeHeaderTable object iterates through rows.
ms.assetid: ac2f5816-4237-4336-8af4-fd5e420d349e
keywords:
- FINDHEADER structure Windows Mail (formerly Outlook Express)
- LPFINDHEADER structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- FINDHEADER
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

# FINDHEADER structure

Do not use. Defines how an [**IMimeHeaderTable**](oe-imimeheadertable.md) object iterates through rows.

## Syntax


```C++
typedef struct tagFINDHEADER {
  LPCSTR pszHeader;
  DWORD  dwReserved;
} FINDHEADER, *LPFINDHEADER;
```



## Members

<dl> <dt>

**pszHeader**
</dt> <dd>

Type: **LPCSTR**

</dd> <dd>

Contains the name of the header to iterate. A **NULL** value indicates that all the rows in the header table should be iterated.

</dd> <dt>

**dwReserved**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Do not use.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





