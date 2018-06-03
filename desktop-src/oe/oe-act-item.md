---
title: ACT\_ITEM structure
description: ACT\_ITEM is no longer available for use as of Windows Vista.
ms.assetid: 34f7c41e-708a-40de-b333-92ebf2714f21
keywords:
- ACT_ITEM structure Windows Mail (formerly Outlook Express)
- PACT_ITEM structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACT_ITEM
api_location:
- Oerules.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ACT\_ITEM structure

\[**ACT\_ITEM** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
typedef struct tagACT_ITEM {
  ACT_TYPE    type;
  DWORD       dwFlags;
  PROPVARIANT propvar;
} ACT_ITEM, *PACT_ITEM;
```



## Members

<dl> <dt>

**type**
</dt> <dd>

Type: **[**ACT\_TYPE**](oe-act-type.md)**

</dd> <dd></dd> <dt>

**dwFlags**
</dt> <dd>

Type: **DWORD**

</dd> <dd> <dl><span id="ACT_FLAG_DEFAULT"></span><span id="act_flag_default"></span><dt>

**ACT\_FLAG\_DEFAULT**
</dt><span id="ACT_FLAG_INVERT"></span><span id="act_flag_invert"></span><dt>

**ACT\_FLAG\_INVERT**
</dt> </dl> </dd> <dt>

**propvar**
</dt> <dd>

Type: **[PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072)**

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



 

 





