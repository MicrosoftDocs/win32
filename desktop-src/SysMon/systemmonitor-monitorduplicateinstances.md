---
title: SystemMonitor.MonitorDuplicateInstances property
description: Retrieves or sets a value that determines whether multiple instances of a counter can be monitored.
ms.assetid: fe8d6074-eb29-4093-9f79-39e6171a3a3f
keywords:
- MonitorDuplicateInstances property SysMon
- MonitorDuplicateInstances property SysMon , SystemMonitor class
- SystemMonitor class SysMon , MonitorDuplicateInstances property
topic_type:
- apiref
api_name:
- SystemMonitor.MonitorDuplicateInstances
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.MonitorDuplicateInstances property

Retrieves or sets a value that determines whether multiple instances of a counter can be monitored.

This property is read-only.

## Syntax


```VB
Property MonitorDuplicateInstances As Boolean
```



## Property value

True indicates that multiple instances of a counter can be monitored (True is the default). False indicates that only one instance of a counter can be monitored.

## Remarks

System Monitor appends \#n to every instance name, except the first, if multiple instances exist. The serial number, n, begins with one and is incremented by one for each new instance. For example, if you specify "\\Process(\*)\\% Processor Time", the counter collection should contain multiple instances of svchost. The first occurrence will be svchost, the next occurrence will be svchost\#1, and so on.

Duplicate instances are monitored only if you use the wildcard character (\*) for the instance name. If you specified "\\Process(svchost)\\% Processor Time" only the first instance found of svchost is monitored, not all instances of svchost.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor**](systemmonitor.md)
</dt> </dl>

 

 





