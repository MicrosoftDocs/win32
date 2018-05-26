---
title: Engine CancelAssessment method
description: Requests that the specified assessment stop running.
ms.assetid: b8086414-1223-4a26-8eb5-b61301c87a29
keywords:
- CancelAssessment method Access Execution Engine
- CancelAssessment method Access Execution Engine , Engine interface
- Engine interface Access Execution Engine , CancelAssessment method
topic_type:
- apiref
api_name:
- Engine.CancelAssessment
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Engine::CancelAssessment method

Requests that the specified assessment stop running.

## Syntax


```C++
virtual HRESULT CancelAssessment(
   INT assessmentIndex
) = 0;
```



## Parameters

<dl> <dt>

*assessmentIndex* 
</dt> <dd>

The index of the assessment to cancel. The assessment can only be cancelled when it is running. An assessment s index is its position in the [**AssessmentRuns**](assessmentruns.md) section of the job manifest..

</dd> </dl>

## Return value

If successful, the method returns a value of **S\_OK**.

If *asmtIndex* parameter does not match the index of the currently running assessment, the method returns **AXE\_E\_INVALID\_INDEX**.

If AXE is not currently running a job, the method returns **AXE\_E\_NO\_JOB\_RUNNING**. The specified assessment must be running to be cancelled.

## Remarks

It is up to the assessment to support cancellation. If the assessment does not support cancellation, it will eventually exit on its own. If the solution wants to terminate the job if the assessment does not support cancellation, it is up to the solution to maintain its own timer and decide when to give up waiting for an assessment to cancel on its own.

Managed code uses [**Engine.CancelAssessment \| cancelAssessment**](axe-engine_cancelassessment_om) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Engine**](engine-if.md)
</dt> <dt>

[**CancelJob**](engine-canceljob.md)
</dt> <dt>

[**TerminateJob**](engine-terminatejob.md)
</dt> <dt>

[**GetCancelEvent**](support-getcancelevent.md)
</dt> <dt>

[**IsCanceled**](support-iscanceled.md)
</dt> </dl>

 

 





