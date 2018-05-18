---
title: Add method of the PS\_DnsServerResourceRecordA class
description: Adds type A resource record to a DNS server.
audience: developer
ms.assetid: '1321dbe2-bdd4-4dc8-9269-fbf005cdcb33'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_DnsServerResourceRecordA class", "PS_DnsServerResourceRecordA class, Add method"]
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordA.Add
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Add method of the PS\_DnsServerResourceRecordA class

Adds type A resource record to a DNS server.

## Syntax


```mof
uint32 Add(
  [in]  boolean                 AllowUpdateAny,
  [in]  boolean                 CreatePtr,
  [in]  string                  Name,
  [in]  string                  IPv4Address[],
  [in]  string                  ComputerName,
  [in]  datetime                TimeToLive,
  [in]  string                  ZoneName,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

**true** to allow any authenticated user to update the DNS record that has the same owner name; otherwise, **false**.

</dd> <dt>

*CreatePtr* \[in\]
</dt> <dd>

**true** to create the corresponding PTR record in the reverse lookup zone if that zone exists on the server; otherwise, **false**.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The host name or the computer name machine assigned to the record.

</dd> <dt>

*IPv4Address* \[in\]
</dt> <dd>

An array that contains the IPv4 address of the record.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The local computer syntax, fully qualified domain name, or host name of the DNS server that is associated with the record. If this property is omitted, the local server is used.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

The Time-To-Live (TTL) setting for the resource record. (The default TTL is defined in the SOA resource record). This TTL indicates the length of time used by other DNS servers to determine how long to cache information for the resource record before expiring and discarding it.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

The zone that contains the record.

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

**true** if the resource record can be aged and scavenged; otherwise, **false**. If this parameter is not used, the resource record will remain in the DNS database unless it is manually updated or removed.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the object that was modified by the method; otherwise, **false**. By default, this method does not generate any output.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

The name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is unavailable prior to Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array that receives and embedded instance of the [**DnsServerResourceRecordA**](dnsserverresourcerecorda.md) class.

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

[**PS\_DnsServerResourceRecordA**](ps-dnsserverresourcerecorda.md)
</dt> </dl>

 

 





