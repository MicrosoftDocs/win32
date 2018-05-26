---
title: PROPINFOMASK enumeration
description: Do not use. Specifies the validity of a member of the MIMEPROPINFO structure.
ms.assetid: ab81f4f9-57f7-4736-87f4-d415fc33ea52
keywords:
- PROPINFOMASK enumeration Windows Mail (formerly Outlook Express)
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

# PROPINFOMASK enumeration

Do not use. Specifies the validity of a member of the [**MIMEPROPINFO**](oe-mimepropinfo.md) structure.

## Syntax


```C++
typedef enum tagPROPINFOMASK { 
  PIM_CHARSET       = 0x00000001,
  PIM_ENCODINGTYPE  = 0x00000002,
  PIM_ROWNUMBER     = 0x00000004,
  PIM_FLAGS         = 0x00000008,
  PIM_PROPID        = 0x00000010,
  PIM_VALUES        = 0x00000020,
  PIM_VTDEFAULT     = 0x00000040,
  PIM_VTCURRENT     = 0x00000080
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="PIM_CHARSET"></span><span id="pim_charset"></span>**PIM\_CHARSET**
</dt> <dd>

Indicates that **hCharset** is valid.

</dd> <dt>

<span id="PIM_ENCODINGTYPE"></span><span id="pim_encodingtype"></span>**PIM\_ENCODINGTYPE**
</dt> <dd>

Indicates that **ietEncoding** is valid.

</dd> <dt>

<span id="PIM_ROWNUMBER"></span><span id="pim_rownumber"></span>**PIM\_ROWNUMBER**
</dt> <dd>

Indicates that **dwRowNumber** is valid.

</dd> <dt>

<span id="PIM_FLAGS"></span><span id="pim_flags"></span>**PIM\_FLAGS**
</dt> <dd>

Indicates that **dwFlags** is valid.

</dd> <dt>

<span id="PIM_PROPID"></span><span id="pim_propid"></span>**PIM\_PROPID**
</dt> <dd>

Indicates that **dwPropId** is valid.

</dd> <dt>

<span id="PIM_VALUES"></span><span id="pim_values"></span>**PIM\_VALUES**
</dt> <dd>

Indicates that **cValues** is valid.

</dd> <dt>

<span id="PIM_VTDEFAULT"></span><span id="pim_vtdefault"></span>**PIM\_VTDEFAULT**
</dt> <dd>

Indicates that **vtDefault** is valid.

</dd> <dt>

<span id="PIM_VTCURRENT"></span><span id="pim_vtcurrent"></span>**PIM\_VTCURRENT**
</dt> <dd>

Indicates that **vtCurrent** is valid.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





