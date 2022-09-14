---
description: Quality of Service indicates the performance and power efficiency of a thread, which can influence thread scheduling and processor power management.
title: Quality of Service
ms.topic: article
ms.date: 07/09/2021
---

# Quality of Service

The Quality of Service (QoS) associated with a thread is used to indicate the desired performance and power efficiency. Each thread is assigned to a QoS level. While scheduling priority remains the main metric by which the system determines which thread to schedule next, QoS can influence core selection and processor power management. On platforms with heterogeneous processors, the QoS of a thread may restrict scheduling to a subset of processors, or indicate a preference for a particular class of processor.

Developers may already be employing other facilities to control when to execute, such as when the user is not present, only on AC/charging, or depending on the battery level. QoS provides a facility to influence how to execute. This facility can help to improve CPU efficiency and thus extend battery life. In addition, this process can assist in reducing CPU power consumption while operating on AC power to reduce thermal output which can lead to high fan noise, or even thermal throttling.

## Quality of Service levels

The system maintains multiple QoS levels, each with differentiated performance and power efficiency. Windows provides standard default settings for scheduling and processor power management for each QoS level. The precise tuning of each QoS level for processor power management and heterogeneous scheduling can be modified through Windows Provisioning. For more information on performance tuning and provisioning, see [Processor power management options](/windows-hardware/customize/power-settings/configure-processor-power-management-options).

| QoS level | Description|Performance and power | Release |
| --- | --- | --- | --- |
| High | Windowed applications that are in the foreground and in focus, or audible, and explicitly tag processes with [SetProcessInformation](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setprocessinformation) or threads with [SetThreadInformation](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadinformation) | Standard high performance. |1709 |
| Medium | Windowed applications that may be visible to the end user but are not in focus. | Varies by platform, between High and Low. | 1709 |
| Low | Windowed applications that are not visible or audible to the end user. | On battery, selects most efficient CPU frequency and schedules to efficient core. | 1709 |
| Utility | Background services | On battery, selects most efficient CPU frequency and schedules to efficient cores. | Windows 11 22H2 |
| Eco | Applications that explicitly tag processes with [SetProcessInformation](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setprocessinformation) or threads with [SetThreadInformation](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadinformation). | Always selects most efficient CPU frequency and schedules to efficient cores. | Windows 11 |
| Media | Threads explicitly tagged by the [Multimedia Class Scheduler Service](/windows/desktop/procthread/multimedia-class-scheduler-service) to denote multimedia batch buffering. | CPU frequency reduced for efficient batch processing. | 2004 |
| Deadline | Threads explicitly tagged by [Multimedia Class Scheduler Service](/windows/desktop/procthread/multimedia-class-scheduler-service) to denote that audio threads require performance to meet deadlines. | High performance to meet media deadlines. | 2004 |

## Quality of Service classification

The following table shows the supported QoS classifications.

| Source | Description |
| --- | --- |
| Multimedia Foundation | The [Multimedia Class Scheduler Service](/windows/desktop/procthread/multimedia-class-scheduler-service) prioritizes CPU resources for multimedia scenarios. The service tags specific threads responsible for multimedia processing using the Media and Deadline QoS levels to provide power efficiency while meeting performance deadlines.  |
| API | [SetProcessInformation](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setprocessinformation) lets developers explicitly tag a process as HighQoS or EcoQoS by toggling the `PROCESS_POWER_THROTTLING_EXECUTION_SPEED` feature in **ProcessPowerThrottling**.</br>[SetThreadInformation](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setprocessinformation) lets developers explicitly tag a thread as HighQoS or EcoQoS by toggling the `THREAD_POWER_THROTTLING_EXECUTION_SPEED` feature in **ThreadPowerThrottling** .  |
| Audible | Processes which are determined to be playing audio are HighQoS. |
| Visible | Processes which directly own a window (or are descendants of window owning processes) are assigned a QoS level according to their visibility and focus state:</br></br><table><tr><th>Window State</th><th>Quality of Service</th></tr><tr><td>In Focus</td><td>High</td></tr><tr><td>Visible</td><td>Medium</td></tr><tr><td>Minimized, or Fully Occluded</td><td>Low</td></tr></table> |
| Heuristic | Threads which are not classified by the above sources are automatically assigned a QoS level by the system. These heuristics include (but are not limited to) thread priority, where threads running with reduced thread priority can imply a lower QoS level. |
