---
title: PS\_RemoteAccessLoadBalancerNode class
description: Represents the servers in a load balancing cluster.
audience: developer
ms.assetid: 26bb3f41-9ccd-4f94-8413-a39ce37f0a19
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_RemoteAccessLoadBalancerNode class
- PS_RemoteAccessLoadBalancerNode class, described
topic_type:
- apiref
api_name:
- PS_RemoteAccessLoadBalancerNode
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_RemoteAccessLoadBalancerNode class

Represents the servers in a load balancing cluster.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_RemoteAccessLoadBalancerNode
{
};
```

## Members

The **PS\_RemoteAccessLoadBalancerNode** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessLoadBalancerNode** class has these methods.



| Method                                                   | Description                                                                                  |
|:---------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**Add**](add-ps-remoteaccessloadbalancernode.md)       | This cmdlet adds a single remote access server to the load balancing cluster<br/>      |
| [**Remove**](remove-ps-remoteaccessloadbalancernode.md) | This cmdlet removes a single remote access server from the load balancing cluster<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





