---
title: Engine CancelJob method
description: Requests that the current assessment stop running and the job end without running any more assessments.
ms.assetid: '9bed9ff8-9e35-4bfc-9839-3d094f7564de'
keywords: ["CancelJob method Access Execution Engine", "CancelJob method Access Execution Engine , Engine interface", "Engine interface Access Execution Engine , CancelJob method"]
topic_type:
- apiref
api_name:
- Engine.CancelJob
api_location:
- AxeCore.dll
api_type:
- COM
---

# Engine::CancelJob method

Requests that the current assessment stop running and the job end without running any more assessments.

## Syntax


```C++
virtual HRESULT CancelJob() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the cancel request is signaled successfully, the method returns **S\_OK**.

If AXE is not currently running a job, the method returns **AXE\_E\_NO\_JOB\_RUNNING**.

## Remarks

This method cancels the entire job. Once the currently running assessment completes, no further assessments are run for the job, and the job terminates with the cancellation error.

Managed code uses the [**Engine.CancelJob \| cancelJob**](axe-engine_canceljob_om) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Engine**](engine-if.md)
</dt> <dt>

[**CancelAssessment**](engine-cancelassessment.md)
</dt> <dt>

[**TerminateJob**](engine-terminatejob.md)
</dt> </dl>

 

 





