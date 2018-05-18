---
title: Job GetToolTip method
description: Retrieve a tool tip for the job.
ms.assetid: 'FCCBCB44-6C6D-436B-9B36-D7A64A027BF7'
keywords: ["GetToolTip method Access Execution Engine", "GetToolTip method Access Execution Engine , Job interface", "Job interface Access Execution Engine , GetToolTip method"]
topic_type:
- apiref
api_name:
- Job.GetToolTip
api_location:
- AxeCore.dll
api_type:
- COM
---

# Job::GetToolTip method

Retrieve a tool tip for the job.

## Syntax


```C++
virtual HRESULT GetToolTip(
  [out, optional] LPCWSTR *toolTip
) const = 0;
```



## Parameters

<dl> <dt>

*toolTip* \[out, optional\]
</dt> <dd>

A short description suitable for displaying in a tool tip control.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

Managed code uses [**Job.ToolTip \| toolTip**](axe-job_tooltip_om) property.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Job**](job-if.md)
</dt> </dl>

 

 





