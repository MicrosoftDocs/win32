---
description: Use event logging to record errors that occur in the performance DLL.
ms.assetid: 61bc4fa1-8185-4e07-a3b5-4bd357f0f75a
title: Error Handling in the DLL
ms.topic: article
ms.date: 05/31/2018
---

# Error Handling in the DLL

Use event logging to record errors that occur in the performance DLL. Logging error events aids in troubleshooting applications that provide performance data during development and after installation. You should limit the amount of error logging that occurs in the [**CollectPerformanceData**](/windows/win32/api/winperf/nc-winperf-pm_collect_proc) function because data collection can be frequent.

The system logs the following errors to the event log if there are problems with the [**OpenPerformanceData**](/previous-versions/windows/desktop/legacy/aa372200(v=vs.85)) function. If one of the following errors occurs, the system does not call the performance DLL again. Instead, the DLL is unloaded.

-   **PERFLIB\_OPEN\_PROC\_NOT\_FOUND**—Logged when the procedure name defined in the registry could not be found in the DLL as an exported function. This usually occurs when the DLL or the service is not installed correctly or the function name has been renamed without updating the installation procedure.
-   **PERFLIB\_OPEN\_PROC\_FAILURE**—Logged when the open procedure returned an error status other than ERROR\_SUCCESS. Should this happen, the DLL should have also entered an event log entry describing the conditions that caused the failure.
-   **PERFLIB\_OPEN\_PROC\_EXCEPTION**—Logged when the open procedure encounters an unhandled exception. This is usually due to an unexpected error condition encountered by the open procedure.

 

 
