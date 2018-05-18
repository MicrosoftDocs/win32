---
Description: 'Specifies the operator for the NodeGroups list.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '801CC533-27A1-400B-810F-9E443A1E8FEA'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: JobNodeGroupOp enumeration
---

# JobNodeGroupOp enumeration

Specifies the operator for the NodeGroups list.

## Syntax


```C++
typedef enum _JobNodeGroupOp { 
  Intersect  = 0,
  Uniform    = 1,
  Union      = 2
} JobNodeGroupOp;
```



## Constants

<dl> <dt>

<span id="Intersect"></span><span id="intersect"></span><span id="INTERSECT"></span>**Intersect**
</dt> <dd>

Nodes belong to all of the specified node groups. This is the default.

</dd> <dt>

<span id="Uniform"></span><span id="uniform"></span><span id="UNIFORM"></span>**Uniform**
</dt> <dd>

Nodes belong to only one of the specified node groups.

</dd> <dt>

<span id="Union"></span><span id="union"></span><span id="UNION"></span>**Union**
</dt> <dd>

Nodes belong to any of the specified node groups.

</dd> </dl>

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This parameter was introduced in HPC Pack 2012. It is not available in previous versions.<br/>              |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Enumerations](hpc-enumerations.md)
</dt> <dt>

[**ISchedulerJob.Priority**](ischedulerjob-priority.md)
</dt> </dl>

 

 




