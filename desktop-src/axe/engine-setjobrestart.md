---
title: Engine SetJobRestart method
description: Specifies the native interface for the Engine to invoke to notify the solution of a job restart event.
ms.assetid: '629314DA-DE2B-40B5-BB7C-D39853A18727'
keywords: ["SetJobRestart method Access Execution Engine", "SetJobRestart method Access Execution Engine , Engine interface", "Engine interface Access Execution Engine , SetJobRestart method"]
topic_type:
- apiref
api_name:
- Engine.SetJobRestart
api_location:
- AxeCore.dll
api_type:
- COM
---

# Engine::SetJobRestart method

Specifies the native interface for the [**Engine**](engine-if.md) to invoke to notify the solution of a job restart event.

## Syntax


```C++
HRESULT SetJobRestart(
  [in, optional] IJobRestartEventHandler *jobRestart
);
```



## Parameters

<dl> <dt>

*jobRestart* \[in, optional\]
</dt> <dd>

The native interface invoked by [**Engine**](engine-if.md) when job restart event occurs. This parameter can be **NULL** to remove an existing handler.

</dd> </dl>

## Return value

If successful, the method returns **S\_OK**.

If a job is running, the method returns **AXE\_E\_JOB\_RUNNING**. Event handlers cannot be changed while a job is running.

If a there are events already queued with the Asynchronous Procedure Call mechanism in the operating system, the method returns **AXE\_E\_QUEUED\_APC\_EVENTS**. The threading model cannot be changed until these queued events are processed.

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
</dt> </dl>

 

 





