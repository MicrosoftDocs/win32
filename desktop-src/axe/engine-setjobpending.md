---
title: Engine SetJobPending method
description: Specifies the native interface for the Engine to invoke to notify the solution of a job pending event.
ms.assetid: '68A504D7-DADC-47A8-B6B9-B7E9468B1D2E'
keywords: ["SetJobPending method Access Execution Engine", "SetJobPending method Access Execution Engine , Engine interface", "Engine interface Access Execution Engine , SetJobPending method"]
topic_type:
- apiref
api_name:
- Engine.SetJobPending
api_location:
- AxeCore.dll
api_type:
- COM
---

# Engine::SetJobPending method

Specifies the native interface for the [**Engine**](engine-if.md) to invoke to notify the solution of a job pending event.

## Syntax


```C++
virtual HRESULT SetJobPending(
  [in, optional] IJobPendingEventHandler *jobPending
) = 0;
```



## Parameters

<dl> <dt>

*jobPending* \[in, optional\]
</dt> <dd>

The native interface invoked by [**Engine**](engine-if.md) when job pending event occurs. This parameter can be **NULL** to remove an existing handler.

</dd> </dl>

## Return value

If successful, the method returns **S\_OK**.

If a job is running, the method returns **AXE\_E\_JOB\_RUNNING**. Event handlers cannot be changed while a job is running.

If a there are events already queued with the Asynchronous Procedure Call mechanism in the operating system, the method returns **AXE\_E\_QUEUED\_APC\_EVENTS**. The threading model cannot be changed until these queued events are processed.

## Remarks

Managed code uses the [**Engine.JobPending \| jobpending**](axe-engine_jobpending_om) event.

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

[**IJobPendingEventHandler**](ijobpendingeventhandler.md)
</dt> <dt>

[**OnJobPending**](ijobpendingeventhandler-onjobpending.md)
</dt> </dl>

 

 





