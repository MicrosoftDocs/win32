---
title: Editing a Work Item using Property Pages
description: You can edit the properties of a work item by using the graphic user interface provided by the Task Scheduler Service.
ms.assetid: 2d7992ce-fa70-41cc-a8e7-74687171537f
keywords:
- editing work items Task Scheduler
ms.topic: article
ms.date: 05/31/2018
---

# Editing a Work Item using Property Pages

You can edit the properties of a work item by using the graphic user interface provided by the Task Scheduler Service. (Currently, the only valid work items are tasks.)

The following procedure describes how to edit a task using its property pages.

**To edit a task using its property pages**

1.  Call [**CoInitialize**](/windows/win32/api/objbase/nf-objbase-coinitialize) to initialize the COM library and [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to get a Task Scheduler object. (These examples assume that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to get the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface of the task object. (Note that tasks are currently the only valid type of work item.)
3.  Call [**IScheduledWorkItem::EditWorkItem**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-editworkitem) to display the property pages for the task.
4.  Edit the properties of the task as needed, then click OK to accept the new values and remove the displayed property pages.



| For a code example of                                                                                      | See                                                                                 |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Displaying the property pages for a known task and allowing a user to edit the properties of the work item | [C/C++ Code Example: Editing a Work Item](c-c-code-example-editing-a-work-item.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 