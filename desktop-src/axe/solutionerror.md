---
title: SolutionError enumeration
description: Provides an enumeration of AXE errors that are pertinent to the Solution interface.
ms.assetid: B9EC0695-ED0E-4C4F-AB2D-E60399D847E0
keywords:
- SolutionError enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- SolutionError
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# SolutionError enumeration

Provides an enumeration of AXE errors that are pertinent to the Solution interface.

## Syntax


```C++
enum SolutionError {
  SolutionErrorNone                   = 0, 
  SolutionErrorAlreadyInit            = AXE_E_ALREADY_INIT, 
  SolutionErrorWorkloadInit           = AXE_E_WORKLOAD_INIT, 
  SolutionErrorInternalError          = AXE_E_INTERNAL_ERROR, 
  SolutionErrorUnknownWin32Error      = AXE_E_UNKNOWN_WIN32_ERROR, 
  SolutionErrorBadManifest            = AXE_E_BAD_MANIFEST, 
  SolutionErrorJobRunning             = AXE_E_JOB_RUNNING, 
  SolutionErrorJobNotRunning          = AXE_E_JOB_NOT_RUNNING, 
  SolutionErrorShellExecuteNoProcess  = AXE_E_SHELLEXECUTE_NOPROCESS, 
  SolutionErrorQueuedEvents           = AXE_E_QUEUED_APC_EVENTS 

};
```



## Constants

<dl> <dt>

<span id="SolutionErrorNone"></span><span id="solutionerrornone"></span><span id="SOLUTIONERRORNONE"></span>**SolutionErrorNone**
</dt> <dd>

0

No error has occurred.

</dd> <dt>

<span id="SolutionErrorAlreadyInit"></span><span id="solutionerroralreadyinit"></span><span id="SOLUTIONERRORALREADYINIT"></span>**SolutionErrorAlreadyInit**
</dt> <dd>

0x80040200

The Axecore.dll cannot be initialized in both assessment and solution modes in the same process. However, it can be initialized in assessment mode and then in workload mode within the same process

</dd> <dt>

<span id="SolutionErrorWorkloadInit"></span><span id="solutionerrorworkloadinit"></span><span id="SOLUTIONERRORWORKLOADINIT"></span>**SolutionErrorWorkloadInit**
</dt> <dd>

0x80040201

The Axecore.dll cannot be initialized by a solution in workload mode unless it is first initialized by an assessment.

</dd> <dt>

<span id="SolutionErrorInternalError"></span><span id="solutionerrorinternalerror"></span><span id="SOLUTIONERRORINTERNALERROR"></span>**SolutionErrorInternalError**
</dt> <dd>

0x80040202

An unexpected internal error occurred.

</dd> <dt>

<span id="SolutionErrorUnknownWin32Error"></span><span id="solutionerrorunknownwin32error"></span><span id="SOLUTIONERRORUNKNOWNWIN32ERROR"></span>**SolutionErrorUnknownWin32Error**
</dt> <dd>

0x80040203

An unknown Win32 system error occurred.

</dd> <dt>

<span id="SolutionErrorBadManifest"></span><span id="solutionerrorbadmanifest"></span><span id="SOLUTIONERRORBADMANIFEST"></span>**SolutionErrorBadManifest**
</dt> <dd>

0x80041000

The job manifest has bad or missing data.

</dd> <dt>

<span id="SolutionErrorJobRunning"></span><span id="solutionerrorjobrunning"></span><span id="SOLUTIONERRORJOBRUNNING"></span>**SolutionErrorJobRunning**
</dt> <dd>

0x80041005

The engine is running a job, and the requested operation is only possible when a job is not executing.

</dd> <dt>

<span id="SolutionErrorJobNotRunning"></span><span id="solutionerrorjobnotrunning"></span><span id="SOLUTIONERRORJOBNOTRUNNING"></span>**SolutionErrorJobNotRunning**
</dt> <dd>

0x80041006

The engine is not currently running a job, and the requested operation is only possible when a job is executing.

</dd> <dt>

<span id="SolutionErrorShellExecuteNoProcess"></span><span id="solutionerrorshellexecutenoprocess"></span><span id="SOLUTIONERRORSHELLEXECUTENOPROCESS"></span>**SolutionErrorShellExecuteNoProcess**
</dt> <dd>

0x80041011

The assessment manifest described a ShellExecute() statement that did not result in a new process being created that AXE could wait on to finish.

</dd> <dt>

<span id="SolutionErrorQueuedEvents"></span><span id="solutionerrorqueuedevents"></span><span id="SOLUTIONERRORQUEUEDEVENTS"></span>**SolutionErrorQueuedEvents**
</dt> <dd>

0x80041012

The registered event handlers cannot be changed while there are outstanding Asynchronous Procedure Calls (APCs) queued for the existing event handlers.

</dd> </dl>

## Remarks

Managed code uses the [**SolutionError**](https://www.bing.com/search?q=**SolutionError**) enum.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





