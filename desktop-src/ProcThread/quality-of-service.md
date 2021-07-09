---
description: Quality of Service indicates the performance and power efficiency of a thread. This can influence thread scheduling and processor power management.
title: Quality of Service
ms.topic: article
ms.date: 07/09/2021
---

# Quality of Service

The Quality of Service (QoS) associated with a thread is used to indicate the desired performance and power efficiency. Each thread is assigned to a Quality of Service level. While scheduling priority remains the main metric by which the system determines which thread to schedule next, Quality of Service can influence core selection and processor power management. On platforms with heterogenous processors, the Quality of Service of a thread may restrict scheduling to a subset of processors, or indicate a preference for a particular class of processor.

Developers may already be employing other facilities to control when to execute such as when the user is not present, only on AC/charging, or depending on the battery level. Quality of Service provides a facility to influence how to execute. This facility can help to improve CPU efficiency and thus extend battery life. In addition, this process can assist in reducing CPU power consumption while operating on AC power to reduce thermal output which can lead to high fan noise, or even thermal throttling.




## Quality of Service Levels

The system maintains multiple QoS Levels each with differentiated performance and power efficiency. Windows provides standard default settings for scheduling and processor power management for each QoS Level. The precise tuning of each QoS Level for processor power management and heterogenous scheduling can be modified via Windows Provisioning. For more information on performance tuning and provisioning, see <a href="/windows-hardware/customize/power-settings/configure-processor-power-management-options">Processor power management options.</a>


<table>
<tr>
<th>QoS Level</th>
<th>Description</th>
<th>Performance and Power</th>
<th>Release</th>
</tr>
<tr>
<td>High</td>
<td>Windowed applications that are in the foreground and in focus, or audible</td>
<td>Standard high performance</td>
<td>1709</td>
</tr>
<tr>
<td>Medium</td>
<td>Windowed applications that may be visible to the end user but are not in focus</td>
<td>Varies by platform, between High and Low</td>
<td>1709</td>
</tr>
<tr>
<td>Low</td>
<td>Windowed applications that are not visible or audible to the end user</td>
<td>On battery, selects most efficient CPU frequency and schedules to efficient cores</td>
<td>1709</td>
</tr>
<tr>
<td>Eco</td>
<td>Applications which explicitly tag processes with <a href="/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setprocessinformation">SetProcessInformation</a> or threads with <a href="/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setprocessinformation">SetThreadInformation</a>
</td>
<td>Always selects most efficient CPU frequency and schedules to efficient cores</td>
<td>Windows 11</td>
</tr>
<tr>
<td>Media</td>
<td>Threads explicitly tagged by the <a href="/windows/desktop/procthread/multimedia-class-scheduler-service">Multimedia Class Scheduler Service</a>  to denote multimedia batch buffering</td>
<td>CPU frequency reduced for efficient batch processing</td>
<td>2004</td>
</tr>
<tr>
<td>Deadline</td>
<td>Threads explicitly tagged by <a href="/windows/desktop/procthread/multimedia-class-scheduler-service">Multimedia Class Scheduler Service</a>  to denote that audio threads require performance to meet deadlines</td>
<td>High performance to meet media deadlines</td>
<td>2004</td>
</tr>
</table>

## Quality of Service Classification

<table>
<tr>
<th>Source</th>
<th>Description</th>
</tr>
<tr>
<td>Multimedia Foundation</td>
<td>The <a href="/windows/desktop/procthread/multimedia-class-scheduler-service">Multimedia Class Scheduler Service</a> prioritizes CPU resources for multimedia scenarios. The service tags specific threads responsible for multimedia processing using the Media and Deadline QoS levels to provide power efficiency while meeting performance deadlines. </td>
</tr>
<tr>
<td>API</td>
<td><a href="/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setprocessinformation">SetProcessInformation</a> allows developers to explicitly tag a process as HighQoS or EcoQoS by toggling the <code>PROCESS_POWER_THROTTLING_EXECUTION_SPEED</code> feature in <b>ProcessPowerThrottling</b>.
<br/>
<a href="/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setprocessinformation">SetThreadInformation</a> allows developers to explicitly tag a thread as HighQoS or EcoQoS by toggling the <code>THREAD_POWER_THROTTLING_EXECUTION_SPEED</code> feature in <b>ThreadPowerThrottling </b>.
</td>
</tr>
<tr>
<td>Audible</td>
<td>Processes which are determined to be playing audio are HighQoS.</td>
</tr>
<tr>
<td>Visible</td>
<td>Processes which directly own a window (or are descendants of window owning processes) are assigned a QoS level according to their visibilty and focus state:
    <table>
        <tr>
            <th>Window State</th>
            <th>Quality of Service</th>
        </tr>
        <tr>
            <td>In Focus</td>
            <td>High</td>
        </tr>
        <tr>
            <td>Visible</td>
            <td>Medium</td>
        </tr>
        <tr>
            <td>Minimized, or Fully Occluded</td>
            <td>Low</td>
        </tr>
    </table>
</td>
</tr>
<tr>
<td>Heuristic</td>
<td>Threads which are not classified by the above sources are automatically assigned a Quality of Service level by the system. These heuristics include (but are not limited to) thread priority, whereby threads running with reduced thread priority may imply a lower Quality of Service level.</td>
</tr>