---
Description: 'Approves the addition of the specified node to the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4c39110c-9d99-48e4-bffb-ba9ccf36281e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::ApproveNode method'
---

# ICluster::ApproveNode method

Approves the addition of the specified node to the cluster.

## Syntax


```C++
HRESULT ApproveNode(
  [in] BSTR NodeName
);
```



## Parameters

<dl> <dt>

*NodeName* \[in\]
</dt> <dd>

The name of the node. Do not use the fully qualified domain name. The node has to be in the same domain as the head node that you [connected](icluster-connect.md) to.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

You call this method to approve nodes whose status is **NodeStatus\_Pending**. To get a list of compute nodes, call the [**ICluster::get\_ComputeNodes**](icluster-get-computenodes.md) method. To determine a node's status, call the [**INode::get\_Status**](inode-get-status.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::PauseNode**](icluster-pausenode.md)
</dt> <dt>

[**ICluster::ResumeNode**](icluster-resumenode.md)
</dt> <dt>

[**NodeStatus**](nodestatus.md)
</dt> </dl>

 

 




