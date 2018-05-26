---
title: Engine ExecuteJob method
description: Runs a loaded job.
ms.assetid: 3e2bf10d-e7a3-46bf-9280-e5c797845634
keywords:
- ExecuteJob method Access Execution Engine
- ExecuteJob method Access Execution Engine , Engine interface
- Engine interface Access Execution Engine , ExecuteJob method
topic_type:
- apiref
api_name:
- Engine.ExecuteJob
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

# Engine::ExecuteJob method

Runs a loaded job.

## Syntax


```C++
virtual HRESULT ExecuteJob(
  [in, out] JobExecutionInfo *JobInfo
) = 0;
```



## Parameters

<dl> <dt>

*JobInfo* \[in, out\]
</dt> <dd>

A structure that the AXE engine populates with the results of the job. AXE completely overwrites this structure s contents.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

This method executes an entire job using the information specified in the [**JobExecutionInfo**](jobexecutioninfo.md) structure.

Managed code uses the [**Engine.ExecuteJob \| executeJob**](axe-engine_executejob_om) method

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Engine**](engine-if.md)
</dt> <dt>

[**JobExecutionInfo**](jobexecutioninfo.md)
</dt> <dt>

[**JobEndEventArgs**](jobendeventargs.md)
</dt> </dl>

 

 





