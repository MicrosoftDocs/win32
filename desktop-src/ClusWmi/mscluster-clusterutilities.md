---
title: MSCluster\_ClusterUtilities class
description: Verifies whether a node is configured to support clustering.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4cde9dfa-62f1-4fe0-8e3b-a83ef6a52f91
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ClusterUtilities class
- MSCluster_ClusterUtilities class, described
topic_type:
- apiref
api_name:
- MSCluster_ClusterUtilities
- MSCluster_ClusterUtilities.Fqdn
- MSCluster_ClusterUtilities.HasSystemAccess
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_ClusterUtilities class

Verifies whether a node is configured to support clustering.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Singleton, Provider("MS_CLUSTER_PROVIDER"), UUID("{6FE4D3D2-4593-4B39-A14A-86EB3E69087F}"), AMENDMENT]
class MSCluster_ClusterUtilities
{
  string  Fqdn;
  boolean HasSystemAccess;
};
```

## Members

The **MSCluster\_ClusterUtilities** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_ClusterUtilities** class has these methods.



| Method                                                                                                        | Description                                                                 |
|:--------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------|
| [**IsClusterSupported**](isclustersupported-mscluster-clusterutilities.md)                                   | Indicates whether the node supports clustering.<br/>                  |
| [**IsStorageSpacesDirectCacheSupported**](mscluster-clusterutilities-isstoragespacesdirectcachesupported.md) | Checks if storage spaces direct cache is supported on this node.<br/> |
| [**IsStorageSpacesDirectSupported**](mscluster-clusterutilities-isstoragespacesdirectsupported.md)           | Checks if storage spaces direct is supported on this node.<br/>       |



 

### Properties

The **MSCluster\_ClusterUtilities** class has these properties.

<dl> <dt>

**Fqdn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the fully qualified domain name of the node.

</dd> <dt>

**HasSystemAccess**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the user has system level access to the **HKEY\_LOCAL\_MACHINE**\\**SYSTEM** registry key, otherwise **False**.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



 

 





