---
title: AddByDhcId method of the PS\_DnsServerResourceRecord class
description: Adds a Dynamic Host Configuration Protocol Information (DHCID) resource record type in the specified zone.
audience: developer
ms.assetid: 6aa76b4c-d4bc-4e7b-9d36-eb5f9fd7d3a7
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByDhcId method
- AddByDhcId method, PS_DnsServerResourceRecord class
- PS_DnsServerResourceRecord class, AddByDhcId method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByDhcId
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByDhcId method of the PS\_DnsServerResourceRecord class

Adds a Dynamic Host Configuration Protocol Information (DHCID) resource record type in the specified zone.

## Syntax


```mof
uint32 AddByDhcId(
  [in]  boolean                 DhcId,
  [in]  string                  ZoneName,
  [in]  datetime                TimeToLive,
  [in]  boolean                 AllowUpdateAny,
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [in]  string                  DhcpIdentifier,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*DhcId* \[in\]
</dt> <dd>

Contains a public key associated with an FQDN as specified in section 3 of \[RFC2535\].

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the zone.

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

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

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

**Windows Server 2012:** Not supported.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is unavailable prior to Windows Server 2016.

</dd> <dt>

*DhcpIdentifier* \[in\]
</dt> <dd>

Contains a public key associated with an FQDN as specified in section 3 of \[RFC2535\].

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

 

 





