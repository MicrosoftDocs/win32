---
title: AddByADReverseLookupZone method of the PS\_DnsServerStubZone class
description: Adds a DNS stub zone.
audience: developer
ms.assetid: 433087eb-c239-473b-bc05-6bc36b51c009
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByADReverseLookupZone method
- AddByADReverseLookupZone method, PS_DnsServerStubZone class
- PS_DnsServerStubZone class, AddByADReverseLookupZone method
topic_type:
- apiref
api_name:
- PS_DnsServerStubZone.AddByADReverseLookupZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByADReverseLookupZone method of the PS\_DnsServerStubZone class

Adds a DNS stub zone.

## Syntax


```mof
uint32 AddByADReverseLookupZone(
  [in]  boolean           LoadExisting,
  [in]  string            MasterServers[],
  [in]  string            NetworkId,
  [in]  string            ComputerName,
  [in]  string            ReplicationScope,
  [in]  string            DirectoryPartitionName,
  [in]  boolean           PassThru,
  [out] DnsServerStubZone cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*LoadExisting* \[in\]
</dt> <dd>

Loads an existing file for the zone. Otherwise, the cmdlet creates default zone records automatically. This switch is relevant only for file-backed zones.

</dd> <dt>

*MasterServers* \[in\]
</dt> <dd>

Specifies an array of IP addresses of the master servers of the zone. You can use both IPv4 and IPv6.

</dd> <dt>

*NetworkId* \[in\]
</dt> <dd>

Specifies a network ID and prefix length for a reverse lookup zone.. Use the format A.B.C.D/prefix. Use the format A.B.C.D/prefix. Only class A, B, C, or D zones are created. If you specify a prefix that is between classes, the longer prefix that is divisible by 8 is used. For example, typing 10.2.10.0/23 for NetworkId will result in the creation of the 10.2.10.0/24 reverse lookup zone, but not the 10.2.11.0/24 reverse lookup zone. If you enter a prefix longer than /24, a /32 reverse lookup zone is created.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*ReplicationScope* \[in\]
</dt> <dd>

Specifies the directory partition on which to store the zone. FQDN: Specifies fully qualified domain name of the directory partition. domain: Stores the zone on the domain directory partition. forest: Stores the zone on the enterprise directory partition. legacy: Stores the zone on a legacy directory partition. Parameter valid only if it is AD based.

The possible values are.

<dt>

<span id="Forest"></span><span id="forest"></span><span id="FOREST"></span>

<span id="Forest"></span><span id="forest"></span><span id="FOREST"></span>**Forest** ("Forest")


</dt> <dd>

The ForestDnsZone directory partition.

</dd> <dt>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>**Domain** ("Domain")


</dt> <dd>

The domain directory partition.

</dd> <dt>

<span id="Legacy"></span><span id="legacy"></span><span id="LEGACY"></span>

<span id="Legacy"></span><span id="legacy"></span><span id="LEGACY"></span>**Legacy** ("Legacy")


</dt> <dd>

A legacy directory partition

</dd> <dt>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>**Custom** ("Custom")


</dt> <dd>

A custom directory partition. The **DirectoryPartitionName** property must also be specified.

</dd> </dl> </dd> <dt>

*DirectoryPartitionName* \[in\]
</dt> <dd>

Specifies a directory partition on which to store the zone. Applicable only when the *ReplicationScope* parameter is set to "Custom".

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerStubZone**](dnsserverstubzone.md) class.

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

[**PS\_DnsServerStubZone**](ps-dnsserverstubzone.md)
</dt> </dl>

 

 





