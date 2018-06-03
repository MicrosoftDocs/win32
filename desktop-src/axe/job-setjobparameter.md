---
title: Job SetJobParameter method
description: Creates or updates a job parameter with the specified name and value.
ms.assetid: 2FFF7E3C-1171-4E5F-BDB5-32E853CB17A4
keywords:
- SetJobParameter method Access Execution Engine
- SetJobParameter method Access Execution Engine , Job interface
- Job interface Access Execution Engine , SetJobParameter method
topic_type:
- apiref
api_name:
- Job.SetJobParameter
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

# Job::SetJobParameter method

Creates or updates a job parameter with the specified name and value.

## Syntax


```C++
virtual HRESULT SetJobParameter(
  [in] LPCWSTR parameterName,
  [in] LPCWSTR parameterValue
) = 0;
```



## Parameters

<dl> <dt>

*parameterName* \[in\]
</dt> <dd>

The name of the parameter to create or update.

</dd> <dt>

*parameterValue* \[in\]
</dt> <dd>

A string value giving the new value of the parameter. This parameter cannot be **NULL**.

</dd> </dl>

## Return value

If successful this method returns **S\_OK**.

The engine is currently running the job. Parameters can only be set or changed when the job is not running. **AXE\_E\_JOB\_RUNNING**

If specified parameter is read-only, this medod returns **AXE\_E\_PARAM\_READ\_ONLY**.

If there is insufficient memory to set the parameter, this method returns **E\_OUTOFMEMORY**.

If *parameterValue* was **NULL**, then this method returns **E\_POINTER**.

## Remarks

Managed code uses [**Job.JobParameter \| jobParameter**](https://msdn.microsoft.com/library/windows/desktop/hh707539) property.

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

 

 





