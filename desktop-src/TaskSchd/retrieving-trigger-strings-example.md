---
title: Retrieving Trigger Strings Example
description: You can retrieve the trigger strings of a known trigger using the IScheduledWorkItem or ITaskTrigger interface, depending on the type of object you are working with.
ms.assetid: adfa95b1-54f0-4bcd-a260-ca76fd77d43e
keywords:
- retrieving trigger strings Task Scheduler
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Trigger Strings Example

You can retrieve the trigger strings of a known trigger using the [**IScheduledWorkItem**](/windows/desktop/api/Mstask/nn-mstask-ischeduledworkitem) or [**ITaskTrigger**](/windows/desktop/api/Mstask/nn-mstask-itasktrigger) interface, depending on the type of object you are working with.

When working with a [*task object*](t.md), use the methods of the [**IScheduledWorkItem**](/windows/desktop/api/Mstask/nn-mstask-ischeduledworkitem) interface to retrieve the trigger strings of a work item.

When you are working with a [*task trigger object*](t.md), use the methods of the [**ITaskTrigger**](/windows/desktop/api/Mstask/nn-mstask-itasktrigger) interface to retrieve the trigger string of the trigger.

The following example shows how to use [**IScheduledWorkItem::GetTriggerString**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-gettriggerstring) to display the strings of all triggers associated with a known task.

The following procedure describes how to retrieve the trigger strings of a task.

**To retrieve the trigger strings of a task**

1.  Call [**CoInitialize**](https://msdn.microsoft.com/en-us/library/ms678543(v=VS.85).aspx) to initialize the COM library and [**CoCreateInstance**](https://msdn.microsoft.com/en-us/library/ms686615(v=VS.85).aspx) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to get the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call **ITask::GetTriggerCount** to find out how many triggers are associated with a task. (Note that [**GetTriggerCount**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-gettriggercount) is an [**IScheduledWorkItem**](/windows/desktop/api/Mstask/nn-mstask-ischeduledworkitem) method inherited by [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask).)
4.  Display the trigger strings, calling **ITask::GetTriggerString** for each trigger associated with the task. (Note that [**GetTriggerString**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-gettriggerstring) is an [**IScheduledWorkItem**](/windows/desktop/api/Mstask/nn-mstask-ischeduledworkitem) method inherited by [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask).)
5.  Release all resources. Call [**CoTaskMemFree**](https://msdn.microsoft.com/en-us/library/ms680722(v=VS.85).aspx) to release the trigger strings and **ITask::Release** to release the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface. (Note that [**Release**](https://msdn.microsoft.com/en-us/library/ms682317(v=VS.85).aspx) is an [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) method inherited by **ITask**.)



| For a code example of                                                         | See                                                                                         |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Retrieving a trigger string for all the triggers associated with a known task | [Code Example: Retrieving Trigger Strings](c-c-code-example-retrieving-trigger-strings.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




