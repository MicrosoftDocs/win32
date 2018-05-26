---
title: DnsServerResourceRecordSrv class
description: Represents a service (SRV) resource record on a DNS server.
audience: developer
ms.assetid: d39cca8d-2abc-4928-864a-83132ba4110e
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordSrv class
- DnsServerResourceRecordSrv class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordSrv
- DnsServerResourceRecordSrv.Priority
- DnsServerResourceRecordSrv.Weight
- DnsServerResourceRecordSrv.Port
- DnsServerResourceRecordSrv.DomainName
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerResourceRecordSrv class

Represents a service (SRV) resource record on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordSrv : DnsServerResourceRecordData
{
  uint16 Priority;
  uint16 Weight;
  uint16 Port;
  string DomainName;
};
```

## Members

The **DnsServerResourceRecordSrv** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordSrv** class has these properties.

<dl> <dt>

**DomainName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The container name of the service that is specified by the SRV resource record.

</dd> <dt>

**Port**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The port number for the host server that is specified by the SRV resource record.

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the priority of the host server that is specified by the SRV resource record.

</dd> <dt>

**Weight**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the load balancing weight for the SRV resource record.

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

 

 





