---
Description: 'Retrieves the list of compute nodes in a cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e198ab79-082e-4753-96f3-05ab5e7627ee'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::get\_ComputeNodes method'
---

# ICluster::get\_ComputeNodes method

Retrieves the list of compute nodes in a cluster.

## Syntax


```C++
HRESULT get_ComputeNodes(
  [out] IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the list of compute nodes in a cluster. The order of the nodes in the collection is arbitrary. The collection will always contain at least one item for the head node. The variant type is VT\_DISPATCH. Query the **pdispVal** member of the variant for the [**INode**](inode.md) interface.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Examples

For an example that calls this method, see [Getting the List of Nodes in the Cluster](getting-the-list-of-nodes-in-the-cluster.md).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::ApproveNode**](icluster-approvenode.md)
</dt> <dt>

[**ICluster::PauseNode**](icluster-pausenode.md)
</dt> <dt>

[**ICluster::ResumeNode**](icluster-resumenode.md)
</dt> <dt>

[**INode**](inode.md)
</dt> </dl>

 

 




