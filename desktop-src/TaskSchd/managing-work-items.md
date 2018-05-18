---
title: Manipulating Work Items
description: The IScheduledWorkItem interface provides methods for retrieving and setting work item properties; creating, retrieving, and deleting triggers for work items (setting the trigger must be done with the ITaskTrigger SetTrigger method); and for running, terminating, and deleting the work item.Note  For the properties of a specific type of work item, refer to the interface for that type of object. For example, you cannot set the priority level of a work item; however, you can use the methods of the ITask interface to retrieve and set the priority of a task.�
ms.assetid: '8aedf96d-e43d-4aac-ad8c-860379209f95'
keywords: ["work items Task Scheduler , managing"]
---

# Manipulating Work Items

The [**IScheduledWorkItem**](ischeduledworkitem.md) interface provides methods for retrieving and setting work item properties; creating, retrieving, and deleting triggers for work items (setting the trigger must be done with the [**ITaskTrigger::SetTrigger**](itasktrigger-settrigger.md) method); and for running, terminating, and deleting the work item.

> [!Note]  
> For the properties of a specific type of work item, refer to the interface for that type of object. For example, you cannot set the priority level of a work item; however, you can use the methods of the [**ITask**](itask.md) interface to retrieve and set the priority of a task.

 

Whenever you modify a work item, you must call the [**IPersistFile::Save**](_com_ipersistfile_save) object to save the modified work item to disk. The [**IPersistFile**](_com_ipersistfile) interface is a standard COM interface that is supported by the [**ITask**](itask.md) interface.

| For examples of                                                            | See                                                                                  |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Retrieving properties that apply to all types of work items                | [Retrieving Work Item Property Examples](retrieving-work-item-property-examples.md) |
| Setting properties that apply to all types of work items                   | [Setting Work Item Property Examples](setting-work-item-property-examples.md)       |
| Running a known task                                                       | [Starting a Task Example](starting-a-task-example.md)                               |
| Terminating a running task                                                 | [Terminating a Task Example](terminating-a-task-example.md)                         |
| Creating a new trigger for a known task                                    | [Creating a New Trigger](creating-a-new-trigger.md)                                 |
| Creating an event-based idle trigger for a known task                      | [Creating an Idle Trigger Example](creating-an-idle-trigger-example.md)             |
| Retrieving the trigger string of all triggers associated with a known task | [Retrieving Trigger Strings Example](retrieving-trigger-strings-example.md)         |



 

 

 




