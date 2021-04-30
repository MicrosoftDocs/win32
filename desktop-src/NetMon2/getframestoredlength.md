---
description: The GetFrameStoredLength function returns the length of the frame.
ms.assetid: 7ac0e528-a45a-4c36-a99d-647347bdd143
title: GetFrameStoredLength function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFrameStoredLength
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetFrameStoredLength function

The **GetFrameStoredLength** function returns the length of the frame.

## Syntax


```C++
DWORD WINAPI GetFrameStoredLength(
  _In_ HFRAME hFrame
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to the frame.

</dd> </dl>

## Return value

If the function is successful, the return value is the length of the frame as stored.

If the function is unsuccessful, the return value is zero.

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetFrameStoredLength** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[GetFrameLength](getframelength.md)
</dt> </dl>

 

 




