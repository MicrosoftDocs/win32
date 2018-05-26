---
title: Support class
description: Provides status and progress reporting capability to assessments.
ms.assetid: 67058FB3-108A-4B09-A6E9-665376FDD12F
keywords:
- Support class Access Execution Engine
- Support class Access Execution Engine , described
topic_type:
- apiref
api_name:
- Support
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Support class

Provides status and progress reporting capability to assessments. Enables assessments access to configuration parameters that have been defined by the job author. The **Support** interface enables an assessment to retrieve pointers to other interfaces.

## When to implement

Never. This is an exposed interface that is already implemented.

## Inheritance

The **Support** interface inherits from [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509).

**Support** has these types of members:

-   [Methods](#methods)

### Methods

The **Support** class has these methods.



| Method                                                                     | Description                                                                                                                                                                |
|:---------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CancelTracing**](support-canceltracing.md)                             | Cancels tracing.<br/>                                                                                                                                                |
| [**CreateLogger**](support-createlogger.md)                               | Retrieves an instance of the [**Logging**](logging.md) interface.<br/>                                                                                              |
| [**CreateResultSnippet**](support-createresultsnippet-overl.md)           | Overloaded. Creates a result snippet.<br/>                                                                                                                           |
| [**GetCancelEvent**](support-getcancelevent.md)                           | Retrieves the handle to an event that Axe signals when a solution requests the assessment should stop running.<br/>                                                  |
| [**GetErrorText**](support-geterrortext.md)                               | Retrieves an Axe error message given the Axe error code.<br/>                                                                                                        |
| [**GetParameterSet**](support-getparameterset.md)                         | Retrieves the specified set of parameters.<br/>                                                                                                                      |
| [**IsCanceled**](support-iscanceled.md)                                   | Determines if there has been a request for the assessment to cancel its operation.<br/>                                                                              |
| [**IsEngineRunning**](support-isenginerunning.md)                         | Determines if the Axe engine is running, which tells an assessment if it is running under Axe.<br/>                                                                  |
| [**ManageSystemState**](support-managesystemstate.md)                     | Retrieves a [**SystemState**](systemstate.md) interface that is bound to a file use to save and restore the system configuration.<br/>                              |
| [**ProcessIdleTasks**](support-processidletasks.md)                       | Requests the system run the maintenance tasks scheduled to run when the system is idle. This prevents the maintenance tasks from running during the assessment.<br/> |
| [**RegisterEventManifest**](support-registereventmanifest-overl.md)       | Overloaded. Registers an event manifest.<br/>                                                                                                                        |
| [**ReportProgress**](support-reportprogress-overl.md)                     | Overloaded. Reports the progress of the assessment to the AXE engine and can inform the assessment if it should stop running.<br/>                                   |
| [**StartTracing**](support-starttracing.md)                               | Begins advanced ETW tracing using a Windows Performance Analyzer (WPA) profile.<br/>                                                                                 |
| [**StartTracingFromManifest**](support-starttracingfrommanifest-overl.md) | Overloaded. Starts tracing from the manifest.<br/>                                                                                                                   |
| [**StopTracing**](support-stoptracing.md)                                 | Finishes advanced ETW tracing using a Windows Performance Analyzer (WPA) profile.<br/>                                                                               |
| [**StopTracingFromManifest**](support-stoptracingfrommanifest.md)         | Stops tracing from the manifest.<br/>                                                                                                                                |
| [**SystemSettingCheckBoolean**](support-systemsettingcheckboolean.md)     | Retrieves the current setting of a specific system configuration item.<br/>                                                                                          |
| [**UnregisterEventManifest**](support-unregistereventmanifest-overl.md)   | Overloaded. Unregisters an event manifest.<br/>                                                                                                                      |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





