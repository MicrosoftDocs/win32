---
title: Creating an Idle Trigger Example
description: To create an idle trigger, you must specify an idle trigger when you create the trigger, and you must set the idle time for the task. For information about idle conditions, see Task Idle Conditions.
ms.assetid: d36a621c-4011-4c3d-b6f4-b56d1f50983c
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Idle Trigger Example

To create an idle trigger, you must specify an idle trigger when you create the trigger, and you must set the idle time for the task. For information about idle conditions, see [Task Idle Conditions](task-idle-conditions.md).

After creating the idle trigger, call [**IPersistFile::Save**](da9581e8-98c7-4592-8ee1-a1bc8232635b) to save the new trigger to disk.

The following procedure describes how to create an idle trigger for a known task.

**To create an idle trigger for a known task**

1.  Call [**CoInitialize**](0f171cf4-87b9-43a6-97f2-80ed344fe376) to initialize the COM library and [**CoCreateInstance**](7295a55b-12c7-4ed0-a7a4-9ecee16afdec) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to get the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call [**SetIdleWait**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-setidlewait) to set how long the system must remain idle before the trigger will fire. (Note that **SetIdleWait** is inherited from [**IScheduledWorkItem**](/windows/desktop/api/Mstask/nn-mstask-ischeduledworkitem).)
4.  Define the [**TASK\_TRIGGER**](/windows/desktop/api/Mstask/ns-mstask-_task_trigger) structure and call [**CreateTrigger**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-createtrigger) to create the idle trigger. (Note that **CreateTrigger** is inherited from [**IScheduledWorkItem**](/windows/desktop/api/Mstask/nn-mstask-ischeduledworkitem).)
5.  Save the task with the new idle trigger to disk using [**IPersistFile::Save**](da9581e8-98c7-4592-8ee1-a1bc8232635b). (The [**IPersistFile**](7d34507f-8a16-43b4-8225-010798abc546) interface is a standard COM interface supported by the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface.)
6.  Call **ITask::Release** to release all resources. (Note that [**Release**](4b494c6f-f0ee-4c35-ae45-ed956f40dc7a) is an [**IUnknown**](33f1d79a-33fc-4ce5-a372-e08bda378332) method inherited by [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask).)



| For a code example of                         | See                                                                                           |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------|
| Creating an idle trigger for an existing task | [C/C++ Code Example: Creating an Idle Trigger](c-c-code-example-creating-an-idle-trigger.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




