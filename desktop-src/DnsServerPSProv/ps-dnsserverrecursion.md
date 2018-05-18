---
title: PS\_DnsServerRecursion class
description: DNS Server Recursion definition.
audience: developer
ms.assetid: '01ea1b2b-5925-468b-bddc-a3f477848edb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerRecursion class", "PS_DnsServerRecursion class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerRecursion
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerRecursion class

DNS Server Recursion definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerRecursion
{
};
```

## Members

The **PS\_DnsServerRecursion** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerRecursion** class has these methods.



| Method                                   | Description                                        |
|:-----------------------------------------|:---------------------------------------------------|
| [**Get**](get-ps-dnsserverrecursion.md) | Retrieve DNS Server Recursion settings.<br/> |
| [**Set**](set-ps-dnsserverrecursion.md) | Sets DNS Server Recursion settings<br/>      |



 

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

 

 





