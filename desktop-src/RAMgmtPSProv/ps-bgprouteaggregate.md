---
title: PS\_BgpRouteAggregate class
description: Holds the route aggregation properties of BGP routes.
audience: developer
ms.assetid: 822e7990-b267-4737-8fe7-a132afc4ab9a
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_BgpRouteAggregate class
- PS_BgpRouteAggregate class, described
topic_type:
- apiref
api_name:
- PS_BgpRouteAggregate
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_BgpRouteAggregate class

Holds the route aggregation properties of BGP routes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_BgpRouteAggregate
{
};
```

## Members

The **PS\_BgpRouteAggregate** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_BgpRouteAggregate** class has these methods.



| Method                                        | Description                                                                        |
|:----------------------------------------------|:-----------------------------------------------------------------------------------|
| [**Add**](add-ps-bgprouteaggregate.md)       | Adds a new aggregate route for more specific BGP routes.<br/>                |
| [**Get**](get-ps-bgprouteaggregate.md)       | Retrieves all the aggregate BGP routes configured by the administrator.<br/> |
| [**Remove**](remove-ps-bgprouteaggregate.md) | removes the set of specified aggregate BGP routes.<br/>                      |
| [**Set**](set-ps-bgprouteaggregate.md)       | Updates the properties of the specified aggregate BGP route.<br/>            |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>Ramgmtpsprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





