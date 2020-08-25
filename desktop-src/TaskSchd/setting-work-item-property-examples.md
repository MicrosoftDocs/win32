---
title: Setting Work Item Property Examples
description: To set the properties of a work item, call ITaskScheduler Activate to retrieve the interface of the work item object, then call the appropriate method to set the task property you are interested in. Currently, the only valid work items are tasks.
ms.assetid: 80a158de-d312-499d-8ff0-b95e794cf169
keywords:
- setting work item properties Task Scheduler
ms.topic: article
ms.date: 05/31/2018
---

# Setting Work Item Property Examples

To set the properties of a work item, call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to retrieve the interface of the work item object, then call the appropriate method to set the task property you are interested in. Currently, the only valid work items are tasks.

The code examples listed at the bottom of the page show how to set the properties that apply to all work items. For other properties that are unique to tasks, see [Setting Task Property Examples](setting-task-property-examples.md).

> [!Note]  
> In the following code example, all interfaces are released after they are no longer needed.

 

In the following examples, the modified object is always saved to disk by a call to [**IPersistFile::Save**](/windows/win32/api/objidl/nf-objidl-ipersistfile-save). (The [**IPersistFile**](/windows/win32/api/objidl/nn-objidl-ipersistfile) interface is a standard COM interface inherited by the task object.)

The following procedure describes how to set a task property.

**To set a task property**

1.  Call [**CoInitialize**](/windows/win32/api/objbase/nf-objbase-coinitialize) to initialize the COM library and [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to get a Task Scheduler object. (These examples assume that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to get the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface of the task object. (Note that tasks are currently the only valid type of work item.)
3.  Call the appropriate [**IScheduledWorkItem**](/windows/desktop/api/Mstask/nn-mstask-ischeduledworkitem) method to set the property you are interested in. Note that **IScheduledWorkItem** methods are inherited by the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface.
4.  Call [**IPersistFile::Save**](/windows/win32/api/objidl/nf-objidl-ipersistfile-save) to store the modified task object to disk.



| For a code example of                            | See                                                                                                           |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Setting the account information for a known task | [C/C++ Code Example: Setting Task Account Information](c-c-code-example-setting-task-account-information.md) |
| Setting the comment of a known task              | [C/C++ Code Example: Setting Task Comment](c-c-code-example-setting-task-comment.md)                         |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 