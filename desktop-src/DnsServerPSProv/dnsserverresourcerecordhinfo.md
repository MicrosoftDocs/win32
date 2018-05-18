---
title: DnsServerResourceRecordHInfo class
description: DNS Server Resource Record.
audience: developer
ms.assetid: '8f422d5c-a757-43b2-94c0-cd8f6bd7689d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerResourceRecordHInfo class", "DnsServerResourceRecordHInfo class, described"]
topic_type:
- apiref
api_name:
- DnsServerResourceRecordHInfo
- DnsServerResourceRecordHInfo.Cpu
- DnsServerResourceRecordHInfo.OperatingSystem
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerResourceRecordHInfo class

DNS Server Resource Record.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordHInfo : DnsServerResourceRecordData
{
  string Cpu;
  string OperatingSystem;
};
```

## Members

The **DnsServerResourceRecordHInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordHInfo** class has these properties.

<dl> <dt>

**Cpu**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

CPU Type

</dd> <dt>

**OperatingSystem**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Operating System

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

 

 





