---
title: Setting Task Property Examples
description: To set the properties of a task, call ITaskScheduler Activate to retrieve the interface of the task object, then call the appropriate ITask method to set the task property you are interested in.
ms.assetid: df438bff-1ce1-4336-93ee-1e6cab1f1ddd
keywords:
- setting task properties Task Scheduler
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Setting Task Property Examples

To set the properties of a task, call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to retrieve the interface of the task object, then call the appropriate [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) method to set the task property you are interested in.

The code examples listed at the bottom of the page show how to set the properties that are unique to task objects. For other [*work item*](w.md) properties that also apply to tasks, see [Setting Work Item Property Examples](setting-work-item-property-examples.md).

> [!Note]  
> In the following code example, all interfaces are released after they are no longer needed.

 

In the following examples, the modified task object is always saved to disk by a call to [**IPersistFile::Save**](da9581e8-98c7-4592-8ee1-a1bc8232635b). (The [**IPersistFile**](7d34507f-8a16-43b4-8225-010798abc546) interface is a standard COM interface inherited by the task object.)

The following procedure describes how to set a task property.

**To set a task property**

1.  Call [**CoInitialize**](0f171cf4-87b9-43a6-97f2-80ed344fe376) to initialize the COM library and [**CoCreateInstance**](7295a55b-12c7-4ed0-a7a4-9ecee16afdec) to get a Task Scheduler object. (These examples assume that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to get the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call the appropriate [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) method to set the property you are interested in.
4.  Call [**IPersistFile::Save**](da9581e8-98c7-4592-8ee1-a1bc8232635b) to store the modified task object to disk.



| For a code example of                                                                                                                                | See                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Setting the name of the application associated with a known task                                                                                     | [C/C++ Code Example: Setting Application Name](c-c-code-example-setting-application-name.md)   |
| Setting the maximum run time of a known task                                                                                                         | [C/C++ Code Example: Setting MaxRunTime](c-c-code-example-setting-maxruntime.md)               |
| Clearing all command-line parameters associated with a known task                                                                                    | [C/C++ Code Example: Setting Task Parameters](c-c-code-example-setting-task-parameters.md)     |
| This example sets the priority of a test task and then saves the task. This example assumes that the test task already exists on the local computer. | [C/C++ Code Example: Setting Task Priority](c-c-code-example-setting-task-priority.md)         |
| Setting the [*working directory*](w.md) of a known task                                                                  | [C/C++ Code Example: Setting Working Directory](c-c-code-example-setting-working-directory.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




