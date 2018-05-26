---
title: Job GetAssessment method
description: Retrieve a specific assessment from the job.
ms.assetid: 883CC3F7-1751-4800-821F-1B668C756F5D
keywords:
- GetAssessment method Access Execution Engine
- GetAssessment method Access Execution Engine , Job interface
- Job interface Access Execution Engine , GetAssessment method
topic_type:
- apiref
api_name:
- Job.GetAssessment
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

# Job::GetAssessment method

Retrieve a specific assessment from the job.

## Syntax


```C++
virtual HRESULT GetAssessment(
  [in]                  INT        assessmentIndex,
  [out, optional] const Assessment **assessment
) const = 0;
```



## Parameters

<dl> <dt>

*assessmentIndex* \[in\]
</dt> <dd>

The zero-based index of the assessment in the job manifest.

</dd> <dt>

*assessment* \[out, optional\]
</dt> <dd>

A pointer to receive the assessment. If the method fails, *assessment* will be **NULL**.

</dd> </dl>

## Return value

If the assessment object is created, the method returns **S\_OK**.

If the *assessment* pointer is **NULL**, the method returns **E\_POINTER**.

If the specified assessment index does not exist in the job. This is the **HRESULT** version of the Win32 error code, **ERROR\_RANGE\_NOT\_FOUND (0x80070284)**.

## Remarks

Managed code uses the [**Job.Item \| item property**](https://msdn.microsoft.com/library/windows/desktop/hh707538) property.

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
</dt> <dt>

[**Assessment**](assessment-inf.md)
</dt> </dl>

 

 





