---
title: Starting a Task Example
description: To start a task, call the Run method of the ITask interface. Run is an asynchronous method that attempts to execute the task and returns as soon as the task has started. The Task Scheduler service must be running for this method to succeed.
ms.assetid: 90f197de-7a32-4e4b-b4c0-d3f706e47de1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Starting a Task Example

To start a task, call the [**Run**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-run?branch=master) method of the [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master) interface. **Run** is an asynchronous method that attempts to execute the task and returns as soon as the task has started. The Task Scheduler service must be running for this method to succeed.

The following procedure describes how to start a task.

**To start a task**

1.  Call [**CoInitialize**](_com_coinitialize) to initialize the COM library and [**CoCreateInstance**](_com_cocreateinstance) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/win32/Mstask/nf-mstask-itaskscheduler-activate?branch=master) to get the [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call [**Run**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-run?branch=master) to start the task. Note that this method is inherited by the [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master) interface.
4.  Continue processing as needed.
5.  Call **ITask::Release** to free resources and [**CoUninitialize**](_com_couninitialize) to uninitialize COM. This example calls [**Release**](_com_iunknown_release) to free the pointer to the [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master) interface. (Note that **Release** is an [**IUnknown**](_com_iunknown) method inherited by **ITask**.)



| For a code example of    | See                                                                         |
|--------------------------|-----------------------------------------------------------------------------|
| Running an existing task | [C/C++ Code Example: Starting a Task](c-c-code-example-starting-a-task.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




