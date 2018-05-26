---
title: Network Private Properties
description: In Windows Server 2003, failover clusters automatically perform heartbeat multicasting, the multicasting of heartbeats and other intranode communication to improve efficiency and allow more nodes to be added to the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0e8bd70b-112c-4013-a567-c9bd127a22c0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- network properties Failover Cluster
- network properties Failover Cluster , private
- properties Failover Cluster , network properties
- properties Failover Cluster , network properties, private
- networks Failover Cluster , properties
- networks Failover Cluster , properties, private
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Network Private Properties

\[The heartbeat multicasting network private properties are no longer available for use as of Windows Server 2012.\]

In Windows Server 2003, failover clusters automatically perform *heartbeat multicasting*, the multicasting of [*heartbeats*](h-gly.md#-wolf-heartbeat-gly) and other intranode communication to improve efficiency and allow more nodes to be added to the [*cluster*](c-gly.md#-wolf-cluster-gly). To implement heartbeat multicasting, the cluster defines a number of [private properties](private-properties.md) for each cluster [network](networks.md). For the sake of completeness these properties are documented in the following sections. However, in the vast majority of cases, cluster application developers will have no use for these properties. Note the following.

-   Most of these properties are read-only and provide no useful information.
-   Modifying the writable properties can cause all intranode communication to fail on a network.
-   Different networks may have different sets of properties, in other words, not all networks will have all of these private properties.



| Property                                                                             | Access                                                                              |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**MulticastAddress**](networks-multicastaddress.md)<br/>                     | Not supported<br/> **Windows Server 2003:** Read/write<br/> <br/> |
| [**MulticastAddressRangeLower**](networks-multicastaddressrangelower.md)<br/> | Not supported<br/> **Windows Server 2003:** Read/write<br/> <br/> |
| [**MulticastAddressRangeUpper**](networks-multicastaddressrangeupper.md)<br/> | Not supported<br/> **Windows Server 2003:** Read/write<br/> <br/> |
| [**MulticastConfigType**](networks-multicastconfigtype.md)<br/>               | Not supported<br/> **Windows Server 2003:** Read-only<br/> <br/>  |
| [**MulticastDisabled**](networks-multicastdisabled.md)<br/>                   | Not supported<br/> **Windows Server 2003:** Read/write<br/> <br/> |
| [**MulticastLeaseExpires**](networks-multicastleaseexpires.md)<br/>           | Not supported<br/> **Windows Server 2003:** Read-only<br/> <br/>  |
| [**MulticastLeaseObtained**](networks-multicastleaseobtained.md)<br/>         | Not supported<br/> **Windows Server 2003:** Read-only<br/> <br/>  |
| [**MulticastLeaseRequestId**](networks-multicastleaserequestid.md)<br/>       | Not supported<br/> **Windows Server 2003:** Read-only<br/> <br/>  |
| [**MulticastLeaseServer**](networks-multicastleaseserver.md)<br/>             | Not supported<br/> **Windows Server 2003:** Read-only<br/> <br/>  |



 

 

 





