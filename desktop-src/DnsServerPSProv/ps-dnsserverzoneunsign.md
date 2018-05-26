---
title: PS\_DnsServerZoneUnsign class
description: DNS Server Zone Unsign Task Definition.
audience: developer
ms.assetid: 83280aed-f0e0-4a25-8ebd-ea7a63318e01
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerZoneUnsign class
- PS_DnsServerZoneUnsign class, described
topic_type:
- apiref
api_name:
- PS_DnsServerZoneUnsign
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DnsServerZoneUnsign class

DNS Server Zone Unsign Task Definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerZoneUnsign
{
};
```

## Members

The **PS\_DnsServerZoneUnsign** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerZoneUnsign** class has these methods.



| Method                                          | Description                                 |
|:------------------------------------------------|:--------------------------------------------|
| [**Invoke**](invoke-ps-dnsserverzoneunsign.md) | Initiates unsigning on the zone.<br/> |



 

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

 

 





