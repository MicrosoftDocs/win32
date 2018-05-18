---
Description: 'Retrieves the types of jobs that this node is configured to run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b7bb1559-7765-4cbc-9f39-cf8695ad377c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNode::JobType property'
---

# ISchedulerNode::JobType property

Retrieves the types of jobs that this node is configured to run.

This property is read-only.

## Syntax


```C++
HRESULT get_JobType(
  [out] JobType *pType
);
```



## Property value

The types of jobs that this node can run. For possible values, see the [**JobType**](jobtype.md) enumeration.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

A node can run more than one type of job. Treat the property value as an integer and the [**JobType**](jobtype.md) enumeration values as flags.

## Examples

For an example, see [Getting a List of Nodes in the Cluster](getting-a-list-of-nodes-in-the-cluster.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerNode**](ischedulernode.md)
</dt> </dl>

 

 




