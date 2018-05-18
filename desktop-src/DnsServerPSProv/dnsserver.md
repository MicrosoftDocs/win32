---
title: DnsServer class
description: Represents a DNS Server configuration.
audience: developer
ms.assetid: 'f1004904-0e11-477b-838d-38e86194ddee'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServer class", "DnsServer class, described"]
topic_type:
- apiref
api_name:
- DnsServer
- DnsServer.ServerSetting
- DnsServer.ServerDsSetting
- DnsServer.ServerScavenging
- DnsServer.ServerRecursion
- DnsServer.ServerDiagnostics
- DnsServer.ServerGlobalNameZone
- DnsServer.ServerCache
- DnsServer.ServerGlobalQueryBlockList
- DnsServer.ServerEdns
- DnsServer.ServerForwarder
- DnsServer.ServerRootHint
- DnsServer.ServerZone
- DnsServer.ServerZoneScope
- DnsServer.ServerRecursionScopes
- DnsServer.ServerClientSubnets
- DnsServer.ServerZoneAging
- DnsServer.ServerPolicies
- DnsServer.ServerResponseRateLimiting
- DnsServer.ServerResponseRateLimitingExceptionlists
- DnsServer.VirtualizedServer
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServer class

Represents a DNS Server configuration.

> [!Note]  
> The DNS server must be running Windows Server 2008 R2 or above.

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServer
{
  DnsServerSetting                           ServerSetting;
  DnsServerDsSetting                         ServerDsSetting;
  DnsServerScavenging                        ServerScavenging;
  DnsServerRecursion                         ServerRecursion;
  DnsServerDiagnostics                       ServerDiagnostics;
  DnsServerGlobalNameZone                    ServerGlobalNameZone;
  DnsServerCache                             ServerCache;
  DnsServerGlobalQueryBlockList              ServerGlobalQueryBlockList;
  DnsServerEdns                              ServerEdns;
  DnsServerForwarder                         ServerForwarder;
  DnsServerRootHint                          ServerRootHint[];
  DnsServerZone                              ServerZone[];
  DnsZoneScope                               ServerZoneScope[];
  DnsServerRecursionScope                    ServerRecursionScopes[];
  DnsServerClientSubnet                      ServerClientSubnets[];
  DnsServerZoneAging                         ServerZoneAging[];
  DnsServerPolicy                            ServerPolicies[];
  DnsServerResponseRateLimiting              ServerResponseRateLimiting;
  DnsServerResponseRateLimitingExceptionlist ServerResponseRateLimitingExceptionlists[];
  DnsVirtualizedServer                       VirtualizedServer[];
};
```

## Members

The **DnsServer** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServer** class has these properties.

<dl> <dt>

**ServerCache**
</dt> <dd> <dl> <dt>

Data type: **DnsServerCache**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerCache**](dnsservercache.md)")
</dt> </dl>

The [**DnsServerCache**](dnsservercache.md) that contains the DNS server cache settings on the DNS sever.

</dd> <dt>

**ServerClientSubnets**
</dt> <dd> <dl> <dt>

Data type: **DnsServerClientSubnet** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerClientSubnet**](dnsserverclientsubnet.md)")
</dt> </dl>

An array of [**DnsServerClientSubnet**](dnsserverclientsubnet.md) that contains the server/client subnet settings.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> <dt>

**ServerDiagnostics**
</dt> <dd> <dl> <dt>

Data type: **DnsServerDiagnostics**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerDiagnostics**](dnsserverdiagnostics.md)")
</dt> </dl>

A [**DnsServerDiagnostics**](dnsserverdiagnostics.md) that contains the DNS event logging details for the DNS server

</dd> <dt>

**ServerDsSetting**
</dt> <dd> <dl> <dt>

Data type: **DnsServerDsSetting**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerDsSetting**](dnsserverdssetting.md)")
</dt> </dl>

A [**DnsServerDsSetting**](dnsserverdssetting.md) that contains the DNS server Active Directory settings on the DNS sever.

</dd> <dt>

**ServerEdns**
</dt> <dd> <dl> <dt>

Data type: **DnsServerEdns**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerEDns**](dnsserveredns.md)")
</dt> </dl>

A [**DnsServerEDns**](dnsserveredns.md) that contains the Extension mechanisms for DNS (EDNS) configuration settings on the DNS sever.

</dd> <dt>

**ServerForwarder**
</dt> <dd> <dl> <dt>

Data type: **DnsServerForwarder**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerForwarder**](dnsserverforwarder.md)")
</dt> </dl>

A [**DnsServerForwarder**](dnsserverforwarder.md) that contains the DNS forwarder configuration settings on the DNS server.

</dd> <dt>

**ServerGlobalNameZone**
</dt> <dd> <dl> <dt>

Data type: **DnsServerGlobalNameZone**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerGlobalNameZone**](dnsserverglobalnamezone.md)")
</dt> </dl>

A [**DnsServerGlobalNameZone**](dnsserverglobalnamezone.md) that contains the DNS server global name zone configuration details on the DNS sever.

</dd> <dt>

**ServerGlobalQueryBlockList**
</dt> <dd> <dl> <dt>

Data type: **DnsServerGlobalQueryBlockList**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerGlobalQueryBlockList**](dnsserverglobalqueryblocklist.md)")
</dt> </dl>

A [**DnsServerGlobalQueryBlockList**](dnsserverglobalqueryblocklist.md) that contains the global query block list on the DNS server.

</dd> <dt>

**ServerPolicies**
</dt> <dd> <dl> <dt>

Data type: **DnsServerPolicy** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerPolicy**](dnsserverpolicy.md)")
</dt> </dl>

An array of [**DnsServerPolicy**](dnsserverpolicy.md) containing the server policy settings.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> <dt>

**ServerRecursion**
</dt> <dd> <dl> <dt>

Data type: **DnsServerRecursion**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerRecursion**](dnsserverrecursion.md)")
</dt> </dl>

A [**DnsServerRecursion**](dnsserverrecursion.md) that contains the DNS server recursion settings on the DNS sever.

</dd> <dt>

**ServerRecursionScopes**
</dt> <dd> <dl> <dt>

Data type: **DnsServerRecursionScope** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerRecursionScope**](dnsserverrecursionscope.md)")
</dt> </dl>

An array of [**DnsServerRecursionScope**](dnsserverrecursionscope.md) that contains the server recursion scope.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> <dt>

**ServerResponseRateLimiting**
</dt> <dd> <dl> <dt>

Data type: **DnsServerResponseRateLimiting**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerResponseRateLimiting**](dnsserverresponseratelimiting.md)")
</dt> </dl>

A [**DnsServerResponseRateLimiting**](dnsserverresponseratelimiting.md) containing the DNS Server Response Rate Limiting.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> <dt>

**ServerResponseRateLimitingExceptionlists**
</dt> <dd> <dl> <dt>

Data type: **DnsServerResponseRateLimitingExceptionlist** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerResponseRateLimitingExceptionlist**](dnsserverresponseratelimitingexceptionlist.md)")
</dt> </dl>

A [**DnsServerResponseRateLimitingExceptionlist**](dnsserverresponseratelimitingexceptionlist.md) containing the DNS Server Response Rate Limiting Exception lists.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> <dt>

**ServerRootHint**
</dt> <dd> <dl> <dt>

Data type: **DnsServerRootHint** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerRootHint**](dnsserverroothint.md)")
</dt> </dl>

An array of [**DnsServerRootHint**](dnsserverroothint.md) that contains the DNS root hints on the DNS server.

</dd> <dt>

**ServerScavenging**
</dt> <dd> <dl> <dt>

Data type: **DnsServerScavenging**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerScavenging**](dnsserverscavenging.md)")
</dt> </dl>

A [**DnsServerScavenging**](dnsserverscavenging.md) that contains the DNS aging and scavenging settings on the DNS sever.

</dd> <dt>

**ServerSetting**
</dt> <dd> <dl> <dt>

Data type: **DnsServerSetting**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerSetting**](dnsserversetting.md)")
</dt> </dl>

A [**DnsServerSetting**](dnsserversetting.md) that contains the DNS server settings.

</dd> <dt>

**ServerZone**
</dt> <dd> <dl> <dt>

Data type: **DnsServerZone** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerZone**](dnsserverzone.md)")
</dt> </dl>

An array of [**DnsServerZone**](dnsserverzone.md) that contains the names of the DNS zones of the DNS server.

</dd> <dt>

**ServerZoneAging**
</dt> <dd> <dl> <dt>

Data type: **DnsServerZoneAging** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerZoneAging**](dnsserverzoneaging.md)")
</dt> </dl>

An array of [**DnsServerZoneAging**](dnsserverzoneaging.md) that contains the aging settings for each DNS zone of the DNS server.

</dd> <dt>

**ServerZoneScope**
</dt> <dd> <dl> <dt>

Data type: **DnsZoneScope** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsZoneScope**](dnszonescope.md)")
</dt> </dl>

An array of [**DnsZoneScope**](dnszonescope.md) that contains the scope of each DNS zone of the DNS server.

**Windows Server 2012:** This property is not supported before Windows Server 2012 R2.

</dd> <dt>

**VirtualizedServer**
</dt> <dd> <dl> <dt>

Data type: **DnsVirtualizedServer** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("DnsVirtualizedServer")
</dt> </dl>

Virtualized DNS server configuration object.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





