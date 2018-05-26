---
title: AddByFileForwardLookupZone method of the PS\_DnsServerStubZone class
description: Adds a DNS stub zone.
audience: developer
ms.assetid: f29928be-ff64-472c-b70f-457f0cae66ae
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByFileForwardLookupZone method
- AddByFileForwardLookupZone method, PS_DnsServerStubZone class
- PS_DnsServerStubZone class, AddByFileForwardLookupZone method
topic_type:
- apiref
api_name:
- PS_DnsServerStubZone.AddByFileForwardLookupZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByFileForwardLookupZone method of the PS\_DnsServerStubZone class

Adds a DNS stub zone.

## Syntax


```mof
uint32 AddByFileForwardLookupZone(
  [in]  boolean           LoadExisting,
  [in]  string            MasterServers[],
  [in]  string            ComputerName,
  [in]  string            Name,
  [in]  string            ZoneFile,
  [in]  boolean           PassThru,
  [out] DnsServerStubZone cmdletOutput
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

*ComputerName* \[in\]
</dt> <dd>

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ZoneFile* \[in\]
</dt> <dd>

Specifies name of the zone file. This parameter is only relevant for file-backed DNS.

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

 

 





