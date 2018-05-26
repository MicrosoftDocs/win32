---
Description: IP Helper provides information about the network configuration of the local computer.
ms.assetid: 6135dca5-00c8-4ed4-bb89-7c99abeb7c7c
title: Retrieving Information About Network Configuration
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Information About Network Configuration

IP Helper provides information about the network configuration of the local computer. To retrieve general configuration information, use the [**GetNetworkParams**](/windows/win32/Iphlpapi/nf-iphlpapi-getnetworkparams?branch=master) function. This function returns information that is not specific to a particular adapter or interface. For example, **GetNetworkParams** returns a list of the DNS servers that are used by the local computer.

-   For code samples involving [**GetNetworkParams**](/windows/win32/Iphlpapi/nf-iphlpapi-getnetworkparams?branch=master) see [Retrieving Information Using GetNetworkParams](retrieving-information-using-getnetworkparams.md).

 

 



