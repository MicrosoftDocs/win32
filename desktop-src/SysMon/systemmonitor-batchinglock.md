---
title: SystemMonitor.BatchingLock method
description: Locks the System Monitor to prevent it from sampling counter data from the newly added counter or log file.
ms.assetid: 6b9d683a-7a97-44a4-9eb6-6caaafe2abdd
keywords:
- BatchingLock method SysMon
- BatchingLock method SysMon , SystemMonitor object
- SystemMonitor object SysMon , BatchingLock method
topic_type:
- apiref
api_name:
- SystemMonitor.BatchingLock
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.BatchingLock method

Locks the System Monitor to prevent it from sampling counter data from the newly added counter or log file.

## Syntax


```VB
SystemMonitor.BatchingLock( _
  ByVal lock As Boolean, _
  ByVal batchReason As SysmonBatchReason _
)
```



## Parameters

<dl> <dt>

*lock* \[in\]
</dt> <dd>

Set to True to lock the System Monitor to prevent it from sampling counter data from the newly added counter or log file. Set to False to remove the lock.

</dd> <dt>

*batchReason* \[in\]
</dt> <dd>

Identifies the source of the data that you are locking. Use the same reason value when locking and unlocking the resource. For possible values, see the [**SysmonBatchReason**](/windows/win32/api/isysmon/ne-isysmon-sysmonbatchreason) enumeration.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

You must call this method twice, once to lock the source (True) and once to unlock the source (False).

You can place only one lock. For example, if you set the lock for SysmonBatchAddFiles and then make a second call using SysmonBatchAddCounters as the reason, the second call removes the lock placed by the first call.

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

 

 





