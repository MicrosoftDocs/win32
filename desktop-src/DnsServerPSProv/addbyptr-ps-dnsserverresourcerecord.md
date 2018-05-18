---
title: AddByPtr method of the PS\_DnsServerResourceRecord class
description: Adds a type PTR resource record to a DNS server.
audience: developer
ms.assetid: '80544979-25e5-4fff-a903-3035415b0e8a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddByPtr method", "AddByPtr method, PS_DnsServerResourceRecord class", "PS_DnsServerResourceRecord class, AddByPtr method"]
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByPtr
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# AddByPtr method of the PS\_DnsServerResourceRecord class

Adds a type PTR resource record to a DNS server.

## Syntax


```mof
uint32 AddByPtr(
  [in]  string                  PtrDomainName,
  [in]  string                  ZoneName,
  [in]  datetime                TimeToLive,
  [in]  boolean                 AllowUpdateAny,
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 Ptr,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*PtrDomainName* \[in\]
</dt> <dd>

Specifies an FQDN for a resource record in the DNS namespace. This value is the response to a reverse lookup using this PTR.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of a reverse lookup zone.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

Specifies the Time to Live (TTL) value, in seconds, for a resource record. Other DNS servers use this length of time to determine how long to cache a record. The Start of Authority (SOA) record defines the default TTL.

</dd> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

Indicates that any authenticated user can update a resource record that has the same owner name.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies part of the IP address for the host. You can use either an IPv4 or IPv6 address. For example, if an IPv4 class C reverse lookup zone is used, then –Name is the last octet of the IP address. If a class B reverse lookup zone is used, then –Name is the last two octets.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

Indicates that the DNS server uses a time stamp for the resource record that this method adds. A DNS server can scavenge resource records that have become stale based on a time stamp.

</dd> <dt>

*Ptr* \[in\]
</dt> <dd>

If specified, creates a PTR record.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is unavailable prior to Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerResourceRecord**](dnsserverresourcerecord.md) class.

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

[**PS\_DnsServerResourceRecord**](ps-dnsserverresourcerecord.md)
</dt> </dl>

 

 





