---
title: RemoveByUnknown method of the PS\_DnsServerResourceRecord class
description: Deletes the specified unknown DNS resource record.
audience: developer
ms.assetid: '216944df-64cd-457c-93e5-cc0619ec0cb3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveByUnknown method", "RemoveByUnknown method, PS_DnsServerResourceRecord class", "PS_DnsServerResourceRecord class, RemoveByUnknown method"]
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.RemoveByUnknown
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# RemoveByUnknown method of the PS\_DnsServerResourceRecord class

Deletes the specified unknown DNS resource record.

## Syntax


```mof
uint32 RemoveByUnknown(
  [in]  string                  ZoneName,
  [in]  boolean                 PassThru,
  [in]  string                  ComputerName,
  [in]  boolean                 Force,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [in]  uint16                  Type,
  [in]  string                  Name,
  [in]  string                  RecordData[],
  [out] DnsServerResourceRecord cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

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

*Name* \[in\]
</dt> <dd>

Name of the resource record that needs to be removed.

</dd> <dt>

*RecordData* \[in\]
</dt> <dd>

Data to be contained in the resource record that needs to be deleted. The record data may be in an object derived from the [**DnsServerResourceRecord**](dnsserverresourcerecord.md) class, such as [**DnsServerResourceRecordA**](dnsserverresourcerecorda.md) or [**DnsServerResourceRecordTxt**](dnsserverresourcerecordtxt.md).

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DnsServerResourceRecord**](dnsserverresourcerecord.md). This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerResourceRecord**](ps-dnsserverresourcerecord.md)
</dt> </dl>

 

 





