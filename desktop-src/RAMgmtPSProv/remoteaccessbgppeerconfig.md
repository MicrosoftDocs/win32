---
title: RemoteAccessBgpPeerConfig class
description: Manages a Border Gateway Protocol (BGP) Peer Connection State.
audience: developer
ms.assetid: 9f51ecb2-a25b-4779-8033-9681d1c067bd
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessBgpPeerConfig class
- RemoteAccessBgpPeerConfig class, described
topic_type:
- apiref
api_name:
- RemoteAccessBgpPeerConfig
- RemoteAccessBgpPeerConfig.RoutingDomain
- RemoteAccessBgpPeerConfig.Peer
- RemoteAccessBgpPeerConfig.PeerStaus
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoteAccessBgpPeerConfig class

Manages a Border Gateway Protocol (BGP) Peer Connection State.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessBgpPeerConfig
{
  string  RoutingDomain;
  string  Peer[];
  boolean PeerStaus[];
};
```

## Members

The **RemoteAccessBgpPeerConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessBgpPeerConfig** class has these properties.

<dl> <dt>

**Peer**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IP address of the peer

</dd> <dt>

**PeerStaus**
</dt> <dd> <dl> <dt>

Data type: **boolean** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The connection state of the peer

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the routing domain

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





