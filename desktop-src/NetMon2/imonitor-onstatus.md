---
description: The MCSVC method calls the OnStatus method to notify the monitor that an NPP status event exists. This method must be implemented by the monitor.
ms.assetid: 771852b1-77d8-4d7d-b3fb-03eb3ea593b8
title: IMonitor::OnStatus method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMonitor.OnStatus
api_type: 
- COM
api_location: 
- Netmon.h
---

# IMonitor::OnStatus method

The MCSVC method calls the **OnStatus** method to notify the monitor that an NPP status event exists. This method must be implemented by the monitor.

## Syntax


```C++
HRESULT OnStatus(
  [in] UPDATE_EVENT Event
);
```



## Parameters

<dl> <dt>

*Event* \[in\]
</dt> <dd>

An [UPDATE\_EVENT](update-event.md) structure.

</dd> </dl>

## Return value

If the method is successful, the return value is S\_OK (which is the same as NOERROR), and the MCSVC passes the returned value back to the NPP for processing.

If the method is unsuccessful, return an error code. On error, the MCSVC passes the returned value back to the NPP for processing.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




