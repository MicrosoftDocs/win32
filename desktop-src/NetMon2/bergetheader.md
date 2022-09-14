---
description: The BERGetHeader function decodes a choice header.
ms.assetid: 2574a9b3-c28e-43d1-904f-d45888617584
title: BERGetHeader function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BERGetHeader
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# BERGetHeader function

The **BERGetHeader** function decodes a choice header.

## Syntax


```C++
BOOL BERGetHeader(
   LPBYTE  pCurrentPointer,
   LPBYTE  pTag,
   LPDWORD pHeaderLength,
   LPDWORD pDataLength,
   LPBYTE  *ppNext
);
```



## Parameters

<dl> <dt>

*pCurrentPointer* 
</dt> <dd>

Pointer to the choice header.

</dd> <dt>

*pTag* 
</dt> <dd>

Pointer to the returned tag.

</dd> <dt>

*pHeaderLength* 
</dt> <dd>

Pointer to the returned header length.

</dd> <dt>

*pDataLength* 
</dt> <dd>

Pointer to the returned data length.

</dd> <dt>

*ppNext* 
</dt> <dd>

Pointer to the header contents.

</dd> </dl>

## Return value

If the function is successful (that is, a valid BER choice header is found) the return value is **TRUE**.

If the function is unsuccessful, the return value is **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Parser.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl>  |



 

 




