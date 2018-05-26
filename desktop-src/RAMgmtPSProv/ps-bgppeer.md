---
title: PS\_BgpPeer class
description: Manages Border Gateway Protocol (BGP) sessions between peers.
audience: developer
ms.assetid: 2acd3cba-7a37-45e4-b5cd-6d40bd861af6
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_BgpPeer class
- PS_BgpPeer class, described
topic_type:
- apiref
api_name:
- PS_BgpPeer
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_BgpPeer class

Manages Border Gateway Protocol (BGP) sessions between peers.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_BgpPeer
{
};
```

## Members

The **PS\_BgpPeer** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_BgpPeer** class has these methods.



| Method                                                                | Description                                                                                                         |
|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-bgppeer.md)                                         | Adds a BGP peer to a BGP router.<br/>                                                                         |
| [**Get**](get-ps-bgppeer.md)                                         | Retrieves configuration information for BGP peers.<br/>                                                       |
| [**GetForAllRoutingDomains**](ps-bgppeer-getforallroutingdomains.md) | This cmdlet retrieves the BGP Peer configuration information for all BGP peers from all routing domains.<br/> |
| [**Remove**](remove-ps-bgppeer.md)                                   | Removes a BGP peer from a BGP router.<br/>                                                                    |
| [**Set**](set-ps-bgppeer.md)                                         | Updates the configuration of the specified BGP peer.<br/>                                                     |
| [**Start**](start-ps-bgppeer.md)                                     | Starts a BGP routing session for one or more peers.<br/>                                                      |
| [**Stop**](stop-ps-bgppeer.md)                                       | Stops a BGP routing session for one or more peers.<br/>                                                       |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





