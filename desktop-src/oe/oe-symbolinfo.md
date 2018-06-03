---
title: SYMBOLINFO structure
description: Do not use. Specifies a name for a symbol.
ms.assetid: c62445e6-9444-4f96-a06e-f28a666d2247
keywords:
- SYMBOLINFO structure Windows Mail (formerly Outlook Express)
- LPSYMBOLINFO structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- SYMBOLINFO
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# SYMBOLINFO structure

Do not use. Specifies a name for a symbol.

## Syntax


```C++
typedef struct tagSYMBOLINFO {
  SYMBOLYTPE tySymbol;
  LPCSTR     pszName;
  DWORD      dwValue;
} SYMBOLINFO, *LPSYMBOLINFO;
```



## Members

<dl> <dt>

**tySymbol**
</dt> <dd>

Type: **SYMBOLYTPE**

</dd> <dd>

The type of the symbol.

</dd> <dt>

**pszName**
</dt> <dd>

Type: **LPCSTR**

</dd> <dd>

A string that represents the name of the symbol.

</dd> <dt>

**dwValue**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The value of the symbol represented as a DWORD.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Product<br/>                  | Outlook Express 6.0<br/>                       |



 

 





