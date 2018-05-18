---
Description: 'Defines the job priority constants.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '00af2e48-f931-4053-b0a4-fe8422602361'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: JobPriority enumeration
---

# JobPriority enumeration

Defines the job priority constants.

## Syntax


```C++
typedef enum  { 
  JobPriority_Lowest       = 0,
  JobPriority_BelowNormal  = 1,
  JobPriority_Normal       = 2,
  JobPriority_AboveNormal  = 3,
  JobPriority_Highest      = 4
} JobPriority;
```



## Constants

<dl> <dt>

<span id="JobPriority_Lowest"></span><span id="jobpriority_lowest"></span><span id="JOBPRIORITY_LOWEST"></span>**JobPriority\_Lowest**
</dt> <dd>

The job has the lowest priority.

</dd> <dt>

<span id="JobPriority_BelowNormal"></span><span id="jobpriority_belownormal"></span><span id="JOBPRIORITY_BELOWNORMAL"></span>**JobPriority\_BelowNormal**
</dt> <dd>

The job has below-normal priority.

</dd> <dt>

<span id="JobPriority_Normal"></span><span id="jobpriority_normal"></span><span id="JOBPRIORITY_NORMAL"></span>**JobPriority\_Normal**
</dt> <dd>

The job has normal priority.

</dd> <dt>

<span id="JobPriority_AboveNormal"></span><span id="jobpriority_abovenormal"></span><span id="JOBPRIORITY_ABOVENORMAL"></span>**JobPriority\_AboveNormal**
</dt> <dd>

The job has above-normal priority.

</dd> <dt>

<span id="JobPriority_Highest"></span><span id="jobpriority_highest"></span><span id="JOBPRIORITY_HIGHEST"></span>**JobPriority\_Highest**
</dt> <dd>

The job has the highest priority.

</dd> </dl>

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Enumerations](hpc-enumerations.md)
</dt> <dt>

[**ISchedulerJob.Priority**](ischedulerjob-priority.md)
</dt> </dl>

 

 




