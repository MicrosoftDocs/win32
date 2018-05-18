---
title: Add method of the PS\_DnsServerResourceRecordCName class
description: Adds a record for mapping an alias DNS domain name to another primary or canonical name.
audience: developer
ms.assetid: '49c88598-e184-4c32-8689-b6b297796923'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_DnsServerResourceRecordCName class", "PS_DnsServerResourceRecordCName class, Add method"]
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordCName.Add
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Add method of the PS\_DnsServerResourceRecordCName class

Adds a record for mapping an alias DNS domain name to another primary or canonical name.

## Syntax


```mof
uint32 Add(
  [in]  string                  HostNameAlias,
  [in]  boolean                 AllowUpdateAny,
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  datetime                TimeToLive,
  [in]  string                  ZoneName,
  [in]  boolean                 AgeRecord,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*HostNameAlias* \[in\]
</dt> <dd>

Alias Name

</dd> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

Allow any authenticated user to update DNS record with same owner name

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the FQDN of any valid DNS host or domain name in the namespace. For FQDN's, a trailing period (.) is used to fully qualify the name.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the DNS server , represented by local computer syntax, FQDN, or Host name. If omitted, the local server is used.

</dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

TTL

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

Specifies that this resource record is aged and scavenged. If this parameter is not used, the resource record remains in the DNS database unless it is manually updated or removed.

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

Receives and embedded instance of the [**DnsServerResourceRecordCName**](dnsserverresourcerecordcname.md) class.

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

[**PS\_DnsServerResourceRecordCName**](ps-dnsserverresourcerecordcname.md)
</dt> </dl>

 

 





