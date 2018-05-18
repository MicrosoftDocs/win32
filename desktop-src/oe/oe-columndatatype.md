---
title: COLUMNDATATYPE enumeration
description: Do not use. Used to specify the type of a column of a database.
ms.assetid: 'daa0b0b1-66bf-486d-963e-46725b68623d'
keywords: ["COLUMNDATATYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Directdb.idl
api_type:
- IDLDef
---

# COLUMNDATATYPE enumeration

Do not use. Used to specify the type of a column of a database.

## Syntax


```C++
typedef enum  { 
  CDT_FILETIME,
  CDT_FIXSTRA,
  CDT_VARSTRA,
  CDT_BYTE,
  CDT_DWORD,
  CDT_WORD,
  CDT_STREAM,
  CDT_VARBLOB,
  CDT_FIXBLOB,
  CDT_FLAGS,
  CDT_UNIQUE,
  CDT_FIXSTRW,
  CDT_VARSTRW,
  CDT_LASTTYPE
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="CDT_FILETIME"></span><span id="cdt_filetime"></span>**CDT\_FILETIME**
</dt> <dd>

Data type is FILETIME

</dd> <dt>

<span id="CDT_FIXSTRA"></span><span id="cdt_fixstra"></span>**CDT\_FIXSTRA**
</dt> <dd>

Data type is ANSI string with fixed size which is independent of string length.

</dd> <dt>

<span id="CDT_VARSTRA"></span><span id="cdt_varstra"></span>**CDT\_VARSTRA**
</dt> <dd>

Data type is ANSI string with variable size which is dependent on string length.

</dd> <dt>

<span id="CDT_BYTE"></span><span id="cdt_byte"></span>**CDT\_BYTE**
</dt> <dd>

Data type is BYTE.

</dd> <dt>

<span id="CDT_DWORD"></span><span id="cdt_dword"></span>**CDT\_DWORD**
</dt> <dd>

Data type is DWORD.

</dd> <dt>

<span id="CDT_WORD"></span><span id="cdt_word"></span>**CDT\_WORD**
</dt> <dd>

Data type is WORD.

</dd> <dt>

<span id="CDT_STREAM"></span><span id="cdt_stream"></span>**CDT\_STREAM**
</dt> <dd>

Data type is file stream.

</dd> <dt>

<span id="CDT_VARBLOB"></span><span id="cdt_varblob"></span>**CDT\_VARBLOB**
</dt> <dd>

Data type is blob of variable size.

</dd> <dt>

<span id="CDT_FIXBLOB"></span><span id="cdt_fixblob"></span>**CDT\_FIXBLOB**
</dt> <dd>

Data type is blob of fixed size.

</dd> <dt>

<span id="CDT_FLAGS"></span><span id="cdt_flags"></span>**CDT\_FLAGS**
</dt> <dd>

Data type is flags (DWORD).

</dd> <dt>

<span id="CDT_UNIQUE"></span><span id="cdt_unique"></span>**CDT\_UNIQUE**
</dt> <dd>

Data type is a unique key (DWORD).

</dd> <dt>

<span id="CDT_FIXSTRW"></span><span id="cdt_fixstrw"></span>**CDT\_FIXSTRW**
</dt> <dd>

Data type is Unicode string with fixed size which is independent of string length.

</dd> <dt>

<span id="CDT_VARSTRW"></span><span id="cdt_varstrw"></span>**CDT\_VARSTRW**
</dt> <dd>

Data type is Unicode string with fixed size which is dependent on string length.

</dd> <dt>

<span id="CDT_LASTTYPE"></span><span id="cdt_lasttype"></span>**CDT\_LASTTYPE**
</dt> <dd>

This is the number of data types supported.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl> |



 

 





