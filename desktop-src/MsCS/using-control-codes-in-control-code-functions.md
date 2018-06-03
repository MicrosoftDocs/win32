---
title: Using Control Codes in Control Code Functions
description: To perform control code operations you need to call a control code function and specify a control code as one of the parameters.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4d15ac9c-6fee-40b7-9481-185cd010f2df
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- control codes Failover Cluster ,using in control code functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Control Codes in Control Code Functions

To perform control code operations you need to call a control code function and specify a [control code](about-control-codes.md) as one of the parameters. The control code determines the values of the other parameters and the general algorithm to use for the function call. There are two general algorithms for calling control code functions based on the type of operation the control code performs. The type of operation, in turn, is determined by the operation code that is part of each control code. For more information on the operations associated with control codes, see [Control Code Architecture](control-code-architecture.md).

The following sections describe these algorithms.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Section</th>
<th>Control code operation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Getting Information with Control Codes](getting-information-with-control-codes.md)</td>
<td><ul>
<li>ENUM_COMMON_PROPERTIES</li>
<li>ENUM_PRIVATE_PROPERTIES</li>
<li>GET_CHARACTERISTICS</li>
<li>GET_COMMON_PROPERTIES</li>
<li>GET_CRYPTO_CHECKPOINTS</li>
<li>GET_FLAGS</li>
<li>GET_ID</li>
<li>GET_NAME</li>
<li>GET_NETWORK_NAME</li>
<li>GET_PRIVATE_PROPERTIES</li>
<li>GET_REGISTRY_CHECKPOINTS</li>
<li>GET_REQUIRED_DEPENDENCIES</li>
<li>GET_RESOURCE_TYPE</li>
<li>GET_RO_COMMON_PROPERTIES</li>
<li>GET_RO_PRIVATE_PROPERTIES</li>
<li>STORAGE_GET_AVAILABLE_DISKS</li>
<li>STORAGE_GET_DISK_INFO</li>
</ul></td>
</tr>
<tr class="even">
<td>[Changing the Cluster Configuration with Control Codes](changing-the-cluster-configuration-with-control-codes.md)</td>
<td><ul>
<li>ADD_CRYPTO_CHECKPOINTS</li>
<li>ADD_REGISTRY_CHECKPOINTS</li>
<li>DELETE_CRYPTO_CHECKPOINTS</li>
<li>DELETE_REGISTRY_CHECKPOINTS</li>
<li>SET_COMMON_PROPERTIES</li>
<li>SET_NAME</li>
<li>SET_PRIVATE_PROPERTIES</li>
<li>VALIDATE_COMMON_PROPERTIES</li>
<li>VALIDATE_PRIVATE_PROPERTIES</li>
</ul></td>
</tr>
</tbody>
</table>



 

 

 




