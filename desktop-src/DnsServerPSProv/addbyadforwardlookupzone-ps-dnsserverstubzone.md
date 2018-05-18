---
title: AddByADForwardLookupZone method of the PS\_DnsServerStubZone class
description: Adds a DNS stub zone.
audience: developer
ms.assetid: '903abf0d-06a0-45cd-94ea-d00af191405f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddByADForwardLookupZone method", "AddByADForwardLookupZone method, PS_DnsServerStubZone class", "PS_DnsServerStubZone class, AddByADForwardLookupZone method"]
topic_type:
- apiref
api_name:
- PS_DnsServerStubZone.AddByADForwardLookupZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# AddByADForwardLookupZone method of the PS\_DnsServerStubZone class

Adds a DNS stub zone.

## Syntax


```mof
uint32 AddByADForwardLookupZone(
  [in]  boolean           LoadExisting,
  [in]  string            MasterServers[],
  [in]  string            ComputerName,
  [in]  string            ReplicationScope,
  [in]  string            Name,
  [in]  string            DirectoryPartitionName,
  [in]  boolean           PassThru,
  [out] DnsServerStubZone cmdletOutput
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

*ReplicationScope* \[in\]
</dt> <dd>

In case of AD it is below: Specifies the directory partition on which to store the zone. FQDN: Specifies fully qualified domain name of the directory partition. domain: Stores the zone on the domain directory partition. forest: Stores the zone on the enterprise directory partition. legacy: Stores the zone on a legacy directory partition. The Parameter is valid only if it is AD based.

The possible values are.

<dt>

<span id="Forest"></span><span id="forest"></span><span id="FOREST"></span>

<span id="Forest"></span><span id="forest"></span><span id="FOREST"></span>**Forest** ("Forest")


</dt> <dd>

(The ForestDnsZone directory partition.)

</dd> <dt>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>**Domain** ("Domain")


</dt> <dd>

(The domain directory partition.)

</dd> <dt>

<span id="Legacy"></span><span id="legacy"></span><span id="LEGACY"></span>

<span id="Legacy"></span><span id="legacy"></span><span id="LEGACY"></span>**Legacy** ("Legacy")


</dt> <dd>

(A legacy directory partition.)

</dd> <dt>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>**Custom** ("Custom")


</dt> <dd>

A custom directory partition specified in the **DirectoryPartitionName** parameter.

</dd> </dl> </dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerStubZone**](ps-dnsserverstubzone.md)
</dt> </dl>

 

 





