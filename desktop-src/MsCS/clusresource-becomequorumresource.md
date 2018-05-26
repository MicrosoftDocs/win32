---
title: ClusResource.BecomeQuorumResource method
description: Establishes a resource as the quorum resource for the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fd316586-8553-4c4a-824e-ee5b7bf48184
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- BecomeQuorumResource method Failover Cluster
- BecomeQuorumResource method Failover Cluster , ClusResource object
- ClusResource object Failover Cluster , BecomeQuorumResource method
topic_type:
- apiref
api_name:
- ClusResource.BecomeQuorumResource
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResource.BecomeQuorumResource method

\[The **BecomeQuorumResource** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Establishes a [resource](resources.md) as the [quorum resource](quorum-resource.md) for the [*cluster*](c-gly.md#-wolf-cluster-gly).

## Syntax


```VB
ClusResource.BecomeQuorumResource( _
  ByVal strDevicePath, _
  ByVal lMaxLogSize _
)
```



## Parameters

<dl> <dt>

*strDevicePath* 
</dt> <dd>

**String** specifying the path to the quorum resource.

</dd> <dt>

*lMaxLogSize* 
</dt> <dd>

**Long** specifying the maximum size that the cluster recovery log can attain, as determined by the storage capacity of the resource.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Failover clusters only allow [Physical Disk](physical-disk.md) resources to operate as quorum resources. However, you can enable other storage devices to act as quorum resources by creating a custom resource type. For more information, see [Creating a Custom Resource Type](creating-resource-types.md) and [Quorum Resource](quorum-resource.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResource is defined as F2E6070A-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





