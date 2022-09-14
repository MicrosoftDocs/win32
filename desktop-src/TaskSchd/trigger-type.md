---
title: Trigger.Type property
description: For scripting, gets the type of the trigger.
ms.assetid: '346e6b02-c89e-4644-aa19-2bbf3d0fb3c3'
keywords:
- Type property Task Scheduler
- Type property Task Scheduler , Trigger object
- Trigger object Task Scheduler , Type property
topic_type:
- apiref
api_name:
- Trigger.Type
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Trigger.Type property

For scripting, gets the type of the trigger. The trigger type is defined when the trigger is created and cannot be changed later. For information on creating a trigger, see [**TriggerCollection.Create**](triggercollection-create.md).

## Syntax


```VB
Trigger.Type As TASK_TRIGGER_TYPE2
```



## Property value

One of the following [**TASK\_TRIGGER\_TYPE2**](/windows/desktop/api/taskschd/ne-taskschd-task_trigger_type2) enumeration values.



| Value                                                                                                                                                                                                                                                                                | Meaning                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <span id="TASK_TRIGGER_EVENT"></span><span id="task_trigger_event"></span><dl> <dt>**TASK\_TRIGGER\_EVENT**</dt> <dt>0</dt> </dl>                                                 | Starts the task when a specific event occurs.<br/>              |
| <span id="TASK_TRIGGER_TIME"></span><span id="task_trigger_time"></span><dl> <dt>**TASK\_TRIGGER\_TIME**</dt> <dt>1</dt> </dl>                                                    | Starts the task at a specific time of day.<br/>                 |
| <span id="TASK_TRIGGER_DAILY"></span><span id="task_trigger_daily"></span><dl> <dt>**TASK\_TRIGGER\_DAILY**</dt> <dt>2</dt> </dl>                                                 | Starts the task daily.<br/>                                     |
| <span id="TASK_TRIGGER_WEEKLY"></span><span id="task_trigger_weekly"></span><dl> <dt>**TASK\_TRIGGER\_WEEKLY**</dt> <dt>3</dt> </dl>                                              | Starts the task weekly.<br/>                                    |
| <span id="TASK_TRIGGER_MONTHLY"></span><span id="task_trigger_monthly"></span><dl> <dt>**TASK\_TRIGGER\_MONTHLY**</dt> <dt>4</dt> </dl>                                           | Starts the task monthly.<br/>                                   |
| <span id="TASK_TRIGGER_MONTHLYDOW"></span><span id="task_trigger_monthlydow"></span><dl> <dt>**TASK\_TRIGGER\_MONTHLYDOW**</dt> <dt>5</dt> </dl>                                  | Starts the task every month on a specific day of the week.<br/> |
| <span id="TASK_TRIGGER_IDLE"></span><span id="task_trigger_idle"></span><dl> <dt>**TASK\_TRIGGER\_IDLE**</dt> <dt>6</dt> </dl>                                                    | Starts the task when the computer goes into an idle state.<br/> |
| <span id="TASK_TRIGGER_REGISTRATION"></span><span id="task_trigger_registration"></span><dl> <dt>**TASK\_TRIGGER\_REGISTRATION**</dt> <dt>7</dt> </dl>                            | Starts the task when the task is registered.<br/>               |
| <span id="TASK_TRIGGER_BOOT"></span><span id="task_trigger_boot"></span><dl> <dt>**TASK\_TRIGGER\_BOOT**</dt> <dt>8</dt> </dl>                                                    | Starts the task when the computer boots.<br/>                   |
| <span id="TASK_TRIGGER_LOGON"></span><span id="task_trigger_logon"></span><dl> <dt>**TASK\_TRIGGER\_LOGON**</dt> <dt>9</dt> </dl>                                                 | Starts the task when a specific user logs on.<br/>              |
| <span id="TASK_TRIGGER_SESSION_STATE_CHANGE"></span><span id="task_trigger_session_state_change"></span><dl> <dt>**TASK\_TRIGGER\_SESSION\_STATE\_CHANGE**</dt> <dt>11</dt> </dl> | Triggers the task when a specific session state changes.<br/>   |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**TriggerCollection.Create**](triggercollection-create.md)
</dt> <dt>

[**TASK\_TRIGGER\_TYPE2**](/windows/desktop/api/taskschd/ne-taskschd-task_trigger_type2)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





