---
title: Editing a Work Item using Property Pages
description: You can edit the properties of a work item by using the graphic user interface provided by the Task Scheduler Service.
ms.assetid: '2d7992ce-fa70-41cc-a8e7-74687171537f'
keywords: ["editing work items Task Scheduler"]
---

# Editing a Work Item using Property Pages

You can edit the properties of a work item by using the graphic user interface provided by the Task Scheduler Service. (Currently, the only valid work items are tasks.)

The following procedure describes how to edit a task using its property pages.

**To edit a task using its property pages**

1.  Call [**CoInitialize**](_com_coinitialize) to initialize the COM library and [**CoCreateInstance**](_com_cocreateinstance) to get a Task Scheduler object. (These examples assume that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](itaskscheduler-activate.md) to get the [**ITask**](itask.md) interface of the task object. (Note that tasks are currently the only valid type of work item.)
3.  Call [**IScheduledWorkItem::EditWorkItem**](ischeduledworkitem-editworkitem.md) to display the property pages for the task.
4.  Edit the properties of the task as needed, then click OK to accept the new values and remove the displayed property pages.



| For a code example of                                                                                      | See                                                                                 |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Displaying the property pages for a known task and allowing a user to edit the properties of the work item | [C/C++ Code Example: Editing a Work Item](c-c-code-example-editing-a-work-item.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




