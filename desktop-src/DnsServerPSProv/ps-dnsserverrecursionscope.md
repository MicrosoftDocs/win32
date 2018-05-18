---
title: PS\_DnsServerRecursionScope class
description: Represents a recursion scope on a DNS server.
audience: developer
ms.assetid: '4db57e06-00bf-4a8b-acbb-cd5e0fdc8aa6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerRecursionScope class", "PS_DnsServerRecursionScope class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerRecursionScope
api_location:
- DNSServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerRecursionScope class

Represents a recursion scope on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerRecursionScope
{
};
```

## Members

The **PS\_DnsServerRecursionScope** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerRecursionScope** class has these methods.



| Method                                              | Description                                               |
|:----------------------------------------------------|:----------------------------------------------------------|
| [**Add**](ps-dnsserverrecursionscope-add.md)       | Adds a new recursion scope to a DNS server.<br/>    |
| [**Get**](get-ps-dnsserverrecursionscope.md)       | Retrieves a recursion scope from a DNS server.<br/> |
| [**Remove**](remove-ps-dnsserverrecursionscope.md) | Deletes a recursion scope from a DNS server.<br/>   |
| [**Set**](set-ps-dnsserverrecursionscope.md)       | Updates a recursion scope on a DNS server.<br/>     |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DNSServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





