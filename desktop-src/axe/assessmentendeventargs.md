---
title: AssessmentEndEventArgs structure
description: Represents information provided to a solution during the OnAssessmentEnd callback.
ms.assetid: 8C0F78DD-A222-4163-B267-B5BF130B369E
keywords:
- AssessmentEndEventArgs structure Access Execution Engine
topic_type:
- apiref
api_name:
- AssessmentEndEventArgs
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AssessmentEndEventArgs structure

Represents information provided to a solution during the *OnAssessmentEnd* callback.

## Syntax


```C++
struct AssessmentEndEventArgs {
  DWORD                    Size;
  INT                      AssessmentIndex;
  const Assessment         *Assessment;
  AssessmentExecutionError Error;
  const ErrorList          *ErrorList;
  INT                      ExitCode;
};
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The number of bytes in the structure. Used to detect different versions of structure.

</dd> <dt>

**AssessmentIndex**
</dt> <dd>

The index of the assessment in the job s assessment list.

</dd> <dt>

**Assessment**
</dt> <dd>

A pointer to the assessment object.

</dd> <dt>

**Error**
</dt> <dd>

The error that caused the assessment to end.

If the assessment process started successfully and exited normally, this value will be **S\_OK**.

If the assessment process started successfully and exited normally, but according to its manifest the exit code indicated the test failed, this value will be **AXE\_E\_ASSESSEMENT\_COMPLETED\_WITH\_ERROR**.

</dd> <dt>

**ErrorList**
</dt> <dd>

The value of the last error that occurred in processing the assessment, i.e. the last error in the assessment error list.

</dd> <dt>

**ExitCode**
</dt> <dd>

The exit code returned by the assessment process.

</dd> </dl>

## Remarks

The error parameter reflects AXE s efforts to execute the assessment. The exitCode is simply a direct copy of the value returned by the assessment s root process. The values are not related.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





