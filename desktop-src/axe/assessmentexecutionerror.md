---
title: AssessmentExecutionError enumeration
description: Provides an enumeration of AXE errors that are relevant to the execution of an assessment.
ms.assetid: 63B8CF87-D99B-4553-95D5-949C9B198C15
keywords:
- AssessmentExecutionError enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- AssessmentExecutionError
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# AssessmentExecutionError enumeration

Provides an enumeration of AXE errors that are relevant to the execution of an assessment.

## Syntax


```C++
enum AssessmentExecutionError {
  AssessmentExecutionErrorNone                = 0, 
  AssessmentExecutionErrorCouldNotStart       = AXE_E_ASSESSMENT_COULD_NOT_START, 
  AssessmentExecutionErrorCouldNotFinish      = AXE_E_ASSESSMENT_COULD_NOT_FINISH, 
  AssessmentExecutionErrorCompletedWithError  = AXE_E_ASSESSMENT_COMPLETED_WITH_ERROR, 
  AssessmentExecutionErrorResultsInvalid      = AXE_E_ASSESSMENT_RESULTS_INVALID, 
  AssessmentExecutionErrorCanceled            = AXE_E_ASSESSMENT_CANCELED, 
  AssessmentExecutionErrorTerminated          = AXE_E_ASSESSMENT_TERMINATED, 
  AssessmentExecutionErrorCrashed             = AXE_E_ASSESSMENT_CRASHED 

};
```



## Constants

<dl> <dt>

<span id="AssessmentExecutionErrorNone"></span><span id="assessmentexecutionerrornone"></span><span id="ASSESSMENTEXECUTIONERRORNONE"></span>**AssessmentExecutionErrorNone**
</dt> <dd>

0

The assessment ran successfully.

</dd> <dt>

<span id="AssessmentExecutionErrorCouldNotStart"></span><span id="assessmentexecutionerrorcouldnotstart"></span><span id="ASSESSMENTEXECUTIONERRORCOULDNOTSTART"></span>**AssessmentExecutionErrorCouldNotStart**
</dt> <dd>

0x80041009

AXE could not start the assessment process.

</dd> <dt>

<span id="AssessmentExecutionErrorCouldNotFinish"></span><span id="assessmentexecutionerrorcouldnotfinish"></span><span id="ASSESSMENTEXECUTIONERRORCOULDNOTFINISH"></span>**AssessmentExecutionErrorCouldNotFinish**
</dt> <dd>

0x8004100A

AXE encountered an error while waiting for the assessment process to finish.

</dd> <dt>

<span id="AssessmentExecutionErrorCompletedWithError"></span><span id="assessmentexecutionerrorcompletedwitherror"></span><span id="ASSESSMENTEXECUTIONERRORCOMPLETEDWITHERROR"></span>**AssessmentExecutionErrorCompletedWithError**
</dt> <dd>

0x8004100B

The assessment process started successfully and exited normally, but according to the assessment manifest, the exit code indicated the assessment failed.

</dd> <dt>

<span id="AssessmentExecutionErrorResultsInvalid"></span><span id="assessmentexecutionerrorresultsinvalid"></span><span id="ASSESSMENTEXECUTIONERRORRESULTSINVALID"></span>**AssessmentExecutionErrorResultsInvalid**
</dt> <dd>

0x8004100C

The assessment completed successfully, but there was an error processing the results files.

</dd> <dt>

<span id="AssessmentExecutionErrorCanceled"></span><span id="assessmentexecutionerrorcanceled"></span><span id="ASSESSMENTEXECUTIONERRORCANCELED"></span>**AssessmentExecutionErrorCanceled**
</dt> <dd>

0x8004100D

The assessment was canceled.

</dd> <dt>

<span id="AssessmentExecutionErrorTerminated"></span><span id="assessmentexecutionerrorterminated"></span><span id="ASSESSMENTEXECUTIONERRORTERMINATED"></span>**AssessmentExecutionErrorTerminated**
</dt> <dd>

0x8004100F

The assessment was terminated.

</dd> <dt>

<span id="AssessmentExecutionErrorCrashed"></span><span id="assessmentexecutionerrorcrashed"></span><span id="ASSESSMENTEXECUTIONERRORCRASHED"></span>**AssessmentExecutionErrorCrashed**
</dt> <dd>

0x80041010

The assessment crashed or caused a system reboot without first notifying AXE of an impending reboot.

</dd> </dl>

## Remarks

Managed code uses the [**AssessmentExecutionError**](https://www.bing.com/search?q=**AssessmentExecutionError**) enum.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





