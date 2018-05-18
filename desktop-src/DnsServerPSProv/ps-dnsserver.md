---
title: PS\_DnsServer class
description: DNS Server definition.
audience: developer
ms.assetid: 'c6014903-554b-4a83-91fc-53f7b1afc676'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServer class", "PS_DnsServer class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServer
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServer class

DNS Server definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServer
{
};
```

## Members

The **PS\_DnsServer** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServer** class has these methods.



| Method                                                    | Description                                                                                          |
|:----------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dnsserver.md)                           | Retrieves entire DNS Server Configuration<br/>                                                 |
| [**Set**](set-ps-dnsserver.md)                           | Overwrites entire DNS server configuration.<br/>                                               |
| [**TestByContext**](testbycontext-ps-dnsserver.md)       | tests that the computers with the addresses that you specify are functioning DNS servers.<br/> |
| [**TestByZoneMaster**](testbyzonemaster-ps-dnsserver.md) | tests that the computers with the addresses that you specify are functioning DNS servers.<br/> |



 

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

 

 





