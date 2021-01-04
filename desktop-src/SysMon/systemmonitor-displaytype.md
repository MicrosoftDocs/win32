---
title: SystemMonitor.DisplayType property
description: Retrieves or sets the type of graph used to graph the performance counter data.
ms.assetid: a04545b1-920e-4fb3-909b-dc47e1374629
keywords:
- DisplayType property SysMon
- DisplayType property SysMon , SystemMonitor class
- SystemMonitor class SysMon , DisplayType property
topic_type:
- apiref
api_name:
- SystemMonitor.DisplayType
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.DisplayType property

Retrieves or sets the type of graph used to graph the performance counter data.

This property is read-only.

## Syntax


```VB
Property DisplayType As DisplayTypeConstants
```



## Property value

Type of graph used to graph the performance counter data. For possible values, see [**DisplayTypeConstants**](/windows/win32/api/isysmon/ne-isysmon-displaytypeconstants).

## Exceptions



| Exception type               | Condition                                         |
|------------------------------|---------------------------------------------------|
| **System.ArgumentException** | The specified graph or report value is not valid. |



 

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

 

 





