---
title: PS\_DnsServerClientSubnet class
description: Represents a client subnet record on a DNS server.
audience: developer
ms.assetid: 'C0B5BE58-0251-4C14-B171-001CB9EBE6B1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Ps_DnsServerClientSubnet class", "Ps_DnsServerClientSubnet class, described"]
topic_type:
- apiref
api_name:
- Ps_DnsServerClientSubnet
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerClientSubnet class

Represents a client subnet record on a DNS server.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerClientSubnet
{
};
```

## Members

The **Ps\_DnsServerClientSubnet** class has these types of members:

-   [Methods](#methods)

### Methods

The **Ps\_DnsServerClientSubnet** class has these methods.



| Method                                            | Description                                                                                    |
|:--------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**Add**](ps-dnsserverclientsubnet-add.md)       | Adds a client subnet record to the client subnet database on the DNS server.<br/>        |
| [**Get**](ps-dnsserverclientsubnet-get.md)       | Retrieves a client subnet record from the client subnet database on the DNS server.<br/> |
| [**Remove**](ps-dnsserverclientsubnet-remove.md) | Deletes a client subnet record from the client subnet database on the DNS server.<br/>   |
| [**Set**](ps-dnsserverclientsubnet-set.md)       | Updates a client subnet record in the client subnet database on the DNS server.<br/>     |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





