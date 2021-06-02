---
description: IP Helper provides information about the network configuration of the local computer.
ms.assetid: 6135dca5-00c8-4ed4-bb89-7c99abeb7c7c
title: Retrieving Information About Network Configuration
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Information About Network Configuration

IP Helper provides information about the network configuration of the local computer. To retrieve general configuration information, use the [**GetNetworkParams**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getnetworkparams) function. This function returns information that is not specific to a particular adapter or interface. For example, **GetNetworkParams** returns a list of the DNS servers that are used by the local computer.

-   For code samples involving [**GetNetworkParams**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getnetworkparams) see [Retrieving Information Using GetNetworkParams](retrieving-information-using-getnetworkparams.md).

 

 



