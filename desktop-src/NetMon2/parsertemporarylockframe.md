---
description: The ParserTemporaryLockFrame function locks a frame when it enters a parser and unlocks the frame when the function exits the parser.
ms.assetid: c1c52f62-1974-47cc-8c37-61918fbce54a
title: ParserTemporaryLockFrame function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ParserTemporaryLockFrame
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# ParserTemporaryLockFrame function

The **ParserTemporaryLockFrame** function locks a frame when it enters a parser and unlocks the frame when the function exits the parser.

## Syntax


```C++
LPBYTE WINAPI ParserTemporaryLockFrame(
  _In_ HFRAME hFrame
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to the frame that the parser points to.

</dd> </dl>

## Return value

If the function is successful, the return value is a pointer to the first byte of data in the frame.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

Parsers should not call the **LockFrame** function. If a parser takes a lock and then generates a fault or returns without unlocking the frame, the parser leaves the system in a state where it cannot change protocols or cut or copy frames. Parsers should use the **ParserTemporaryLockFrame** function, which grants a lock only during the context of the function entry into the parser. On exit from the parser, the lock for that frame is released. As a result, the pointer will be valid only after the parser returns from the call to the **AttachProperties** or **RecognizeFrame** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




