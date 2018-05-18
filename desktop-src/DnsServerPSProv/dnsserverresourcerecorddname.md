---
title: DnsServerResourceRecordDName class
description: DNS Server Resource Record.
audience: developer
ms.assetid: 'bb1c75a3-aa84-48b7-84cf-9b094f46c3a2'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerResourceRecordDName class", "DnsServerResourceRecordDName class, described"]
topic_type:
- apiref
api_name:
- DnsServerResourceRecordDName
- DnsServerResourceRecordDName.DomainNameAlias
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerResourceRecordDName class

DNS Server Resource Record.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordDName : DnsServerResourceRecordData
{
  string DomainNameAlias;
};
```

## Members

The **DnsServerResourceRecordDName** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordDName** class has these properties.

<dl> <dt>

**DomainNameAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Domain Name.

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

[**DnsServerResourceRecordData**](dnsserverresourcerecorddata.md)
</dt> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





