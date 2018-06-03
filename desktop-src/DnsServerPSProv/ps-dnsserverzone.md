---
title: PS\_DnsServerZone class
description: DNS Server Zone definition.
audience: developer
ms.assetid: b591b20f-15b6-4787-b94e-b6206db4a956
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerZone class
- PS_DnsServerZone class, described
topic_type:
- apiref
api_name:
- PS_DnsServerZone
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerZone class

DNS Server Zone definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerZone
{
};
```

## Members

The **PS\_DnsServerZone** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerZone** class has these methods.



| Method                                      | Description                                                                    |
|:--------------------------------------------|:-------------------------------------------------------------------------------|
| [**Export**](export-ps-dnsserverzone.md)   | Exports Zone information<br/>                                            |
| [**Get**](get-ps-dnsserverzone.md)         | Lists the zones that exist on the specified DNS server.<br/>             |
| [**Remove**](remove-ps-dnsserverzone.md)   | Removes the specified zone<br/>                                          |
| [**Resume**](resume-ps-dnsserverzone.md)   | Resumes name resolution on suspended zone<br/>                           |
| [**Suspend**](suspend-ps-dnsserverzone.md) | Pauses the specified zone, which then ignores query requests.<br/>       |
| [**Sync**](sync-ps-dnsserverzone.md)       | Write back all zone or roothint datafile(s) for the specified zone.<br/> |



 

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

 

 





