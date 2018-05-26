---
title: T
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Robots: noindex, nofollow
ms.assetid: 5d8ac31c-ce07-4801-a04e-e12e996b88c6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# T

A B C D [E](e.md) F G H [I](i.md) J K L M N O [P](p.md) Q R [S](s.md) T U V [W](w.md) X Y Z

<dl> <dt>

<span id="_msb_task_objects_gly"></span><span id="_MSB_TASK_OBJECTS_GLY"></span>**task objects**
</dt> <dd>

Instances of an object that provides methods for managing tasks. This includes methods for setting and retrieving properties; running, terminating, and deleting tasks; and creating new triggers and retrieving old triggers.

The task object is created by calls to [**IScheduledWorkItem::CreateTrigger**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-createtrigger?branch=master) and [**IScheduledWorkItem::GetTrigger**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-gettrigger?branch=master).

</dd> <dt>

<span id="_msb_task_scheduler_objects_gly"></span><span id="_MSB_TASK_SCHEDULER_OBJECTS_GLY"></span>**task scheduler objects**
</dt> <dd>

Instances of an object the represents the Task Scheduler service. This object supports two interfaces: **IUnknown** and [**ITaskScheduler**](/windows/win32/Mstask/nn-mstask-itaskscheduler?branch=master) (currently tasks are the only type of work items supported by the Task Scheduler service).

Task scheduler objects are created by calls to **CoCreateInstance**.

</dd> <dt>

<span id="_msb_task_trigger_objects_gly"></span><span id="_MSB_TASK_TRIGGER_OBJECTS_GLY"></span>**task trigger objects**
</dt> <dd>

Instances of an object the provides methods for setting and retrieving task triggers. This object supports two interfaces: **IUnknown** and [**ITaskTrigger**](/windows/win32/Mstask/nn-mstask-itasktrigger?branch=master).

Task trigger objects are created by calls to [**IScheduledWorkItem::CreateTrigger**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-createtrigger?branch=master) and [**IScheduledWorkItem::GetTrigger**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-gettrigger?branch=master).

See also: *triggers*.

</dd> <dt>

<span id="_msb_tasks_gly"></span><span id="_MSB_TASKS_GLY"></span>**tasks**
</dt> <dd>

Any item that the Task Scheduler can execute. These items may include any of the following (as supported by the operating system on which the task will execute): Win32® applications, Win16 applications, OS/2 applications, MS-DOS® applications, batch files (\*.bat), command files (\*.cmd), or any properly registered file type.

</dd> <dt>

<span id="_msb_tasks_folder_gly"></span><span id="_MSB_TASKS_FOLDER_GLY"></span>**Tasks folder**
</dt> <dd>

The folder that lists all task files (currently, tasks are the only work items available). These files contain the information about the task. The name of these files reflects the name of the task.

You can retrieve the location of the Tasks folder from the registry by getting data for the following value:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         SchedulingAgent
            TasksFolder
```

</dd> <dt>

<span id="_msb_triggers_gly"></span><span id="_MSB_TRIGGERS_GLY"></span>**triggers**
</dt> <dd>

A set of criteria that, when met, will cause a task to be executed. Task Scheduler provides time-based and event-based triggers that can specify task start times, repetition criteria, and other parameters.

</dd> <dt>

<span id="_msb_trigger_strings_gly"></span><span id="_MSB_TRIGGER_STRINGS_GLY"></span>**trigger strings**
</dt> <dd>

A string that describes the trigger. This string is created by the Task Scheduler service, and appears in the Task Scheduler user interface in a form similar to "At 2PM every day, starting 5/11/97."

</dd> <dt>

<span id="_msb_trigger_structures_gly"></span><span id="_MSB_TRIGGER_STRUCTURES_GLY"></span>**trigger structures**
</dt> <dd>

The [**TASK\_TRIGGER**](/windows/win32/Mstask/ns-mstask-_task_trigger?branch=master) structure used when setting or retrieving the criteria that defines the trigger. The criteria includes when the trigger will fire, and the type of the trigger.

</dd> </dl>

 

 




