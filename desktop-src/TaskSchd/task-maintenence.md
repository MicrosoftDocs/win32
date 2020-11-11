---
title: Automatic maintenance (Task Scheduler)
description: Maintenance activity refers to an application or process that helps maintain the health and performance of a Windows PC.
ms.assetid: 1D38341B-15AA-422F-AED1-647FCDE69E2E
ms.topic: article
ms.date: 05/31/2018
---

# Automatic maintenance

Maintenance activity refers to an application or process that helps maintain the health and performance of a Windows PC. Maintenance includes keeping the Windows operating system (OS) and applications up-to-date, checking security, and running scans for malware. Windows Automatic Management (WAM) is a set of enhancements to the Task Scheduler API that you can use to link your applications into the Windows maintenance schedule. Specifically, WAM allows you to add activities that require regular scheduling, but that don't have exact time requirements. Instead, WAM relies on the operating system to choose the appropriate time to activate the task throughout the day. The system chooses those times based on minimal impact to the user, PC performance, and energy efficiency.

## How scheduled maintenance works

Task Scheduler maintenance tasks are opportunistic tasks that run when the machine is idle and on AC power. One of the major goals of maintenance tasks is to minimize impact to the PC by scheduling maintenance only when the PC is plugged in to AC power and idle (that is, when you're not using, or have stepped away from, the machine). The idea of maintenance today is for the machine to do work with the least disruption to the user. Hence the old-style maintenance hour (we talk more about this in the **Automatic maintenance&mdash;daily wakeup** section later in this topic) has been improved in order to take advantage of these idle periods. While the maintenance hour can still be leveraged, running opportunistic maintenance is better for system health.

Your task may be starved if a machine doesn't spend much time both idle and on AC power. Make sure that your scenario will still provide value to the user, even if it is delayed. If the user is actively using the machine, then the system defers maintenance until a later time. The system also suspends any executing maintenance task if the user returns to using the PC.

The system restarts a suspended maintenance task during the next idle period; however, the system won't suspend any task marked as critical. Instead, the system allows a critical task to complete, regardless of user action.

Due to the nature of scheduling, some scheduled tasks may not finish: perhaps there are too many scheduled events to fit into the 1-hour maintenance window, or maybe the computer was simply not turned on. In such cases, you can define a task with a deadline. A deadline is defined as a recurring timeframe in which the system must successfully perform the task at least once.

If a task misses a deadline, then the maintenance scheduler will continue to attempt to execute the task during the maintenance window. Further, the scheduler will not limit itself to the regular 1-hour time limit. Instead, the scheduler extends the duration of the maintenance window in order to complete the delayed task.

Once the system completes the task (even with a failure error code), the attempt is considered successful. After a successful attempt, the scheduler resets to the regular maintenance schedule, and will attempt the task during the next period.

## Automatic maintenance&mdash;daily wakeup

On Windows 7, a maintenance task runs exclusively during *maintenance hour*, defaulting to 3 AM, and configurable via Group Policy. The machine would wake up from standby, run maintenance tasks, and go back to sleep. This daily session was limited to a maximum duration of 1 hour per attempt. This would allow the system to perform maintenance daily, starting at 3 AM by default. Note that the user may re-schedule the time that the maintenance is triggered by configuring these settings.

With the advent of laptops, and the heavy focus on battery life, machines are no longer configured to allow S3 wakeup in most circumstances, and generally Doze-To-S4 (hibernate) as soon as possible, to save battery. In response to these changes, Task Scheduler (> Win7) runs maintenance tasks whenever they are due, and the machine is idle and on AC power.

This setting can be configured in Control Panel.

Open **Control Panel** > **System and Security** > **Security and Maintenance** > **Automatic Maintenance**.

So based on how your machines and your tasks are configured, the daily wakeup behavior may not occur today as expected because of this new configuration. 
You can first determine whether your machine is S3 capable or CS (Connected Standby) capable.
This can be done by opening an elevated power shell prompt, and running the following command.

```console
powercfg /a
```

Maintenance hour, if the machine is configured correctly, still works, but if it doesn't,
  - Check your BIOS settings for Wake settings. 
  - Check whether Allow Wake Timer is enabled in Power Options.
    Go to **Control Panel** > **Hardware and Sound** > **Power Options** > **Edit Plan Settings** > **Change advanced power settings** > click **Sleep** > **Allow Wake Timer**.
  - Check whether your scheduled task is configured with following.
      * MaintenanceSettings: Task should be configured with Period, Deadline.
      * Enabled: Task should be enabled.
      * WakeToRun: Task should be allowed to wake the machine.
  - For scheduling wakes from CS, the machine should be AOAC capable.
  - For scheduling wakes in S3 machines,
      * Check whether the machine went into S3 on AC Power.
      * The system should have **Wake Enabled** in Group Policy for Maintenance.
 
Connected Standby is the system state that an AOAC-compliant system can enter.

See differences between Modern Standby and S3 in the topic [Modern Standby vs S3](/windows-hardware/design/device-experiences/modern-standby-vs-s3).

## Defining an Automatic Maintenance Task

You can convert any Task Scheduler task to a maintenance task. To do so, you must confirm that your application can be suspended. Then, you must extend the task definition with the new [**MaintenanceSettings**](taskschedulerschema-maintenancesettings-maintenancesettingstype-element.md) and [**AllowStartOnDemand**](taskschedulerschema-allowstartondemand-settingstype-element.md) elements.

The main concern with creating a maintenance task is ensuring that the system can suspend and restart the task. The system will likely suspend a maintenance task multiple times; therefore, you need to ensure that your application is able to save its own state, and then resume at an arbitrary time. This ensures that the system does not perform the same part of your task repeatedly.

Once you have ensured that your application can be suspended and resumed gracefully, you can use the **MaintenanceSettings** and **AllowStartOnDemand** elements to define the schedule. **MaintenanceSettings** is defined according to the period, deadline, and exclusivity.

-   The **period** is mandatory, and defines how often the task should occur. Usually, this is defined in terms of a multi-day cycle, such as “once every 5 days”. A period must be at least one day, meaning that you can't schedule a task to occur multiple times in a day.
-   The **deadline** is optional, and defines how long the scheduler can fail to complete the task before notifying the user or performing emergency maintenance. The deadline must be longer than the period, meaning that the system must have the opportunity to attempt the task at least once before notifying the user.
-   In addition, a maintenance task can optionally be defined as *exclusive*. An exclusive task runs separate from other maintenance tasks. Usually, an exclusive task is one that uses a great deal of resources, such as a large amount of CPU time, or exclusive access to a database. The system completes all non-exclusive maintenance tasks before starting an exclusive task. Therefore, you should declare a task as exclusive only when necessary.

In contrast, **AllowStartOnDemand** merely indicates that the system or the user can start the task at any time. This allows the system to start the task during regular maintenance. Otherwise, you would have to set a unique trigger for the task.
