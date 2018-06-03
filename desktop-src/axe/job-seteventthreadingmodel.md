---
title: Engine SetEventThreadingModel method
description: Specifies the threading model that is being used to call the solution s native events that have been registered with the Engine.
ms.assetid: 0028E3FA-C6C4-499D-A330-94E8F4BC1E23
keywords:
- SetEventThreadingModel method Access Execution Engine
- SetEventThreadingModel method Access Execution Engine , Engine interface
- Engine interface Access Execution Engine , SetEventThreadingModel method
topic_type:
- apiref
api_name:
- Engine.SetEventThreadingModel
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

# Engine::SetEventThreadingModel method

Specifies the threading model that is being used to call the solution s native events that have been registered with the [**Engine**](engine-if.md).

## Syntax


```C++
virtual HRESULT SetEventThreadingModel(
  [in] ThreadingModel eventThreadingModel
) = 0;
```



## Parameters

<dl> <dt>

*eventThreadingModel* \[in\]
</dt> <dd>

The threading model to use when invoking the solution s callbacks. See the [**ThreadingModel**](threadingmodel.md) enumeration for details.

</dd> </dl>

## Return value

If successful, the method returns **S\_OK**.

If a job is running, the method returns **AXE\_E\_JOB\_RUNNING**. Event handlers cannot be changed while a job is running.

If a there are events already queued with the Asynchronous Procedure Call mechanism in the operating system, the method returns **AXE\_E\_QUEUED\_APC\_EVENTS**. The threading model cannot be changed until these queued events are processed.

If the specified threading model is not a valid [**ThreadingModel**](threadingmodel.md) enumerator, the method returns **E\_INVALIDARG**.

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

[**Job**](job-if.md)
</dt> </dl>

 

 





