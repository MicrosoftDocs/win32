---
title: DnsServerResourceRecordUnknown class
description: Represents an unknown resource record for the DNS database.
audience: developer
ms.assetid: 1dcace39-6690-4709-b41a-5cb31f146651
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordUnknown class
- DnsServerResourceRecordUnknown class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordUnknown
- DnsServerResourceRecordUnknown.Data
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerResourceRecordUnknown class

Represents an unknown resource record for the DNS database.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordUnknown : DnsServerResourceRecordData
{
  string Data;
};
```

## Members

The **DnsServerResourceRecordUnknown** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordUnknown** class has these properties.

<dl> <dt>

**Data**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The unknown data.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**DnsServerResourceRecordData**](dnsserverresourcerecorddata.md)
</dt> </dl>

 

 





