---
title: Automatic Maintenance
description: Maintenance activity refers to an application or process that helps maintain the health and performance of a Windows PC.
ms.assetid: 1D38341B-15AA-422F-AED1-647FCDE69E2E
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Automatic Maintenance

Maintenance activity refers to an application or process that helps maintain the health and performance of a Windows PC. Maintenance includes keeping Windows and applications up-to-date, checking security, and running scans for malware. Windows Automatic Management (WAM) is a set of enhancements to the Task Scheduler API you can use to link your applications into the Windows maintenance schedule. Specifically, WAM allows you to add activities that require regular scheduling, but do not have exact time requirements. Instead, WAM relies on the operating system to choose the appropriate time to activate the task throughout the day. The system chooses those times based on minimal impact to the user, PC performance, and energy efficiency.

## How Scheduled Maintenance Works

Windows Automatic Maintenance minimizes impact to the PC by scheduling maintenance only when the PC is on and idle. By default, the system performs maintenance daily, starting at 3 AM. (Note that the user may re-schedule when the maintenance occurs.) This daily session is limited to a maximum duration of 1 hour per attempt. If the user is actively using the machine, the system defers maintenance until a later time. The system also suspends any executing maintenance task if the user returns to the PC.

The system restarts a suspended maintenance task during the next idle period; however, the system will not suspend any task marked as critical. Instead, the system allows a critical task to complete, regardless of user action.

Due to the nature of scheduling, some scheduled tasks may not finish: perhaps there are too many scheduled events to fit in the 1 hour maintenance window, or maybe the computer was simply not turned on. In such cases, you can define a task with a deadline. A deadline is defined as a recurring time frame in which the system must successfully perform the task at least once.

If a task misses a deadline, the maintenance scheduler will continue to attempt to execute the task during the maintenance window. Further, the scheduler will not limit itself to the regular 1 hour time limit. Instead, the scheduler extends the duration of the maintenance window in order to complete the delayed task. If the system still cannot complete the task, the Action Center displays a warning notification to the user. The user can then manually initiate the maintenance action from the Action center.

Once the system completes the task (even with a failure error code), the attempt is considered successful. After a successful attempt, the scheduler resets to the regular maintenance schedule, and will attempt the task during the next period.

## Defining an Automatic Maintenance Task

You can convert any Task Scheduler task to a maintenance task. To do so, you must confirm that your application can be suspended. Then, you must extend the task definition with the new [**MaintenanceSettings**](taskschedulerschema-maintenancesettings-maintenancesettingstype-element.md) and [**AllowStartOnDemand**](taskschedulerschema-allowstartondemand-settingstype-element.md) elements.

The main concern with creating a maintenance task is ensuring that the system can suspend and restart the task. The system will likely suspend a maintenance task multiple times; therefore, you need to ensure that your application is able to save its own state, and then resume at an arbitrary time. This ensures that the system does not perform the same part of your task repeatedly.

Once you have ensured that your application can be suspended and resumed gracefully, you can use the new **MaintenanceSettings** and **AllowStartOnDemand** elements to define the schedule. **MaintenanceSettings** is defined according to the period, deadline, and exclusivity.

-   The **period** is mandatory, and defines how often the task should occur. Usually, this is defined in terms of a multi-day cycle, such as “once every 5 days”. A period must be at least one day, meaning that you cannot schedule a task to occur multiple times in a day.
-   The **deadline** is optional, and defines how long the scheduler can fail to complete the task before notifying the user or performing emergency maintenance. The deadline must be longer than the period, meaning that the system must have the opportunity to attempt the task at least once before notifying the user.
-   In addition, a maintenance task can optionally be defined as **exclusive**. An exclusive task runs separate from other maintenance tasks. Usually, an exclusive task is one that uses a great deal of resources, such as a large amount of CPU time, or exclusive access to a database. The system completes all non-exclusive maintenance tasks before starting an exclusive task. Therefore, you should declare a task as exclusive only when necessary.

In contrast, **AllowStartOnDemand** merely indicates that the system or the user can start the task at any time. This allows the system to start the task during regular maintenance. Otherwise, you would have to set a unique trigger for the task.

 

 




