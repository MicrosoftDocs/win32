---
title: LogFiles.Remove method
description: Removes the specified LogFileItem instance from the collection.
ms.assetid: d2885ffd-5957-472c-9a67-2f1469d9b48b
keywords:
- Remove method SysMon
- Remove method SysMon , LogFiles class
- LogFiles class SysMon , Remove method
topic_type:
- apiref
api_name:
- LogFiles.Remove
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# LogFiles.Remove method

Removes the specified [**LogFileItem**](logfileitem.md) instance from the collection.

## Syntax


```VB
LogFiles.Remove( _
  ByVal index As Object _
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

Integer index of the log file to remove from the collection. The index is one-based.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

**Prior to Windows Vista:** You cannot remove log files from the [**log file collection**](systemmonitor-logfiles.md) if the value of [**SystemMonitor.DataSourceType**](systemmonitor-datasourcetype.md) is set to sysmonLogFiles.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[LogFiles](logfiles.md)
</dt> <dt>

[**LogFileItem**](logfileitem.md)
</dt> <dt>

[**LogFiles**](systemmonitor-logfiles.md)
</dt> </dl>

 

 





