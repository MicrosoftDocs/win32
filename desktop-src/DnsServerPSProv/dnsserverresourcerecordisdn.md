---
title: DnsServerResourceRecordIsdn class
description: DNS Server Resource Record ISDN.
audience: developer
ms.assetid: 2a0f9582-0de1-4929-99e6-fcba89be091d
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordIsdn class
- DnsServerResourceRecordIsdn class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordIsdn
- DnsServerResourceRecordIsdn.IsdnNumber
- DnsServerResourceRecordIsdn.IsdnSubAddress
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerResourceRecordIsdn class

DNS Server Resource Record ISDN.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordIsdn : DnsServerResourceRecordData
{
  string IsdnNumber;
  string IsdnSubAddress;
};
```

## Members

The **DnsServerResourceRecordIsdn** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordIsdn** class has these properties.

<dl> <dt>

**IsdnNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

ISDN Phone Number.

</dd> <dt>

**IsdnSubAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

ISDN Sub Address.

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

 

 





