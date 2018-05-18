---
Description: 'Retrieves a list of job template names defined in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e3c8ae66-32a3-4608-a139-513eaa3bc3bb'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::GetJobTemplateList method'
---

# IScheduler::GetJobTemplateList method

Retrieves a list of job template names defined in the cluster.

## Syntax


```C++
HRESULT GetJobTemplateList(
  [out] IStringCollection **pTemplates
);
```



## Parameters

<dl> <dt>

*pTemplates* \[out\]
</dt> <dd>

An [**IStringCollection**](istringcollection.md) interface that contains a collection of job template names.

</dd> </dl>

## Return value

If the method succeeds, the return value is **S\_OK**. Otherwise, the return value is an error code.

## Remarks

If you use the enumerator to enumerate each item in the collection, the item is a **VARIANT** of type **VT\_BSTR**. Query the **bstrVal** member for the template name.

## Requirements



|                         |                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This method was introduced in Windows HPC Server 2008 R2 Service Pack 2 (SP2) and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>                              |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**ISchedulerJob::JobTemplate**](ischedulerjob-jobtemplate.md)
</dt> <dt>

[**ISchedulerJob::SetJobTemplate**](ischedulerjob-setjobtemplate.md)
</dt> </dl>

 

 




