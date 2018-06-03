---
title: AddBySrv method of the PS\_DnsServerResourceRecord class
description: Adds the record to a specified zone in a DNS server.
audience: developer
ms.assetid: 3fa08a4d-3aef-4cc0-ae91-700873d0f061
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddBySrv method
- AddBySrv method, PS_DnsServerResourceRecord class
- PS_DnsServerResourceRecord class, AddBySrv method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddBySrv
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddBySrv method of the PS\_DnsServerResourceRecord class

Adds the record to a specified zone in a DNS server.

## Syntax


```mof
uint32 AddBySrv(
  [in]  string                  DomainName,
  [in]  uint16                  Priority,
  [in]  uint16                  Weight,
  [in]  string                  ZoneName,
  [in]  uint16                  Port,
  [in]  datetime                TimeToLive,
  [in]  boolean                 AllowUpdateAny,
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 Srv,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*DomainName* \[in\]
</dt> <dd>

Name of the domain

</dd> <dt>

*Priority* \[in\]
</dt> <dd>

Specifies the priority of a DNS server. Clients try to contact the server that has the lowest priority.

</dd> <dt>

*Weight* \[in\]
</dt> <dd>

Specifies a value for the weight of the target host for a resource record. You can use this parameter when you have multiple hosts that have an identical priority. Use of the host is proportional to its weight.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the DNS zone.

</dd> <dt>

*Port* \[in\]
</dt> <dd>

Specifies the port where the server listens for the service.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

Specifies the Time to Live (TTL) value, in seconds, for a resource record. Other DNS servers use this length of time to determine how long to cache a record.

</dd> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

Allow any authenticated user to update DNS record with same owner name

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of a DNS server resource record object.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

Indicates that the DNS server uses a time stamp for the resource record that this method adds. A DNS server can scavenge resource records that have become stale based on a time stamp.

</dd> <dt>

*Srv* \[in\]
</dt> <dd>

If specified, creates an SRV DNS Server resource record.

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

 

 





