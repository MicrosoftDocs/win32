---
title: TriggerCollection.Create method
description: For scripting, creates a new trigger for the task.
ms.assetid: '3d7dc811-0d83-475f-8a6e-87e59dae0113'
keywords:
- triggers Task Scheduler , creating
- Create method Task Scheduler
- Create method Task Scheduler , TriggerCollection object
- TriggerCollection object Task Scheduler , Create method
topic_type:
- apiref
api_name:
- TriggerCollection.Create
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TriggerCollection.Create method

For scripting, creates a new trigger for the task.

## Syntax


```VB
TriggerCollection.Create( _
  ByVal type _
)
```



## Parameters

<dl> <dt>

*type* \[in\]
</dt> <dd>

This parameter is set to one of the following [**TASK\_TRIGGER\_TYPE2**](/windows/desktop/api/taskschd/ne-taskschd-task_trigger_type2) enumeration constants.



| Value                                                                                                                                                                                                                                                                                | Meaning                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TASK_TRIGGER_EVENT"></span><span id="task_trigger_event"></span><dl> <dt>**TASK\_TRIGGER\_EVENT**</dt> <dt>0</dt> </dl>                                                 | Triggers the task when a specific event occurs.<br/>                                                                                                               |
| <span id="TASK_TRIGGER_TIME"></span><span id="task_trigger_time"></span><dl> <dt>**TASK\_TRIGGER\_TIME**</dt> <dt>1</dt> </dl>                                                    | Triggers the task at a specific time of day.<br/>                                                                                                                  |
| <span id="TASK_TRIGGER_DAILY"></span><span id="task_trigger_daily"></span><dl> <dt>**TASK\_TRIGGER\_DAILY**</dt> <dt>2</dt> </dl>                                                 | Triggers the task on a daily schedule. For example, the task starts at a specific time every day, every-other day, every third day, and so on.<br/>                |
| <span id="TASK_TRIGGER_WEEKLY"></span><span id="task_trigger_weekly"></span><dl> <dt>**TASK\_TRIGGER\_WEEKLY**</dt> <dt>3</dt> </dl>                                              | Triggers the task on a weekly schedule. For example, the task starts at 8:00 AM on a specific day every week or other week.<br/>                                   |
| <span id="TASK_TRIGGER_MONTHLY"></span><span id="task_trigger_monthly"></span><dl> <dt>**TASK\_TRIGGER\_MONTHLY**</dt> <dt>4</dt> </dl>                                           | Triggers the task on a monthly schedule. For example, the task starts on specific days of specific months.<br/>                                                    |
| <span id="TASK_TRIGGER_MONTHLYDOW"></span><span id="task_trigger_monthlydow"></span><dl> <dt>**TASK\_TRIGGER\_MONTHLYDOW**</dt> <dt>5</dt> </dl>                                  | Triggers the task on a monthly day-of-week schedule. For example, the task starts on a specific days of the week, weeks of the month, and months of the year.<br/> |
| <span id="TASK_TRIGGER_IDLE"></span><span id="task_trigger_idle"></span><dl> <dt>**TASK\_TRIGGER\_IDLE**</dt> <dt>6</dt> </dl>                                                    | Triggers the task when the computer goes into an idle state.<br/>                                                                                                  |
| <span id="TASK_TRIGGER_REGISTRATION"></span><span id="task_trigger_registration"></span><dl> <dt>**TASK\_TRIGGER\_REGISTRATION**</dt> <dt>7</dt> </dl>                            | Triggers the task when the task is registered.<br/>                                                                                                                |
| <span id="TASK_TRIGGER_BOOT"></span><span id="task_trigger_boot"></span><dl> <dt>**TASK\_TRIGGER\_BOOT**</dt> <dt>8</dt> </dl>                                                    | Triggers the task when the computer boots.<br/>                                                                                                                    |
| <span id="TASK_TRIGGER_LOGON"></span><span id="task_trigger_logon"></span><dl> <dt>**TASK\_TRIGGER\_LOGON**</dt> <dt>9</dt> </dl>                                                 | Triggers the task when a specific user logs on.<br/>                                                                                                               |
| <span id="TASK_TRIGGER_SESSION_STATE_CHANGE"></span><span id="task_trigger_session_state_change"></span><dl> <dt>**TASK\_TRIGGER\_SESSION\_STATE\_CHANGE**</dt> <dt>11</dt> </dl> | Triggers the task when a specific session state changes.<br/>                                                                                                      |



 

</dd> </dl>

## Return value

A [**Trigger**](trigger.md) object that represents the new trigger.

## Remarks

For information about each trigger type see [Trigger Types](trigger-types.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> <dt>

[**Trigger**](trigger.md)
</dt> </dl>

 

 





