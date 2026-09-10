---
title: About the Task Scheduler
description: The Task Scheduler service allows you to perform automated tasks on a chosen computer.
ms.assetid: 13816b8b-3090-4d17-86bb-8e632ca0cd37
keywords:
- Task Scheduler Task Scheduler , about
ms.topic: concept-article
ms.date: 07/16/2026
---

# About the Task Scheduler

The Task Scheduler service allows you to perform automated tasks on a chosen computer. With this service, you can schedule any program to run at a convenient time for you or when a specific event occurs. The Task Scheduler monitors the time or event criteria that you choose and then executes the task when those criteria are met.

## Where Task Scheduler is Installed

The Task Scheduler is automatically installed with all supported versions of Windows. Always use the Task Scheduler 2.0 API for new development.

> [!NOTE]
> Task Scheduler 1.0 interfaces are deprecated. All new code should target the [Task Scheduler 2.0 API](task-scheduler-reference.md), which is available on Windows Vista and later.

Task Scheduler is started each time the operating system is started. It can be run either through the Task Scheduler graphical user interface (GUI) or through the Task Scheduler API described in this SDK.

## Power-aware scheduling

Task Scheduler integrates with Windows power management to minimize impact on battery life and user experience. When designing scheduled tasks:

> [!IMPORTANT]
> **Never use short-interval polling tasks on battery-powered devices.** A task that runs every 5 minutes prevents the system from entering low-power idle states. Use event triggers, idle triggers, or maintenance scheduling instead.

| Approach | When to use | Power behavior |
|----------|-------------|----------------|
| **Automatic maintenance** | Housekeeping that can defer (defrag, scans, cleanup). | Runs only when idle + AC power. Defers indefinitely on battery. |
| **Idle trigger** | Work that requires low system load but not AC power. | Waits for user absence + CPU idle. |
| **Event trigger** | Reactive work (Event Log entry, WMI event). | Runs only when the event fires. Zero cost otherwise. |
| **Time trigger + conditions** | Recurring schedules with `StartWhenAvailable` and `StopIfGoingOnBatteries`. | Task defers if conditions not met; catches up when they are. |

For maintenance tasks on Modern Standby devices, configure:
- `AllowStartIfOnBatteries = false`
- `StopIfGoingOnBatteries = true`
- `MaintenanceSettings` with a `Period` and `Deadline`

See [Automatic Maintenance](task-maintenence.md) for details on how maintenance scheduling works with Connected Standby and S3 systems.

## Information about Tasks

Tasks are the main component of the Task Scheduler. For information on what tasks are and what their components are, see the following topics:

-   [Tasks](tasks.md)
-   [Task Actions](task-actions.md)
-   [Task Triggers](task-triggers.md)
-   [Task Registration Information](task-registration-information.md)
-   [Task Idle Conditions](task-idle-conditions.md)
-   [Security Contexts for Tasks](security-contexts-for-running-tasks.md)
-   [Repeating A Task](repeating-a-task.md)
-   [Automatic Maintenance](task-maintenence.md)

For more information and examples about how to use the Task Scheduler interfaces, scripting objects, and XML, see [Using the Task Scheduler](using-the-task-scheduler.md).

## Related topics

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 




