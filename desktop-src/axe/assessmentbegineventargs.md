---
title: AssessmentBeginEventArgs structure
description: Represents information provided to a solution during the OnAssessmentBegin callback.
ms.assetid: FCE7FD87-EA7C-4ACF-ACF6-86188BDEA883
keywords:
- AssessmentBeginEventArgs structure Access Execution Engine
topic_type:
- apiref
api_name:
- AssessmentBeginEventArgs
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

# AssessmentBeginEventArgs structure

Represents information provided to a solution during the *OnAssessmentBegin* callback.

## Syntax


```C++
struct AssessmentBeginEventArgs {
  DWORD            Size;
  INT              AssessmentIndex;
  const Assessment *Assessment;
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

</dd> </dl>

## Remarks

The *AssessmentIndex* parameter can be used in a call to [**CancelAssessment**](engine-cancelassessment.md) to identify the correct assessment. This parameter is used to avoid a race condition where one assessment ends before the **CancelAssessment** method is received by the engine.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





