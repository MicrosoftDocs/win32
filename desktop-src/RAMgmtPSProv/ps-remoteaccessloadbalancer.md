---
title: PS\_RemoteAccessLoadBalancer class
description: Represents load balancing configuration for Remote Access.
audience: developer
ms.assetid: c1c49050-38ae-49a7-80f2-d99d4596afd3
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_RemoteAccessLoadBalancer class
- PS_RemoteAccessLoadBalancer class, described
topic_type:
- apiref
api_name:
- PS_RemoteAccessLoadBalancer
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_RemoteAccessLoadBalancer class

Represents load balancing configuration for Remote Access.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_RemoteAccessLoadBalancer
{
};
```

## Members

The **PS\_RemoteAccessLoadBalancer** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessLoadBalancer** class has these methods.



| Method                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                          |
|:-----------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-remoteaccessloadbalancer.md)                                                 | This cmdlet displays the load balancing configuration.<br/>                                                                                                                                                                                                                                                                                                                    |
| [**SetByDisableLoadBalancing**](setbydisableloadbalancing-ps-remoteaccessloadbalancer.md)     | This cmdlet does the following1. Configures load balancing clusters on the internal and Internet interfaces (in case of double NIC) or on a single interface (in case of single NIC) for remote access and adds the current server to the cluster. Current server refers to the server on which this cmdlet is run. 2. Enables/disables usage of 3rd party load balancer.<br/> |
| [**SetByEnableLoadBalancing**](setbyenableloadbalancing-ps-remoteaccessloadbalancer.md)       | This cmdlet does the following1. Configures load balancing clusters on the internal and Internet interfaces (in case of double NIC) or on a single interface (in case of single NIC) for remote access and adds the current server to the cluster. Current server refers to the server on which this cmdlet is run. 2. Enables/disables usage of 3rd party load balancer.<br/> |
| [**SetByThirdPartyLoadBalancer**](setbythirdpartyloadbalancer-ps-remoteaccessloadbalancer.md) | This cmdlet does the following1. Configures load balancing clusters on the internal and Internet interfaces (in case of double NIC) or on a single interface (in case of single NIC) for remote access and adds the current server to the cluster. Current server refers to the server on which this cmdlet is run. 2. Enables/disables usage of 3rd party load balancer.<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





