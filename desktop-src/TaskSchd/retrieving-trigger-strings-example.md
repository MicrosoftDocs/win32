---
title: Retrieving Trigger Strings Example
description: You can retrieve the trigger strings of a known trigger using the IScheduledWorkItem or ITaskTrigger interface, depending on the type of object you are working with.
ms.assetid: 'adfa95b1-54f0-4bcd-a260-ca76fd77d43e'
keywords: ["retrieving trigger strings Task Scheduler"]
---

# Retrieving Trigger Strings Example

You can retrieve the trigger strings of a known trigger using the [**IScheduledWorkItem**](ischeduledworkitem.md) or [**ITaskTrigger**](itasktrigger.md) interface, depending on the type of object you are working with.

When working with a [*task object*](t.md#-msb-task-objects-gly), use the methods of the [**IScheduledWorkItem**](ischeduledworkitem.md) interface to retrieve the trigger strings of a work item.

When you are working with a [*task trigger object*](t.md#-msb-task-trigger-objects-gly), use the methods of the [**ITaskTrigger**](itasktrigger.md) interface to retrieve the trigger string of the trigger.

The following example shows how to use [**IScheduledWorkItem::GetTriggerString**](ischeduledworkitem-gettriggerstring.md) to display the strings of all triggers associated with a known task.

The following procedure describes how to retrieve the trigger strings of a task.

**To retrieve the trigger strings of a task**

1.  Call [**CoInitialize**](_com_coinitialize) to initialize the COM library and [**CoCreateInstance**](_com_cocreateinstance) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](itaskscheduler-activate.md) to get the [**ITask**](itask.md) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call **ITask::GetTriggerCount** to find out how many triggers are associated with a task. (Note that [**GetTriggerCount**](ischeduledworkitem-gettriggercount.md) is an [**IScheduledWorkItem**](ischeduledworkitem.md) method inherited by [**ITask**](itask.md).)
4.  Display the trigger strings, calling **ITask::GetTriggerString** for each trigger associated with the task. (Note that [**GetTriggerString**](ischeduledworkitem-gettriggerstring.md) is an [**IScheduledWorkItem**](ischeduledworkitem.md) method inherited by [**ITask**](itask.md).)
5.  Release all resources. Call [**CoTaskMemFree**](_com_cotaskmemfree) to release the trigger strings and **ITask::Release** to release the [**ITask**](itask.md) interface. (Note that [**Release**](_com_iunknown_release) is an [**IUnknown**](_com_iunknown) method inherited by **ITask**.)



| For a code example of                                                         | See                                                                                         |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Retrieving a trigger string for all the triggers associated with a known task | [Code Example: Retrieving Trigger Strings](c-c-code-example-retrieving-trigger-strings.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




