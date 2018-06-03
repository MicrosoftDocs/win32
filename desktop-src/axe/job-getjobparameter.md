---
title: Job GetJobParameter method
description: Retrieve the value of a specified job parameter.
ms.assetid: 46520170-E08A-40D2-97D5-7F3E5E9F37AD
keywords:
- GetJobParameter method Access Execution Engine
- GetJobParameter method Access Execution Engine , Job interface
- Job interface Access Execution Engine , GetJobParameter method
topic_type:
- apiref
api_name:
- Job.GetJobParameter
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

# Job::GetJobParameter method

Retrieve the value of a specified job parameter.

## Syntax


```C++
virtual HRESULT GetJobParameter(
  [in]            LPCWSTR parameterName,
  [out, optional] LPCWSTR *parameterValue
) const = 0;
```



## Parameters

<dl> <dt>

*parameterName* \[in\]
</dt> <dd>

The name of the parameter for which to retrieve the value.

</dd> <dt>

*parameterValue* \[out, optional\]
</dt> <dd>

The parameter value retrieved.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

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

 

 





