---
description: How to use Work Unit performance counters. Work Unit performance counters are a mechanism giving insight into an application's process to the Windows platform. With Work Units, apps can describe which work units are running on a particular process and claim ownership of those units.
ms.assetid: 
title: Using Work Unit Performance Counters
ms.topic: article
ms.date: 02/25/2022
---

# Using Work Unit Performance Counters

`Work Unit` performance counters give the Windows platform insight into an application's processes. Work Units enable apps to describe which parts of the application run on a particular process and claim ownership. For example, a web browser has its own Task Manager to manage all its processes; with the Work Unit performance counter, that level of detail and control can be available from the Windows Task Manager.

For instance, consider the Microsoft Edge browser running on a user's device. The browser runs on a particular process, but other processes are created to host tabs, network and audio services, extensions, and other functionality. The particular process can be used to run multiple units of work, and different apps can share them. Internally, the browser knows its dependencies and how to communicate with the necessary processes, but the Windows platform and other applications do not know how the browser is composed. Having such information is helpful to provide more precise resource usage information and help diagnose issues with the app; Task Manager can report which units of work are running on a process. With this, debuggers can simplify developer workloads by describing what kind of work is running on a process.

Work Units are a data contract implemented over performance counters to allow apps to reveal to the Windows platform what a specific process is being used for. surface their composition to the Windows platform. Each work unit carries the following properties.

- AppOwnerProcessId: ID for the process which owns the given Work Unit.
- HostProcessId: ID for the process in which the given Work Unit is running.
- Kind: how the Work Unit should be interpreted by the application receiving it.
- Title: label for the Work Unit.
- UniqueId: identifier for the Work Unit.

## Data contract

Information shared with Work Units in the Windows platform is available to be queried by any app running in the system. The data is provided and consumed using [Performance Counter APIs](https://docs.microsoft.com/en-us/windows/win32/api/_perf/), publicly available and documented. As part of their implementation, performance counters must have a unique identifier string, which we use to identify the label for the Work Unit. The expected format of the perf-counter unique identifier string is.

- Leading "WorkUnit" string.
- 1-based uniqueId.
- identifier of the process in which the Work Unit is running.
- identifier of the main process which represents the application.
- user-friendly title for the Work Unit.

> [!NOTE]
> If a work unit information must be updated (for example, the title was changed), it retains its uniqueId. New units must use new unique identifiers. The uniqueId must be concatenated using the pipe character "|", like the sample below.

Sample:

    "WorkUnit|1|4321|1019|Instance 1 of pid 1111, owned by 1111"
    "WorkUnit|1|8765|1019|Instance 1 of pid 5555, owned by 5555"
    "WorkUnit|1|9999|1019|Instance 1 of pid 9999, owned by 9999"
    "WorkUnit|2|4321|1019|Instance 2 of pid 1234, owned by 4321"
    "WorkUnit|2|8765|1019|Instance 2 of pid 5678, owned by 8765"

## Providing Work Units

You can create instances of the Work Unit performance counter set using [Performance Counter APIs](https://docs.microsoft.com/en-us/windows/win32/api/_perf/). Follow the [data contract](#data-contract) documented above to ensure that other apps can successfully validate and consume your data.

## Visualizing Work Units

If you would like to query data from a Work Unit performance counter, you can use the Performance Counter APIs or the Performance Monitor application.

1. Type "perfmon" at a CMD prompt or Run dialog to start the PerfMon tool.
2. Select "Performance Monitor" under "Monitoring Tools".
3. Click the "Add counters" button (green '+' sign).
4. Select and expand "Work Unit" to see counters provided by running applications.
5. Select the counters listed: "App Owner Process ID" and "Host Process ID".
6. Select "<All instances>" and click "Add".
7. Click "OK".

> - Selection of the Work Unit counter from the UI
:::image type="content" source="images/workunit-count-select.png" alt-text="Screenshot of the Add Counter window. Work Unit is highlighted on the window as a counter to add.":::