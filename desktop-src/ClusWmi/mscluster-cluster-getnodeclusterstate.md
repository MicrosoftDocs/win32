---
title: GetNodeClusterState method of the MSCluster\_Cluster class
description: Determines whether the Cluster service is installed and running on a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd4edae90-bec5-4d5b-a257-a106dec9f0fc'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetNodeClusterState method", "GetNodeClusterState method, MSCluster_Cluster class", "MSCluster_Cluster class, GetNodeClusterState method"]
topic_type:
- apiref
api_name:
- MSCluster_Cluster.GetNodeClusterState
api_location:
- ClusWMI.dll
api_type:
- COM
---

# GetNodeClusterState method of the MSCluster\_Cluster class

Determines whether the Cluster service is installed and running on a node.

## Syntax


```mof
void GetNodeClusterState(
  [out] sint32 ClusterState
);
```



## Parameters

<dl> <dt>

*ClusterState* \[out\]
</dt> <dd>

State of the Cluster service on the node as enumerated by the [**NODE\_CLUSTER\_STATE**](https://msdn.microsoft.com/library/bb394679) enumeration.

<dt>

<span id="ClusterStateNotInstalled"></span><span id="clusterstatenotinstalled"></span><span id="CLUSTERSTATENOTINSTALLED"></span>

<span id="ClusterStateNotInstalled"></span><span id="clusterstatenotinstalled"></span><span id="CLUSTERSTATENOTINSTALLED"></span>**ClusterStateNotInstalled** (0)


</dt> <dd>

The Cluster service is not installed on the node.

</dd> <dt>

<span id="ClusterStateNotConfigured"></span><span id="clusterstatenotconfigured"></span><span id="CLUSTERSTATENOTCONFIGURED"></span>

<span id="ClusterStateNotConfigured"></span><span id="clusterstatenotconfigured"></span><span id="CLUSTERSTATENOTCONFIGURED"></span>**ClusterStateNotConfigured** (1)


</dt> <dd>

The Cluster service is installed on the node but has not yet been configured.

</dd> <dt>

<span id="ClusterStateNotRunning"></span><span id="clusterstatenotrunning"></span><span id="CLUSTERSTATENOTRUNNING"></span>

<span id="ClusterStateNotRunning"></span><span id="clusterstatenotrunning"></span><span id="CLUSTERSTATENOTRUNNING"></span>**ClusterStateNotRunning** (3)


</dt> <dd>

The Cluster service is installed and configured on the node but is not currently running.

</dd> <dt>

<span id="ClusterStateRunning"></span><span id="clusterstaterunning"></span><span id="CLUSTERSTATERUNNING"></span>

<span id="ClusterStateRunning"></span><span id="clusterstaterunning"></span><span id="CLUSTERSTATERUNNING"></span>**ClusterStateRunning** (19)


</dt> <dd>

The Cluster service is installed, configured, and running on the node.

</dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>**Running** (19)


</dt> <dd></dd> <dt>

<span id="Not_Running"></span><span id="not_running"></span><span id="NOT_RUNNING"></span>

<span id="Not_Running"></span><span id="not_running"></span><span id="NOT_RUNNING"></span>**Not Running** (3)


</dt> <dd></dd> <dt>

<span id="Not_Configured"></span><span id="not_configured"></span><span id="NOT_CONFIGURED"></span>

<span id="Not_Configured"></span><span id="not_configured"></span><span id="NOT_CONFIGURED"></span>**Not Configured** (1)


</dt> <dd></dd> <dt>

<span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span>

<span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span>**Not Installed** (0)


</dt> <dd></dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| Header<br/>                   | <dl> <dt>Clusapi.h</dt> </dl>   |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> <dt>

[**NODE\_CLUSTER\_STATE**](https://msdn.microsoft.com/library/bb394679)
</dt> </dl>

 

 





