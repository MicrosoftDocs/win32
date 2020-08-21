---
title: Retrieving a Task Page Example
description: To retrieve a task page you must call ITask QueryInterface to retrieve the IProvideTaskPage interface, then call IProvideTaskPage GetPage. The GetPage method returns a handle to the page, which can then be used to display the page you requested.
ms.assetid: 97525419-c480-465a-97c6-e701043c0af2
keywords:
- retrieving task page Task Scheduler
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving a Task Page Example

To retrieve a task page you must call **ITask::QueryInterface** to retrieve the [**IProvideTaskPage**](/windows/desktop/api/Mstask/nn-mstask-iprovidetaskpage) interface, then call [**IProvideTaskPage::GetPage**](/windows/desktop/api/Mstask/nf-mstask-iprovidetaskpage-getpage). The **GetPage** method returns a handle to the page, which can then be used to display the page you requested.

> [!Note]  
> In the following code example, all interfaces are released after they are no longer needed.

 

The following procedure describes how to create a new trigger.

**To create a new trigger**

1.  Call [**CoInitialize**](/windows/win32/api/objbase/nf-objbase-coinitialize) to initialize the COM library and [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/desktop/api/Mstask/nf-mstask-itaskscheduler-activate) to get the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call **ITask::QueryInterface** to retrieve the [**IProvideTaskPage**](/windows/desktop/api/Mstask/nn-mstask-iprovidetaskpage) interface and [**IProvideTaskPage::GetPage**](/windows/desktop/api/Mstask/nf-mstask-iprovidetaskpage-getpage) to retrieve the page.
4.  Using the returned page handle, display the page.



| For a code example of                                   | See                                                                   |
|---------------------------------------------------------|-----------------------------------------------------------------------|
| Retrieving and displaying the Task page of a known task | [Retrieving a Task Page](c-c-code-example-retrieving-a-task-page.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 