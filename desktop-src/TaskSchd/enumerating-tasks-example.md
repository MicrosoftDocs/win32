---
title: Enumerating Tasks Example
description: To enumerate tasks, you must call ITaskScheduler Enum to create an enumeration object. Then, use the enumeration objects IEnumWorkItems interface to enumerate the tasks in the Scheduled Tasks folder.
ms.assetid: 65a8a8af-f4d8-4948-8dd4-b592f1381bfe
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Tasks Example

To enumerate tasks, you must call [**ITaskScheduler::Enum**](/windows/win32/Mstask/nf-mstask-itaskscheduler-enum?branch=master) to create an [*enumeration object*](e.md#-msb-enumeration-objects-gly). Then, use the enumeration object's [**IEnumWorkItems**](/windows/win32/Mstask/nn-mstask-ienumworkitems?branch=master) interface to enumerate the tasks in the Scheduled Tasks folder.

The following procedure describes how to enumerate the tasks in the Scheduled Tasks folder.

**To enumerate the tasks in the Scheduled Tasks folder**

1.  Call [**CoInitialize**](_com_coinitialize) to initialize the COM library and [**CoCreateInstance**](_com_cocreateinstance) to get a Task Scheduler object. (This example assumes that the Task Scheduler service is running.)
2.  Call [**ITaskScheduler::Enum**](/windows/win32/Mstask/nf-mstask-itaskscheduler-enum?branch=master) to get an enumeration object.
3.  Call [**IEnumWorkItems::Next**](/windows/win32/Mstask/nf-mstask-ienumworkitems-next?branch=master) to retrieve the tasks. (This example tries to retrieve five tasks with each call.)
4.  Process the tasks returned. (This example simply prints the name of each task to the screen.
5.  Release resources. Call [**CoTaskMemFree**](_com_cotaskmemfree) to free the memory used for names.



| For a code example of                                                         | See                                                                             |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Enumerating all the tasks in the Scheduled Tasks folder of the local computer | [C/C++ Code Example: Enumerating Tasks](c-c-code-example-enumerating-tasks.md) |



 

## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




