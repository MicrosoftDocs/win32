---
title: SYMBOLTABLE structure
description: Do not use. Specifies a set of symbols.
ms.assetid: 57de6342-5a2e-4ece-af87-44be9f08a243
keywords:
- SYMBOLTABLE structure Windows Mail (formerly Outlook Express)
- LPSYMBOLTABLE structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- SYMBOLTABLE
api_type:
- NA
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SYMBOLTABLE structure

Do not use. Specifies a set of symbols.

## Syntax


```C++
typedef struct tagSYMBOLTABLE {
  DWORD      cSymbols;
  SYMBOLINFO rgSymbol[32];
} SYMBOLTABLE, *LPSYMBOLTABLE;
```



## Members

<dl> <dt>

**cSymbols**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Number of SYMBOLINFO in the symbol array.

</dd> <dt>

**rgSymbol**
</dt> <dd>

Type: **[**SYMBOLINFO**](oe-symbolinfo.md)\[32\]**

</dd> <dd>

Array of SYMBOLINFO.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Product<br/>                  | Outlook Express 6.0<br/>                       |



 

 





