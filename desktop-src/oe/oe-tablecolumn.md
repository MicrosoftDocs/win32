---
title: TABLECOLUMN structure
description: Do not use. This structure describes a database table column.
ms.assetid: 0f8c07df-0f08-49ec-bb11-aa47e9e85c8a
keywords:
- TABLECOLUMN structure Windows Mail (formerly Outlook Express)
- LPTABLECOLUMN structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- TABLECOLUMN
api_type:
- NA
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TABLECOLUMN structure

Do not use. This structure describes a database table column.

## Syntax


```C++
typedef struct tagTABLECOLUMN {
  COLUMNORDINAL  iOrdinal;
  COLUMNDATATYPE type;
  DWORD          ofBinding;
  DWORD          cbSize;
} TABLECOLUMN, *LPTABLECOLUMN;
```



## Members

<dl> <dt>

**iOrdinal**
</dt> <dd>

Type: **COLUMNORDINAL**

</dd> <dd>

Index of the column in the table. These should be sequential across all columns in a table.

</dd> <dt>

**type**
</dt> <dd>

Type: **[**COLUMNDATATYPE**](oe-columndatatype.md)**

</dd> <dd>

Data type that this column will store. See COLUMNDATATYPE for a list of valid types.

</dd> <dt>

**ofBinding**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Offset from a record start for the data storage of types CDT\_DWORD, CDT\_FLAGS, CDT\_UNIQUE, CDT\_VARSTRA, CDT\_VARSTRW, CDT\_VARBLOB, and CDT\_STREAM.

</dd> <dt>

**cbSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Size of data storage for types CDT\_FIXSTRA, CDT\_FIXSTRW, and CDT\_FIXBLOB.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Product<br/>                  | Outlook Express 6.0<br/>                       |



 

 





