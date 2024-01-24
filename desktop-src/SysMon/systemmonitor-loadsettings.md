---
title: SystemMonitor.LoadSettings method
description: Adds the counters in the HTML template file to the System Monitor.
ms.assetid: 3f88e590-df2b-4861-8ee6-a08f8742e6ad
keywords:
- LoadSettings method SysMon
- LoadSettings method SysMon , SystemMonitor object
- SystemMonitor object SysMon , LoadSettings method
topic_type:
- apiref
api_name:
- SystemMonitor.LoadSettings
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.LoadSettings method

Adds the counters in the HTML template file to the System Monitor.

## Syntax


```VB
SystemMonitor.LoadSettings( _
  ByVal SettingsFileName As String _
)
```



## Parameters

<dl> <dt>

*SettingsFileName* \[in\]
</dt> <dd>

HTML string that specifies the counters to add to the System Monitor.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To save the current counters in the System Monitor to an HTML file, call the [**SystemMonitor.SaveAs**](systemmonitor-saveas.md) method.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor**](systemmonitor.md)
</dt> </dl>

 

 





