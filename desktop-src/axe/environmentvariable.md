---
title: EnvironmentVariable
description: Defines the names of environment variables that the AXE engine creates in the process space for assessments.
ms.assetid: 736E4BB7-AF15-40E1-A49C-E76878621EEA
topic_type:
- apiref
api_name:
- AssessmentExecutionPath
- AssessmentResultsPath
- AssessmentTempPath
- AssessmentJobFile
- AssessmentAxeBinPath
- AssessmentUniqueSession
- AssessmentRebootIteration
- AssessmentRunIndex
api_location:
- AxeRuntime.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EnvironmentVariable

Defines the names of environment variables that the AXE engine creates in the process space for assessments.

<dl> <dt>

<span id="AssessmentExecutionPath"></span><span id="assessmentexecutionpath"></span><span id="ASSESSMENTEXECUTIONPATH"></span>**AssessmentExecutionPath**
</dt> <dd> <dl> <dt>


</dt> <dt>



The assessment execution path. At execution time it is the same as the assessment results path; at analysis time, the execution path remains the same, but the results path is an empty folder where analysis results are to be placed.


</dt> </dl> </dd> <dt>

<span id="AssessmentResultsPath"></span><span id="assessmentresultspath"></span><span id="ASSESSMENTRESULTSPATH"></span>**AssessmentResultsPath**
</dt> <dd> <dl> <dt>


</dt> <dt>



The path where the assessment is to create its result files. At analysis time, the results path is an empty folder where analysis results are to be placed.


</dt> </dl> </dd> <dt>

<span id="AssessmentTempPath"></span><span id="assessmenttemppath"></span><span id="ASSESSMENTTEMPPATH"></span>**AssessmentTempPath**
</dt> <dd> <dl> <dt>


</dt> <dt>



The path the assessment can use to create and store temporary files. This path is deleted after the job finishes.


</dt> </dl> </dd> <dt>

<span id="AssessmentJobFile"></span><span id="assessmentjobfile"></span><span id="ASSESSMENTJOBFILE"></span>**AssessmentJobFile**
</dt> <dd> <dl> <dt>


</dt> <dt>



The path to the job file that contains the assessment that are being executed.


</dt> </dl> </dd> <dt>

<span id="AssessmentAxeBinPath"></span><span id="assessmentaxebinpath"></span><span id="ASSESSMENTAXEBINPATH"></span>**AssessmentAxeBinPath**
</dt> <dd> <dl> <dt>


</dt> <dt>



The path to the AxeCore.dll.


</dt> </dl> </dd> <dt>

<span id="AssessmentUniqueSession"></span><span id="assessmentuniquesession"></span><span id="ASSESSMENTUNIQUESESSION"></span>**AssessmentUniqueSession**
</dt> <dd> <dl> <dt>


</dt> <dt>



A unique identifier for the assessment that is valid as long as the assessment is running.


</dt> </dl> </dd> <dt>

<span id="AssessmentRebootIteration"></span><span id="assessmentrebootiteration"></span><span id="ASSESSMENTREBOOTITERATION"></span>**AssessmentRebootIteration**
</dt> <dd> <dl> <dt>


</dt> <dt>



The number of times the system has restarted while the assessment has been running.


</dt> </dl> </dd> <dt>

<span id="AssessmentRunIndex"></span><span id="assessmentrunindex"></span><span id="ASSESSMENTRUNINDEX"></span>**AssessmentRunIndex**
</dt> <dd> <dl> <dt>


</dt> <dt>



The 0-based index of the current assessment in the list of assessments contained within the job.


</dt> </dl> </dd> </dl>

## Remarks

These constants are guaranteed to exist in a collection retrieved with a call to [**GetParameterSet**](support-getparameterset.md).

The Session parameters are valid for a single instance of the Axe engine and job execution. The values may change between job runs.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |



 

 





