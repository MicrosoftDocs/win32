---
title: AddByUnknown method of the PS\_DnsServerResourceRecord class
description: Adds the record to a specified zone in a DNS server.
audience: developer
ms.assetid: 08d06d43-54cd-4192-8e09-1a90bed7124c
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByUnknown method
- AddByUnknown method, PS_DnsServerResourceRecord class
- PS_DnsServerResourceRecord class, AddByUnknown method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByUnknown
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByUnknown method of the PS\_DnsServerResourceRecord class

Adds the record to a specified zone in a DNS server.

## Syntax


```mof
uint32 AddByUnknown(
  [in]  string                  ZoneName,
  [in]  string                  ComputerName,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [in]  uint16                  Type,
  [in]  string                  RecordData,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 AllowUpdateAny,
  [in]  datetime                TimeToLive,
  [in]  string                  Name,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type for Unknown record.

</dd> <dt>

*RecordData* \[in\]
</dt> <dd>

The record to add. The record data may be in an object derived from the [**DnsServerResourceRecord**](dnsserverresourcerecord.md) class, such as [**DnsServerResourceRecordA**](dnsserverresourcerecorda.md) or [**DnsServerResourceRecordTxt**](dnsserverresourcerecordtxt.md).

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

If specified, creates the record with current timestamp so that the record can be scavenged.

</dd> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

**true** to allow any authenticated user to update DNS record with same owner name.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

The Time To Live, in seconds.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The record Name.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerResourceRecord**](dnsserverresourcerecord.md) class. Note that the Record Data object is dependent on Record type.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerResourceRecord**](ps-dnsserverresourcerecord.md)
</dt> </dl>

 

 





