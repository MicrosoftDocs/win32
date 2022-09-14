---
description: The GetFrameMacHeaderLength function returns the length, in bytes, of the MAC header of the frame.
ms.assetid: 4a0f6a8c-04e0-47cb-abd1-b4011cd2d062
title: GetFrameMacHeaderLength function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFrameMacHeaderLength
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetFrameMacHeaderLength function

The **GetFrameMacHeaderLength** function returns the length, in bytes, of the MAC header of the frame.

## Syntax


```C++
DWORD WINAPI GetFrameMacHeaderLength(
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

If the function is successful, the return value is the length   in bytes   of the MAC header.

If the function is not successful, or an unknown MAC type is encountered, the return value is zero.

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetFrameMacHeaderLength** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




