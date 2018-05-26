---
title: PS\_DnsServerGlobalQueryBlockList class
description: DNS Server Global Query Blocklist definition.
audience: developer
ms.assetid: 541c35f0-57b5-46f7-9fbf-d08c5220fcb4
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerGlobalQueryBlockList class
- PS_DnsServerGlobalQueryBlockList class, described
topic_type:
- apiref
api_name:
- PS_DnsServerGlobalQueryBlockList
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DnsServerGlobalQueryBlockList class

DNS Server Global Query Blocklist definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerGlobalQueryBlockList
{
};
```

## Members

The **PS\_DnsServerGlobalQueryBlockList** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerGlobalQueryBlockList** class has these methods.



| Method                                              | Description                                                          |
|:----------------------------------------------------|:---------------------------------------------------------------------|
| [**Get**](get-ps-dnsserverglobalqueryblocklist.md) | Retrieve DNS Server block List settings<br/>                   |
| [**Set**](set-ps-dnsserverglobalqueryblocklist.md) | Overwrites the list of names the server does not resolve.<br/> |



 

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

 

 





