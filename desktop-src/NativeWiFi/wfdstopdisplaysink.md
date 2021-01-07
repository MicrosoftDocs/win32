---
description: Stops the Miracast sink mode, turns off discoverability, and un-registers the callback.
ms.assetid: 38AE60CB-F601-4C03-A725-9B802341B84B
title: WFDDisplaySinkStop function (Wfdsink.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WFDStopDisplaySink
api_type: 
- DllExport
api_location: 
- wifidisplay.dll
---

# WFDDisplaySinkStop function

Stops the Miracast sink mode, turns off discoverability, and un-registers the callback. Your app should call this once on shutdown.

## Syntax


```C++
DWORD WINAPI WFDStopDisplaySink(void);
```



## Parameters

This function has no parameters.

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

## Remarks

It is expected that your app has unblocked any callbacks in progress before calling **WFDStopDisplaySink**.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows 10<br/>                                                                      |
| End of server support<br/>    | Windows Server 2016<br/>                                                             |
| Header<br/>                   | <dl> <dt>Wfdsink.h</dt> </dl>       |
| Library<br/>                  | <dl> <dt>Wifidisplay.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wifidisplay.dll</dt> </dl> |



 

 




