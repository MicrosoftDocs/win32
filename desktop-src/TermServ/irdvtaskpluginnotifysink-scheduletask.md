---
title: IRDVTaskPluginNotifySink ScheduleTask method
description: Called by the task agent to schedule a task.
ms.assetid: 06793439-cf16-40ca-8a91-08acc22c73ed
ms.tgt_platform: multiple
keywords:
- ScheduleTask method Remote Desktop Services
- ScheduleTask method Remote Desktop Services , IRDVTaskPluginNotifySink interface
- IRDVTaskPluginNotifySink interface Remote Desktop Services , ScheduleTask method
topic_type:
- apiref
api_name:
- IRDVTaskPluginNotifySink.ScheduleTask
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IRDVTaskPluginNotifySink::ScheduleTask method

Called by the task agent to schedule a task.

## Syntax


```C++
HRESULT ScheduleTask(
  [in] FILETIME        ftStartTime,
  [in] FILETIME        ftEndTime,
  [in] FILETIME        ftDeadline,
  [in] BSTR            bstrLabel,
  [in] BSTR            bstrIdentifier,
  [in] SAFEARRAY(BYTE) saContext
);
```



## Parameters

<dl> <dt>

*ftStartTime* \[in\]
</dt> <dd>

Type: **[**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime)**

The earliest task start time, in UTC.

</dd> <dt>

*ftEndTime* \[in\]
</dt> <dd>

Type: **[**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime)**

The task end time, in UTC. Pass a [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime) set to all zeros if no end time is specified.

</dd> <dt>

*ftDeadline* \[in\]
</dt> <dd>

Type: **[**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime)**

The task deadline, in UTC. This is used to set priority for multiple tasks that are within their start window. If more than one task should be started, the one with the earliest deadline will be started first.

</dd> <dt>

*bstrLabel* \[in\]
</dt> <dd>

Type: **BSTR**

The label for the task. This is passed to the [**StartTask**](irdvtaskplugin-starttask.md) method.

</dd> <dt>

*bstrIdentifier* \[in\]
</dt> <dd>

Type: **BSTR**

The identifier of the task. This is passed to the [**StartTask**](irdvtaskplugin-starttask.md) method.

</dd> <dt>

*saContext* \[in\]
</dt> <dd>

Type: **SAFEARRAY(BYTE)**

Optional data for the task. This is passed to the [**StartTask**](irdvtaskplugin-starttask.md) method.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | Windows 7 Enterprise<br/>   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/> |



## See also

<dl> <dt>

[**IRDVTaskPluginNotifySink**](irdvtaskpluginnotifysink.md)
</dt> </dl>

 

