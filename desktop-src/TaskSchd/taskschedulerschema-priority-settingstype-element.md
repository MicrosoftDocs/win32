---
title: Priority (settingsType) Element
description: Specifies the priority level for the task.
ms.assetid: 4885fffa-b7d9-4f5e-b6e8-6f18b01c2427
keywords:
- Priority element Task Scheduler
topic_type:
- apiref
api_name:
- Priority
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Priority (settingsType) Element

Specifies the priority level for the task.

``` syntax
<xs:element name="Priority"
    type="priorityType"
    default="7"
    minOccurs="0"
 />
```

The **Priority** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                           | Derived from                                                         | Description                                                                        |
|-------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**Settings**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Contains the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

Priority level 0 is the highest priority, and priority level 10 is the lowest priority. The default value is 7. The minimum and maximum values are set by the [**priorityType**](taskschedulerschema-prioritytype-simpletype.md) simple type. Priority levels 7 and 8 are used for background tasks, and priority levels 4, 5, and 6 are used for interactive tasks.

The task's action is started in a process with a priority that is based on a Priority Class value. A Priority Level value (thread priority) is used for COM handler, message box, and email task actions. For more information about the Priority Class and Priority Level values, see [Scheduling Priorities](/windows/desktop/ProcThread/scheduling-priorities). The following table lists the possible values for the **Priority** element, and the corresponding Priority Class and Priority Level values.



| Task Priority | Priority Class                 | Priority Level                   |
|---------------|--------------------------------|----------------------------------|
| 0             | REALTIME\_PRIORITY\_CLASS      | THREAD\_PRIORITY\_TIME\_CRITICAL |
| 1             | HIGH\_PRIORITY\_CLASS          | THREAD\_PRIORITY\_HIGHEST        |
| 2             | ABOVE\_NORMAL\_PRIORITY\_CLASS | THREAD\_PRIORITY\_ABOVE\_NORMAL  |
| 3             | ABOVE\_NORMAL\_PRIORITY\_CLASS | THREAD\_PRIORITY\_ABOVE\_NORMAL  |
| 4             | NORMAL\_PRIORITY\_CLASS        | THREAD\_PRIORITY\_NORMAL         |
| 5             | NORMAL\_PRIORITY\_CLASS        | THREAD\_PRIORITY\_NORMAL         |
| 6             | NORMAL\_PRIORITY\_CLASS        | THREAD\_PRIORITY\_NORMAL         |
| 7             | BELOW\_NORMAL\_PRIORITY\_CLASS | THREAD\_PRIORITY\_BELOW\_NORMAL  |
| 8             | BELOW\_NORMAL\_PRIORITY\_CLASS | THREAD\_PRIORITY\_BELOW\_NORMAL  |
| 9             | IDLE\_PRIORITY\_CLASS          | THREAD\_PRIORITY\_LOWEST         |
| 10            | IDLE\_PRIORITY\_CLASS          | THREAD\_PRIORITY\_IDLE           |



 

For C++ development, see [**Priority Property of ITaskSettings**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_priority).

For script development, see [**TaskSettings.Priority**](tasksettings-priority.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> </dl>

 

