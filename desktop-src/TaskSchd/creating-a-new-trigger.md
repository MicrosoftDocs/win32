---
title: Creating a New Trigger
description: To create a trigger you must use three interfaces.
ms.assetid: 'c0f121ff-d0a5-4b6c-935c-6f47b4ea26d5'
---

# Creating a New Trigger

To create a trigger you must use three interfaces. [**IScheduledWorkItem**](ischeduledworkitem.md) provides the [**IScheduledWorkItem::CreateTrigger**](ischeduledworkitem-createtrigger.md) method for creating the trigger object, [**ITaskTrigger**](itasktrigger.md) provides the [**ITaskTrigger::SetTrigger**](itasktrigger-settrigger.md) method for setting the criteria for the trigger, and the COM interface [**IPersistFile**](_com_ipersistfile) provides a **Save** method for saving the new trigger to disk.

The following procedure describes how to create a new trigger.

**To create a new trigger**

1.  Call [**CoInitialize**](_com_coinitialize) to initialize the COM library and [**CoCreateInstance**](_com_cocreateinstance) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](itaskscheduler-activate.md) to get the [**ITask**](itask.md) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call [**CreateTrigger**](ischeduledworkitem-createtrigger.md) to create a trigger object. (Note that [**CreateTrigger**](ischeduledworkitem-createtrigger.md) is inherited from [**IScheduledWorkItem**](ischeduledworkitem.md).)
4.  Define a [**TASK\_TRIGGER**](task-trigger.md) structure. Note that wBeginDay, wBeginMonth, and wBeginYear members of **TASK\_TRIGGER** must be set to a valid day, month, and year respectively.
5.  Call [**ITaskTrigger::SetTrigger**](itasktrigger-settrigger.md) to set the trigger criteria.
6.  Save the task with the new trigger to disk using [**IPersistFile::Save**](_com_ipersistfile_save). (The [**IPersistFile**](_com_ipersistfile) interface is a standard COM interface supported by the [**ITask**](itask.md) interface.)
7.  Call [**Release**](_com_iunknown_release) to release all resources. (Note that **Release** is an [**IUnknown**](_com_iunknown) method inherited by [**ITask**](itask.md).)



| For a code example of                       | See                                                                                         |
|---------------------------------------------|---------------------------------------------------------------------------------------------|
| Creating a new trigger for an existing task | [C/C++ Code Example: Creating a Task Trigger](c-c-code-example-creating-a-task-trigger.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




