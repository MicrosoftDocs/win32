---
title: Engine SetAssessmentEnd method
description: Specifies the native interface for the Engine to invoke to notify the solution of an assessment end event.
ms.assetid: 2281ADC6-5B35-4EA8-B835-34FBDCF1F9BA
keywords:
- SetAssessmentEnd method Access Execution Engine
- SetAssessmentEnd method Access Execution Engine , Engine interface
- Engine interface Access Execution Engine , SetAssessmentEnd method
topic_type:
- apiref
api_name:
- Engine.SetAssessmentEnd
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

# Engine::SetAssessmentEnd method

Specifies the native interface for the [**Engine**](engine-if.md) to invoke to notify the solution of an assessment end event.

## Syntax


```C++
virtual HRESULT SetAssessmentEnd(
  [in, optional] IAssessmentEndEventHandler *assessmentEnd
) = 0;
```



## Parameters

<dl> <dt>

*assessmentEnd* \[in, optional\]
</dt> <dd>

The native interface invoked by [**Engine**](engine-if.md) when an assessment end event occurs. This parameter can be **NULL** to remove an existing handler.

</dd> </dl>

## Return value

If successful, the method returns **S\_OK**.

If a job is running, the method returns **AXE\_E\_JOB\_RUNNING**. Event handlers cannot be changed while a job is running.

If a there are events already queued with the Asynchronous Procedure Call mechanism in the operating system, the method returns **AXE\_E\_QUEUED\_APC\_EVENTS**. The threading model cannot be changed until these queued events are processed.

## Remarks

Managed code uses the [**Engine.AssessmentEnd \| assessmentend**](https://www.bing.com/search?q=**Engine.AssessmentEnd \| assessmentend**) event to notify solutions.

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

[**IAssessmentEndEventHandler**](iassessmentendeventhandler.md)
</dt> <dt>

[**OnAssessmentEnd**](ievents-onassessmentend.md)
</dt> </dl>

 

 





