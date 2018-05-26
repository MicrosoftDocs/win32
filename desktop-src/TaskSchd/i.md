---
title: I
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Robots: noindex, nofollow
ms.assetid: 84a58712-72fb-47c6-8d92-e2a0ebfccaca
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# I

A B C D [E](e.md) F G H I J K L M N O [P](p.md) Q R [S](s.md) [T](t.md) U V [W](w.md) X Y Z

<dl> <dt>

<span id="_msb_idle_conditions_gly"></span><span id="_MSB_IDLE_CONDITIONS_GLY"></span>**idle conditions**
</dt> <dd>

A period of time in which there is no user input on the computer. Idle conditions are associated with the scheduled start time for the task.

These conditions are set by calling [**IScheduledWorkItem::SetFlags**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-setflags?branch=master).

</dd> <dt>

<span id="_msb_idle_triggers_gly"></span><span id="_MSB_IDLE_TRIGGERS_GLY"></span>**idle triggers**
</dt> <dd>

An event-based trigger that is fired when the computer becomes idle for a specific amount of time.

Idle triggers are created by setting the TASK\_TRIGGER\_TYPE member of the [**TASK\_TRIGGER**](/windows/win32/Mstask/ns-mstask-_task_trigger?branch=master) structure to TASK\_EVENT\_TRIGGER\_ON\_IDLE.

</dd> <dt>

<span id="_msb_idle_wait_time_gly"></span><span id="_MSB_IDLE_WAIT_TIME_GLY"></span>**idle wait time**
</dt> <dd>

The time interval (in minutes) used by an idle trigger or idle condition. Idle triggers are event-based triggers that are not associated with a scheduled time. Idle conditions are associated with the scheduled start time for the task.

The idle time is set by a call to [**IScheduledWorkItem::SetIdleWait**](/windows/win32/Mstask/nf-mstask-ischeduledworkitem-setidlewait?branch=master).

</dd> </dl>

 

 




