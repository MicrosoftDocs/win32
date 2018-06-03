---
title: DnsServerResourceRecordNS class
description: DNS Server Resource Record NS.
audience: developer
ms.assetid: 8b3855e1-fc66-4d62-af4e-ae2ef2d4b1e5
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordNS class
- DnsServerResourceRecordNS class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordNS
- DnsServerResourceRecordNS.NameServer
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerResourceRecordNS class

DNS Server Resource Record NS.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordNS : DnsServerResourceRecordData
{
  string NameServer;
};
```

## Members

The **DnsServerResourceRecordNS** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordNS** class has these properties.

<dl> <dt>

**NameServer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

DNS Server Name.

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

 

 





