---
title: Retrieving Task Property Examples
description: To retrieve the properties of a task, call ITaskScheduler Activate to get retrieve the interface of the task object, then call the appropriate ITask method to retrieve the task property that you are interested in.
ms.assetid: 9ec9d836-c735-4a32-96b1-3dbd0a31b22a
keywords:
- retrieving task properties Task Scheduler
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Task Property Examples

To retrieve the properties of a task, call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to get retrieve the interface of the task object, then call the appropriate [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) method to retrieve the task property that you are interested in. The code examples listed at the bottom of the page show how to retrieve the different task properties.

The code examples listed at the bottom of the page show how to retrieve the properties that are unique to task objects. For other [*work item*](w.md) properties that also apply to tasks, see [Retrieving Work Item Examples](retrieving-work-item-property-examples.md).

> [!Note]  
> In the following code example, all interfaces are released after they are no longer needed.

 

Note that if you are retrieving a string property (such as the application name, parameters, or working directory), you must call [CoTaskMemFree](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemfree) to free the memory allocated for the returned string.

The following procedure describes how to retrieve a task property.

**To retrieve a task property**

1.  Call [**CoInitialize**](/windows/win32/api/objbase/nf-objbase-coinitialize) to initialize the COM library and [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to get a Task Scheduler object. (These examples assume that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to get the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call the appropriate [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) method to retrieve the property you are interested in.
4.  Process the property as needed. (These examples print the property to the screen.)
5.  If the returned property is a string, call [CoTaskMemFree](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemfree) to free the memory allocated for the returned string.



| For a code example of                                                                                                                           | See                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Retrieving the name of the application associated with a given task                                                                             | [C/C++ Code Example: Retrieving the Task Application Name](c-c-code-example-retrieving-the-task-application-name.md)   |
| Retrieving the maximum amount of time the task can run and displaying that number on the screen                                                 | [C/C++ Code Example: Retrieving the Task MaxRunTime](c-c-code-example-retrieving-the-task-maxruntime.md)               |
| Retrieving the parameter string that is executed when the task is run and displaying that string on the screen                                  | [C/C++ Code Example: Retrieving Task Parameters](c-c-code-example-retrieving-task-parameters.md)                       |
| Retrieving the [*priority level*](p.md) of the task                                                                    | [C/C++ Code Example: Retrieving Task Priority](c-c-code-example-retrieving-task-priority.md)                           |
| Retrieving the [*working directory*](w.md) of a task and displaying the path to the working directory on the screen | [C/C++ Code Example: Retrieving the Task Working Directory](c-c-code-example-retrieving-the-task-working-directory.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 