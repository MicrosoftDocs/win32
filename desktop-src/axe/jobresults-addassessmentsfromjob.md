---
title: JobResults AddAssessmentsFromJob method
description: Adds Assessment objects to this JobResults object.
ms.assetid: C34CBC16-E49D-40F7-92F9-E8AFE8369F99
keywords:
- AddAssessmentsFromJob method Access Execution Engine
- AddAssessmentsFromJob method Access Execution Engine , JobResults interface
- JobResults interface Access Execution Engine , AddAssessmentsFromJob method
topic_type:
- apiref
api_name:
- JobResults.AddAssessmentsFromJob
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

# JobResults::AddAssessmentsFromJob method

Adds [**Assessment**](assessment-inf.md) objects to this **JobResults** object.

## Syntax


```C++
virtual HRESULT AddAssessmentsFromJob(
  [in] LPCWSTR path
) = 0;
```



## Parameters

<dl> <dt>

*path* \[in\]
</dt> <dd>

The path to the job manifest file that contains the assessments.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

All assessments in the job manifest file are added.

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

 

 





