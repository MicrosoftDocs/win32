---
title: Data (taskType) Element
description: Defines addition data that is associated with the task, but is otherwise unused by the Task Scheduler service.
ms.assetid: 296cd33d-5f82-4de7-84a7-e791619ad0b5
keywords:
- Data element Task Scheduler
topic_type:
- apiref
api_name:
- Data
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Data (taskType) Element

Defines addition data that is associated with the task, but is otherwise unused by the Task Scheduler service.

``` syntax
<xs:element name="Data"
    type="dataType"
 />
```

The **Data** element is defined by the [**taskType**](taskschedulerschema-tasktype-complextype.md) complex type.

## Parent element



| Element                                          | Derived from                                                 | Description                                                                  |
|--------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------------------------|
| [**Task**](taskschedulerschema-task-element.md) | [**taskType**](taskschedulerschema-tasktype-complextype.md) | Defines the task that is performed by the Task Scheduler service.<br/> |



## Remarks

As an example of this type of data, the Performance Logs and Alerts service uses this property as a storage container for the perf counter query associated with a task.

For C++ development, the data of a task is specified using the [**Data property of ITaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_data).

In scripting development, the data of a task is specified using the [**TaskDefinition.Data**](taskdefinition-data.md) property.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





