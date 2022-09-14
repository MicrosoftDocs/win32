---
title: Enumerating Tasks
description: Task Scheduler 1.0 provides an enumeration object for enumerating the tasks in the Scheduled Tasks folder.
ms.assetid: 'ccd140a1-06f6-4e6b-afa6-f7ac9b9ff904'
keywords:
- enumerating tasks Task Scheduler
- enumerating tasks Task Scheduler , described
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Tasks

Task Scheduler 1.0 provides an enumeration object for enumerating the tasks in the [*Scheduled Tasks folder*](s.md).

> [!Note]  
> For a Windows Server 2003, Windows XP, or Windows 2000 computer to create, monitor, or control tasks on a Windows Vista computer, certain operations must be completed on the Windows Vista computer. For more information, see [Tasks](tasks.md).

 

## Using the Enumeration Object

The [**IEnumWorkItems**](/windows/desktop/api/Mstask/nn-mstask-ienumworkitems) interface of this object provides methods for enumerating the tasks in the folder, resetting the enumeration sequence to the start of the list, skipping tasks, and making a copy of the current enumeration object for later use.

For information about enumerating the tasks in the Scheduled tasks folder, see [**IEnumWorkItems::Next**](/windows/desktop/api/Mstask/nf-mstask-ienumworkitems-next).

For information about resetting the enumeration to the start of the list, see [**IEnumWorkItems::Reset**](/windows/desktop/api/Mstask/nf-mstask-ienumworkitems-reset).

For information about skipping tasks, see [**IEnumWorkItems::Skip**](/windows/desktop/api/Mstask/nf-mstask-ienumworkitems-skip).

For information about making a copy of the current enumeration object, see [**IEnumWorkItems::Clone**](/windows/desktop/api/Mstask/nf-mstask-ienumworkitems-clone).

For an example of enumerating the tasks in the Scheduled Tasks folder, see [Enumerating Tasks Example](enumerating-tasks-example.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Task Scheduler 1.0 Task Information](task-scheduler-1-0-task-informatation.md)
</dt> </dl>

 

 




