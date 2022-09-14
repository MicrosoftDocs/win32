---
description: The BERGetInteger function decodes a BER-encoded integer.
ms.assetid: 1ab0dcec-05cf-4322-a44e-28aa9131495a
title: BERGetInteger function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BERGetInteger
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# BERGetInteger function

The **BERGetInteger** function decodes a BER-encoded integer.

## Syntax


```C++
BOOL BERGetInteger(
   LPBYTE  pCurrentPointer,
   LPBYTE  *ppValuePointer,
   LPDWORD pHeaderLength,
   LPDWORD pDataLength,
   LPBYTE  *ppNext
);
```



## Parameters

<dl> <dt>

*pCurrentPointer* 
</dt> <dd>

Pointer to the integer that is decoded.

</dd> <dt>

*ppValuePointer* 
</dt> <dd>

Pointer to the pointer to returned value.

</dd> <dt>

*pHeaderLength* 
</dt> <dd>

Pointer to the returned header length.

</dd> <dt>

*pDataLength* 
</dt> <dd>

Pointer to the data length.

</dd> <dt>

*ppNext* 
</dt> <dd>

Pointer to the pointer to the next BER entry.

</dd> </dl>

## Return value

If the function is successful (that is, if a valid BER encoded integer is found and converted), the return value is **TRUE**.

If function is unsuccessful, the return value is **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Parser.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl>  |



 

 




