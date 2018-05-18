---
title: Function Calls to Avoid in Resource DLLs
description: Function calls involving the following functions or control codes can cause deadlock when made from resource DLLs. The following table lists these functions along with a usage code. A subsequent table describes the usage codes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0eaa4aea-8d9a-4552-b43a-fafa23a3e736'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource DLLs Failover Cluster ,function calls to avoid", "entry point functions Failover Cluster ,function calls to avoid in resource DLLs"]
---

# Function Calls to Avoid in Resource DLLs

Function calls involving the following functions or control codes can cause deadlock when made from resource DLLs. The following table lists these functions along with a usage code. A subsequent table describes the usage codes.



| API element                                                                                          | Usage code              |
|------------------------------------------------------------------------------------------------------|-------------------------|
| [**AddClusterResourceDependency**](addclusterresourcedependency.md)                                 | Do not use.             |
| [**AddClusterResourceNode**](addclusterresourcenode.md)                                             | Worker thread only.     |
| [**CanResourceBeDependent**](canresourcebedependent.md)                                             | Worker thread only.     |
| [**ChangeClusterResourceGroup**](changeclusterresourcegroup.md)                                     | Do not use.             |
| [CLUSCTL\_GROUP\_ENUM\_COMMON\_PROPERTIES](clusctl-group-enum-common-properties.md)                 | Worker thread only.     |
| [CLUSCTL\_GROUP\_ENUM\_PRIVATE\_PROPERTIES](clusctl-group-enum-private-properties.md)               | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_CHARACTERISTICS](clusctl-group-get-characteristics.md)                        | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTIES](clusctl-group-get-common-properties.md)                   | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-group-get-common-property-fmts.md)            | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_FLAGS](clusctl-group-get-flags.md)                                            | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_ID](clusctl-group-get-id.md)                                                  | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_NAME](clusctl-group-get-name.md)                                              | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_PRIVATE\_PROPERTIES](clusctl-group-get-private-properties.md)                 | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-group-get-private-property-fmts.md)          | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_RO\_COMMON\_PROPERTIES](clusctl-group-get-ro-common-properties.md)            | Worker thread only.     |
| [CLUSCTL\_GROUP\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-group-get-ro-private-properties.md)          | Worker thread only.     |
| [CLUSCTL\_GROUP\_QUERY\_DELETE](clusctl-group-query-delete.md)                                      | Worker thread only.     |
| [CLUSCTL\_GROUP\_SET\_COMMON\_PROPERTIES](clusctl-group-set-common-properties.md)                   | Worker thread only.     |
| [CLUSCTL\_GROUP\_SET\_PRIVATE\_PROPERTIES](clusctl-group-set-private-properties.md)                 | Worker thread only.     |
| [CLUSCTL\_GROUP\_UNKNOWN](clusctl-group-unknown.md)                                                 | Worker thread only.     |
| [CLUSCTL\_GROUP\_VALIDATE\_COMMON\_PROPERTIES](clusctl-group-validate-common-properties.md)         | Worker thread only.     |
| [CLUSCTL\_GROUP\_VALIDATE\_PRIVATE\_PROPERTIES](clusctl-group-validate-private-properties.md)       | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_ADD\_DEPENDENCY](clusctl-resource-add-dependency.md)                            | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_ADD\_OWNER](clusctl-resource-add-owner.md)                                      | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_CLUSTER\_NAME\_CHANGED](clusctl-resource-cluster-name-changed.md)               | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_CLUSTER\_VERSION\_CHANGED](clusctl-resource-cluster-version-changed.md)         | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_DELETE](clusctl-resource-delete.md)                                             | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_ENUM\_COMMON\_PROPERTIES](clusctl-resource-enum-common-properties.md)           | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_ENUM\_PRIVATE\_PROPERTIES](clusctl-resource-enum-private-properties.md)         | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_EVICT\_NODE](clusctl-resource-evict-node.md)                                    | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](clusctl-resource-get-characteristics.md)                  | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_CLASS\_INFO](clusctl-resource-get-class-info.md)                           | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_COMMON\_PROPERTIES](clusctl-resource-get-common-properties.md)             | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_FLAGS](clusctl-resource-get-flags.md)                                      | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_ID](clusctl-resource-get-id.md)                                            | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_NAME](clusctl-resource-get-name.md)                                        | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_NETWORK\_NAME](clusctl-resource-get-network-name.md)                       | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTIES](clusctl-resource-get-private-properties.md)           | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-get-required-dependencies.md)     | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_RESOURCE\_TYPE](clusctl-resource-get-resource-type.md)                     | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-resource-get-ro-common-properties.md)      | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-resource-get-ro-private-properties.md)    | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_INSTALL\_NODE](clusctl-resource-install-node.md)                                | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_REMOVE\_DEPENDENCY](clusctl-resource-remove-dependency.md)                      | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_REMOVE\_OWNER](clusctl-resource-remove-owner.md)                                | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_SET\_COMMON\_PROPERTIES](clusctl-resource-set-common-properties.md)             | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_SET\_NAME](clusctl-resource-set-name.md)                                        | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_SET\_PRIVATE\_PROPERTIES](clusctl-resource-set-private-properties.md)           | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO](clusctl-resource-storage-get-disk-info.md)            | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX](clusctl-resource-storage-get-disk-info-ex.md)     | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_STORAGE\_GET\_MOUNTPOINTS](clusctl-resource-storage-get-mountpoints.md)         | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_STORAGE\_IS\_PATH\_VALID](clusctl-resource-storage-is-path-valid.md)            | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_UNKNOWN](clusctl-resource-unknown.md)                                           | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_VALIDATE\_COMMON\_PROPERTIES](clusctl-resource-validate-common-properties.md)   | Worker thread only.     |
| [CLUSCTL\_RESOURCE\_VALIDATE\_PRIVATE\_PROPERTIES](clusctl-resource-validate-private-properties.md) | Worker thread only.     |
| [**ClusterGroupEnum**](clustergroupenum.md)                                                         | Worker thread only.     |
| [**ClusterGroupOpenEnum**](clustergroupopenenum.md)                                                 | Worker thread only.     |
| [**ClusterRegCreateKey**](clusterregcreatekey.md)                                                   | Some entry points okay. |
| [**ClusterRegDeleteKey**](clusterregdeletekey.md)                                                   | Some entry points okay. |
| [**ClusterRegDeleteValue**](clusterregdeletevalue.md)                                               | Some entry points okay. |
| [**ClusterRegSetKeySecurity**](clusterregsetkeysecurity.md)                                         | Some entry points okay. |
| [**ClusterRegSetValue**](clusterregsetvalue.md)                                                     | Some entry points okay. |
| [**ClusterResourceEnum**](clusterresourceenum.md)                                                   | Worker thread only.     |
| [**ClusterResourceOpenEnum**](clusterresourceopenenum.md)                                           | Worker thread only.     |
| [**CreateClusterGroup**](createclustergroup.md)                                                     | Do not use.             |
| [**CreateClusterResource**](createclusterresource.md)                                               | Do not use.             |
| [**DeleteClusterGroup**](deleteclustergroup.md)                                                     | Do not use.             |
| [**DeleteClusterResource**](deleteclusterresource.md)                                               | Do not use.             |
| [**DestroyClusterGroup**](destroyclustergroup.md)                                                   | Do not use.             |
| [**FailClusterResource**](failclusterresource.md)                                                   | Do not use.             |
| [**GetClusterGroupState**](getclustergroupstate.md)                                                 | Worker thread only.     |
| [**GetClusterResourceNetworkName**](getclusterresourcenetworkname.md)                               | Worker thread only.     |
| [**GetClusterResourceState**](getclusterresourcestate.md)                                           | Worker thread only.     |
| [**MoveClusterGroup**](moveclustergroup.md)                                                         | Do not use.             |
| [**OfflineClusterGroup**](offlineclustergroup.md)                                                   | Do not use.             |
| [**OfflineClusterResource**](offlineclusterresource.md)                                             | Do not use.             |
| [**OnlineClusterGroup**](onlineclustergroup.md)                                                     | Do not use.             |
| [**OnlineClusterResource**](onlineclusterresource.md)                                               | Do not use.             |
| [**RemoveClusterResourceDependency**](removeclusterresourcedependency.md)                           | Do not use.             |
| [**RemoveClusterResourceNode**](removeclusterresourcenode.md)                                       | Do not use.             |
| [**ResUtilFindDependentDiskResourceDriveLetter**](resutilfinddependentdiskresourcedriveletter.md)   | Do not use.             |
| [**ResUtilGetResourceDependentIPAddressProps**](resutilgetresourcedependentipaddressprops.md)       | Worker thread only.     |
| [**ResUtilGetEnvironmentWithNetName**](resutilgetenvironmentwithnetname.md)                         | Worker thread only.     |
| [**ResUtilGetResourceDependency**](resutilgetresourcedependency.md)                                 | Worker thread only.     |
| [**ResUtilGetResourceDependencyByClass**](resutilgetresourcedependencybyclass.md)                   | Worker thread only.     |
| [**ResUtilGetResourceDependencyByName**](resutilgetresourcedependencybyname.md)                     | Worker thread only.     |
| [**ResUtilGetResourceNameDependency**](resutilgetresourcenamedependency.md)                         | Worker thread only.     |
| [**ResUtilSetBinaryValue**](resutilsetbinaryvalue.md)                                               | Some entry points okay. |
| [**ResUtilSetDwordValue**](resutilsetdwordvalue.md)                                                 | Some entry points okay. |
| [**ResUtilSetExpandSzValue**](resutilsetexpandszvalue.md)                                           | Some entry points okay. |
| [**ResUtilSetMultiSzValue**](resutilsetmultiszvalue.md)                                             | Some entry points okay. |
| [**ResUtilSetPrivatePropertyList**](resutilsetprivatepropertylist.md)                               | Some entry points okay. |
| [**ResUtilSetPropertyParameterBlock**](resutilsetpropertyparameterblock.md)                         | Some entry points okay. |
| [**ResUtilSetPropertyParameterBlockEx**](resutilsetpropertyparameterblockex.md)                     | Some entry points okay. |
| [**ResUtilSetPropertyTable**](resutilsetpropertytable.md)                                           | Some entry points okay. |
| [**ResUtilSetPropertyTableEx**](resutilsetpropertytableex.md)                                       | Some entry points okay. |
| [**ResUtilSetResourceServiceEnvironment**](resutilsetresourceserviceenvironment.md)                 | Worker thread only.     |
| [**ResUtilSetSzValue**](resutilsetszvalue.md)                                                       | Some entry points okay. |
| [**ResUtilSetUnknownProperties**](resutilsetunknownproperties.md)                                   | Some entry points okay. |
| [**SetClusterGroupName**](setclustergroupname.md)                                                   | Do not use.             |
| [**SetClusterGroupNodeList**](setclustergroupnodelist.md)                                           | Do not use.             |
| [**SetClusterName**](setclustername.md)                                                             | Do not use.             |
| [**SetClusterQuorumResource**](setclusterquorumresource.md)                                         | Do not use.             |
| [**SetClusterResourceName**](setclusterresourcename.md)                                             | Do not use.             |
| [**SetClusterServiceAccountPassword**](setclusterserviceaccountpassword.md)                         | Do not use.             |



 

The following table describes the usage codes presented in the previous table.

### 



| Usage code              | Usage notes                                                                                                                                                                                                                                                                                                                           |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Some entry points okay. | Do not call these functions from the following resource DLL entry point functions: [**Close**](close.md), [**Offline**](offline.md), [**Online**](online.md), [**Open**](open.md), [**Terminate**](terminate.md). These functions can be safely called from any other resource DLL entry point function or from a worker thread. |
| Worker thread only.     | These functions should be called only from a worker thread (see [**ClusWorkerCreate**](clusworkercreate.md), [**ClusWorkerCheckTerminate**](clusworkercheckterminate.md), and [**ClusWorkerTerminate**](clusworkerterminate.md)).                                                                                                  |
| Do not use.             | Do not call any of these functions from a resource DLL. Functions in this category modify dependency relationships, add or remove resources from groups, create or delete groups or resources, cause resource or group state changes, or change the node lists of groups or resources.                                                |



 

 

 




