---
Description: 'Connects to the specified cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c43308e3-759d-4a2d-9db0-874e7df92788'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::Connect method'
---

# ICluster::Connect method

Connects to the specified cluster.

## Syntax


```C++
HRESULT Connect(
  [in] BSTR clusterName
);
```



## Parameters

<dl> <dt>

*clusterName* \[in\]
</dt> <dd>

The computer name of the cluster's head node (the head node is the node on which the Compute Cluster Service is installed). If your application is running on the head node, you can specify the node's name or use "localhost" as the name.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

To connect to the cluster, the user needs to have an account on the head node or be a member of the Guest Users, Power Users, or Administrators group.

You can use the following filter to look up the name of the head nodes in a domain in Active Directory:

(&(objectClass=ServiceConnectionPoint)(serviceClassName=MicrosoftComputeCluster))

## Examples

For an example that shows how to connect to the cluster, see [Connecting to the Cluster](connecting-to-the-cluster.md).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> </dl>

 

 




