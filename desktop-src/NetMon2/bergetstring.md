---
description: The BERGetString function decodes a BER-encoded string.
ms.assetid: 1f72f061-c0ed-4634-9709-e08c2b9468bb
title: BERGetString function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BERGetString
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# BERGetString function

The **BERGetString** function decodes a BER-encoded string.

## Syntax


```C++
BOOL BERGetString(
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

Pointer to the string that is decoded.

</dd> <dt>

*ppValuePointer* 
</dt> <dd>

Pointer to the pointer of the decoded string.

</dd> <dt>

*pHeaderLength* 
</dt> <dd>

Pointer to the returned header length.

</dd> <dt>

*pDataLength* 
</dt> <dd>

Pointer to the string length.

</dd> <dt>

*ppNext* 
</dt> <dd>

Pointer to the pointer of the next BER entry.

</dd> </dl>

## Return value

If the function is successful (that is, if a valid BER-encoded string is decoded), the return value is **TRUE**.

If function is unsuccessful, the return value is **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Parser.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl>  |



 

 




