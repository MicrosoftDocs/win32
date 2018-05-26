---
title: DnsServerResourceRecordRP class
description: DNS Server Resource Record RP.
audience: developer
ms.assetid: 9fc812a7-6bb4-4925-89d6-81391f6833c2
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordRP class
- DnsServerResourceRecordRP class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordRP
- DnsServerResourceRecordRP.ResponsiblePerson
- DnsServerResourceRecordRP.Description
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerResourceRecordRP class

DNS Server Resource Record RP.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordRP : DnsServerResourceRecordData
{
  string ResponsiblePerson;
  string Description;
};
```

## Members

The **DnsServerResourceRecordRP** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordRP** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Description.

</dd> <dt>

**ResponsiblePerson**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Responsible Person.

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

 

 





