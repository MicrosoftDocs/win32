---
description: The SendNMEvent method submits events to Windows Management Instrumentation (WMI).
ms.assetid: 85c33a71-72aa-4b0a-8e8b-3a220a080bb2
title: IMonitorEventer::SendNMEvent method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMonitorEventer.SendNMEvent
api_type: 
- COM
api_location: 
- Netmon.h
---

# IMonitorEventer::SendNMEvent method

The **SendNMEvent** method submits events to Windows Management Instrumentation (WMI).

## Syntax


```C++
HRESULT SendNMEvent(
  [in] PNMEVENTDATA pNMEventData
);
```



## Parameters

<dl> <dt>

*pNMEventData* \[in\]
</dt> <dd>

Pointer to the event submitted to WMI.

</dd> </dl>

## Return value

If the method is successful, the return value is S\_OK.

If the method is unsuccessful, the return value is NMERR\_OUT\_OF\_MEMORY.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




