---
title: TABLESCHEMA structure
description: Do not use. Describes the schema of a database table.
ms.assetid: 6b2b0a9b-ee64-48fe-93ee-522668149a5d
keywords:
- TABLESCHEMA structure Windows Mail (formerly Outlook Express)
- LPTABLESCHEMA structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- TABLESCHEMA
api_type:
- NA
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TABLESCHEMA structure

Do not use. Describes the schema of a database table.

## Syntax


```C++
typedef struct tagTABLESCHEMA {
  LPVOID           pReserved;
  DWORD            cbBinding;
  DWORD            ofMemory;
  DWORD            ofVersion;
  DWORD            dwReserved;
  TABLESCHEMAFLAGS dwFlags;
  DWORD            cbUserData;
  DWORD            ofUniqueId;
  BYTE             cColumns;
  LPCTABLECOLUMN   prgColumn;
  LPCTABLEINDEX    pPrimaryIndex;
  LPCSYMBOLTABLE   pSymbols;
} TABLESCHEMA, *LPTABLESCHEMA;
```



## Members

<dl> <dt>

**pReserved**
</dt> <dd>

Type: **LPVOID**

</dd> <dd>

A reserved field.

</dd> <dt>

**cbBinding**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The size of a record that will be stored in the database.

</dd> <dt>

**ofMemory**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Each record must contain a member reserved for the database. This member must be large enough to store a pointer and must not be modified by the caller in any record. ofMemory must be the offset into the record of that column.

</dd> <dt>

**ofVersion**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

All records must contain a BYTE that the database uses to store a version number. Set ofVersion to the offset, in bytes, of that struct member.

</dd> <dt>

**dwReserved**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

A reserved field for the minor version.

</dd> <dt>

**dwFlags**
</dt> <dd>

Type: **[**TABLESCHEMAFLAGS**](oe-tableschemaflags.md)**

</dd> <dd>

Can be set to one of the values of TABLESCHEMAFLAGS.

</dd> <dt>

**cbUserData**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Specifies the number of bytes in the UserData that will be set using SetUserData. Must be the same value as cbUserData passed to SetUserData.

</dd> <dt>

**ofUniqueId**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Specifies the location of the primary key inside of a record for this database. This is specified as an offset in bytes from the beginning of a record.

</dd> <dt>

**cColumns**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

Number of columns in a record.

</dd> <dt>

**prgColumn**
</dt> <dd>

Type: **LPCTABLECOLUMN**

</dd> <dd>

Should point to an array of TABLECOLUMN structures specifying the columns of the database.

</dd> <dt>

**pPrimaryIndex**
</dt> <dd>

Type: **LPCTABLEINDEX**

</dd> <dd>

The primary index for the table.

</dd> <dt>

**pSymbols**
</dt> <dd>

Type: **LPCSYMBOLTABLE**

</dd> <dd>

The array of symbols for this table.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Product<br/>                  | Outlook Express 6.0<br/>                       |



 

 





