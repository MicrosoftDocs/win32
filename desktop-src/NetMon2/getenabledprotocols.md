---
description: The GetEnabledProtocols function returns a table of all protocols that are marked Enabled.
ms.assetid: 11feac64-c770-47b2-a740-fc372e97b8ed
title: GetEnabledProtocols function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetEnabledProtocols
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetEnabledProtocols function

The **GetEnabledProtocols** function returns a table of all protocols that are marked Enabled.

## Syntax


```C++
LPPROTOCOLTABLE WINAPI GetEnabledProtocols(
  _In_ HCAPTURE hCapture
);
```



## Parameters

<dl> <dt>

*hCapture* \[in\]
</dt> <dd>

Handle to the capture.

</dd> </dl>

## Return value

If the function is successful, the return value is a pointer to a [PROTOCOLTABLE](protocoltable.md) structure that lists all the enabled protocols in the capture.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetEnabledProtocols** function.

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

[PROTOCOLTABLE](protocoltable.md)
</dt> </dl>

 

 




