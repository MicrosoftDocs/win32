---
title: AssessmentResults class
description: This interface provides access to AssessmentResults objects.
ms.assetid: 2682566D-552F-44CD-939E-304E7F6E73C5
keywords:
- AssessmentResults class Access Execution Engine
- AssessmentResults class Access Execution Engine , described
topic_type:
- apiref
api_name:
- AssessmentResults
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# AssessmentResults class

This interface provides access to **AssessmentResults** objects.

**AssessmentResults** has these types of members:

-   [Methods](#methods)

### Methods

The **AssessmentResults** class has these methods.



| Method                                                             | Description                                                                                        |
|:-------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**~AssessmentResults**](assessmentresults--assessmentresults.md) | Destructor method.<br/>                                                                      |
| [**GetAssessment**](assessmentresults-getassessment.md)           | Returns the [**Assessment**](assessment-inf.md) for this **AssessmentResults** object.<br/> |
| [**GetCanBeAnalyzed**](assessmentresults-getcanbeanalyzed.md)     | Returns the cannot analyze reason for this **AssessmentResults** object.<br/>                |
| [**GetToBeAnalyzed**](assessmentresults-gettobeanalyzed.md)       | Returns the indicator of whether the assessment results are to be analyzed.<br/>             |
| [**SetToBeAnalyzed**](assessmentresults-settobeanalyzed.md)       | Sets the indicator of whether the assessment results are to be analyzed.<br/>                |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





