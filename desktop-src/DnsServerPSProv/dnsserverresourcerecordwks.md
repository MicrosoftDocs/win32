---
title: DnsServerResourceRecordWks class
description: Represents a well-known service (WKS) resource record on a DNS server.
audience: developer
ms.assetid: 98d2ab56-2098-47a2-980d-a6dc64e0809b
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordWks class
- DnsServerResourceRecordWks class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordWks
- DnsServerResourceRecordWks.InternetAddress
- DnsServerResourceRecordWks.Service
- DnsServerResourceRecordWks.InternetProtocol
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerResourceRecordWks class

Represents a well-known service (WKS) resource record on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordWks : DnsServerResourceRecordData
{
  string InternetAddress;
  string Service[];
  string InternetProtocol;
};
```

## Members

The **DnsServerResourceRecordWks** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordWks** class has these properties.

<dl> <dt>

**InternetAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The internet address assigned to the resource record.

</dd> <dt>

**InternetProtocol**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of IP protocol that provides the services that are described by the WKS resource record.

The possible values are.

<dt>

<span id="UDP"></span><span id="udp"></span>

**UDP** ("UDP")


</dt> <dd></dd> <dt>

<span id="TCP"></span><span id="tcp"></span>

**TCP** ("TCP")


</dt> <dd></dd> </dl>

</dd> <dt>

**Service**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains the container name of the services that are described by the WKS resource record.

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

 

 





