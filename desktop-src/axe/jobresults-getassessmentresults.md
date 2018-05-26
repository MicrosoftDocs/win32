---
title: JobResults GetAssessmentResults method
description: Returns the AssessmentResultsCollection for the job.
ms.assetid: 61BC2EF7-449B-4D96-832D-ED7066E1982A
keywords:
- GetAssessmentResults method Access Execution Engine
- GetAssessmentResults method Access Execution Engine , JobResults interface
- JobResults interface Access Execution Engine , GetAssessmentResults method
topic_type:
- apiref
api_name:
- JobResults.GetAssessmentResults
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

# JobResults::GetAssessmentResults method

Returns the [**AssessmentResultsCollection**](assessmentresultscollection.md) for the job.

## Syntax


```C++
virtual HRESULT GetAssessmentResults(
  [out, optional] AssessmentResultsCollection **result
) const = 0;
```



## Parameters

<dl> <dt>

*result* \[out, optional\]
</dt> <dd>

The **AssessmentResultsCollection**.

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

[**JobResults**](jobresults.md)
</dt> </dl>

 

 





