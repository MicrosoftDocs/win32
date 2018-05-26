---
title: DnsServerResourceRecordSoa class
description: Represents a Start of Authority (SOA) resource record for a DNS zone.
audience: developer
ms.assetid: 9f9daac1-9ff0-4af9-b373-9773e7497c5b
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordSoa class
- DnsServerResourceRecordSoa class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordSoa
- DnsServerResourceRecordSoa.SerialNumber
- DnsServerResourceRecordSoa.PrimaryServer
- DnsServerResourceRecordSoa.ResponsiblePerson
- DnsServerResourceRecordSoa.RefreshInterval
- DnsServerResourceRecordSoa.RetryDelay
- DnsServerResourceRecordSoa.ExpireLimit
- DnsServerResourceRecordSoa.MinimumTimeToLive
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerResourceRecordSoa class

Represents a Start of Authority (SOA) resource record for a DNS zone.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordSoa : DnsServerResourceRecordData
{
  uint32   SerialNumber;
  string   PrimaryServer;
  string   ResponsiblePerson;
  datetime RefreshInterval;
  datetime RetryDelay;
  datetime ExpireLimit;
  datetime MinimumTimeToLive;
};
```

## Members

The **DnsServerResourceRecordSoa** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordSoa** class has these properties.

<dl> <dt>

**ExpireLimit**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The expire setting of the DNS zone.

</dd> <dt>

**MinimumTimeToLive**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The minimum time to live (TTL) value, in seconds, to use for caching negative server responses.

</dd> <dt>

**PrimaryServer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the primary name server of the DNS zone.

</dd> <dt>

**RefreshInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Refresh interval to use for DNS zone updates.

</dd> <dt>

**ResponsiblePerson**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The email address of the administrator of the DNS zone.

> [!Note]  
> The @ character in the email address is replaced with a period (.).

 

</dd> <dt>

**RetryDelay**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The retry delay to use for zone transfer requests received by the DNS zone.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The serial number of the DNS zone.

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

 

 





