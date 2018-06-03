---
title: AddByA method of the PS\_DnsServerResourceRecord class
description: Adds a host address (A) resource record resource to a DNS server.
audience: developer
ms.assetid: 69f3616f-da9d-4c73-9f9a-8289e927d7bd
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByA method
- AddByA method, PS_DnsServerResourceRecord class
- PS_DnsServerResourceRecord class, AddByA method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByA
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByA method of the PS\_DnsServerResourceRecord class

Adds a host address (A) resource record resource to a DNS server.

## Syntax


```mof
uint32 AddByA(
  [in]  boolean                 CreatePtr,
  [in]  string                  IPv4Address,
  [in]  string                  ZoneName,
  [in]  string                  Name,
  [in]  datetime                TimeToLive,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 AllowUpdateAny,
  [in]  boolean                 A,
  [in]  string                  ComputerName,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*CreatePtr* \[in\]
</dt> <dd>

Indicates that the DNS server automatically creates an associated pointer (PTR) resource record for an A record. A PTR resource record maps an IP address to an FQDN.

</dd> <dt>

*IPv4Address* \[in\]
</dt> <dd>

The IPv4 address of a host.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

The name of the DNS zone.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The host name.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

Specifies the Time to Live (TTL) value, in seconds, for a resource record. Other DNS servers use this length of time to determine how long to cache a record.

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

Indicates that the DNS server uses a time stamp for the resource record that this method adds. A DNS server can scavenge resource records that have become stale based on a time stamp.

</dd> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

Specifies that any authenticated user can update a resource record that has the same owner name.

</dd> <dt>

*A* \[in\]
</dt> <dd>

If specified, creates a DNS Server Resource Record A.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

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

 

 





