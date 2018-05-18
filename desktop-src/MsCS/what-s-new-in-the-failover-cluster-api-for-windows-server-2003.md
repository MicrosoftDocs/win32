---
title: What's New in the Failover Cluster API for Windows Server 2003
description: This summarizes the changes in the Failover Cluster APIs for Windows Server 2003.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e83a5d5b-4cf1-464b-9637-9c7b7ff4ae8e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
---

# What's New in the Failover Cluster API for Windows Server 2003

This summarizes the changes in the Failover Cluster APIs for Windows Server 2003.

## New APIs introduced in Windows Server 2003:

-   [**CLUS\_FORCE\_QUORUM\_INFO**](clus-force-quorum-info.md)
-   [CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-cluster-get-common-property-fmts.md)
-   [CLUSCTL\_CLUSTER\_GET\_FQDN](clusctl-cluster-get-fqdn.md)
-   [CLUSCTL\_CLUSTER\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-cluster-get-private-property-fmts.md)
-   [CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-group-get-common-property-fmts.md)
-   [CLUSCTL\_GROUP\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-group-get-private-property-fmts.md)
-   [CLUSCTL\_NETINTERFACE\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-netinterface-get-common-property-fmts.md)
-   [CLUSCTL\_NETINTERFACE\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-netinterface-get-private-property-fmts.md)
-   [CLUSCTL\_NETWORK\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-network-get-common-property-fmts.md)
-   [CLUSCTL\_NETWORK\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-network-get-private-property-fmts.md)
-   [CLUSCTL\_NODE\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-node-get-common-property-fmts.md)
-   [CLUSCTL\_NODE\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-node-get-private-property-fmts.md)
-   [CLUSCTL\_RESOURCE\_FORCE\_QUORUM](clusctl-resource-force-quorum.md)
-   [CLUSCTL\_RESOURCE\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-resource-get-common-property-fmts.md)
-   [CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-resource-get-private-property-fmts.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_GET\_COMMON\_PROPERTY\_FMTS](clusctl-resource-type-get-common-property-fmts.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_GET\_COMMON\_RESOURCE\_PROPERTY\_FMTS](clusctl-resource-type-get-common-resource-property-fmts.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_PROPERTY\_FMTS](clusctl-resource-type-get-private-property-fmts.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_RESOURCE\_PROPERTY\_FMTS](clusctl-resource-type-get-private-resource-property-fmts.md)
-   [CLUSCTL\_RESOURCE\_UPGRADE\_DLL](clusctl-resource-upgrade-dll.md)
-   [**CLUSPROP\_WORD**](clusprop-word.md)
-   [Cluster Configuration Interfaces](https://msdn.microsoft.com/library/aa372941)
-   [**ClusterGetEnumCount**](clustergetenumcount.md)
-   [**ClusterGroupGetEnumCount**](clustergroupgetenumcount.md)
-   [**ClusterNetworkGetEnumCount**](clusternetworkgetenumcount.md)
-   [**ClusterNodeGetEnumCount**](clusternodegetenumcount.md)
-   [**ClusterResourceGetEnumCount**](clusterresourcegetenumcount.md)
-   [**ClusterResourceTypeGetEnumCount**](clusterresourcetypegetenumcount.md)
-   [**CSCCache Property for File Shares**](file-shares-csccache.md)
-   [**EvictClusterNodeEx**](evictclusternodeex.md)
-   [**MulticastAddress Property for Networks**](networks-multicastaddress.md)
-   [**MulticastAddressRangeLower Property for Networks**](networks-multicastaddressrangelower.md)
-   [**MulticastAddressRangeUpper Property for Networks**](networks-multicastaddressrangeupper.md)
-   [**MulticastConfigType Property for Networks**](networks-multicastconfigtype.md)
-   [**MulticastDisabled Property for Networks**](networks-multicastdisabled.md)
-   [**MulticastLeaseExpires Property for Networks**](networks-multicastleaseexpires.md)
-   [**MulticastLeaseObtained Property for Networks**](networks-multicastleaseobtained.md)
-   [**MulticastLeaseRequestId Property for Networks**](networks-multicastleaserequestid.md)
-   [**MulticastLeaseServer Property for Networks**](networks-multicastleaseserver.md)
-   [**ResUtilEnumResourcesEx**](resutilenumresourcesex.md)
-   [**ResUtilGetPropertyFormats**](resutilgetpropertyformats.md)
-   [**ResUtilGetCoreClusterResources**](resutilgetcoreclusterresources.md)
-   [**ResUtilGetResourceName**](resutilgetresourcename.md)
-   [**ResUtilTerminateServiceProcessFromResDll**](resutilterminateserviceprocessfromresdll.md)
-   [The Generic Script Resource Type](generic-script.md)
-   [The Failover Cluster WMI provider](https://msdn.microsoft.com/library/aa372946)

## Changed APIs for Windows Server 2003:

-   New localquorum characteristics flags are defined for [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](clusctl-resource-get-characteristics.md).
-   A new event, **CLUSTER\_CHANGE\_CLUSTER\_RECONNECT**, is available to [**CreateClusterNotifyPort**](createclusternotifyport.md), [**RegisterClusterNotify**](registerclusternotify.md), and [**GetClusterNotify**](getclusternotify.md).

 

 




