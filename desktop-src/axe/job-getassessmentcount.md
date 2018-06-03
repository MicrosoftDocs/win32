---
title: Job GetAssessmentCount method
description: Retrieve the number of assessments in the job.
ms.assetid: B0769BC5-47CB-4E18-99B7-6B23463D6747
keywords:
- GetAssessmentCount method Access Execution Engine
- GetAssessmentCount method Access Execution Engine , Job interface
- Job interface Access Execution Engine , GetAssessmentCount method
topic_type:
- apiref
api_name:
- Job.GetAssessmentCount
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

# Job::GetAssessmentCount method

Retrieve the number of assessments in the job.

## Syntax


```C++
virtual HRESULT GetAssessmentCount(
  [out] INT *count
) const = 0;
```



## Parameters

<dl> <dt>

*count* \[out\]
</dt> <dd>

The number of assessments in the job.

</dd> </dl>

## Return value

The method always returns **S\_OK**.

## Remarks

Managed code uses the [**Job.AssessmentCount \| assessmentCount**](https://www.bing.com/search?q=**Job.AssessmentCount \| assessmentCount**) property.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Job**](job-if.md)
</dt> </dl>

 

 





