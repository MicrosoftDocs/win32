---
description: The VarLenSmallIntToDword function converts a variable-length, small integer to a DWORD.
ms.assetid: e26dc206-ac85-4346-9fcf-93ebc8948ced
title: VarLenSmallIntToDword function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- VarLenSmallIntToDword
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# VarLenSmallIntToDword function

The **VarLenSmallIntToDword** function converts a variable-length, small integer to a **DWORD**.

## Syntax


```C++
LPDWORD WINAPI VarLenSmallIntToDword(
   LPBYTE  pValue,
   WORD    ValueLen,
   BOOL    fIsByteswapped,
   LPDWORD lpDword
);
```



## Parameters

<dl> <dt>

*pValue* 
</dt> <dd>

Pointer to the variable-length, small integer.

</dd> <dt>

*ValueLen* 
</dt> <dd>

Length (in bytes) of the variable-length, small integer .

</dd> <dt>

*fIsByteswapped* 
</dt> <dd>

Flag that indicates whether the variable length small integer is byte-swapped.

</dd> <dt>

*lpDword* 
</dt> <dd>

The **DWORD** that the integer is converted to.

</dd> </dl>

## Return value

The return value is a pointer to the **DWORD**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Parser.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl>  |



 

 




