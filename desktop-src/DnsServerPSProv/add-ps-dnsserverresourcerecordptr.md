---
title: Add method of the PS\_DnsServerResourceRecordPtr class
description: Adds a pointer (PTR) resource record to a reverse zone.
audience: developer
ms.assetid: 84cc7ebd-a9d4-420e-a2a7-a2dce546f669
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DnsServerResourceRecordPtr class
- PS_DnsServerResourceRecordPtr class, Add method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordPtr.Add
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add method of the PS\_DnsServerResourceRecordPtr class

Adds a pointer (PTR) resource record to a reverse zone.

## Syntax


```mof
uint32 Add(
  [in]  boolean                 AllowUpdateAny,
  [in]  string                  PtrDomainName,
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  string                  ZoneName,
  [in]  datetime                TimeToLive,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

Allow any authenticated user to update DNS record with same owner name

</dd> <dt>

*PtrDomainName* \[in\]
</dt> <dd>

Specifies the FQDN of a resource record located in the DNS namespace. The host you specify is used as the data for answering reverse lookups based on the address information specified by this pointer (PTR) resource record.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

IPv4/IPv6 address of the record

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

Specifies the Time-To-Live (TTL) setting for the resource record. (The default TTL is defined in SOA resource record). Indicates a length of time used by other DNS servers to determine how long to cache information for a record before expiring and discarding it.

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

Specifies that this resource record is able to be aged and scavenged. If this command is used, this resource record is able to be aged and scavenged. If this command is not used, the resource record remains in the DNS database unless it is manually updated or removed.

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

Receives and embedded instance of the [**DnsServerResourceRecordPtr**](dnsserverresourcerecordptr.md) class.

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

[**PS\_DnsServerResourceRecordPtr**](ps-dnsserverresourcerecordptr.md)
</dt> </dl>

 

 





