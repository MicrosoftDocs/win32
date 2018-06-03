---
title: Failover Cluster Administrator Extension Registration Functions
description: A Failover Cluster Administrator extension DLL must be registered with the cluster and with COM. For information on how to register a Failover Cluster Administrator extension DLL, see Registering Resource Types.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2b3f3cf3-3793-4ea9-b420-6eb8aac55c40
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Failover Cluster Administrator Failover Cluster ,Failover Cluster Administrator Extension API,registration functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Failover Cluster Administrator Extension Registration Functions

A [Failover Cluster Administrator](cluster-administrator.md) extension DLL must be registered with the [*cluster*](https://www.bing.com/search?q=*cluster*) and with COM. For information on how to register a Failover Cluster Administrator extension DLL, see [Registering Resource Types](registering-resource-types.md).

The Failover Cluster Administrator extension registration functions follow.



| Function                                                                            | Description                                                                                                                                                 |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DllRegisterCluAdminExtension**](dllregistercluadminextension.md)<br/>     | Registers a Failover Cluster Administrator extension DLL with the cluster by adding information to the [cluster database](cluster-database.md).<br/> |
| [**DllUnregisterCluAdminExtension**](dllunregistercluadminextension.md)<br/> | Cancels the registration of a Failover Cluster Administrator extension DLL with the cluster by removing information from the cluster database.<br/>   |
| [**DllRegisterServer**](/previous-versions/windows/desktop/api/WtClusRes/)<br/>                           | Registers a Failover Cluster Administrator extension DLL with COM by adding information to the registry.<br/>                                         |
| [**DllUnregisterServer**](/previous-versions/windows/desktop/api/WtClusRes/)<br/>                       | Cancels the registration of a Failover Cluster Administrator extension DLL with COM by removing information from the registry.<br/>                   |



 

## Related topics

<dl> <dt>

[Failover Cluster Administrator Extension Functions and Interfaces](cluster-administrator-extension-functions.md)
</dt> </dl>

 

 





