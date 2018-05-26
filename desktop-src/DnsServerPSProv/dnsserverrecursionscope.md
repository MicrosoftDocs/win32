---
title: DnsServerRecursionScope class
description: Represents a recursion scope on a DNS server.
audience: developer
ms.assetid: 7d9c9a0b-f74e-445c-971f-ae440153dcb3
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerRecursionScope class
- DnsServerRecursionScope class, described
topic_type:
- apiref
api_name:
- DnsServerRecursionScope
- DnsServerRecursionScope.Name
- DnsServerRecursionScope.Forwarder
- DnsServerRecursionScope.EnableRecursion
api_location:
- DNSServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerRecursionScope class

Represents a recursion scope on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerRecursionScope
{
  string  Name;
  string  Forwarder[];
  boolean EnableRecursion;
};
```

## Members

The **DnsServerRecursionScope** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerRecursionScope** class has these properties.

<dl> <dt>

**EnableRecursion**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable recursion; otherwise, **false**.

</dd> <dt>

**Forwarder**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains the IP addresses of DNS servers to query.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the scope settings.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DNSServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





