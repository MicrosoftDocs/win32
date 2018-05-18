---
Description: 'Retrieves or sets the operator for the node group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2A286DCD-47C0-4597-A782-BA693A306377'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::NodeGroupOp property'
---

# ISchedulerJob::NodeGroupOp property

Retrieves or sets the operator for the node group.

This property is read/write.

## Syntax


```C++
HRESULT put_NodeGroupOp(
  [in]  long value
);

HRESULT get_NodeGroupOp(
  [out] long *pValue
);
```



## Property value

The operator for the node group.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

The NodeGroupOp property stores the group operation, for this job which is a member of the JobNodeGroupOp enum. Valid values are Intersect which signifies that nodes belong to all of the specified node groups, Uniform which signifies that nodes belong to only one of the specified node groups, and Union which signifies that nodes belong to any of the specified node groups.

## Requirements



|                         |                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This property was introduced in Windows HPC Pack 2012 and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>      |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




