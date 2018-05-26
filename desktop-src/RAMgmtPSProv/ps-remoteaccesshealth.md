---
title: PS\_RemoteAccessHealth class
description: Health of Remote Access cluster, server (DA and VPN) and its components.
audience: developer
ms.assetid: debb3728-c023-4cdf-a2f4-98388a6c0a7b
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_RemoteAccessHealth class
- PS_RemoteAccessHealth class, described
topic_type:
- apiref
api_name:
- PS_RemoteAccessHealth
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_RemoteAccessHealth class

Health of Remote Access cluster, server (DA and VPN) and its components

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_RemoteAccessHealth
{
};
```

## Members

The **PS\_RemoteAccessHealth** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessHealth** class has these methods.



| Method                                                                   | Description                                                                                                                                                                                                                                                                                                                                                         |
|:-------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetByCluster**](ps-remoteaccesshealth-getbycluster.md)               | This cmdlet is used to obtain the current health of a Remote Access deployment.<br/> 1. Health of a specific Remote Access server<br/> 2. Health of a load balancing cluster<br/> 3. Health of a site, in case of a multisite deployment - this again corresponds to the health of a single server or health of a cluster at that site<br/> |
| [**GetByEntrypointName**](ps-remoteaccesshealth-getbyentrypointname.md) | This cmdlet is used to obtain the current health of a Remote Access deployment.<br/> 1. Health of a specific Remote Access server<br/> 2. Health of a load balancing cluster<br/> 3. Health of a site, in case of a multisite deployment - this again corresponds to the health of a single server or health of a cluster at that site<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





