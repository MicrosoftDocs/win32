---
title: PS\_DnsServerStatistics class
description: DNS Server Statistics definition.
audience: developer
ms.assetid: d256df31-22cd-4935-8722-9b5df5cf026b
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerStatistics class
- PS_DnsServerStatistics class, described
topic_type:
- apiref
api_name:
- PS_DnsServerStatistics
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DnsServerStatistics class

DNS Server Statistics definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerStatistics
{
};
```

## Members

The **PS\_DnsServerStatistics** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerStatistics** class has these methods.



| Method                                                                        | Description                                  |
|:------------------------------------------------------------------------------|:---------------------------------------------|
| [**Clear**](clear-ps-dnsserverstatistics.md)                                 | Clears all DNS server statistics.<br/> |
| [**ClearByZoneStatistics**](clearbyzonestatistics-ps-dnsserverstatistics.md) | Clear DNS server statistics.<br/>      |
| [**Get**](get-ps-dnsserverstatistics.md)                                     | Retrieve DNS server statistics.<br/>   |
| [**GetByZoneStatistics**](getbyzonestatistics-ps-dnsserverstatistics.md)     | Gets DNS server statistics.<br/>       |



 

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

 

 





