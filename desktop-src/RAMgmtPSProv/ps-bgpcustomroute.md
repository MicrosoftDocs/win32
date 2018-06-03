---
title: PS\_BgpCustomRoute class
description: Admin configured static routes.
audience: developer
ms.assetid: 1acf8fef-3963-4388-9da4-f5fad6d05d81
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_BgpCustomRoute class
- PS_BgpCustomRoute class, described
topic_type:
- apiref
api_name:
- PS_BgpCustomRoute
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_BgpCustomRoute class

Admin configured static routes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_BgpCustomRoute
{
};
```

## Members

The **PS\_BgpCustomRoute** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_BgpCustomRoute** class has these methods.



| Method                                                                       | Description                                                                                                                    |
|:-----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-bgpcustomroute.md)                                         | Adds custom BGP routes to a BGP routing table.<br/>                                                                      |
| [**Get**](get-ps-bgpcustomroute.md)                                         | Retrieves custom BGP routing information from a BGP routing table.<br/>                                                  |
| [**GetForAllRoutingDomains**](ps-bgpcustomroute-getforallroutingdomains.md) | Retrieves the custom/administrator-configured route information from the BGP routing table for all routing domains.<br/> |
| [**Remove**](remove-ps-bgpcustomroute.md)                                   | Removes network prefixes and network interfaces from a BGP routing table.<br/>                                           |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





