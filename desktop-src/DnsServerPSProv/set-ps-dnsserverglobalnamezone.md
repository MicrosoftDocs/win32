---
title: Set method of the PS\_DnsServerGlobalNameZone class
description: Enables or disables support for the GlobalNames zone. The GlobalNames zone supports resolution of single-label DNS names across a forest.
audience: developer
ms.assetid: 2a5db42f-1f67-41bc-833c-1c6699c30541
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DnsServerGlobalNameZone class
- PS_DnsServerGlobalNameZone class, Set method
topic_type:
- apiref
api_name:
- PS_DnsServerGlobalNameZone.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DnsServerGlobalNameZone class

Enables or disables support for the GlobalNames zone. The GlobalNames zone supports resolution of single-label DNS names across a forest.

## Syntax


```mof
uint32 Set(
  [in]  boolean                 AlwaysQueryServer,
  [in]  boolean                 BlockUpdates,
  [in]  boolean                 Enable,
  [in]  boolean                 EnableEDnsProbes,
  [in]  boolean                 GlobalOverLocal,
  [in]  boolean                 PreferAaaa,
  [in]  string                  ComputerName,
  [in]  uint32                  SendTimeout,
  [in]  datetime                ServerQueryInterval,
  [in]  boolean                 PassThru,
  [out] DnsServerGlobalNameZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*AlwaysQueryServer* \[in\]
</dt> <dd>

A Boolean value that indicates, when FALSE, that the DNS server will attempt to use GNZ service records (SRV records named \_globalnames.\_msdcs.\[forestroot\]) from the server's cache when updating the list of remote DNS servers hosting a GNZ, or when TRUE, that the server MUST always attempt a remote DNS query for such records. The value MUST be ignored if the server hosts a GNZ. The value MUST be limited to 0x00000000 and 0x00000001. The default value MUST be 0x00000000, and the value zero MUST be allowed.

</dd> <dt>

*BlockUpdates* \[in\]
</dt> <dd>

A Boolean value that indicates whether the DNS server will block updates in authoritative zones if they are for FQDNs that would collide with labels found in the GNZ. If the value of this property is 0x00000000, then a check for this collision MUST NOT be performed. To test whether a name collides with a name present in the GNZ, the DNS server MUST extract the relative portion of the name that is being updated by removing the rightmost labels that make up the zone name, and then perform a case-insensitive search in the locally hosted GNZ for a name matching the remaining labels. If a match for these labels is found in the locally hosted GNZ and the value of this property is 0x00000001 then the update MUST be blocked. The value MUST be limited to 0x00000000 and 0x00000001. The default value MUST be 0x00000001, and the value zero MUST be allowed.

</dd> <dt>

*Enable* \[in\]
</dt> <dd>

0: Disables support for the GlobalNames zone. When you set the value of this command to 0, the DNS Server service does not resolve single-label names in the GlobalNames zone. 1: Enables support for the GlobalNames zone. When you set the value of this command to 1, the DNS Server service resolves single-label names in the GlobalNames zone.

</dd> <dt>

*EnableEDnsProbes* \[in\]
</dt> <dd>

A Boolean value that indicates whether the DNS server will honor the EnableEDnsProbes Boolean value for a remote GNZ. A value of TRUE indicates that the server MUST attempt to use EDNS for queries sent to a remote GNZ if the Boolean value of EnableEDnsProbes is also TRUE, and otherwise MUST NOT attempt to use EDNS for such queries. A value of FALSE indicates that the server MUST NOT attempt to use EDNS for queries sent to a remote GNZ, regardless of the value of EnableEDnsProbes. The value MUST be limited to 0x00000000 and 0x00000001. The default value MUST be 0x00000001, and the value zero MUST be allowed.

</dd> <dt>

*GlobalOverLocal* \[in\]
</dt> <dd>

Specifies whether the DNS Server service looks first in the GlobalNames zone or local zones when it resolves names. 0: The DNS Server service attempts to resolve names by querying the GlobalNames zone before it queries the zones for which it is authoritative. 1: The DNS Server service attempts to resolve names by querying the zones for which it is authoritative before it queries the GlobalNames zone. A Boolean value that indicates whether the DNS server will prefer GNZ or authoritative zone data when determining what data to use to answer queries. If TRUE, the DNS server MUST prefer authoritative zone data. otherwise, the DNS server MUST prefer GNZ data. The value MUST be limited to 0x00000000 and 0x00000001. The default value MUST be 0x00000000.

</dd> <dt>

*PreferAaaa* \[in\]
</dt> <dd>

A Boolean value that indicates whether the DNS server will prefer type AAAA address records to type A records when sending queries to a remote DNS server that is hosting a GNZ. If the value is 0x00000000 then queries to a remote DNS server hosting a GNZ MUST be sent using IPv4 if any IPv4 addresses for the remote DNS server name can be found. If no IPv4 addresses are found for the remote DNS server name, then IPv6 addresses MUST be used. If the value of this property is 0x00000001, then IPv6 addresses for the remote DNS server MUST be used, and IPv4 addresses MUST NOT be used unless no IPv6 addresses can be found. The value MUST be limited to 0x00000000 and 0x00000001. The default value MUST be 0x00000000, and the value zero MUST be allowed and treated literally.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*SendTimeout* \[in\]
</dt> <dd>

The number of seconds the DNS server will wait when sending a query to a remote GNZ before assuming that no answer will ever be received. The value MUST be limited to the range 0x00000001 to 0x0000000F, inclusive. The default value MUST be 0x00000003, and the value zero MUST be treated as a flag value for the default. Range = 1, 15

</dd> <dt>

*ServerQueryInterval* \[in\]
</dt> <dd>

The maximum interval in seconds between queries to refresh the set of remote DNS servers hosting the GNZ. The value MUST be limited to the range 0x0000003C (60 seconds) to 0x00278D00 (30 days), inclusive. The default value MUST be 0x00005460 (6 hours), and the value zero MUST be treated as a flag value for the default. Range = 60, 2592000

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerGlobalNameZone**](ps-dnsserverglobalnamezone.md)
</dt> </dl>

 

 





