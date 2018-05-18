---
Description: 'Defines the job priority constants.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fd5cd3ed-3ca7-41ac-ace2-0c80496a99bb'
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



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[CCP Enumerations](enumeration-types.md)
</dt> <dt>

[**IJob::get\_Priority**](ijob-get-priority.md)
</dt> <dt>

[**IJob::put\_Priority**](ijob-put-priority.md)
</dt> </dl>

 

 




