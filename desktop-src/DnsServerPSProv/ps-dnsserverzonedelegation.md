---
title: PS\_DnsServerZoneDelegation class
description: DNS Server Zone Delegation definition.
audience: developer
ms.assetid: 019a95cb-6c6f-4afe-b2fc-5a6a7ea38c41
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerZoneDelegation class
- PS_DnsServerZoneDelegation class, described
topic_type:
- apiref
api_name:
- PS_DnsServerZoneDelegation
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerZoneDelegation class

DNS Server Zone Delegation definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerZoneDelegation
{
};
```

## Members

The **PS\_DnsServerZoneDelegation** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerZoneDelegation** class has these methods.



| Method                                                                        | Description                                                            |
|:------------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**AddByInputObject**](addbyinputobject-ps-dnsserverzonedelegation.md)       | Adds a new delegation.<br/>                                      |
| [**AddByParameters**](addbyparameters-ps-dnsserverzonedelegation.md)         | Adds a new delegation.<br/>                                      |
| [**Get**](get-ps-dnsserverzonedelegation.md)                                 | Retrieves the delegations of the specified DNS server zone.<br/> |
| [**RemoveByInputObject**](removebyinputobject-ps-dnsserverzonedelegation.md) | Removes the zone delegation.<br/>                                |
| [**RemoveByParameters**](removebyparameters-ps-dnsserverzonedelegation.md)   | Removes the zone delegation.<br/>                                |
| [**SetByInputObject**](setbyinputobject-ps-dnsserverzonedelegation.md)       | Updates the zone delegation.<br/>                                |
| [**SetByName**](setbyname-ps-dnsserverzonedelegation.md)                     | Updates the zone delegation.<br/>                                |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





