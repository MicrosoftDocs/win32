---
title: DnsServerResourceRecordA class
description: DNS Server Resource Record A.
audience: developer
ms.assetid: 1321dbe2-bdd4-4dc8-9269-fbf005cdcb33
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordA class
- DnsServerResourceRecordA class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordA
- DnsServerResourceRecordA.IPv4Address
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerResourceRecordA class

DNS Server Resource Record A.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordA : DnsServerResourceRecordData
{
  string IPv4Address;
};
```

## Members

The **DnsServerResourceRecordA** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordA** class has these properties.

<dl> <dt>

**IPv4Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

IPv4 Address

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

 

 





