---
title: AddByAAAA method of the PS\_DnsServerResourceRecord class
description: Adds a type AAAA resource record to a DNS server.
audience: developer
ms.assetid: eb36f338-10fe-48b4-927f-7c005b960ef7
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByAAAA method
- AddByAAAA method, PS_DnsServerResourceRecord class
- PS_DnsServerResourceRecord class, AddByAAAA method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByAAAA
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByAAAA method of the PS\_DnsServerResourceRecord class

Adds a type AAAA resource record to a DNS server.

## Syntax


```mof
uint32 AddByAAAA(
  [in]  string                  IPv6Address,
  [in]  string                  ZoneName,
  [in]  boolean                 CreatePtr,
  [in]  boolean                 AgeRecord,
  [in]  datetime                TimeToLive,
  [in]  boolean                 AllowUpdateAny,
  [in]  string                  ComputerName,
  [in]  string                  Name,
  [in]  boolean                 AAAA,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*IPv6Address* \[in\]
</dt> <dd>

Specifies an array of IPv6 addresses.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the DNS zone to which the record is being added.

</dd> <dt>

*CreatePtr* \[in\]
</dt> <dd>

Indicates that the DNS server automatically creates an associated pointer (PTR) resource record for an AAAA record. A PTR resource record maps an IP address to an FQDN.

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

Indicates that the DNS server uses a time stamp for the resource record that this method adds. A DNS server can scavenge resource records that have become stale based on a time stamp.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

Specifies the Time to Live (TTL) value, in seconds, for a resource record. Other DNS servers use this length of time to determine how long to cache a record.

</dd> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

Allows any authenticated user to update DNS record with same owner name

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies a host name.

</dd> <dt>

*AAAA* \[in\]
</dt> <dd>

If specified, creates a DNS Server Resource Record AAAA.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is unavailable prior to Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerResourceRecord**](dnsserverresourcerecord.md) class.

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

[**PS\_DnsServerResourceRecord**](ps-dnsserverresourcerecord.md)
</dt> </dl>

 

 





