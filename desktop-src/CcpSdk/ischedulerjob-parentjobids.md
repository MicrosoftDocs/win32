---
Description: 'Retrieves or sets the list of parent job IDs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '633DC1E7-72FD-4066-90AD-3D731499CAA4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::ParentJobIds property'
---

# ISchedulerJob::ParentJobIds property

Retrieves or sets the list of parent job IDs.

This property is read/write.

## Syntax


```C++
HRESULT put_ParentJobIds(
  [in]  IIntCollection value
);

HRESULT get_ParentJobIds(
  [out] IIntCollection *pValue
);
```



## Property value

The collection of parent job IDs.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

> [!Note]  
> Child jobs will not begin until all parent jobs have completed.

 

## Requirements



|                         |                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This property was introduced in Windows HPC Pack 2012 and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>      |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




