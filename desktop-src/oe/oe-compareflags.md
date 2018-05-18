---
title: COMPAREFLAGS enumeration
description: Do not use. This flag is used when defining indices of a database table. It specifies how database should compare two values.
ms.assetid: '20e28048-003b-4d67-b991-bfc4a8db9de9'
keywords: ["COMPAREFLAGS enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Directdb.idl
api_type:
- IDLDef
---

# COMPAREFLAGS enumeration

Do not use. This flag is used when defining indices of a database table. It specifies how database should compare two values.

## Syntax


```C++
typedef enum  { 
  COMPARE_IGNORECASE  = 0x00000001,
  COMPARE_DESCENDING  = 0x00000002,
  COMPARE_ASANSI      = 0x00000004
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="COMPARE_IGNORECASE"></span><span id="compare_ignorecase"></span>**COMPARE\_IGNORECASE**
</dt> <dd>

String value comparison is case-insensitive.

</dd> <dt>

<span id="COMPARE_DESCENDING"></span><span id="compare_descending"></span>**COMPARE\_DESCENDING**
</dt> <dd>

The index will be built in descending order.

</dd> <dt>

<span id="COMPARE_ASANSI"></span><span id="compare_asansi"></span>**COMPARE\_ASANSI**
</dt> <dd>

String value is treated as ANSI.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl> |



 

 





