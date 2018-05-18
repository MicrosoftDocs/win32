---
Description: 'Retrieves or sets the exit codes to be used for checking whether tasks in the job successfully exit.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '51BD1EEE-9B5C-48DE-A5D7-F65B8B639BA2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::ValidExitCodes property'
---

# ISchedulerTask::ValidExitCodes property

Retrieves or sets the exit codes to be used for checking whether tasks in the job successfully exit.

This property is read/write.

## Syntax


```C++
HRESULT put_ValidExitCodes(
  [in]  BSTR value
);

HRESULT get_ValidExitCodes(
  [out] BSTR *pValue
);
```



## Property value

The exit codes that indicate whether task successfully exited.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

Specifies the exit codes to be used for checking whether the task successfully exited. You can specify discrete integers and integer ranges separated by commas.

Integer ranges are denoted by integers separated by two periods. For example, 10..20 represents an integer range from ten to twenty.

**min** and **max** may be used to specify minimum and maximum integer values. For example, 0..max represents nonnegative integers.

> [!Note]  
> The **ISchedulerTask::ValidExitCodes** property overrides the job success exit codes specified by the [**ISchedulerJob::ValidExitCodes**](ischedulerjob-validexitcodes.md) property.

 

## Requirements



|                         |                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This property was introduced in Windows HPC Pack 2012 and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>      |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




