---
title: FINDBODY structure
description: Do not use. Used to iterate through the message bodies in an IMimeMessageTree object.
ms.assetid: bbb7049a-ed44-48bd-aa9c-26e8b0a55056
keywords:
- FINDBODY structure Windows Mail (formerly Outlook Express)
- LPFINDBODY structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- FINDBODY
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# FINDBODY structure

Do not use. Used to iterate through the message bodies in an [**IMimeMessageTree**](oe-imimemessagetree.md) object.

## Syntax


```C++
typedef struct tagFINDBODY {
  LPSTR pszPriType;
  LPSTR pszSubType;
  DWORD dwReserved;
} FINDBODY, *LPFINDBODY;
```



## Members

<dl> <dt>

**pszPriType**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the primary [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) to iterate.

</dd> <dt>

**pszSubType**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the secondary [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) to iterate.

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



 

 





