---
Description: 'Connects you to the specified cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e3352d63-96cf-4e7d-afdb-94731c542be3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::Connect method'
---

# IScheduler::Connect method

Connects you to the specified cluster.

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

The computer name of the cluster's head node (the head node is the node on which Microsoft HPC Service is installed). If your application is running on the head node, you can specify the node's name or use "localhost" as the name.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

To connect to the cluster, the user needs to have an account on the head node or be a member of the Users or Administrators group.

You can use the HPC SDK to schedule jobs on Microsoft HPC Server 2008 and later HPC servers; you cannot use this SDK to schedule jobs on Microsoft Compute Cluster Server 2003 (CCS).

If you use Active Directory to look up the names of the head nodes in a domain, use the following filter:

`(&(objectClass=ServiceConnectionPoint)(serviceClassName=MicrosoftComputeCluster)(keywords=*Version2*))`

## Examples

For an example, see [Connecting to a Cluster](connecting-to-a-cluster.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> </dl>

 

 




