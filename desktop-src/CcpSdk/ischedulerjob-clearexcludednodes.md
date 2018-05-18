---
Description: 'Removes all of the nodes in the list of nodes that should not be used for the job from that list.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'D06ADFFC-606C-4F61-8DB6-7A2A003F15CB'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::ClearExcludedNodes method'
---

# ISchedulerJob::ClearExcludedNodes method

Removes all of the nodes in the list of nodes that should not be used for the job from that list.

## Syntax


```C++
HRESULT ClearExcludedNodes();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

To remove specific nodes from the list of nodes that should not be used for the job, use the [**ISchedulerJob::RemoveExcludedNodes**](ischedulerjob-removeexcludednodes.md) method.

To confirm that the **ISchedulerJob::ClearExcludedNodes** method succeeded, check the value of the [**ISchedulerJob::ExcludedNodes**](ischedulerjob-excludednodes.md) property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::AddExcludedNodes**](ischedulerjob-addexcludednodes.md)
</dt> <dt>

[**ISchedulerJob::RemoveExcludedNodes**](ischedulerjob-removeexcludednodes.md)
</dt> <dt>

[**ISchedulerJob::ExcludedNodes**](ischedulerjob-excludednodes.md)
</dt> </dl>

 

 




