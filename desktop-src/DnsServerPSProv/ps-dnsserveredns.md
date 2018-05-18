---
title: PS\_DnsServerEDns class
description: DNS Server EDns definition.
audience: developer
ms.assetid: '60eca66d-640d-4475-9ca1-d22da4106718'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerEDns class", "PS_DnsServerEDns class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerEDns
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerEDns class

DNS Server EDns definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerEDns
{
};
```

## Members

The **PS\_DnsServerEDns** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerEDns** class has these methods.



| Method                              | Description                                 |
|:------------------------------------|:--------------------------------------------|
| [**Get**](get-ps-dnsserveredns.md) | Retrieve DNS Sever EDNS settings<br/> |
| [**Set**](set-ps-dnsserveredns.md) | Sets DNS server EDNS settings.<br/>   |



 

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

 

 





