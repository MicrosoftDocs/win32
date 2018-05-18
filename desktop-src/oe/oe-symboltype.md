---
title: SYMBOLTYPE enumeration
description: Do not use. Specifies the type of symbols being used.
ms.assetid: 'ad354f52-a1cb-467d-a39c-e18728034d25'
keywords: ["SYMBOLTYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Directdb.idl
api_type:
- IDLDef
---

# SYMBOLTYPE enumeration

Do not use. Specifies the type of symbols being used.

## Syntax


```C++
typedef enum tagSYMBOLTYPE { 
  SYMBOL_INVALID,
  SYMBOL_COLUMN,
  SYMBOL_DWORD,
  SYMBOL_METHOD
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="SYMBOL_INVALID"></span><span id="symbol_invalid"></span>**SYMBOL\_INVALID**
</dt> <dd>

Symbol type is invalid.

</dd> <dt>

<span id="SYMBOL_COLUMN"></span><span id="symbol_column"></span>**SYMBOL\_COLUMN**
</dt> <dd>

Symbol type is column.

</dd> <dt>

<span id="SYMBOL_DWORD"></span><span id="symbol_dword"></span>**SYMBOL\_DWORD**
</dt> <dd>

Symbol type is DWORD.

</dd> <dt>

<span id="SYMBOL_METHOD"></span><span id="symbol_method"></span>**SYMBOL\_METHOD**
</dt> <dd>

Symbol type is method, indicating the value of the SYMBOLINFO is a predefined method.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl> |



 

 





