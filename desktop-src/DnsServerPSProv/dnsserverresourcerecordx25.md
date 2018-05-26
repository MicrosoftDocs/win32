---
title: DnsServerResourceRecordX25 class
description: Represents an X.25 resource record on a DNS server.
audience: developer
ms.assetid: b134d08e-ff2c-45ef-9346-dc14157d52a5
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordX25 class
- DnsServerResourceRecordX25 class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordX25
- DnsServerResourceRecordX25.PSDNAddress
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerResourceRecordX25 class

Represents an X.25 resource record on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordX25 : DnsServerResourceRecordData
{
  string PSDNAddress;
};
```

## Members

The **DnsServerResourceRecordX25** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordX25** class has these properties.

<dl> <dt>

**PSDNAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The public switched data network (PSDN) address of record owner.

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

 

 





