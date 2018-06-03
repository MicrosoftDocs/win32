---
title: IAssessmentBeginEventHandler OnAssessmentBegin method
description: The AXE Core raises this event to notify the solution that an assessment has started.
ms.assetid: 24DCC923-A20F-4E4D-916A-81477AA37BA3
keywords:
- OnAssessmentBegin method Access Execution Engine
- OnAssessmentBegin method Access Execution Engine , IAssessmentBeginEventHandler interface
- IAssessmentBeginEventHandler interface Access Execution Engine , OnAssessmentBegin method
topic_type:
- apiref
api_name:
- IAssessmentBeginEventHandler.OnAssessmentBegin
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

# IAssessmentBeginEventHandler::OnAssessmentBegin method

The AXE Core raises this event to notify the solution that an assessment has started.

## Syntax


```C++
virtual void OnAssessmentBegin(
             Engine                   *sender,
  [in] const AssessmentBeginEventArgs *e
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

The [**AssessmentBeginEventArgs**](assessmentbegineventargs.md) structure that contains information about the assessment begin event.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Managed codes uses the [**AssessmentBeginEventHandler**](https://www.bing.com/search?q=**AssessmentBeginEventHandler**) delegate.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IAssessmentBeginEventHandler**](iassessmentbegineventhandler.md)
</dt> <dt>

[**AssessmentBeginEventArgs**](assessmentbegineventargs.md)
</dt> </dl>

 

 





