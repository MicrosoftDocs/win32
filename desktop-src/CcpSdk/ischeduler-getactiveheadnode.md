---
Description: 'Retrieves the name of the active head node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4091DE7D-836C-4C43-A482-E7FE1BFEA856'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::GetActiveHeadNode method'
---

# IScheduler::GetActiveHeadNode method

Retrieves the name of the active head node.

## Syntax


```C++
HRESULT GetActiveHeadNode(
  [out] BSTR *headnodeName
);
```



## Parameters

<dl> <dt>

*headnodeName* \[out\]
</dt> <dd>

Retrieves a String that contains the name of the active head node.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Requirements



|                         |                                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------|
| Product<br/>      | This method was introduced in Windows HPC Pack 2012 and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>    |



 

 




