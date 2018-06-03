---
title: Engine SetProgressUpdate method
description: Specifies the native interface for the Engine to invoke to notify the solution of a progress update event.
ms.assetid: 1A10C751-072A-42E6-9A80-2416B82309BF
keywords:
- SetProgressUpdate method Access Execution Engine
- SetProgressUpdate method Access Execution Engine , Engine interface
- Engine interface Access Execution Engine , SetProgressUpdate method
topic_type:
- apiref
api_name:
- Engine.SetProgressUpdate
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Engine::SetProgressUpdate method

Specifies the native interface for the [**Engine**](engine-if.md) to invoke to notify the solution of a progress update event.

## Syntax


```C++
virtual HRESULT SetProgressUpdate(
  [in, optional] IProgressUpdateEventHandler *progressUpdate
) = 0;
```



## Parameters

<dl> <dt>

*progressUpdate* \[in, optional\]
</dt> <dd>

The native interface invoked by [**Engine**](engine-if.md) when an progress update event occurs. This parameter can be **NULL** to remove an existing handler.

</dd> </dl>

## Return value

If successful, the method returns **S\_OK**.

If a job is running, the method returns **AXE\_E\_JOB\_RUNNING**. Event handlers cannot be changed while a job is running.

If a there are events already queued with the Asynchronous Procedure Call mechanism in the operating system, the method returns **AXE\_E\_QUEUED\_APC\_EVENTS**. The threading model cannot be changed until these queued events are processed.

## Remarks

Managed code uses the [**Engine.ProgressUpdate \| progressupdate**](https://www.bing.com/search?q=**Engine.ProgressUpdate \| progressupdate**) event.

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

[**OnProgressUpdate**](ievents-onprogressupdate.md)
</dt> </dl>

 

 





