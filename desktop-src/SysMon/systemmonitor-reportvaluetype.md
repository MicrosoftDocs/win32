---
title: SystemMonitor.ReportValueType property
description: Retrieves or sets a value that determines if the Histogram and Report views graph the last value sampled during the sampling interval or a calculated value from the sampling, such as the average or minimum counter value.
ms.assetid: add75744-c3ab-48ab-b567-28a072facfdd
keywords:
- ReportValueType property SysMon
- ReportValueType property SysMon , SystemMonitor class
- SystemMonitor class SysMon , ReportValueType property
topic_type:
- apiref
api_name:
- SystemMonitor.ReportValueType
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.ReportValueType property

Retrieves or sets a value that determines if the Histogram and Report views graph the last value sampled during the sampling interval or a calculated value from the sampling, such as the average or minimum counter value.

This property is read-only.

## Syntax


```VB
Property ReportValueType As ReportValueTypeConstants
```



## Property value

Determines if the Histogram and Report views graph the last value sampled during the sampling interval or a calculated value from the sampling interval. For possible values, see [**ReportValueTypeConstants**](/windows/win32/api/isysmon/ne-isysmon-reportvaluetypeconstants).

## Remarks

SYSMON ignores this value and uses [**ReportValueTypeConstants.sysmonDefaultValue**](/windows/win32/api/isysmon/ne-isysmon-reportvaluetypeconstants) if [**SystemMonitor.DisplayType**](systemmonitor-displaytype.md) is not [**DisplayTypeConstants.sysmonHistogram**](/windows/win32/api/isysmon/ne-isysmon-displaytypeconstants) or **DisplayTypeConstants.sysmonReport**.

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

 

 





