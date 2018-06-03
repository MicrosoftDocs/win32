---
title: DnsServerResourceRecordAAAA class
description: DNS Server Resource Record AAAA.
audience: developer
ms.assetid: 9b894486-ce70-4502-b82d-242cc30f5e81
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordAAAA class
- DnsServerResourceRecordAAAA class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordAAAA
- DnsServerResourceRecordAAAA.IPv6Address
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerResourceRecordAAAA class

DNS Server Resource Record AAAA.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordAAAA : DnsServerResourceRecordData
{
  string IPv6Address;
};
```

## Members

The **DnsServerResourceRecordAAAA** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordAAAA** class has these properties.

<dl> <dt>

**IPv6Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

IPv6 Address

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

[**DnsServerResourceRecordData**](dnsserverresourcerecorddata.md)
</dt> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





