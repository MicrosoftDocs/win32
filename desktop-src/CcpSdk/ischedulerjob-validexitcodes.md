---
Description: 'Retrieves or sets the exit codes to be used for checking whether tasks in the job successfully exit.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '02914348-8C38-4AAA-B6AE-25B04886FB79'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::ValidExitCodes property'
---

# ISchedulerJob::ValidExitCodes property

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

The exit codes that indicate whether tasks in the job successfully exited.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

Specifies the exit codes to be used for checking whether the task successfully exited. You can specify discrete integers and integer ranges separated by commas.

Integer ranges are denoted by integers separated by two periods. For example, 10..20 represents an integer range from ten to twenty.

The values **min** and **max** may be used to specify minimum and maximum integer values. For example, 0..max represents nonnegative integers.

## Requirements



|                         |                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This property was introduced in Windows HPC Pack 2012 and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>      |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




