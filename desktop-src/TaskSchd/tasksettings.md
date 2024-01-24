---
title: TaskSettings object
description: A scripting object that provides the settings that the Task Scheduler service uses to perform the task.
ms.assetid: 'f2ba952b-7864-467d-8709-eb6995dd5df5'
keywords:
- TaskSettings object Task Scheduler
- TaskSettings object Task Scheduler , described
topic_type:
- apiref
api_name:
- TaskSettings
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings object

A scripting object that provides the settings that the Task Scheduler service uses to perform the task.

## Members

The **TaskSettings** object has these types of members:

-   [Properties](#properties)

### Properties

The **TaskSettings** object has these properties.



| Property                                                                                 | Access type           | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-----------------------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllowDemandStart**](tasksettings-allowdemandstart.md)<br/>                     | Read/write<br/> | Gets or sets a Boolean value that indicates that the task can be started by using either the Run command or the Context menu.<br/>                                                                                                                                                                                                                                                                                     |
| [**AllowHardTerminate**](tasksettings-allowhardterminate.md)<br/>                 | Read/write<br/> | Gets or sets a Boolean value that indicates that the task may be terminated by using [**TerminateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-terminateprocess).<br/>                                                                                                                                                                                                                                                                               |
| [**Compatibility**](tasksettings-compatibility.md)<br/>                           | Read/write<br/> | Gets or sets an integer value that indicates which version of Task Scheduler a task is compatible with.<br/>                                                                                                                                                                                                                                                                                                           |
| [**DeleteExpiredTaskAfter**](tasksettings-deleteexpiredtaskafter.md)<br/>         | Read/write<br/> | Gets or sets the amount of time that the Task Scheduler will wait before deleting the task after it expires.<br/>                                                                                                                                                                                                                                                                                                      |
| [**DisallowStartIfOnBatteries**](tasksettings-disallowstartifonbatteries.md)<br/> | Read/write<br/> | Gets or sets a Boolean value that indicates that the task will not be started if the computer is running on battery power.<br/>                                                                                                                                                                                                                                                                                        |
| [**Enabled**](tasksettings-enabled.md)<br/>                                       | Read/write<br/> | Gets or sets a Boolean value that indicates that the task is enabled. The task can be performed only when this setting is True.<br/>                                                                                                                                                                                                                                                                                   |
| [**ExecutionTimeLimit**](tasksettings-executiontimelimit.md)<br/>                 | Read/write<br/> | Gets or sets the amount of time allowed to complete the task.<br/>                                                                                                                                                                                                                                                                                                                                                     |
| [**Hidden**](tasksettings-hidden.md)<br/>                                         | Read/write<br/> | Gets or sets a Boolean value that indicates that the task will not be visible in the UI. However, administrators can override this setting through the use of a "master switch" that makes all tasks visible in the UI.<br/>                                                                                                                                                                                           |
| [**IdleSettings**](tasksettings-idlesettings.md)<br/>                             | Read/write<br/> | Gets or sets the information that specifies how the Task Scheduler performs tasks when the computer is in an idle state.<br/>                                                                                                                                                                                                                                                                                          |
| [**MultipleInstances**](tasksettings-multipleinstances.md)<br/>                   | Read/write<br/> | Gets or sets the policy that defines how the Task Scheduler deals with multiple instances of the task.<br/>                                                                                                                                                                                                                                                                                                            |
| [**NetworkSettings**](tasksettings-networksettings.md)<br/>                       | Read/write<br/> | Gets or sets the network settings object that contains a network profile identifier and name. If the [**RunOnlyIfNetworkAvailable**](tasksettings-runonlyifnetworkavailable.md) property of **TaskSettings** is **True** and a network propfile is specified in the [**NetworkSettings**](tasksettings-networksettings.md) property, then the task will run only if the specified network profile is available.<br/> |
| [**Priority**](tasksettings-priority.md)<br/>                                     | Read/write<br/> | Gets or sets the priority level of the task.<br/>                                                                                                                                                                                                                                                                                                                                                                      |
| [**RestartCount**](tasksettings-restartcount.md)<br/>                             | Read/write<br/> | Gets or sets the number of times that the Task Scheduler will attempt to restart the task.<br/>                                                                                                                                                                                                                                                                                                                        |
| [**RestartInterval**](tasksettings-restartinterval.md)<br/>                       | Read/write<br/> | Gets or sets a value that specifies how long the Task Scheduler will attempt to restart the task.<br/>                                                                                                                                                                                                                                                                                                                 |
| [**RunOnlyIfIdle**](tasksettings-runonlyifidle.md)<br/>                           | Read/write<br/> | Gets or sets a Boolean value that indicates that the Task Scheduler will run the task only if the computer is in an idle state.<br/>                                                                                                                                                                                                                                                                                   |
| [**RunOnlyIfNetworkAvailable**](tasksettings-runonlyifnetworkavailable.md)<br/>   | Read/write<br/> | Gets or sets a Boolean value that indicates that the Task Scheduler will run the task only when a network is available.<br/>                                                                                                                                                                                                                                                                                           |
| [**StartWhenAvailable**](tasksettings-startwhenavailable.md)<br/>                 | Read/write<br/> | Gets or sets a Boolean value that indicates that the Task Scheduler can start the task at any time after its scheduled time has passed.<br/>                                                                                                                                                                                                                                                                           |
| [**StopIfGoingOnBatteries**](tasksettings-stopifgoingonbatteries.md)<br/>         | Read/write<br/> | Gets or sets a Boolean value that indicates that the task will be stopped if the computer begins to run on battery power.<br/>                                                                                                                                                                                                                                                                                         |
| [**WakeToRun**](tasksettings-waketorun.md)<br/>                                   | Read/write<br/> | Gets or sets a Boolean value that indicates that the Task Scheduler will wake the computer when it is time to run the task.<br/>                                                                                                                                                                                                                                                                                       |
| [**XmlText**](tasksettings-xmltext.md)<br/>                                       | Read/write<br/> | Gets or sets an XML-formatted definition of the task settings.<br/>                                                                                                                                                                                                                                                                                                                                                    |



 

## Remarks

By default, a task will be stopped 72 hours after it starts to run. You can change this by changing the [**ExecutionTimeLimit**](tasksettings-executiontimelimit.md) setting.

When reading or writing XML for a task, the task settings are defined in the [**Settings**](taskschedulerschema-settings-tasktype-element.md) element of the Task Scheduler schema.

## Examples

For more information and a code example for this scripting object, see [Time Trigger Example (Scripting)](time-trigger-example--scripting-.md).

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

[**TaskDefinition**](taskdefinition.md)
</dt> <dt>

[**NetworkSettings**](networksettings.md)
</dt> <dt>

[**IdleSettings**](idlesettings.md)
</dt> </dl>

 

