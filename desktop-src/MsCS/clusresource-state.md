---
title: ClusResource.State property
description: Returns a description of the operational condition of a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3bae66a8-cc45-49e6-acea-c506623b25bc
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- State property Failover Cluster
- State property Failover Cluster , ClusResource object
- ClusResource object Failover Cluster , State property
topic_type:
- apiref
api_name:
- ClusResource.State
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResource.State property

\[The **State** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a description of the operational condition of a [resource](resources.md).

This property is read-only.

## Syntax


```VB
ClusResource.State
```



## Property value

**Long** that receives a constant describing the state of the resource. The values are enumerated from the [**CLUSTER\_RESOURCE\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_state?branch=master) enumeration.

<dt>

<span id="ClusterResourceStateUnknown"></span><span id="clusterresourcestateunknown"></span><span id="CLUSTERRESOURCESTATEUNKNOWN"></span>

<span id="ClusterResourceStateUnknown"></span><span id="clusterresourcestateunknown"></span><span id="CLUSTERRESOURCESTATEUNKNOWN"></span>**ClusterResourceStateUnknown** (-1)


</dt> <dd>

The operation was not successful. For more information about the error, call the function [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

</dd> <dt>

<span id="ClusterResourceInherited"></span><span id="clusterresourceinherited"></span><span id="CLUSTERRESOURCEINHERITED"></span>

<span id="ClusterResourceInherited"></span><span id="clusterresourceinherited"></span><span id="CLUSTERRESOURCEINHERITED"></span>**ClusterResourceInherited** (0)


</dt> <dd>

The resource has been inherited.

</dd> <dt>

<span id="ClusterResourceInitializing"></span><span id="clusterresourceinitializing"></span><span id="CLUSTERRESOURCEINITIALIZING"></span>

<span id="ClusterResourceInitializing"></span><span id="clusterresourceinitializing"></span><span id="CLUSTERRESOURCEINITIALIZING"></span>**ClusterResourceInitializing** (1)


</dt> <dd>

The resource is performing initialization.

</dd> <dt>

<span id="ClusterResourceOnline"></span><span id="clusterresourceonline"></span><span id="CLUSTERRESOURCEONLINE"></span>

<span id="ClusterResourceOnline"></span><span id="clusterresourceonline"></span><span id="CLUSTERRESOURCEONLINE"></span>**ClusterResourceOnline** (2)


</dt> <dd>

The resource is operational and functioning normally.

</dd> <dt>

<span id="ClusterResourceOffline"></span><span id="clusterresourceoffline"></span><span id="CLUSTERRESOURCEOFFLINE"></span>

<span id="ClusterResourceOffline"></span><span id="clusterresourceoffline"></span><span id="CLUSTERRESOURCEOFFLINE"></span>**ClusterResourceOffline** (3)


</dt> <dd>

The resource is not operational.

</dd> <dt>

<span id="ClusterResourceFailed"></span><span id="clusterresourcefailed"></span><span id="CLUSTERRESOURCEFAILED"></span>

<span id="ClusterResourceFailed"></span><span id="clusterresourcefailed"></span><span id="CLUSTERRESOURCEFAILED"></span>**ClusterResourceFailed** (4)


</dt> <dd>

The resource has [*failed*](f-gly.md#-wolf-failed-gly).

</dd> <dt>

<span id="ClusterResourcePending"></span><span id="clusterresourcepending"></span><span id="CLUSTERRESOURCEPENDING"></span>

<span id="ClusterResourcePending"></span><span id="clusterresourcepending"></span><span id="CLUSTERRESOURCEPENDING"></span>**ClusterResourcePending** (128)


</dt> <dd>

The resource is in the process of coming [*online*](o-gly.md#-wolf-online-gly) or going [*offline*](o-gly.md#-wolf-offline-gly).

</dd> <dt>

<span id="ClusterResourceOnlinePending"></span><span id="clusterresourceonlinepending"></span><span id="CLUSTERRESOURCEONLINEPENDING"></span>

<span id="ClusterResourceOnlinePending"></span><span id="clusterresourceonlinepending"></span><span id="CLUSTERRESOURCEONLINEPENDING"></span>**ClusterResourceOnlinePending** (129)


</dt> <dd>

The resource is in the process of coming online.

</dd> <dt>

<span id="ClusterResourceOfflinePending"></span><span id="clusterresourceofflinepending"></span><span id="CLUSTERRESOURCEOFFLINEPENDING"></span>

<span id="ClusterResourceOfflinePending"></span><span id="clusterresourceofflinepending"></span><span id="CLUSTERRESOURCEOFFLINEPENDING"></span>**ClusterResourceOfflinePending** (130)


</dt> <dd>

The resource is in the process of going offline.

</dd> </dl>

## Remarks

For information about making constants defined by the Cluster Automation Server type library (MsClus.tlb) available to scripts, see [Creating a Cluster Automation Server Script](creating-a-cluster-automation-server-script.md).

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
</dt> <dt>

[**CLUSTER\_RESOURCE\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_state?branch=master)
</dt> </dl>

 

 





