---
title: ErrorType enumeration
description: Specifies the types of errors that can occur in the Axe engine.
ms.assetid: '0111F168-0949-4B1F-8E44-AC226DC70978'
keywords: ["ErrorType enumeration Access Execution Engine"]
topic_type:
- apiref
api_name:
- ErrorType
api_location:
- AxeHosting.h
api_type:
- HeaderDef
---

# ErrorType enumeration

Specifies the types of errors that can occur in the Axe engine.

## Syntax


```C++
enum ErrorType {
  None                  = 0, 
  JobParsing            = 1, 
  AssessmentParsing     = 2, 
  AssessmentValidation  = 3, 
  AssessmentExecution   = 4 

};
```



## Constants

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None**
</dt> <dd>

No error type was specified. This is an invalid value.

</dd> <dt>

<span id="JobParsing"></span><span id="jobparsing"></span><span id="JOBPARSING"></span>**JobParsing**
</dt> <dd>

A problem occurred while parsing the job-specific portions of the job manifest XML file. Errors that occur in the assessment definitions contained within the job manifest will report an error type of AssessmentParsing. The associated error value will be the error returned by the XML parser.

</dd> <dt>

<span id="AssessmentParsing"></span><span id="assessmentparsing"></span><span id="ASSESSMENTPARSING"></span>**AssessmentParsing**
</dt> <dd>

A problem occurred while parsing the assessment-specific portion of the job manifest XML file. The associated error value will be the error returned by the XML parser.

</dd> <dt>

<span id="AssessmentValidation"></span><span id="assessmentvalidation"></span><span id="ASSESSMENTVALIDATION"></span>**AssessmentValidation**
</dt> <dd>

A problem occurred while validating one of the files for an assessment. The associated error value will describe the exact nature of the failure.

</dd> <dt>

<span id="AssessmentExecution"></span><span id="assessmentexecution"></span><span id="ASSESSMENTEXECUTION"></span>**AssessmentExecution**
</dt> <dd>

A problem occurred while executing an assessment. The associated error value will describe the exact nature of the failure.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





