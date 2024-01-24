---
title: SystemMonitor.ManualUpdate property
description: Retrieves or sets a value indicating whether the contents of the System Monitor will be updated manually, or automatically at specified intervals.
ms.assetid: e068a955-ec1d-4f93-9261-25ba87773913
keywords:
- ManualUpdate property SysMon
- ManualUpdate property SysMon , SystemMonitor class
- SystemMonitor class SysMon , ManualUpdate property
topic_type:
- apiref
api_name:
- SystemMonitor.ManualUpdate
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.ManualUpdate property

Retrieves or sets a value indicating whether the contents of the System Monitor will be updated manually, or automatically at specified intervals.

This property is read-only.

## Syntax


```VB
Property ManualUpdate As Boolean
```



## Property value

True indicates that graph is updated manually. False indicates that the graph is updated automatically based on the update interval specified in [**SystemMonitor.UpdateInterval**](systemmonitor-updateinterval.md).

## Remarks

By default, the graph is updated automatically.

To update the graph manually, call the [**SystemMonitor.CollectSample**](systemmonitor-collectsample.md) method.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor**](systemmonitor.md)
</dt> <dt>

[**SystemMonitor.CollectSample**](systemmonitor-collectsample.md)
</dt> <dt>

[**SystemMonitor.UpdateGraph**](systemmonitor-updategraph.md)
</dt> </dl>

 

 





