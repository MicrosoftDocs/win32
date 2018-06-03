---
title: PS\_DnsServerVirtualizationInstance class
description: Describes a DNS virtualization instance.
audience: developer
ms.assetid: 4bb6d122-cbe1-4d66-a8ee-73a3f9ac4757
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerVirtualizationInstance class
- PS_DnsServerVirtualizationInstance class, described
topic_type:
- apiref
api_name:
- PS_DnsServerVirtualizationInstance
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerVirtualizationInstance class

Describes a DNS virtualization instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerVirtualizationInstance
{
};
```

## Members

The **PS\_DnsServerVirtualizationInstance** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerVirtualizationInstance** class has these methods.



| Method                                                      | Description                                       |
|:------------------------------------------------------------|:--------------------------------------------------|
| [**Add**](ps-dnsservervirtualizationinstance-add.md)       | Adds a DNS virtualization instance.<br/>    |
| [**Get**](ps-dnsservervirtualizationinstance-get.md)       | Gets a DNS virtualization instance.<br/>    |
| [**Remove**](ps-dnsservervirtualizationinstance-remove.md) | Removes a DNS virtualization instance.<br/> |
| [**Set**](ps-dnsservervirtualizationinstance-set.md)       | Sets a DNS virtualization instance.<br/>    |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



 

 





