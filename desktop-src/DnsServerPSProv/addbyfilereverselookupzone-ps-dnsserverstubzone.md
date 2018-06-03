---
title: AddByFileReverseLookupZone method of the PS\_DnsServerStubZone class
description: Adds a DNS stub zone.
audience: developer
ms.assetid: 7f70d6cb-f657-4e64-a045-da4a5d7b3061
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByFileReverseLookupZone method
- AddByFileReverseLookupZone method, PS_DnsServerStubZone class
- PS_DnsServerStubZone class, AddByFileReverseLookupZone method
topic_type:
- apiref
api_name:
- PS_DnsServerStubZone.AddByFileReverseLookupZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByFileReverseLookupZone method of the PS\_DnsServerStubZone class

Adds a DNS stub zone.

## Syntax


```mof
uint32 AddByFileReverseLookupZone(
  [in]  boolean           LoadExisting,
  [in]  string            MasterServers[],
  [in]  string            NetworkId,
  [in]  string            ComputerName,
  [in]  string            ZoneFile,
  [in]  boolean           PassThru,
  [out] DnsServerStubZone cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*LoadExisting* \[in\]
</dt> <dd>

Loads an existing file for the zone. Otherwise, the method creates default zone records automatically. This switch is relevant only for file-backed zones.

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

*ZoneFile* \[in\]
</dt> <dd>

Indicates the name of the zone file.

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

 

 





