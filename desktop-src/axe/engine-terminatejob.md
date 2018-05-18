---
title: Engine TerminateJob method
description: This method ends an entire job without waiting for any assessment to exit.
ms.assetid: '5b20897b-c84e-4af2-a810-89da0e7dd72f'
keywords: ["TerminateJob method Access Execution Engine", "TerminateJob method Access Execution Engine , Engine interface", "Engine interface Access Execution Engine , TerminateJob method"]
topic_type:
- apiref
api_name:
- Engine.TerminateJob
api_location:
- AxeCore.dll
api_type:
- COM
---

# Engine::TerminateJob method

This method ends an entire job without waiting for any assessment to exit.

> [!Note]  
> **TerminateJob** ends the current assessment abruptly by calling the [**TerminateProcess**](https://msdn.microsoft.com/library/windows/desktop/ms686714) function, this can leave the system in an unrecoverable state. **TerminateJob** should be used only as a last resort.

 

## Syntax


```C++
virtual HRESULT TerminateJob() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the job is successfully terminated, the method returns **S\_OK**.

If AXE is not currently running a job, the method returns **AXE\_E\_NO\_JOB\_RUNNING**.

If the job was not terminated, the method returns **AXE\_E\_TERMINATE\_FAILED**.

## Remarks

Unlike the [**CancelAssessment**](engine-cancelassessment.md) and [**CancelJob**](engine-canceljob.md) methods, this is a synchronous call.

This method will still raise an assessment end and job end event.

Managed code uses the [**Engine.TerminateJob \| terminateJob**](axe-engine_terminatejob_om) method.

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

[**TerminateProcess**](https://msdn.microsoft.com/library/windows/desktop/ms686714)
</dt> </dl>

 

 





