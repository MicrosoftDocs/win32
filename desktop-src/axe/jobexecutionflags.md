---
title: JobExecutionFlags enumeration
description: Specifies whether jobs are executed synchronously or asynchronously.
ms.assetid: '7793F06A-713B-4580-B72D-71A0A4582AE8'
keywords: ["JobExecutionFlags enumeration Access Execution Engine"]
topic_type:
- apiref
api_name:
- JobExecutionFlags
api_location:
- AxeHosting.h
api_type:
- HeaderDef
---

# JobExecutionFlags enumeration

Specifies whether jobs are executed synchronously or asynchronously.

## Syntax


```C++
enum JobExecutionFlags {
  None          = 0, 
  ExecuteAsync  = 1 

};
```



## Constants

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None**
</dt> <dd>

The job will be executed synchronously. The call to [**ExecuteJob**](engine-executejob.md) will not return until after the job has completed.

</dd> <dt>

<span id="ExecuteAsync"></span><span id="executeasync"></span><span id="EXECUTEASYNC"></span>**ExecuteAsync**
</dt> <dd>

The job will be executed asynchronously. The call to [**ExecuteJob**](engine-executejob.md) will return immediately. The caller must rely on registered event handlers to determine when the job completes.

</dd> </dl>

## Remarks

**JobExecutionFlags** are specified in the [**JobExecutionInfo**](jobexecutioninfo.md)::Flags field.

Managed code uses the [**JobExecutionFlags**](axe-jobexecutionflags_om) enum.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





