---
title: SessionParameter
description: Defines the names of parameters that exist in the Session parameter collection.
ms.assetid: '21682C94-EDEB-4E25-B694-8A3D8F234608'
topic_type:
- apiref
api_name:
- ExecutionPath
- ResultsPath
- TempPath
- JobFile
- AxeBinPath
- UniqueSession
- RebootIteration
- RunIndex
api_location:
- AxeRuntime.h
api_type:
- HeaderDef
---

# SessionParameter

Defines the names of parameters that exist in the Session parameter collection.

<dl> <dt>

<span id="ExecutionPath"></span><span id="executionpath"></span><span id="EXECUTIONPATH"></span>**ExecutionPath**
</dt> <dd> <dl> <dt>


</dt> <dt>



The assessment execution path. At execution time it is the same as the assessment results path; at analysis time, the execution path remains the same, but the results path is an empty folder where analysis results are to be placed.


</dt> </dl> </dd> <dt>

<span id="ResultsPath"></span><span id="resultspath"></span><span id="RESULTSPATH"></span>**ResultsPath**
</dt> <dd> <dl> <dt>


</dt> <dt>



Assessments can use this parameter to determine where their own results should be placed. After each assessment finishes running, its single "Results.xml" file is integrated with the overall job "Results.xml" file. When all assessments are finished running, the results path for all assessments will be packaged up with the results from all the other assessments in the job in a final results package.

An assessment should produce one or more results files conforming to the AXE Results Schema Design in this directory.


</dt> </dl> </dd> <dt>

<span id="TempPath"></span><span id="temppath"></span><span id="TEMPPATH"></span>**TempPath**
</dt> <dd> <dl> <dt>


</dt> <dt>



Assessments can use this parameter to determine where it can store temporary data and state while the assessment is running. For example, if the assessment includes rebooting the system, the assessment needs to record its state before rebooting the system so it knows where to resume when the assessment is invoked again. Such state information should be recorded in this temporary location.

AXE will use the standard Windows Temporary directory as root. This lets Windows clean up temporary data in case AXE fails to due to a crash or other failure.

AXE will recursively delete all the data in this directory after the assessment as exited. Note that there is a job flag that disables this deletion. This is designed for debugging assessment problems during development.


</dt> </dl> </dd> <dt>

<span id="JobFile"></span><span id="jobfile"></span><span id="JOBFILE"></span>**JobFile**
</dt> <dd> <dl> <dt>


</dt> <dt>



The fully qualified path to the job file that contains the assessments that are being executed.


</dt> </dl> </dd> <dt>

<span id="AxeBinPath"></span><span id="axebinpath"></span><span id="AXEBINPATH"></span>**AxeBinPath**
</dt> <dd> <dl> <dt>


</dt> <dt>



The path to the AxeCore.dll.


</dt> </dl> </dd> <dt>

<span id="UniqueSession"></span><span id="uniquesession"></span><span id="UNIQUESESSION"></span>**UniqueSession**
</dt> <dd> <dl> <dt>


</dt> <dt>



A unique identifier for the assessment that is valid as long as the assessment is running.


</dt> </dl> </dd> <dt>

<span id="RebootIteration"></span><span id="rebootiteration"></span><span id="REBOOTITERATION"></span>**RebootIteration**
</dt> <dd> <dl> <dt>


</dt> <dt>



The number of times the system has restarted while the assessment has been running.


</dt> </dl> </dd> <dt>

<span id="RunIndex"></span><span id="runindex"></span><span id="RUNINDEX"></span>**RunIndex**
</dt> <dd> <dl> <dt>


</dt> <dt>



The 0-based index of the current assessment in the list of assessments contained within the job.


</dt> </dl> </dd> </dl>

## Remarks

These parameters are guaranteed to exist in a parameter collection retrieved with a call to [**GetParameterSet**](support-getparameterset.md). In addition, environment variables with the same name prefixed by "Assessment" exist in the process space for the assessment while it is executing. For example, "AssessmentResultsPath", "AssessmentTempPath", etc.

The Session parameters are valid for a single instance of the Axe engine and job execution. The values may change between job runs.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |



 

 





