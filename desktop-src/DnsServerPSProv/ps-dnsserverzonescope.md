---
title: PS\_DnsServerZoneScope class
description: Describes the scope of a DNS Server zone.
audience: developer
ms.assetid: 8245318b-d2b1-4ba5-b2b4-a91c69487f25
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerZoneScope class
- PS_DnsServerZoneScope class, described
topic_type:
- apiref
api_name:
- PS_DnsServerZoneScope
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerZoneScope class

Describes the scope of a DNS Server zone.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerZoneScope
{
};
```

## Members

The **PS\_DnsServerZoneScope** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerZoneScope** class has these methods.



| Method                                         | Description                                                |
|:-----------------------------------------------|:-----------------------------------------------------------|
| [**Add**](add-ps-dnsserverzonescope.md)       | Adds a zone scope to a DNS zone.<br/>                |
| [**Get**](get-ps-dnsserverzonescope.md)       | Retrieves a zone scope from a DNS zone.<br/>         |
| [**Remove**](remove-ps-dnsserverzonescope.md) | Removes a zone scope from an existing DNS zone.<br/> |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider Classes](dns-server-classes.md)
</dt> </dl>

 

 





