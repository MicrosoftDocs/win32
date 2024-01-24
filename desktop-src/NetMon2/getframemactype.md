---
description: The GetFrameMacType function returns the MAC type of the frame.
ms.assetid: 8d3da770-1392-4638-a267-32c2dae289b0
title: GetFrameMacType function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFrameMacType
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetFrameMacType function

The **GetFrameMacType** function returns the MAC type of the frame.

## Syntax


```C++
DWORD WINAPI GetFrameMacType(
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

The function returns the MAC type of the frame, which can have one of the following values.

-   MAC\_TYPE\_UNKNOWN
-   MAC\_TYPE\_ETHERNET
-   MAC\_TYPE\_TOKENRING
-   MAC\_TYPE\_FDDI

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetFrameMacType** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




