---
title: HEADERTABLEFLAGS enumeration
description: Do not use. Used to control how various methods in the IMimeHeaderTable interface work.
ms.assetid: 83638e1c-a241-4b57-bf11-3896c5c32cd6
keywords:
- HEADERTABLEFLAGS enumeration Windows Mail (formerly Outlook Express)
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

# HEADERTABLEFLAGS enumeration

Do not use. Used to control how various methods in the [**IMimeHeaderTable**](oe-imimeheadertable.md) interface work.

## Syntax


```C++
typedef enum tagHEADERTABLEFLAGS { 
  HTF_NAMEINDATA       = 0x00000001,
  HTF_ENUMHANDLESONLY  = 0x00000002
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="HTF_NAMEINDATA"></span><span id="htf_nameindata"></span>**HTF\_NAMEINDATA**
</dt> <dd>

Indicates that the header name is contained in the header data.

</dd> <dt>

<span id="HTF_ENUMHANDLESONLY"></span><span id="htf_enumhandlesonly"></span>**HTF\_ENUMHANDLESONLY**
</dt> <dd>

Indicates that only row handles should be returned, rather than data.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





