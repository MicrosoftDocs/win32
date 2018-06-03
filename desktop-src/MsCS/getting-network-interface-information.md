---
title: Getting Network Interface Information
description: The following table lists network interface \ 8211;related information and objects and the recommended API elements for obtaining them. If the specified API element does not have an example, look in the Index of Examples for a similar API element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6bbae505-07de-4968-8125-eab3d37999a9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- network interfaces Failover Cluster ,retrieving information
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Network Interface Information

The following table lists [network interface](network-interfaces.md)–related information and objects and the recommended API elements for obtaining them. If the specified API element does not have an example, look in the [Index of Examples](index-of-examples.md) for a similar API element.



| Information or Object to Get                       | API element to Use                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cluster that contains the network interface        | [**GetClusterFromNetInterface**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_from_net_interface)                                                                                                                                                                                                                                                                                                                                                          |
| GUID identifying the network interface             | [CLUSCTL\_NETINTERFACE\_GET\_ID](clusctl-netinterface-get-id.md)                                                                                                                                                                                                                                                                                                                                                         |
| Name of the network interface                      | [CLUSCTL\_NETINTERFACE\_GET\_NAME](clusctl-netinterface-get-name.md)                                                                                                                                                                                                                                                                                                                                                     |
| Network to which the network interface is attached | [CLUSCTL\_NETINTERFACE\_GET\_NETWORK](clusctl-netinterface-get-network.md)                                                                                                                                                                                                                                                                                                                                               |
| Node to which the network interface is attached    | [CLUSCTL\_NETINTERFACE\_GET\_NODE](clusctl-netinterface-get-node.md)                                                                                                                                                                                                                                                                                                                                                     |
| Properties of the network interface                | [CLUSCTL\_NETINTERFACE\_GET\_COMMON\_PROPERTIES](clusctl-netinterface-get-common-properties.md), [CLUSCTL\_NETINTERFACE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-netinterface-get-ro-common-properties.md), [CLUSCTL\_NETINTERFACE\_GET\_PRIVATE\_PROPERTIES](clusctl-netinterface-get-private-properties.md), [CLUSCTL\_NETINTERFACE\_GET\_RO\_PRIVATE\_PROPERTIES](clusctl-netinterface-get-ro-private-properties.md), |
| Property names                                     | [CLUSCTL\_NETINTERFACE\_ENUM\_COMMON\_PROPERTIES](clusctl-netinterface-enum-common-properties.md), [CLUSCTL\_NETINTERFACE\_ENUM\_PRIVATE\_PROPERTIES](clusctl-netinterface-enum-private-properties.md)                                                                                                                                                                                                                  |
| State of the network interface                     | [**GetClusterNetInterfaceState**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_net_interface_state)                                                                                                                                                                                                                                                                                                                                                        |



 

For additional network interface-related APIs elements, see [Network Interface Management Functions](network-interface-management-functions.md) and [Network Interface Control Codes](network-interface-control-codes.md).

 

 




