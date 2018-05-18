---
title: PROPTYPE enumeration
description: Defines the data type of a property.
ms.assetid: 'b806a7a2-f92e-48f4-a563-6502a4a006b7'
keywords: ["PROPTYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnact.h
api_type:
- HeaderDef
---

# PROPTYPE enumeration

\[**PROPTYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Defines the data type of a property.

## Syntax


```C++
typedef enum  { 
  TYPE_ERROR          = 1000,
  TYPE_DWORD,
  TYPE_LONG,
  TYPE_WORD,
  TYPE_SHORT,
  TYPE_BYTE,
  TYPE_CHAR,
  TYPE_FILETIME,
  TYPE_STRING,
  TYPE_BINARY,
  TYPE_FLAGS,
  TYPE_STREAM,
  TYPE_WSTRING,
  TYPE_BOOL,
  TYPE_PASS,
  TYPE_ULARGEINTEGER,
  TYPE_LAST
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="TYPE_ERROR"></span><span id="type_error"></span>**TYPE\_ERROR**
</dt> <dd>

Indicates an unknown data type or that the data type is in error.

</dd> <dt>

<span id="TYPE_DWORD"></span><span id="type_dword"></span>**TYPE\_DWORD**
</dt> <dd>

Indicates an unsigned 32-bit value.

</dd> <dt>

<span id="TYPE_LONG"></span><span id="type_long"></span>**TYPE\_LONG**
</dt> <dd>

Indicates a signed 32-bit value.

</dd> <dt>

<span id="TYPE_WORD"></span><span id="type_word"></span>**TYPE\_WORD**
</dt> <dd>

Indicates an unsigned 16-bit value.

</dd> <dt>

<span id="TYPE_SHORT"></span><span id="type_short"></span>**TYPE\_SHORT**
</dt> <dd>

Indicates a signed 16-bit value.

</dd> <dt>

<span id="TYPE_BYTE"></span><span id="type_byte"></span>**TYPE\_BYTE**
</dt> <dd>

Indicates an unsigned 8-bit value.

</dd> <dt>

<span id="TYPE_CHAR"></span><span id="type_char"></span>**TYPE\_CHAR**
</dt> <dd>

Indicates a signed 8-bit value.

</dd> <dt>

<span id="TYPE_FILETIME"></span><span id="type_filetime"></span>**TYPE\_FILETIME**
</dt> <dd>

Indicates a [FILETIME](http://msdn.microsoft.com/library/com/htm/cms_a2z_3vdx.asp) structure.

</dd> <dt>

<span id="TYPE_STRING"></span><span id="type_string"></span>**TYPE\_STRING**
</dt> <dd>

Indicates a fixed-length **NULL**-terminated string.

</dd> <dt>

<span id="TYPE_BINARY"></span><span id="type_binary"></span>**TYPE\_BINARY**
</dt> <dd>

Indicates fixed-length binary data.

</dd> <dt>

<span id="TYPE_FLAGS"></span><span id="type_flags"></span>**TYPE\_FLAGS**
</dt> <dd>

Indicates a flags field.

</dd> <dt>

<span id="TYPE_STREAM"></span><span id="type_stream"></span>**TYPE\_STREAM**
</dt> <dd>

Indicates a data stream.

</dd> <dt>

<span id="TYPE_WSTRING"></span><span id="type_wstring"></span>**TYPE\_WSTRING**
</dt> <dd>

Indicates a Unicode fixed-length **null**-terminated string.

</dd> <dt>

<span id="TYPE_BOOL"></span><span id="type_bool"></span>**TYPE\_BOOL**
</dt> <dd>

Indicates a **BOOL** checked to be equal to one or zero.

</dd> <dt>

<span id="TYPE_PASS"></span><span id="type_pass"></span>**TYPE\_PASS**
</dt> <dd>

Indicates password data.

</dd> <dt>

<span id="TYPE_ULARGEINTEGER"></span><span id="type_ulargeinteger"></span>**TYPE\_ULARGEINTEGER**
</dt> <dd>

Indicates a [ULARGE\_INTEGER](http://msdn.microsoft.com/library/winprog/winprog/ularge_integer_str.asp) structure.

</dd> <dt>

<span id="TYPE_LAST"></span><span id="type_last"></span>**TYPE\_LAST**
</dt> <dd>

Indicates the total number of property types in this enumeration.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Product<br/>                  | Outlook Express 6.0<br/>                                                        |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl> |



 

 





