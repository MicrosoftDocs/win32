---
title: Creating a New Trigger
description: To create a trigger you must use three interfaces.
ms.assetid: c0f121ff-d0a5-4b6c-935c-6f47b4ea26d5
ms.topic: article
ms.date: 05/31/2018
---

# Creating a New Trigger

To create a trigger you must use three interfaces. [**IScheduledWorkItem**](/windows/desktop/api/Mstask/nn-mstask-ischeduledworkitem) provides the [**IScheduledWorkItem::CreateTrigger**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-createtrigger) method for creating the trigger object, [**ITaskTrigger**](/windows/desktop/api/Mstask/nn-mstask-itasktrigger) provides the [**ITaskTrigger::SetTrigger**](/windows/desktop/api/Mstask/nf-mstask-itasktrigger-settrigger) method for setting the criteria for the trigger, and the COM interface [**IPersistFile**](https://msdn.microsoft.com/en-us/library/ms687223(v=VS.85).aspx) provides a **Save** method for saving the new trigger to disk.

The following procedure describes how to create a new trigger.

**To create a new trigger**

1.  Call [**CoInitialize**](https://msdn.microsoft.com/en-us/library/ms678543(v=VS.85).aspx) to initialize the COM library and [**CoCreateInstance**](https://msdn.microsoft.com/en-us/library/ms686615(v=VS.85).aspx) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to get the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call [**CreateTrigger**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-createtrigger) to create a trigger object. (Note that [**CreateTrigger**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-createtrigger) is inherited from [**IScheduledWorkItem**](/windows/desktop/api/Mstask/nn-mstask-ischeduledworkitem).)
4.  Define a [**TASK\_TRIGGER**](/windows/desktop/api/Mstask/ns-mstask-_task_trigger) structure. Note that wBeginDay, wBeginMonth, and wBeginYear members of **TASK\_TRIGGER** must be set to a valid day, month, and year respectively.
5.  Call [**ITaskTrigger::SetTrigger**](/windows/desktop/api/Mstask/nf-mstask-itasktrigger-settrigger) to set the trigger criteria.
6.  Save the task with the new trigger to disk using [**IPersistFile::Save**](https://msdn.microsoft.com/en-us/library/ms693701(v=VS.85).aspx). (The [**IPersistFile**](https://msdn.microsoft.com/en-us/library/ms687223(v=VS.85).aspx) interface is a standard COM interface supported by the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface.)
7.  Call [**Release**](https://msdn.microsoft.com/en-us/library/ms682317(v=VS.85).aspx) to release all resources. (Note that **Release** is an [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) method inherited by [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask).)



| For a code example of                       | See                                                                                         |
|---------------------------------------------|---------------------------------------------------------------------------------------------|
| Creating a new trigger for an existing task | [C/C++ Code Example: Creating a Task Trigger](c-c-code-example-creating-a-task-trigger.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




