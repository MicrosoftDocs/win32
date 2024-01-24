---
description: The Multimedia Class Scheduler service (MMCSS) enables multimedia applications to ensure that their time-sensitive processing receives prioritized access to CPU resources.
ms.assetid: a7169938-1c72-4c4c-881a-cb08ad6182c7
title: Multimedia Class Scheduler Service
ms.topic: article
ms.date: 05/31/2018
---

# Multimedia Class Scheduler Service

The Multimedia Class Scheduler service (MMCSS) enables multimedia applications to ensure that their time-sensitive processing receives prioritized access to CPU resources. This service enables multimedia applications to utilize as much of the CPU as possible without denying CPU resources to lower-priority applications.

MMCSS uses information stored in the registry to identify supported tasks and determine the relative priority of threads performing these tasks. Each thread that is performing work related to a particular task calls the [**AvSetMmMaxThreadCharacteristics**](/windows/desktop/api/Avrt/nf-avrt-avsetmmmaxthreadcharacteristicsa) or [**AvSetMmThreadCharacteristics**](/windows/desktop/api/Avrt/nf-avrt-avsetmmthreadcharacteristicsa) function to inform MMCSS that it is working on that task.

For an example of a program that uses MMCSS, see [Exclusive-Mode Streams](/previous-versions//bb614507(v=vs.85)).

**Windows Server 2003 and Windows XP:** MMCSS is not available.

## Registry Settings

The MMCSS settings are stored in the following registry key:

**HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile**

This key contains a **REG\_DWORD** value named **SystemResponsiveness** that determines the percentage of CPU resources that should be guaranteed to low-priority tasks. For example, if this value is 20, then 20% of CPU resources are reserved for low-priority tasks. Note that values that are not evenly divisible by 10 are rounded up to the nearest multiple of 10. A value of 0 is also treated as 10.

The key also contains a subkey named **Tasks** that contains the list of tasks. By default, Windows supports the following tasks:

-   **Audio**
-   **Capture**
-   **Distribution**
-   **Games**
-   **Playback**
-   **Pro Audio**
-   **Window Manager**

OEMs can add additional tasks as required.

Each task key contains the following set of values that represent characteristics to be applied to threads that are associated with the task.

| Value                   | Format         | Possible values                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Affinity**            | **REG\_DWORD** | A bitmask that indicates the processor affinity. Both 0x00 and 0xFFFFFFFF indicate that processor affinity is not used.                                                                                                                                                                                                                                                 |
| **Background Only**     | **REG\_SZ**    | Indicates whether this is a background task (no user interface). The threads of a background task do not change because of a change in window focus. This value can be set to True or False.                                                                                                                                                                            |
| **BackgroundPriority**  | **REG\_DWORD** | The background priority. The range of values is 1-8.                                                                                                                                                                                                                                                                                                                    |
| **Clock Rate**          | **REG\_DWORD** | A hint used by MMCSS to determine the granularity of processor resource scheduling.**Windows Server 2008 and Windows Vista:** The maximum guaranteed clock rate the system uses if a thread joins this task, in 100-nanosecond intervals. Starting with Windows 7 and Windows Server 2008 R2, this guarantee was removed to reduce system power consumption.<br/> |
| **GPU Priority**        | **REG\_DWORD** | The GPU priority. The range of values is 0-31. This priority is not yet used.                                                                                                                                                                                                                                                                                           |
| **Priority**            | **REG\_DWORD** | The task priority. The range of values is 1 (low) to 8 (high).For tasks with a **Scheduling Category** of High, this value is always treated as 2.<br/>                                                                                                                                                                                                           |
| **Scheduling Category** | **REG\_SZ**    | The scheduling category. This value can be set to High, Medium, or Low.                                                                                                                                                                                                                                                                                                 |
| **SFIO Priority**       | **REG\_SZ**    | The scheduled I/O priority. This value can be set to Idle, Low, Normal, or High. This value is not used.                                                                                                                                                                                                                                                                |



 

> [!Note]  
> To conserve power, applications should not set the resolution of the system-wide timer to a small value unless absolutely necessary. For more information, see [Performance](../win7devguide/performance.md) in the [Windows 7 Developers Guide](../win7devguide/windows-7-developer-guide.md).

 

## Thread Priorities

The MMCSS boosts the priority of threads that are working on high-priority multimedia tasks.

MMCSS determines the priority of a thread using the following factors:

-   The base priority of the task.
-   The *Priority* parameter of the [**AvSetMmThreadPriority**](/windows/desktop/api/Avrt/nf-avrt-avsetmmthreadpriority) function.
-   Whether the application is in the foreground.
-   How much CPU time is being consumed by the threads in each category.

MMCSS sets the priority of client threads depending on their scheduling category.

| Category | Priority | Description                                                                                                                               |
|----------|----------|-------------------------------------------------------------------------------------------------------------------------------------------|
| High     | 23-26    | These threads run at a thread priority that is lower than only certain system-level tasks. This category is designed for Pro Audio tasks. |
| Medium   | 16-22    | These threads are part of the application that is in the foreground.                                                                      |
| Low      | 8-15     | This category contains the remainder of the threads. They are guaranteed a minimum percentage of the CPU resources if required.           |
|          | 1-7      | These threads have used their quota of CPU resource. They can continue to run if no low-priority threads are ready to run.                |



 

 

 
