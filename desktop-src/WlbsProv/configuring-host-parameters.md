---
title: Configuring Host Parameters
description: The settings shown on the \ 0034;Host Parameters \ 0034; tab of the Network Load Balancing Properties dialog box are accessed through the MicrosoftNLB\_NodeSetting class, by using the properties and methods shown in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 91045f0d-ba19-44af-83b9-fd5ab3d65ddb
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- host parameters in NLB Failover Cluster
- host parameters in NLB Failover Cluster ,configuring
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Host Parameters

The settings shown on the "Host Parameters" tab of the Network Load Balancing Properties dialog box are accessed through the [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) class, by using the properties and methods shown in the following table.



| Setting                         | Property or method                  |
|---------------------------------|-------------------------------------|
| Priority<br/>             | **HostPriority**<br/>         |
| Initial state active<br/> | **ClusterModeOnStart**<br/>   |
| Dedicated IP Address<br/> | **DedicatedIPAddress**<br/>   |
| Subnet mask<br/>          | **DedicatedNetworkMask**<br/> |



 

 

 





