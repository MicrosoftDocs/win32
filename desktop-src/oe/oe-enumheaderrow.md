---
title: ENUMHEADERROW structure
description: Do not use. Used by the IMimeEnumHeaderRows interface to enumerate the rows in an IMimeHeaderTable object.
ms.assetid: f36963b8-f2a5-4e35-8b8a-3a4d154d9c40
keywords:
- ENUMHEADERROW structure Windows Mail (formerly Outlook Express)
- LPENUMHEADERROW structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ENUMHEADERROW
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

# ENUMHEADERROW structure

Do not use. Used by the [**IMimeEnumHeaderRows**](oe-imimeenumheaderrows.md) interface to enumerate the rows in an [**IMimeHeaderTable**](oe-imimeheadertable.md) object.

## Syntax


```C++
typedef struct tagENUMHEADERROW {
  HHEADERROW hRow;
  LPSTR      pszHeader;
  LPSTR      pszData;
  ULONG      cchData;
  DWORD_PTR  dwReserved;
} ENUMHEADERROW, *LPENUMHEADERROW;
```



## Members

<dl> <dt>

**hRow**
</dt> <dd>

Type: **HHEADERROW**

</dd> <dd>

Contains the handle of this row in the [**IMimeHeaderTable**](oe-imimeheadertable.md) object.

</dd> <dt>

**pszHeader**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the name of the header for this row.

</dd> <dt>

**pszData**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the data for this row.

</dd> <dt>

**cchData**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains the number of characters in **pszData**.

</dd> <dt>

**dwReserved**
</dt> <dd>

Type: **DWORD\_PTR**

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



 

 





