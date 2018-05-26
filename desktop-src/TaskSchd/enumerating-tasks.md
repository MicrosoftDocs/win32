---
title: Enumerating Tasks
description: Task Scheduler 1.0 provides an enumeration object for enumerating the tasks in the Scheduled Tasks folder.
ms.assetid: 3a6a2262-cc5e-469e-b9f0-981879beb4ef
keywords:
- enumerating tasks Task Scheduler
- enumerating tasks Task Scheduler , described
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Tasks

Task Scheduler 1.0 provides an enumeration object for enumerating the tasks in the [*Scheduled Tasks folder*](s.md#-msb-scheduled-tasks-folder-gly).

> [!Note]  
> For a Windows Server 2003, Windows XP, or Windows 2000 computer to create, monitor, or control tasks on a Windows Vista computer, certain operations must be completed on the Windows Vista computer. For more information, see [Tasks](tasks.md).

 

## Using the Enumeration Object

The [**IEnumWorkItems**](/windows/win32/Mstask/nn-mstask-ienumworkitems?branch=master) interface of this object provides methods for enumerating the tasks in the folder, resetting the enumeration sequence to the start of the list, skipping tasks, and making a copy of the current enumeration object for later use.

For information about enumerating the tasks in the Scheduled tasks folder, see [**IEnumWorkItems::Next**](/windows/win32/Mstask/nf-mstask-ienumworkitems-next?branch=master).

For information about resetting the enumeration to the start of the list, see [**IEnumWorkItems::Reset**](/windows/win32/Mstask/nf-mstask-ienumworkitems-reset?branch=master).

For information about skipping tasks, see [**IEnumWorkItems::Skip**](/windows/win32/Mstask/nf-mstask-ienumworkitems-skip?branch=master).

For information about making a copy of the current enumeration object, see [**IEnumWorkItems::Clone**](/windows/win32/Mstask/nf-mstask-ienumworkitems-clone?branch=master).

For an example of enumerating the tasks in the Scheduled Tasks folder, see [Enumerating Tasks Example](enumerating-tasks-example.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Task Scheduler 1.0 Task Information](task-scheduler-1-0-task-informatation.md)
</dt> </dl>

 

 




