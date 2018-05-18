---
Description: 'Retrieves the list of nodes that are allocated to the job or task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cc8722c0-13a1-4120-81b5-6ff2a981172b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IResourceUsage::get\_AllocatedNodes method'
---

# IResourceUsage::get\_AllocatedNodes method

Retrieves the list of nodes that are allocated to the job or task.

## Syntax


```C++
HRESULT get_AllocatedNodes(
  [out] INameValueCollection **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**INameValueCollection**](inamevaluecollection.md) interface that contains a list of nodes that are allocated to the job or task. To enumerate the list of [**INameValue**](inamevalue.md) interfaces, call the [**INameValueCollection::GetEnumerator**](inamevaluecollection-getenumerator.md) method.

The name member of the name/value pair contains the name of the node, and the value member contains the number of processors on the node.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

For a task, the list of required nodes (see [**ITask::put\_RequiredNodes**](itask-put-requirednodes.md)), or if you did not specify required nodes, the node on which the task ran.

For a job, the list of nodes that you requested for the job (see [**IJob::put\_AskedNodes**](ijob-put-askednodes.md)), or if you did not request nodes, the list of all nodes in the cluster.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IResourceUsage**](iresourceusage.md)
</dt> </dl>

 

 




