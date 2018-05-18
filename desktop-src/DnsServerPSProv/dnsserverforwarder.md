---
title: DnsServerForwarder class
description: Represents a server level forwarder on a DNS server.
audience: developer
ms.assetid: 'd584e8f3-8eb2-4376-a45f-6b8e747acccb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerForwarder class", "DnsServerForwarder class, described"]
topic_type:
- apiref
api_name:
- DnsServerForwarder
- DnsServerForwarder.UseRootHint
- DnsServerForwarder.Timeout
- DnsServerForwarder.EnableReordering
- DnsServerForwarder.IPAddress
- DnsServerForwarder.ReorderedIPAddress
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerForwarder class

Represents a server level forwarder on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerForwarder
{
  boolean UseRootHint;
  uint32  Timeout;
  boolean EnableReordering;
  string  IPAddress[];
  string  ReorderedIPAddress[];
};
```

## Members

The **DnsServerForwarder** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerForwarder** class has these properties.

<dl> <dt>

**EnableReordering**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable reordering of the forwarders; otherwise, **false**.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains the IP addresses of DNS servers where queries are forwarded.

</dd> <dt>

**ReorderedIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the reordered IP addresses of the forwarder.

</dd> <dt>

**Timeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The timeout for the forwarder, in seconds.

</dd> <dt>

**UseRootHint**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to use a root hint; otherwise, **false**.

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

 

 





