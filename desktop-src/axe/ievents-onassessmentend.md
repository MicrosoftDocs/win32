---
title: IAssessmentEndEventHandler OnAssessmentEnd method
description: The AXE Core raises this event to notify the solution that an assessment has ended.
ms.assetid: A89E0F08-3E2B-470E-8BA4-66CDDA77FB18
keywords:
- OnAssessmentEnd method Access Execution Engine
- OnAssessmentEnd method Access Execution Engine , IAssessmentEndEventHandler interface
- IAssessmentEndEventHandler interface Access Execution Engine , OnAssessmentEnd method
topic_type:
- apiref
api_name:
- IAssessmentEndEventHandler.OnAssessmentEnd
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

# IAssessmentEndEventHandler::OnAssessmentEnd method

The AXE Core raises this event to notify the solution that an assessment has ended.

## Syntax


```C++
virtual void OnAssessmentEnd(
             Engine                 *sender,
  [in] const AssessmentEndEventArgs *e
) = 0;
```



## Parameters

<dl> <dt>

*sender* 
</dt> <dd>

The [**Engine**](engine-if.md) object that raised the event.

</dd> <dt>

*e* \[in\]
</dt> <dd>

The [**AssessmentEndEventArgs**](assessmentendeventargs.md) structure that contains information about the assessment end event.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Managed code uses the [**AssessmentEndEventHandler**](https://www.bing.com/search?q=**AssessmentEndEventHandler**) delegate.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IAssessmentEndEventHandler**](iassessmentendeventhandler.md)
</dt> <dt>

[**AssessmentEndEventArgs**](assessmentendeventargs.md)
</dt> <dt>

[**CancelAssessment**](engine-cancelassessment.md)
</dt> <dt>

[**TerminateJob**](engine-terminatejob.md)
</dt> </dl>

 

 





