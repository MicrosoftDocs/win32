---
description: The OnStop method must be implemented by the monitor. The MSCVC calls this method to notify the monitor that the capture will be stopped.
ms.assetid: 5988bfb8-2068-42a1-a774-6f6be9828568
title: IMonitor::OnStop method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMonitor.OnStop
api_type: 
- COM
api_location: 
- Netmon.h
---

# IMonitor::OnStop method

The **OnStop** method must be implemented by the monitor. The MSCVC calls this method to notify the monitor that the capture will be stopped.

## Syntax


```C++
HRESULT OnStop();
```



## Parameters

This method has no parameters.

## Return value

If the method is successful, the return value is S\_OK (which is the same as NOERROR).

If the method is unsuccessful, the return value is an error code. When an error code is returned, the monitor cannot be restarted.

## Remarks

The MCSVC calls this method after [IRTC::Stop](irtc-stop.md) is called.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




