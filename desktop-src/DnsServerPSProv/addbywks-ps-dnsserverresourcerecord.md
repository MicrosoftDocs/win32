---
title: AddByWks method of the PS\_DnsServerResourceRecord class
description: Adds the record to a specified zone in a DNS server.
audience: developer
ms.assetid: '15f8b957-8039-4c96-8aea-8ebf8ad0124f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddByWks method", "AddByWks method, PS_DnsServerResourceRecord class", "PS_DnsServerResourceRecord class, AddByWks method"]
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByWks
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# AddByWks method of the PS\_DnsServerResourceRecord class

Adds the record to a specified zone in a DNS server.

## Syntax


```mof
uint32 AddByWks(
  [in]  string                  InternetAddress,
  [in]  string                  InternetProtocol,
  [in]  string                  Service[],
  [in]  string                  ZoneName,
  [in]  datetime                TimeToLive,
  [in]  boolean                 Wks,
  [in]  boolean                 AllowUpdateAny,
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*InternetAddress* \[in\]
</dt> <dd>

The IP address of the owner of a resource record.

</dd> <dt>

*InternetProtocol* \[in\]
</dt> <dd>

String representing the Internet protocol for this record. Valid values are UDP or TCP.

</dd> <dt>

*Service* \[in\]
</dt> <dd>

The service or services that are available for the current rewrite path. It can also specify a particular protocol to use for a service. Available services include Well-known Service (WKS) and NAPTR.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

The name of the DNS zone.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

The Time to Live (TTL) value, in seconds, for a resource record. Other DNS servers use this length of time to determine how long to cache a record.

</dd> <dt>

*Wks* \[in\]
</dt> <dd>

If specified, creates a DNS Server resource record.

</dd> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

Indicates that any authenticated user can update a resource record that has the same owner name.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of a DNS server resource record object.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name of a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

Indicates that the DNS server uses a time stamp for the resource record that this method adds. A DNS server can scavenge resource records that have become stale based on a time stamp.

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

 

 





