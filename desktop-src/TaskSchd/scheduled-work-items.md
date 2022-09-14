---
title: Scheduled Work Items
description: The Task Scheduler uses two terms to describe what it can schedule work items and tasks.
ms.assetid: 6ca182c3-eba8-43dd-bf2e-27dd972e3cf8
keywords:
- work items Task Scheduler
- work items Task Scheduler , compared to tasks
- tasks Task Scheduler
- tasks Task Scheduler , compared to work items
ms.topic: article
ms.date: 05/31/2018
---

# Scheduled Work Items

The Task Scheduler uses two terms to describe what it can schedule: work items and tasks. Of these two terms, [*work item*](w.md) is a more general term that describes any type of item that can be scheduled. A *work item* can be any item that the Task Scheduler service runs at a time that is specified by the item's trigger(s).

In contrast, a [*task*](t.md) is a specific type of work item. Currently, the only type of scheduled work item that is supported is a task.

The [**IScheduledWorkItem**](/windows/desktop/api/Mstask/nn-mstask-ischeduledworkitem) interface contains methods that are supported by all types of scheduled work items. For example, account information, run times, and application-defined comments are properties that may apply to all types of work items. These properties can be set and retrieved through the **IScheduledWorkItem** interface.

The [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface contains methods that are supported only by tasks.

The methods of the [**IScheduledWorkItem**](/windows/desktop/api/Mstask/nn-mstask-ischeduledworkitem) interface are currently inherited by the [**ITask**](/windows/desktop/api/Mstask/nn-mstask-itask) interface and in the future will be inherited by other work item interfaces.

| For examples of                                              | See                                                                                        |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Creating a new task.                                         | [Creating a Task Using NewWorkItem Example](creating-a-task-using-newworkitem-example.md) |
| Running an existing task.                                    | [Starting a Task Example](starting-a-task-example.md)                                     |
| Retrieving properties that apply to all types of work items. | [Retrieving Work Item Property Examples](retrieving-work-item-property-examples.md)       |
| Setting properties that apply to all types of work items.    | [Setting Work Item Property Examples](setting-work-item-property-examples.md)             |



 

 

 




