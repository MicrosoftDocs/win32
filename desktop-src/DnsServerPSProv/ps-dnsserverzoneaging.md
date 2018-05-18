---
title: PS\_DnsServerZoneAging class
description: DNS Server Zone Aging definition.
audience: developer
ms.assetid: '6faf6d59-fbf4-4492-9847-530afe85be5d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerZoneAging class", "PS_DnsServerZoneAging class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerZoneAging
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerZoneAging class

DNS Server Zone Aging definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerZoneAging
{
};
```

## Members

The **PS\_DnsServerZoneAging** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerZoneAging** class has these methods.



| Method                                   | Description                                        |
|:-----------------------------------------|:---------------------------------------------------|
| [**Get**](get-ps-dnsserverzoneaging.md) | Retrieves DNS Aging settings for a zone<br/> |
| [**Set**](set-ps-dnsserverzoneaging.md) | Sets DNS Aging settings for a zone<br/>      |



 

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

 

 





