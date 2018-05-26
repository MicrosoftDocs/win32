---
title: Creating a New Trigger
description: To create a trigger you must use three interfaces.
ms.assetid: c0f121ff-d0a5-4b6c-935c-6f47b4ea26d5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating a New Trigger

To create a trigger you must use three interfaces. [**IScheduledWorkItem**](/windows/win32/Mstask/nn-mstask-ischeduledworkitem?branch=master) provides the [**IScheduledWorkItem::CreateTrigger**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-createtrigger?branch=master) method for creating the trigger object, [**ITaskTrigger**](/windows/win32/Mstask/nn-mstask-itasktrigger?branch=master) provides the [**ITaskTrigger::SetTrigger**](/windows/win32/Mstask/nf-mstask-itasktrigger-settrigger?branch=master) method for setting the criteria for the trigger, and the COM interface [**IPersistFile**](_com_ipersistfile) provides a **Save** method for saving the new trigger to disk.

The following procedure describes how to create a new trigger.

**To create a new trigger**

1.  Call [**CoInitialize**](_com_coinitialize) to initialize the COM library and [**CoCreateInstance**](_com_cocreateinstance) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/win32/Mstask/nf-mstask-itaskscheduler-activate?branch=master) to get the [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call [**CreateTrigger**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-createtrigger?branch=master) to create a trigger object. (Note that [**CreateTrigger**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-createtrigger?branch=master) is inherited from [**IScheduledWorkItem**](/windows/win32/Mstask/nn-mstask-ischeduledworkitem?branch=master).)
4.  Define a [**TASK\_TRIGGER**](/windows/win32/Mstask/ns-mstask-_task_trigger?branch=master) structure. Note that wBeginDay, wBeginMonth, and wBeginYear members of **TASK\_TRIGGER** must be set to a valid day, month, and year respectively.
5.  Call [**ITaskTrigger::SetTrigger**](/windows/win32/Mstask/nf-mstask-itasktrigger-settrigger?branch=master) to set the trigger criteria.
6.  Save the task with the new trigger to disk using [**IPersistFile::Save**](_com_ipersistfile_save). (The [**IPersistFile**](_com_ipersistfile) interface is a standard COM interface supported by the [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master) interface.)
7.  Call [**Release**](_com_iunknown_release) to release all resources. (Note that **Release** is an [**IUnknown**](_com_iunknown) method inherited by [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master).)



| For a code example of                       | See                                                                                         |
|---------------------------------------------|---------------------------------------------------------------------------------------------|
| Creating a new trigger for an existing task | [C/C++ Code Example: Creating a Task Trigger](c-c-code-example-creating-a-task-trigger.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




