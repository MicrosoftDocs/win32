---
title: RELOADTYPE enumeration
description: Do not use. Affects how an IMimePropertySet is initialized when IMimePropertySet Load is called consecutive times without calling IMimeMessageTree InitNew.
ms.assetid: 67947d4d-a3c9-4719-82c6-5cab53253917
keywords:
- RELOADTYPE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RELOADTYPE enumeration

Do not use. Affects how an [**IMimePropertySet**](oe-imimepropertyset.md) is initialized when [IMimePropertySet::Load](http://msdn.microsoft.com/library/com/htm/cmi_n2p_63ac.asp) is called consecutive times without calling [IMimeMessageTree::InitNew](http://msdn.microsoft.com/library/com/htm/cmi_n2p_19vb.asp).

## Syntax


```C++
typedef enum tagRELOADTYPE { 
  RELOAD_HEADER_NONE     = 0,
  RELOAD_HEADER_RESET    = 1,
  RELOAD_HEADER_APPEND   = 2,
  RELOAD_HEADER_REPLACE  = 3
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="RELOAD_HEADER_NONE"></span><span id="reload_header_none"></span>**RELOAD\_HEADER\_NONE**
</dt> <dd>

Indicates that there should be no effect.

</dd> <dt>

<span id="RELOAD_HEADER_RESET"></span><span id="reload_header_reset"></span>**RELOAD\_HEADER\_RESET**
</dt> <dd>

Indicates that a message object should reset by calling [IMimeMessageTree::InitNew](http://msdn.microsoft.com/library/com/htm/cmi_n2p_19vb.asp).

</dd> <dt>

<span id="RELOAD_HEADER_APPEND"></span><span id="reload_header_append"></span>**RELOAD\_HEADER\_APPEND**
</dt> <dd>

Indicates that duplicate headers should be appended when the object is reloaded.

</dd> <dt>

<span id="RELOAD_HEADER_REPLACE"></span><span id="reload_header_replace"></span>**RELOAD\_HEADER\_REPLACE**
</dt> <dd>

Indicates that duplicate headers should be replaced when the object is reloaded.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





