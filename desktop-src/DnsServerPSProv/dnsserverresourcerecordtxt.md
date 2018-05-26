---
title: DnsServerResourceRecordTxt class
description: Represents a TXT resource record for DNS database.
audience: developer
ms.assetid: 88acd1e2-e603-45f2-b801-7f3abb87879c
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordTxt class
- DnsServerResourceRecordTxt class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordTxt
- DnsServerResourceRecordTxt.DescriptiveText
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerResourceRecordTxt class

Represents a TXT resource record for DNS database.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordTxt : DnsServerResourceRecordData
{
  string DescriptiveText;
};
```

## Members

The **DnsServerResourceRecordTxt** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordTxt** class has these properties.

<dl> <dt>

**DescriptiveText**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The content of the TXT resource record.

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

 

 





