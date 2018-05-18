---
title: PS\_DnsServerResourceRecord class
description: A DNS Server Resource Record definition.
audience: developer
ms.assetid: 'eb36f338-10fe-48b4-927f-7c005b960ef7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerResourceRecord class", "PS_DnsServerResourceRecord class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerResourceRecord class

A DNS Server Resource Record definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerResourceRecord
{
};
```

## Members

The **PS\_DnsServerResourceRecord** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerResourceRecord** class has these methods.



| Method                                                                        | Description                                                                                                           |
|:------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| [**AddByA**](addbya-ps-dnsserverresourcerecord.md)                           | Adds a host address (A) resource record resource to a DNS server.<br/>                                          |
| [**AddByAAAA**](addbyaaaa-ps-dnsserverresourcerecord.md)                     | Adds a type AAAA resource record to a DNS server.<br/>                                                          |
| [**AddByAfsdb**](addbyafsdb-ps-dnsserverresourcerecord.md)                   | Adds an Andrew File System cell database server (AFSDB) resource record type in the specified zone.<br/>        |
| [**AddByAtma**](addbyatma-ps-dnsserverresourcerecord.md)                     | Adds an ATM address resource record type in the specified zone.<br/>                                            |
| [**AddByCName**](addbycname-ps-dnsserverresourcerecord.md)                   | Adds a type CNAME resource record to a DNS server.<br/>                                                         |
| [**AddByDhcId**](addbydhcid-ps-dnsserverresourcerecord.md)                   | Adds a Dynamic Host Configuration Protocol Information (DHCID) resource record type in the specified zone.<br/> |
| [**AddByDName**](addbydname-ps-dnsserverresourcerecord.md)                   | Adds a domain alias (DNAME) resource record on a DNS server. type in the specified zone.<br/>                   |
| [**AddByHInfo**](addbyhinfo-ps-dnsserverresourcerecord.md)                   | Adds a host information (HINFO) resource record type in the specified zone.<br/>                                |
| [**AddByInputObject**](addbyinputobject-ps-dnsserverresourcerecord.md)       | Adds a resource record of specified type in the specified zone.<br/>                                            |
| [**AddByIsdn**](addbyisdn-ps-dnsserverresourcerecord.md)                     | Adds an Integrated Services Digital Network (ISDN) resource record type in the specified zone.<br/>             |
| [**AddByMX**](addbymx-ps-dnsserverresourcerecord.md)                         | Adds an MX resource record to a DNS server.<br/>                                                                |
| [**AddByNs**](addbyns-ps-dnsserverresourcerecord.md)                         | Adds a Name Server (NS) resource record type in the specified zone.<br/>                                        |
| [**AddByPtr**](addbyptr-ps-dnsserverresourcerecord.md)                       | Adds a type PTR resource record to a DNS server.<br/>                                                           |
| [**AddByRP**](addbyrp-ps-dnsserverresourcerecord.md)                         | Adds a Responsible Person (RP) resource record type in the specified zone.<br/>                                 |
| [**AddByRt**](addbyrt-ps-dnsserverresourcerecord.md)                         | Adds a Route Through (RT) resource record type in the specified zone.<br/>                                      |
| [**AddBySrv**](addbysrv-ps-dnsserverresourcerecord.md)                       | Adds a service (SRV) resource record type in the specified zone.<br/>                                           |
| [**AddByTLSA**](ps-dnsserverresourcerecord-addbytlsa.md)                     | Adds the record to a specified zone in a DNS server.<br/>                                                       |
| [**AddByTxt**](addbytxt-ps-dnsserverresourcerecord.md)                       | Adds a TXT resource record type in the specified zone.<br/>                                                     |
| [**AddByUnknown**](ps-dnsserverresourcerecord-addbyunknown.md)               | Adds the record to a specified zone in a DNS server.<br/>                                                       |
| [**AddByWins**](addbywins-ps-dnsserverresourcerecord.md)                     | Adds a WINS resource record type in the specified zone.<br/>                                                    |
| [**AddByWinsR**](addbywinsr-ps-dnsserverresourcerecord.md)                   | Adds a WINS reverse (WinsR) resource record type in the specified zone.<br/>                                    |
| [**AddByWks**](addbywks-ps-dnsserverresourcerecord.md)                       | Adds a WKS resource record type in the specified zone.<br/>                                                     |
| [**AddByX25**](addbyx25-ps-dnsserverresourcerecord.md)                       | Adds an X25 resource record type in the specified zone.<br/>                                                    |
| [**Get**](get-ps-dnsserverresourcerecord.md)                                 | Gets resource records from a specified zone.<br/>                                                               |
| [**GetByUnknown**](ps-dnsserverresourcerecord-getbyunknown.md)               | Retrieve resource record from a specified zone.<br/>                                                            |
| [**RemoveByInputObject**](removebyinputobject-ps-dnsserverresourcerecord.md) | Removes specified DNS server resource records from a zone.<br/>                                                 |
| [**RemoveByName**](removebyname-ps-dnsserverresourcerecord.md)               | Removes specified DNS server resource records from a zone.<br/>                                                 |
| [**RemoveByUnknown**](ps-dnsserverresourcerecord-removebyunknown.md)         | Deletes the specified DNS Resource Record.<br/>                                                                 |
| [**Set**](set-ps-dnsserverresourcerecord.md)                                 | Changes a resource record in a DNS server zone.<br/>                                                            |



 

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

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





