---
title: AssessmentError enumeration
description: Specifies errors returned in the AssessmentEndEvents event.
ms.assetid: C36A43ED-B860-4990-98BF-4849209D7BF5
keywords:
- AssessmentError enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- AssessmentError
api_location:
- AxeRuntime.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# AssessmentError enumeration

Specifies errors returned in the AssessmentEndEvents event.

## Syntax


```C++
enum AssessmentError {
  AssessmentErrorNone                       = 0, 
  AssessmentErrorAlreadyInit                = AXE_E_ALREADY_INIT, 
  AssessmentErrorInternalError              = AXE_E_INTERNAL_ERROR, 
  AssessmentErrorUnknownWin32Error          = AXE_E_WIN32_ERROR, 
  AssessmentErrorParameterConversionFailed  = AXE_E_PARAM_CONVERSION_FAILED, 
  AssessmentErrorEngineNotRunning           = AXE_E_PARAMETER_NOT_FOUND, 
  AssessmentErrorParameterNotFound          = AXE_E_ENGINE_NOT_RUNNING 

};
```



## Constants

<dl> <dt>

<span id="AssessmentErrorNone"></span><span id="assessmenterrornone"></span><span id="ASSESSMENTERRORNONE"></span>**AssessmentErrorNone**
</dt> <dd>

No error occurred.

</dd> <dt>

<span id="AssessmentErrorAlreadyInit"></span><span id="assessmenterroralreadyinit"></span><span id="ASSESSMENTERRORALREADYINIT"></span>**AssessmentErrorAlreadyInit**
</dt> <dd>

The [**AxeInitAssessment**](axeinitassessment.md) function was called multiple times.

</dd> <dt>

<span id="AssessmentErrorInternalError"></span><span id="assessmenterrorinternalerror"></span><span id="ASSESSMENTERRORINTERNALERROR"></span>**AssessmentErrorInternalError**
</dt> <dd>

An unspecified internal error occurred within Axe.

</dd> <dt>

<span id="AssessmentErrorUnknownWin32Error"></span><span id="assessmenterrorunknownwin32error"></span><span id="ASSESSMENTERRORUNKNOWNWIN32ERROR"></span>**AssessmentErrorUnknownWin32Error**
</dt> <dd>

An unknown error has occurred.

</dd> <dt>

<span id="AssessmentErrorParameterConversionFailed"></span><span id="assessmenterrorparameterconversionfailed"></span><span id="ASSESSMENTERRORPARAMETERCONVERSIONFAILED"></span>**AssessmentErrorParameterConversionFailed**
</dt> <dd>

The conversion of a parameter from one type to another failed.

</dd> <dt>

<span id="AssessmentErrorEngineNotRunning"></span><span id="assessmenterrorenginenotrunning"></span><span id="ASSESSMENTERRORENGINENOTRUNNING"></span>**AssessmentErrorEngineNotRunning**
</dt> <dd>

The assessment is attempting to use parts of the API that require the Axe engine to be running, but it is not.

</dd> <dt>

<span id="AssessmentErrorParameterNotFound"></span><span id="assessmenterrorparameternotfound"></span><span id="ASSESSMENTERRORPARAMETERNOTFOUND"></span>**AssessmentErrorParameterNotFound**
</dt> <dd>

The assessment requested a parameter whose name is not present in the assessment manifest.

</dd> </dl>

## Remarks

Managed code uses the [**AssessmentError**](https://www.bing.com/search?q=**AssessmentError**) enumeration.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |



 

 





