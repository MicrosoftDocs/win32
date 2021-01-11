---
description: Windows power management makes computers instantly accessible to users at the touch of a button or key.
ms.assetid: 388dadb9-b722-43f8-ab2b-a9bbd96600a3
title: Windows Power Management
ms.topic: article
ms.date: 05/31/2018
---

# Windows Power Management

Windows power management makes computers instantly accessible to users at the touch of a button or key. It also ensures that all elements of the system—applications, devices, and user interface—can take advantage of the vast improvements in power management technology and capabilities.

The Windows operating system uses power-management hardware to put the computer into a low-power *sleep state* instead of shutting down completely, so that the system can quickly resume working. The operating system will automatically enter the sleep state when the computer is idle or when the user presses a button to indicate that the current work session is over. To the user, the system appears to be off. While in the sleep state, the computer's processor is not executing code and no work is being accomplished for the user. However, events in the system from both hardware devices and the real-time clock can be enabled to cause the system to exit the sleep state (that is, "wake up") and quickly return to the working state.

When the computer is in the sleep state, the computer hardware, the system, and applications running on the computer must be capable of responding immediately to the power switch, communications events, and other actions. If all applications handle power state transitions gracefully, the user will perceive a more elegant and integrated system. Applications that do not handle these transitions can fail when the power is turned off and then on, because of data loss or a dependency on a device that may have been removed.

The following are benefits of Windows power management:

-   Eliminates startup and shutdown delays. The computer need not perform a full system boot when exiting the sleep state or a full system shutdown when the user initiates the sleep state.
-   Enables automated tasks to run while the computer is in the sleep state. The Task Scheduler enables the user to schedule applications to run; scheduled events can run even when the system is in the sleep state. The Task Scheduler uses [waitable timers](/windows/desktop/Sync/waitable-timer-objects) to ensure that the system is ready when the application is scheduled to run. For more information, see the help file included with the Task Scheduler.
-   Enables per-device power management. Devices that are not in use can save power by entering the sleep state.
-   Improves power efficiency. Power efficiency is particularly important on portable computers. Reducing system power consumption translates directly to lower energy costs and longer battery life.
-   Enables users to create [power schemes](power-schemes.md), set alarms, and specify battery options through the Power Options application in Control Panel. The operating system coordinates all power management activities, based on power policy settings. For more information, see the help file included with the Power Options application.

## Related topics

<dl> <dt>

[About Power Management](about-power-management.md)
</dt> <dt>

[Task Scheduler](/windows/desktop/TaskSchd/task-scheduler-start-page)
</dt> </dl>

 

 
