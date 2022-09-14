---
title: TaskSettings.MultipleInstances property
description: For scripting, gets or sets the policy that defines how the Task Scheduler deals with multiple instances of the task.
ms.assetid: 'a25be615-fbb9-47fe-805a-5b93eab95f47'
keywords:
- MultipleInstances property Task Scheduler
- MultipleInstances property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , MultipleInstances property
topic_type:
- apiref
api_name:
- TaskSettings.MultipleInstances
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.MultipleInstances property

For scripting, gets or sets the policy that defines how the Task Scheduler deals with multiple instances of the task.

This property is read/write.

## Syntax


```VB
TaskSettings.MultipleInstances As Integer
```



## Property value

[**TASK\_INSTANCES\_POLICY**](/windows/desktop/api/taskschd/ne-taskschd-task_instances_policy) constants.



| Value                                                                                                                                                                                                                                                               | Meaning                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <span id="TASK_INSTANCES_PARALLEL"></span><span id="task_instances_parallel"></span><dl> <dt>**TASK\_INSTANCES\_PARALLEL**</dt> <dt>0</dt> </dl>                 | Starts a new instance while an existing instance of the task is running.<br/>              |
| <span id="TASK_INSTANCES_QUEUE"></span><span id="task_instances_queue"></span><dl> <dt>**TASK\_INSTANCES\_QUEUE**</dt> <dt>1</dt> </dl>                          | Starts a new instance of the task after all other instances of the task are complete.<br/> |
| <span id="TASK_INSTANCES_IGNORE_NEW"></span><span id="task_instances_ignore_new"></span><dl> <dt>**TASK\_INSTANCES\_IGNORE\_NEW**</dt> <dt>2</dt> </dl>          | Does not start a new instance if an existing instance of the task is running.<br/>         |
| <span id="TASK_INSTANCES_STOP_EXISTING"></span><span id="task_instances_stop_existing"></span><dl> <dt>**TASK\_INSTANCES\_STOP\_EXISTING**</dt> <dt>3</dt> </dl> | Stops an existing instance of the task before it starts new instance.<br/>                 |



 

## Remarks

When reading or writing XML for a task, this setting is specified in the [**MultipleInstancesPolicy**](taskschedulerschema-multipleinstancespolicy-settingstype-element.md) element of the Task Scheduler schema.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**TASK\_INSTANCES\_POLICY**](/windows/desktop/api/taskschd/ne-taskschd-task_instances_policy)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





