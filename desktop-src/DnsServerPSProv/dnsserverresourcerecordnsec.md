---
title: DnsServerResourceRecordNSec class
description: DNS Server Resource Record Data NSEC.
audience: developer
ms.assetid: 729b17c3-e994-4cf7-a11b-192d5bf53f05
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordNSec class
- DnsServerResourceRecordNSec class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordNSec
- DnsServerResourceRecordNSec.Name
- DnsServerResourceRecordNSec.CoveredRecordTypes
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerResourceRecordNSec class

DNS Server Resource Record Data NSEC.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordNSec : DnsServerResourceRecordData
{
  String Name;
  string CoveredRecordTypes[];
};
```

## Members

The **DnsServerResourceRecordNSec** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordNSec** class has these properties.

<dl> <dt>

**CoveredRecordTypes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The covered records in this record set.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name covered by this record.

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

 

 





