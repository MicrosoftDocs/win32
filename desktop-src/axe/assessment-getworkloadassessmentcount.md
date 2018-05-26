---
title: Assessment GetWorkloadAssessmentCount method
description: Retrieves the number of assessments in the job.
ms.assetid: 58B8304C-C6EF-45E8-944F-2D9416AA9963
keywords:
- GetWorkloadAssessmentCount method Access Execution Engine
- GetWorkloadAssessmentCount method Access Execution Engine , Assessment interface
- Assessment interface Access Execution Engine , GetWorkloadAssessmentCount method
topic_type:
- apiref
api_name:
- Assessment.GetWorkloadAssessmentCount
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Assessment::GetWorkloadAssessmentCount method

Retrieves the number of assessments in the job.

## Syntax


```C++
virtual HRESULT GetWorkloadAssessmentCount(
  [out] INT *count
) const = 0;
```



## Parameters

<dl> <dt>

*count* \[out\]
</dt> <dd>

The number of workloads that will be run by the assessment.

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
</dt> </dl>

 

 





