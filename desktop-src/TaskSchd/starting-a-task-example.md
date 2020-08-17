---
title: Starting a Task Example
description: To start a task, call the Run method of the ITask interface. Run is an asynchronous method that attempts to execute the task and returns as soon as the task has started. The Task Scheduler service must be running for this method to succeed.
ms.assetid: 90f197de-7a32-4e4b-b4c0-d3f706e47de1
ms.topic: article
ms.date: 05/31/2018
---

# Starting a Task Example

To start a task, call the [**Run**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-run) method of the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface. **Run** is an asynchronous method that attempts to execute the task and returns as soon as the task has started. The Task Scheduler service must be running for this method to succeed.

The following procedure describes how to start a task.

**To start a task**

1.  Call [**CoInitialize**](/windows/win32/api/objbase/nf-objbase-coinitialize) to initialize the COM library and [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to get the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call [**Run**](/windows/desktop/api/Mstask/nf-mstask-ischeduledworkitem-run) to start the task. Note that this method is inherited by the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface.
4.  Continue processing as needed.
5.  Call **ITask::Release** to free resources and [**CoUninitialize**](/windows/win32/api/combaseapi/nf-combaseapi-couninitialize) to uninitialize COM. This example calls [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) to free the pointer to the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface. (Note that **Release** is an [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) method inherited by **ITask**.)



| For a code example of    | See                                                                         |
|--------------------------|-----------------------------------------------------------------------------|
| Running an existing task | [C/C++ Code Example: Starting a Task](c-c-code-example-starting-a-task.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 