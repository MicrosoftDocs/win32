---
description: how to use WorkUnit performance counters.
ms.assetid: 
title: Using WorkUnit Performance Counters
ms.topic: article
ms.date: 02/25/2022
---

Using WorkUnit Performance Counters

WorkUnit performance counters provide further insight into an application's process to the Windows platform. Via work units, apps can describe which work units are running on a particular process and claim ownership of those units.

For instance, consider the Microsoft Edge browser running on a user's device. The browser runs on a particular process, but other processes are created to host tabs, network and audio services, extensions, and other functionalities. Furthermore, a particular process may be used to run multiple units of work (e.g., a process responsible for multiple tabs); and different apps may share it (e.g., Microsoft Edge browser and WPA apps sharing resources). Internally, the browser knows its dependencies and how to communicate with the necessary processes, but the Windows platform and other applications do not know how the browser is composed. Having such information is helpful to provide more precise resource usage information (e.g., TaskManager can report which units of work are running on a process). As well as to improve the diagnosability of the app: debuggers can simplify developer workloads by showing descriptions of what kind of work is running on a process.

WorkUnits are a data contract implemented over performance counters to allow apps to surface their composition to the Windows platform. Each work unit carries the following properties:

- AppOwnerProcessId: ID for the process which owns the given Work Unit;
- HostProcessId: ID for the process in which the given Work Unit is running;
- Kind: how the Work Unit should be interpreted by the application receiving it;
- Title: label for the Work Unit;
- UniqueId: identifier for the Work Unit.

Data contract
-------------

Information shared via work units in the Windows platform is available to be queried by any app running in the system. The data is provided and consumed using Performance Counter APIs, publicly available and documented [here](https://docs.microsoft.com/en-us/windows/win32/api/_perf/). As part of their implementation, performance counters must have a unique identifier string, which we use to surface the label for the work unit. The expected format of the perf-counter unique identifier string is:

- Leading "WorkUnit" string;
- 1-based uniqueId;
- identifier of the process in which the work unit is running;
- identifier of the main process which represents the application;
- user-friendly title for the work unit.

Notice that if a work unit information must be updated, e.g., the title was changed, it must be informed with the same uniqueId it had when first notified of the platform. New units must use a new unique identifier. The information must be concatenated using the pipe character "|". E.g.:

    "WorkUnit|1|4321|1019|Instance 1 of pid 1111, owned by 1111"
    "WorkUnit|1|8765|1019|Instance 1 of pid 5555, owned by 5555"
    "WorkUnit|1|9999|1019|Instance 1 of pid 9999, owned by 9999"
    "WorkUnit|2|4321|1019|Instance 2 of pid 1234, owned by 4321"
    "WorkUnit|2|8765|1019|Instance 2 of pid 5678, owned by 8765"

Providing WorkUnits

Create instances of the WorkUnit performance counter set using Performance Counter APIs. Follow the data contract documented above to ensure that other apps can successfully validate and consume your data.

Visualizing WorkUnits

Either query data from WorkUnit perf-counters via Performance Counter APIs or use the Performance Monitor application.

1. Type "perfmon" at a CMD prompt or Run dialog to start the PerfMon tool.
2. Select "Performance Monitor" under "Monitoring Tools".
3. Click the "Add counters" button (green '+' sign).
4. Select and expand "Work Unit" to see counters provided by running applications.
5. Select the counters listed: "App Owner Process ID" and "Host Process ID".
6. Select "<All instances>" and click "Add".
7. Click "OK".
