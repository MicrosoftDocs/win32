---
title: DnsServerRootHint class
description: Represents a root hint on a DNS server.
audience: developer
ms.assetid: '799266d0-adbf-4a88-9369-31c683db2bdd'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerRootHint class", "DnsServerRootHint class, described"]
topic_type:
- apiref
api_name:
- DnsServerRootHint
- DnsServerRootHint.NameServer
- DnsServerRootHint.IPAddress
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerRootHint class

Represents a root hint on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerRootHint
{
  DnsServerResourceRecord NameServer;
  DnsServerResourceRecord IPAddress[];
};
```

## Members

The **DnsServerRootHint** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerRootHint** class has these properties.

<dl> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **DnsServerResourceRecord** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerResourceRecord**](dnsserverresourcerecord.md)")
</dt> </dl>

An array that contains the IP addresses of the DNS servers.

</dd> <dt>

**NameServer**
</dt> <dd> <dl> <dt>

Data type: **DnsServerResourceRecord**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerResourceRecord**](dnsserverresourcerecord.md)")
</dt> </dl>

The fully qualified domain name of the root name server.

</dd> </dl>

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

 

 





