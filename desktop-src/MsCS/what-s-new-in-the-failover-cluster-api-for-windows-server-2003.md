---
title: What's New in the Failover Cluster API for Windows Server 2003
description: This summarizes the changes in the Failover Cluster APIs for Windows Server 2003.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e83a5d5b-4cf1-464b-9637-9c7b7ff4ae8e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New in the Failover Cluster API for Windows Server 2003

This summarizes the changes in the Failover Cluster APIs for Windows Server 2003.

## New APIs introduced in Windows Server 2003:

-   [**CLUS\_FORCE\_QUORUM\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_force_quorum_info)
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
-   [**CLUSPROP\_WORD**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_word)
-   [Cluster Configuration Interfaces](https://msdn.microsoft.com/library/aa372941)
-   [**ClusterGetEnumCount**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_get_enum_count)
-   [**ClusterGroupGetEnumCount**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_get_enum_count)
-   [**ClusterNetworkGetEnumCount**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_network_get_enum_count)
-   [**ClusterNodeGetEnumCount**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_node_get_enum_count)
-   [**ClusterResourceGetEnumCount**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_get_enum_count)
-   [**ClusterResourceTypeGetEnumCount**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_type_get_enum_count)
-   [**CSCCache Property for File Shares**](file-shares-csccache.md)
-   [**EvictClusterNodeEx**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_evict_cluster_node_ex)
-   [**MulticastAddress Property for Networks**](networks-multicastaddress.md)
-   [**MulticastAddressRangeLower Property for Networks**](networks-multicastaddressrangelower.md)
-   [**MulticastAddressRangeUpper Property for Networks**](networks-multicastaddressrangeupper.md)
-   [**MulticastConfigType Property for Networks**](networks-multicastconfigtype.md)
-   [**MulticastDisabled Property for Networks**](networks-multicastdisabled.md)
-   [**MulticastLeaseExpires Property for Networks**](networks-multicastleaseexpires.md)
-   [**MulticastLeaseObtained Property for Networks**](networks-multicastleaseobtained.md)
-   [**MulticastLeaseRequestId Property for Networks**](networks-multicastleaserequestid.md)
-   [**MulticastLeaseServer Property for Networks**](networks-multicastleaseserver.md)
-   [**ResUtilEnumResourcesEx**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_enum_resources_ex)
-   [**ResUtilGetPropertyFormats**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_property_formats)
-   [**ResUtilGetCoreClusterResources**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_core_cluster_resources)
-   [**ResUtilGetResourceName**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_resource_name)
-   [**ResUtilTerminateServiceProcessFromResDll**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_terminate_service_process_from_res_dll)
-   [The Generic Script Resource Type](generic-script.md)
-   [The Failover Cluster WMI provider](https://msdn.microsoft.com/library/aa372946)

## Changed APIs for Windows Server 2003:

-   New localquorum characteristics flags are defined for [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](clusctl-resource-get-characteristics.md).
-   A new event, **CLUSTER\_CHANGE\_CLUSTER\_RECONNECT**, is available to [**CreateClusterNotifyPort**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_notify_port), [**RegisterClusterNotify**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_register_cluster_notify), and [**GetClusterNotify**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_notify).

 

 




