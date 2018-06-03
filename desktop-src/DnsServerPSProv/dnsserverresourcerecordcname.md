---
title: DnsServerResourceRecordCName class
description: DNS Server Resource Record.
audience: developer
ms.assetid: 49c88598-e184-4c32-8689-b6b297796923
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordCName class
- DnsServerResourceRecordCName class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordCName
- DnsServerResourceRecordCName.HostNameAlias
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerResourceRecordCName class

DNS Server Resource Record.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordCName : DnsServerResourceRecordData
{
  string HostNameAlias;
};
```

## Members

The **DnsServerResourceRecordCName** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordCName** class has these properties.

<dl> <dt>

**HostNameAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Alias

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

 

 





