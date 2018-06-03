---
title: Assessment GetWorkloadAssessment method
description: Retrieves the specified assessment.
ms.assetid: 54675CC2-6B39-41F4-8644-E5EE8895FAAC
keywords:
- GetWorkloadAssessment method Access Execution Engine
- GetWorkloadAssessment method Access Execution Engine , Assessment interface
- Assessment interface Access Execution Engine , GetWorkloadAssessment method
topic_type:
- apiref
api_name:
- Assessment.GetWorkloadAssessment
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

# Assessment::GetWorkloadAssessment method

Retrieves the specified assessment.

## Syntax


```C++
virtual HRESULT GetWorkloadAssessment(
  [in]                  INT        assessmentIndex,
  [out, optional] const Assessment **assessment
) const = 0;
```



## Parameters

<dl> <dt>

*assessmentIndex* \[in\]
</dt> <dd>

The position in the job manifest of the entry for the assessment that will be running as a solution assessment that executes workloads. This index is used to locate the nested [**AssessmentRuns**](assessmentruns.md) collection that describes the workloads to run. The index is zero-based. This field is ignored if the Solution API is not configured in Workload mode.

</dd> <dt>

*assessment* \[out, optional\]
</dt> <dd>

The assessment to be retrieved.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Assessment**](assessment-inf.md)
</dt> <dt>

[**SolutionFlags**](solutionflags.md)
</dt> </dl>

 

 





