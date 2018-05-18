---
title: Enumerating Tasks
description: Task Scheduler 1.0 provides an enumeration object for enumerating the tasks in the Scheduled Tasks folder.
ms.assetid: '3a6a2262-cc5e-469e-b9f0-981879beb4ef'
keywords: ["enumerating tasks Task Scheduler", "enumerating tasks Task Scheduler , described"]
---

# Enumerating Tasks

Task Scheduler 1.0 provides an enumeration object for enumerating the tasks in the [*Scheduled Tasks folder*](s.md#-msb-scheduled-tasks-folder-gly).

> [!Note]  
> For a Windows Server 2003, Windows XP, or Windows 2000 computer to create, monitor, or control tasks on a Windows Vista computer, certain operations must be completed on the Windows Vista computer. For more information, see [Tasks](tasks.md).

 

## Using the Enumeration Object

The [**IEnumWorkItems**](ienumworkitems.md) interface of this object provides methods for enumerating the tasks in the folder, resetting the enumeration sequence to the start of the list, skipping tasks, and making a copy of the current enumeration object for later use.

For information about enumerating the tasks in the Scheduled tasks folder, see [**IEnumWorkItems::Next**](ienumworkitems-next.md).

For information about resetting the enumeration to the start of the list, see [**IEnumWorkItems::Reset**](ienumworkitems-reset.md).

For information about skipping tasks, see [**IEnumWorkItems::Skip**](ienumworkitems-skip.md).

For information about making a copy of the current enumeration object, see [**IEnumWorkItems::Clone**](ienumworkitems-clone.md).

For an example of enumerating the tasks in the Scheduled Tasks folder, see [Enumerating Tasks Example](enumerating-tasks-example.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Task Scheduler 1.0 Task Information](task-scheduler-1-0-task-informatation.md)
</dt> </dl>

 

 




