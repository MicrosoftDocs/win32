---
title: AddByMX method of the PS\_DnsServerResourceRecord class
description: Adds an MX resource record to a DNS server.
audience: developer
ms.assetid: 49a4cfca-370a-4c23-8f97-cc90c49ed183
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByMX method
- AddByMX method, PS_DnsServerResourceRecord class
- PS_DnsServerResourceRecord class, AddByMX method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByMX
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByMX method of the PS\_DnsServerResourceRecord class

Adds an MX resource record to a DNS server.

## Syntax


```mof
uint32 AddByMX(
  [in]  string                  ZoneName,
  [in]  string                  MailExchange,
  [in]  uint16                  Preference,
  [in]  datetime                TimeToLive,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 AllowUpdateAny,
  [in]  string                  Name,
  [in]  boolean                 MX,
  [in]  string                  ComputerName,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*MailExchange* \[in\]
</dt> <dd>

Specifies an FQDN for a mail exchanger. This value must resolve to a corresponding host (A) resource record.

</dd> <dt>

*Preference* \[in\]
</dt> <dd>

Specifies a priority, from 0 to 65535, for this MX resource record. A service attempts to contact mail servers in the order of preference from lowest priority value to highest priority value.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

Specifies the Time to Live (TTL) value, in seconds, for a resource record. Other DNS servers use this length of time to determine how long to cache a record. The Start of Authority (SOA) record defines the default TTL.

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

Indicates that the DNS server uses a time stamp for the resource record that this method adds. A DNS server can scavenge resource records that have become stale based on a time stamp.

</dd> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

Indicates that any authenticated user can update a resource record that has the same owner name.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the host or child domain for the mail exchange record. To add an MX resource record for the parent domain, specify a dot (.).

</dd> <dt>

*MX* \[in\]
</dt> <dd>

If specified, creates a DNS Server Resource Record MX.

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

 

 





