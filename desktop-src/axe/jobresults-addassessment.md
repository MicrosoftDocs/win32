---
title: JobResults AddAssessment method
description: Adds an Assessment to this JobResults object.
ms.assetid: 'DAADAD29-CAA2-44D2-9F00-733AB73732D3'
keywords: ["AddAssessment method Access Execution Engine", "AddAssessment method Access Execution Engine , JobResults interface", "JobResults interface Access Execution Engine , AddAssessment method"]
topic_type:
- apiref
api_name:
- JobResults.AddAssessment
api_location:
- AxeCore.dll
api_type:
- COM
---

# JobResults::AddAssessment method

Adds an [**Assessment**](assessment-inf.md) to this **JobResults** object.

## Syntax


```C++
virtual HRESULT AddAssessment(
  [in] LPCWSTR path
) = 0;
```



## Parameters

<dl> <dt>

*path* \[in\]
</dt> <dd>

The path to the file that contains the assessment.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The method takes the path to the assessment manifest file and, if the assessment was executed, adds it to the **JobResults** object to be analyzed. The **JobResults** starts out empty.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**JobResults**](jobresults.md)
</dt> </dl>

 

 





