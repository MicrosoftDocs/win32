---
title: AddByAtma method of the PS\_DnsServerResourceRecord class
description: Adds an ATM address resource record type in the specified zone.
audience: developer
ms.assetid: 8b1db5ee-8076-4739-adb5-c31376500101
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByAtma method
- AddByAtma method, PS_DnsServerResourceRecord class
- PS_DnsServerResourceRecord class, AddByAtma method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByAtma
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByAtma method of the PS\_DnsServerResourceRecord class

Adds an ATM address resource record type in the specified zone.

## Syntax


```mof
uint32 AddByAtma(
  [in]  string                  Address,
  [in]  string                  AddressType,
  [in]  string                  ZoneName,
  [in]  datetime                TimeToLive,
  [in]  boolean                 AllowUpdateAny,
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 Atma,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*Address* \[in\]
</dt> <dd>

Specifies a byte array that contains the asynchronous transfer mode (ATM) address of the owner to which this resource record object pertains. The AddressType parameter specifies the format of the byte array. The first 4 bytes of the array store the size of the octet string. The most significant byte is byte 0.

</dd> <dt>

*AddressType* \[in\]
</dt> <dd>

Specifies the format of an ATM address in an ATM address (ATMA) resource record. Valid values are: 0, for an ATM End System Address (AESA) format, and 1, for an E.164 address format.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the DNS zone.

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

*Atma* \[in\]
</dt> <dd>

If specified, creates a DNS Server Resource Record ATMA.

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

 

 





