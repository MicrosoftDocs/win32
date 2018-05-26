---
title: AssessmentResults GetAssessment method
description: Returns the Assessment for this AssessmentResults object.
ms.assetid: 326C24D3-F4B1-4FD6-BCC8-1B9AEE8F17EE
keywords:
- GetAssessment method Access Execution Engine
- GetAssessment method Access Execution Engine , AssessmentResults interface
- AssessmentResults interface Access Execution Engine , GetAssessment method
topic_type:
- apiref
api_name:
- AssessmentResults.GetAssessment
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

# AssessmentResults::GetAssessment method

Returns the [**Assessment**](assessment-inf.md) for this **AssessmentResults** object.

## Syntax


```C++
virtual HRESULT GetAssessment(
  [out] const Assessment **assessment
) const = 0;
```



## Parameters

<dl> <dt>

*assessment* \[out\]
</dt> <dd>

The **Assessment**.

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

[**AssessmentResults**](assessmentresults-struct.md)
</dt> </dl>

 

 





