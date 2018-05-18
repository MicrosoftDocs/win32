---
title: AddByIsdn method of the PS\_DnsServerResourceRecord class
description: Adds an Integrated Services Digital Network (ISDN) resource record type in the specified zone.
audience: developer
ms.assetid: '908121c4-3f69-4e35-b7ae-cfb2d0113412'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddByIsdn method", "AddByIsdn method, PS_DnsServerResourceRecord class", "PS_DnsServerResourceRecord class, AddByIsdn method"]
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByIsdn
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# AddByIsdn method of the PS\_DnsServerResourceRecord class

Adds an Integrated Services Digital Network (ISDN) resource record type in the specified zone.

## Syntax


```mof
uint32 AddByIsdn(
  [in]  string                  IsdnNumber,
  [in]  string                  IsdnSubAddress,
  [in]  string                  ZoneName,
  [in]  datetime                TimeToLive,
  [in]  boolean                 AllowUpdateAny,
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 Isdn,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*IsdnNumber* \[in\]
</dt> <dd>

Specifies the number in the ISDN address that maps to the FQDN of a DNS server. An ISDN address, which consists of a phone number and an optional subaddress, is located in an ISDN resource record. The phone number can contain a country/region code, an area code, and a local phone number.

</dd> <dt>

*IsdnSubAddress* \[in\]
</dt> <dd>

Specifies the number that is contained in an ISDN address that maps to the FQDN of a DNS server. An ISDN address consists of a phone number and an optional subaddress and is located in an ISDN resource record. The subaddress is an identifier that describes the ISDN subaddress encoding type.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of a DNS zone.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

Specifies the Time to Live (TTL) value, in seconds, for a resource record. Other DNS servers use this length of time to determine how long to cache a record.

</dd> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

Indicates that any authenticated user can update a resource record that has the same owner name.

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

*Isdn* \[in\]
</dt> <dd>

If specified, creates a DNS Server Resource Record ISDN.

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

 

 





