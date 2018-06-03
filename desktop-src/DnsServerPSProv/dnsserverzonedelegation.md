---
title: DnsServerZoneDelegation class
description: Retrieves information about a DNS zone delegation.
audience: developer
ms.assetid: 019a95cb-6c6f-4afe-b2fc-5a6a7ea38c41
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerZoneDelegation class
- DnsServerZoneDelegation class, described
topic_type:
- apiref
api_name:
- DnsServerZoneDelegation
- DnsServerZoneDelegation.ZoneName
- DnsServerZoneDelegation.ChildZoneName
- DnsServerZoneDelegation.NameServer
- DnsServerZoneDelegation.IPAddress
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerZoneDelegation class

Retrieves information about a DNS zone delegation.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerZoneDelegation
{
  string                  ZoneName;
  string                  ChildZoneName;
  DnsServerResourceRecord NameServer;
  DnsServerResourceRecord IPAddress[];
};
```

## Members

The **DnsServerZoneDelegation** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerZoneDelegation** class has these properties.

<dl> <dt>

**ChildZoneName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the child DNS zone specified by the zone delegation.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **DnsServerResourceRecord** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerResourceRecord**](dnsserverresourcerecord.md)")
</dt> </dl>

An array that contains the IP address of DNS Server hat manages the zone delegation.

</dd> <dt>

**NameServer**
</dt> <dd> <dl> <dt>

Data type: **DnsServerResourceRecord**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerResourceRecord**](dnsserverresourcerecord.md)")
</dt> </dl>

The name of the DNS Server that manages the zone delegation.

</dd> <dt>

**ZoneName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the parent DNS zone specified by the zone delegation.

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

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





