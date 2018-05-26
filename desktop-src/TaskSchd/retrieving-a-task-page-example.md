---
title: Retrieving a Task Page Example
description: To retrieve a task page you must call ITask QueryInterface to retrieve the IProvideTaskPage interface, then call IProvideTaskPage GetPage. The GetPage method returns a handle to the page, which can then be used to display the page you requested.
ms.assetid: 97525419-c480-465a-97c6-e701043c0af2
keywords:
- retrieving task page Task Scheduler
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving a Task Page Example

To retrieve a task page you must call **ITask::QueryInterface** to retrieve the [**IProvideTaskPage**](/windows/win32/Mstask/nn-mstask-iprovidetaskpage?branch=master) interface, then call [**IProvideTaskPage::GetPage**](/windows/win32/Mstask/nf-mstask-iprovidetaskpage-getpage?branch=master). The **GetPage** method returns a handle to the page, which can then be used to display the page you requested.

> [!Note]  
> In the following code example, all interfaces are released after they are no longer needed.

 

The following procedure describes how to create a new trigger.

**To create a new trigger**

1.  Call [**CoInitialize**](_com_coinitialize) to initialize the COM library and [**CoCreateInstance**](_com_cocreateinstance) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Activate**](/windows/win32/Mstask/nf-mstask-itaskscheduler-activate?branch=master) to get the [**ITask**](/windows/win32/Mstask/nn-mstask-itask?branch=master) interface of the task object. (Note that this example gets the "Test Task" task.)
3.  Call **ITask::QueryInterface** to retrieve the [**IProvideTaskPage**](/windows/win32/Mstask/nn-mstask-iprovidetaskpage?branch=master) interface and [**IProvideTaskPage::GetPage**](/windows/win32/Mstask/nf-mstask-iprovidetaskpage-getpage?branch=master) to retrieve the page.
4.  Using the returned page handle, display the page.



| For a code example of                                   | See                                                                   |
|---------------------------------------------------------|-----------------------------------------------------------------------|
| Retrieving and displaying the Task page of a known task | [Retrieving a Task Page](c-c-code-example-retrieving-a-task-page.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




