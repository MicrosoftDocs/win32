---
title: DnsServerClientSubnet class
description: Represents a client subnet record on a DNS server.
audience: developer
ms.assetid: FB25F44C-6F4D-461A-B701-8B865D439E8A
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerClientSubnet class
- DnsServerClientSubnet class, described
topic_type:
- apiref
api_name:
- DnsServerClientSubnet
- DnsServerClientSubnet.Name
- DnsServerClientSubnet.IPV4Subnet
- DnsServerClientSubnet.IPV6Subnet
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerClientSubnet class

Represents a client subnet record on a DNS server.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerClientSubnet
{
  string Name;
  string IPV4Subnet[];
  string IPV6Subnet[];
};
```

## Members

The **DnsServerClientSubnet** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerClientSubnet** class has these properties.

<dl> <dt>

**IPV4Subnet**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPV4 subnet list for the record in Classless Inter-Domain Routing (CIDR) notation.

</dd> <dt>

**IPV6Subnet**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPV6 subnet list for the record in Classless Inter-Domain Routing (CIDR) notation.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the client subnet record.

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

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





