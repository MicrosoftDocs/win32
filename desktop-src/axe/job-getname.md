---
title: Job GetName method
description: Retrieve the name of the job as specified in the job manifest.
ms.assetid: DF56FEEB-4026-4B57-8F2D-ABFA876EF449
keywords:
- GetName method Access Execution Engine
- GetName method Access Execution Engine , Job interface
- Job interface Access Execution Engine , GetName method
topic_type:
- apiref
api_name:
- Job.GetName
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Job::GetName method

Retrieve the name of the job as specified in the job manifest.

## Syntax


```C++
virtual HRESULT GetName(
  [out, optional] LPCWSTR *jobName
) const = 0;
```



## Parameters

<dl> <dt>

*jobName* \[out, optional\]
</dt> <dd>

The name of the job.

</dd> </dl>

## Return value

This method always returns **S\_OK**.

## Remarks

Managed code uses the [**Job.Name**](axe-job_name_om) property.

## See also

<dl> <dt>

[**Job**](job-if.md)
</dt> </dl>

 

 




