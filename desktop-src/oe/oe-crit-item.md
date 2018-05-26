---
title: CRIT\_ITEM structure
description: CRIT\_ITEM is no longer available for use as of Windows Vista.
ms.assetid: b77075c1-5c00-4c0f-b8c7-428d131f6f84
keywords:
- CRIT_ITEM structure Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- CRIT_ITEM
api_location:
- Oerules.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CRIT\_ITEM structure

\[**CRIT\_ITEM** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
typedef struct tagCRIT_ITEM {
  CRIT_TYPE   type;
  DWORD       dwFlags;
  PROPVARIANT propvar;
  CRIT_LOGIC  logic;
} CRIT_ITEM;
```



## Members

<dl> <dt>

**type**
</dt> <dd>

Type: **[**CRIT\_TYPE**](oe-crit-type.md)**

</dd> <dd></dd> <dt>

**dwFlags**
</dt> <dd>

Type: **DWORD**

</dd> <dd></dd> <dt>

**propvar**
</dt> <dd>

Type: **[PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072)**

</dd> <dd></dd> <dt>

**logic**
</dt> <dd>

Type: **[**CRIT\_LOGIC**](oe-crit-logic.md)**

</dd> <dd></dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP<br/>                                                                  |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Oerules.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl> |



 

 





