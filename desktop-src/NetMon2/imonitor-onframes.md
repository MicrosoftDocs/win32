---
description: The OnFrames method must be implemented by the monitor. The MCSVC calls this method when either the capture buffer is full or the update time has passed.
ms.assetid: 243bd35b-2527-463e-b3d2-4bd840fe9c3f
title: IMonitor::OnFrames method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMonitor.OnFrames
api_type: 
- COM
api_location: 
- Netmon.h
---

# IMonitor::OnFrames method

The **OnFrames** method must be implemented by the monitor. The MCSVC calls this method when either the capture buffer is full or the update time has passed.

## Syntax


```C++
HRESULT OnFrames(
  [in] UPDATE_EVENT Event
);
```



## Parameters

<dl> <dt>

*Event* \[in\]
</dt> <dd>

[UPDATE\_EVENT](update-event.md) structure that holds frame information used to update events.

</dd> </dl>

## Return value

If the method is successful, the return value is S\_OK (which is the same as NOERROR). The MCSVC passes the returned value back to the NPP for processing.

If the method is unsuccessful, the return value is an error code. The MCSVC passes the returned value back to the NPP for processing.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




