---
title: Configuring Cluster Parameters
description: The settings shown on the Cluster Parameters tab of the Network Load Balancing Properties dialog are accessed through the MicrosoftNLB\_ClusterSetting class, using the properties and methods shown in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 187448d8-6e61-4383-8fbf-9ff2daf02d17
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- cluster parameters in NLB Failover Cluster
- cluster parameters in NLB Failover Cluster ,configuring
- clusters Failover Cluster ,configuring parameters in NLB
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Configuring Cluster Parameters

The settings shown on the Cluster Parameters tab of the **Network Load Balancing Properties** dialog are accessed through the [**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md) class, using the properties and methods shown in the following table.



| Dialog setting                                                                          | Property or method                                                        |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **Cluster name** (full Internet name)<br/>                                        | **ClusterName**<br/>                                                |
| Primary [*cluster IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly)<br/> | **ClusterIPAddress**<br/>                                           |
| **Subnet mask**<br/>                                                              | **ClusterNetworkMask**<br/>                                         |
| **Network address**<br/>                                                          | **ClusterMACAddress**<br/>                                          |
| **Multicast support enabled check box**<br/>                                      | **MulticastSupportEnabled**<br/>                                    |
| **Remote control password**<br/>                                                  | [**SetPassword**](microsoftnlb-clustersetting-setpassword.md)<br/> |
| **Remote control enabled** check box<br/>                                         | **RemoteControlEnabled**<br/>                                       |



 

 

 





