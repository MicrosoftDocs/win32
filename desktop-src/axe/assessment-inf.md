---
title: Assessment class
description: Describes and provides information about an individual assessment.
ms.assetid: 3B576600-EF77-46A7-81DC-C2E610E4CA97
keywords:
- Assessment class Access Execution Engine
- Assessment class Access Execution Engine , described
topic_type:
- apiref
api_name:
- Assessment
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

# Assessment class

Describes and provides information about an individual assessment.

## When to implement

Never. This interface is implemented by the AXE engine.

**Assessment** has these types of members:

-   [Methods](#methods)

### Methods

The **Assessment** class has these methods.



| Method                                                                      | Description                                                                                                        |
|:----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
| [**~Assessment**](assessment--assessment.md)                               | Destructor method.<br/>                                                                                      |
| [**GetFilePath**](assessment-getfilepath.md)                               | Returns the file path for the assessment.<br/>                                                               |
| [**GetId**](assessment-getid.md)                                           | Returns the ID of the assessment, a GUID.<br/>                                                               |
| [**GetName**](assessment-getname.md)                                       | Retrieve the localized name of the assessment.<br/>                                                          |
| [**GetProgrammaticName**](assessment-getprogrammaticname.md)               | Returns the programmatic name of the assessment.<br/>                                                        |
| [**GetSupportsAnalyze**](assessment-getsupportsanalyze.md)                 | Returns an indicator of whether the assessment supports re-analysis (analysis separate from execution).<br/> |
| [**GetToolTip**](assessment-gettooltip.md)                                 | Retrieve the short description of the assessment. <br/>                                                      |
| [**GetWorkloadAssessment**](assessment-getworkloadassessment.md)           | Retrieves the specified assessment.<br/>                                                                     |
| [**GetWorkloadAssessmentCount**](assessment-getworkloadassessmentcount.md) | Retrieves the number of assessments in the job.<br/>                                                         |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Execution Solution Interfaces**](execution-solution-interfaces.md)
</dt> </dl>

 

 





