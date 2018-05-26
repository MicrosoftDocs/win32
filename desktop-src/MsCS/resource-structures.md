---
title: Resource Structures
description: A resource structure is a user-defined structure for storing instance data. A resource structure resides in a Resource DLL. The following code illustrates a resource structure for use with 32-bit operating systems.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 24aa082d-9cb0-4e32-8cfa-da801ab3eb52
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource DLLs Failover Cluster ,resource structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Resource Structures

A resource structure is a user-defined structure for storing [instance data](instance-data.md). A resource structure resides in a [Resource DLL](resource-dlls.md). The following code illustrates a resource structure for use with 32-bit operating systems.

``` syntax
typedef struct _MYTYPE_RESOURCE
{
  RESID                  resid;
  MYTYPE_PROPS           propsActive;
  MYTYPE_PROPS           props;
  HCLUSTER               hCluster;
  HRESOURCE              hResource;
  SC_HANDLE              hService;
  DWORD                  dwServicePid;
  HKEY                   hkeyParameters;
  RESOURCE_HANDLE        hResourceHandle;
  LPWSTR                 pszResourceName;
  CLUS_WORKER            cwWorkerThread;
  CLUSTER_RESOURCE_STATE state;
} 
MYTYPE_RESOURCE, *PMYTYPE_RESOURCE;
```

<dl> <dt>

<span id="resid"></span><span id="RESID"></span>**resid**
</dt> <dd>

Stores the [resource identifier](resource-identifiers.md) (RESID) of the resource instance. The RESID is the address of the structure that is allocated for a [resource](resources.md) instance.

</dd> <dt>

<span id="propsActive"></span><span id="propsactive"></span><span id="PROPSACTIVE"></span>**propsActive**
</dt> <dd>

A parameter block that stores the most current in-memory values of the instance's [private properties](private-properties.md). If a resource is online, changes to its private properties are stored here until the resource can be taken offline and brought back online.

</dd> <dt>

<span id="props"></span><span id="PROPS"></span>**props**
</dt> <dd>

A [parameter block](parameter-blocks.md) that stores the most current [cluster database](cluster-database.md) values of the instance's private properties. These are the values under which the instance is currently operating.

</dd> <dt>

<span id="hCluster"></span><span id="hcluster"></span><span id="HCLUSTER"></span>**hCluster**
</dt> <dd>

Stores a [*cluster*](c-gly.md#-wolf-cluster-gly) handle.

</dd> <dt>

<span id="hResource"></span><span id="hresource"></span><span id="HRESOURCE"></span>**hResource**
</dt> <dd>

Stores a resource handle.

</dd> <dt>

<span id="hService"></span><span id="hservice"></span><span id="HSERVICE"></span>**hService**
</dt> <dd>

Handle to the service controlled by the resource.

</dd> <dt>

<span id="dwServicePid"></span><span id="dwservicepid"></span><span id="DWSERVICEPID"></span>**dwServicePid**
</dt> <dd>

Stores the service process identifier of the service controlled by the resource.

</dd> <dt>

<span id="hkeyParameters"></span><span id="hkeyparameters"></span><span id="HKEYPARAMETERS"></span>**hkeyParameters**
</dt> <dd>

Stores the name of the cluster database key under which the resource's private properties are stored.

</dd> <dt>

<span id="hResourceHandle"></span><span id="hresourcehandle"></span><span id="HRESOURCEHANDLE"></span>**hResourceHandle**
</dt> <dd>

Stores the Resource Monitor's handle to the instance, which is used to identify the instance in the [**LogEvent**](/windows/previous-versions/ResApi/nc-resapi-plog_event_routine?branch=master) and [**SetResourceStatus**](/windows/previous-versions/ResApi/nc-resapi-pset_resource_status_routine?branch=master) callback functions.

</dd> <dt>

<span id="pszResourceName"></span><span id="pszresourcename"></span><span id="PSZRESOURCENAME"></span>**pszResourceName**
</dt> <dd>

Stores the name of the resource.

</dd> <dt>

<span id="cwWorkerThread"></span><span id="cwworkerthread"></span><span id="CWWORKERTHREAD"></span>**cwWorkerThread**
</dt> <dd>

A [**CLUS\_WORKER**](/windows/previous-versions/ResApi/ns-resapi-clus_worker?branch=master) thread used to handle pending operations.

</dd> <dt>

<span id="state"></span><span id="STATE"></span>**state**
</dt> <dd>

Stores the state of the resource. The value of this member is taken from the [**CLUSTER\_RESOURCE\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_state?branch=master) enumeration. The possible values are as follows.



| Value                                    | Meaning                                                                                                                                     |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| ClusterResourceStateUnknown<br/>   | The operation was not successful. For more information about the error, call the function [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).<br/> |
| ClusterResourceInherited<br/>      | The resource has been inherited.<br/>                                                                                                 |
| ClusterResourceInitializing<br/>   | The resource is performing initialization.<br/>                                                                                       |
| ClusterResourceOnline<br/>         | The resource is operational and functioning normally.<br/>                                                                            |
| ClusterResourceOffline<br/>        | The resource is not operational.<br/>                                                                                                 |
| ClusterResourceFailed<br/>         | The resource has [*failed*](f-gly.md#-wolf-failed-gly).<br/>                                                                         |
| ClusterResourcePending<br/>        | The resource is in the process of coming online or going [*offline*](o-gly.md#-wolf-offline-gly).<br/>                               |
| ClusterResourceOnlinePending<br/>  | The resource is in the process of coming online.<br/>                                                                                 |
| ClusterResourceOfflinePending<br/> | The resource is in the process of going offline.<br/>                                                                                 |



 

</dd> </dl>

For more information on instance management, see [Implementing Instance Management](implementing-instance-management.md).

## Related topics

<dl> <dt>

[Managing Instances](managing-instances.md)
</dt> <dt>

[**CLUSTER\_RESOURCE\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_state?branch=master)
</dt> </dl>

 

 





