---
title: AddByHInfo method of the PS\_DnsServerResourceRecord class
description: Adds a host information (HINFO) resource record type in the specified zone.
audience: developer
ms.assetid: 'ad077568-7360-499a-9f91-c72b4b47955e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddByHInfo method", "AddByHInfo method, PS_DnsServerResourceRecord class", "PS_DnsServerResourceRecord class, AddByHInfo method"]
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByHInfo
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# AddByHInfo method of the PS\_DnsServerResourceRecord class

Adds a host information (HINFO) resource record type in the specified zone.

## Syntax


```mof
uint32 AddByHInfo(
  [in]  boolean                 AllowUpdateAny,
  [in]  string                  Cpu,
  [in]  string                  OperatingSystem,
  [in]  string                  ZoneName,
  [in]  datetime                TimeToLive,
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 HInfo,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

Allow any authenticated user to update DNS record with same owner name

</dd> <dt>

*Cpu* \[in\]
</dt> <dd>

Specifies the CPU type of a DNS server. You can find the CPU type in a host information (HINFO) resource record.

</dd> <dt>

*OperatingSystem* \[in\]
</dt> <dd>

Specifies the operating system identifier of a DNS server. You can find the operating system identifier in a HINFO resource record.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the DNS zone.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

Specifies the Time to Live (TTL) value, in seconds, for a resource record. Other DNS servers use this length of time to determine how long to cache a record.

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

*HInfo* \[in\]
</dt> <dd>

If specified, creates a DNS Server Resource Record HINFO.

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

 

 





