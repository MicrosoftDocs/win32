---
title: Retrieving Work Item Property Examples
description: To retrieve the properties of a work item, call ITaskScheduler Activate to retrieve the interface of the work item object, then call the appropriate method to retrieve the task property you are interested in.
ms.assetid: d9723dea-1a82-4993-b4d0-bc7d944e775f
keywords:
- retrieving work item properties Task Scheduler
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Work Item Property Examples

To retrieve the properties of a work item, call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to retrieve the interface of the work item object, then call the appropriate method to retrieve the task property you are interested in. Currently, the only valid work items are tasks.

The code examples listed at the bottom of this page show how to retrieve the properties that apply to all work items. For other properties that are unique to tasks, see [Setting Task Property Examples](setting-task-property-examples.md).

> [!Note]  
> In the following code example, all interfaces are released after they are no longer needed.

 

Note that if you are retrieving a string property (such as comment for a work item), you must call [**CoTaskMemFree**](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemfree) to free the memory allocated for the returned string.

The following procedure describes how to retrieve a task property.

**To retrieve a task property**

1.  Call [**CoInitialize**](/windows/win32/api/objbase/nf-objbase-coinitialize) to initialize the COM library and [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to get a Task Scheduler object. (These examples assume that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to get the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface of the task object. (Note that tasks are currently the only valid type of work item.)
3.  Call the appropriate method to retrieve the property you are interested in.
4.  Process the property as needed. (These examples simply print the property to the screen.)
5.  If the returned property is a string, call [**CoTaskMemFree**](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemfree) to free the memory allocated for the returned string.



| For a code example of                                                                        | See                                                                                                                       |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Retrieving the account information of a known task                                           | [C/C++ Code Example: Retrieving Task Account Information](c-c-code-example-retrieving-task-account-information.md)       |
| Retrieving the comment string of a known task                                                | [C/C++ Code Example: Retrieving a Task Comment](c-c-code-example-retrieving-a-task-comment.md)                           |
| Retrieving the name of the creator of the task and displaying it on the screen               | [C/C++ Code Example: Retrieving the Task Creator](c-c-code-example-retrieving-the-task-creator.md)                       |
| Retrieving the last exit code returned by a known task                                       | [C/C++ Code Example: Retrieving Task Exit Code](c-c-code-example-retrieving-task-exit-code.md)                           |
| Retrieving the idle-wait time of the task and displaying it on the screen                    | [C/C++ Code Example: Retrieving Task Idle-wait Time](c-c-code-example-retrieving-task-idle-wait-time.md)                 |
| Retrieving the time the task was last run and displaying it on the screen                    | [C/C++ Code Example: Retrieving the Task MostRecentRun Time](c-c-code-example-retrieving-the-task-mostrecentrun-time.md) |
| Retrieving the next time the task is scheduled to run and displaying that time on the screen | [C/C++ Code Example: Retrieving the Task NextRun Time](c-c-code-example-retrieving-the-task-nextrun-time.md)             |
| Retrieving the run times of the task and displaying them on the screen                       | [C/C++ Code Example: Retrieving Task Run Times](c-c-code-example-retrieving-task-run-times.md)                           |
| Retrieving the current status of the task and displaying it on the screen                    | [C/C++ Code Example: Retrieving Task Status](c-c-code-example-retrieving-task-status.md)                                 |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 