---
title: PS\_BgpRouteFlapDampening class
description: Contains the BGP route flap dampening engine configuration.
audience: developer
ms.assetid: a6422eb6-7a50-4893-82b3-fff0bdf22901
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_BgpRouteFlapDampening class
- PS_BgpRouteFlapDampening class, described
topic_type:
- apiref
api_name:
- PS_BgpRouteFlapDampening
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_BgpRouteFlapDampening class

Contains the BGP route flap dampening engine configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_BgpRouteFlapDampening
{
};
```

## Members

The **PS\_BgpRouteFlapDampening** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_BgpRouteFlapDampening** class has these methods.



| Method                                              | Description                                                                            |
|:----------------------------------------------------|:---------------------------------------------------------------------------------------|
| [**Clear**](clear-ps-bgprouteflapdampening.md)     | Clears the route dampening information for the specified set of BGP routes.<br/> |
| [**Disable**](disable-ps-bgprouteflapdampening.md) | Stops performing route dampening for the flapping BGP routes.<br/>               |
| [**Enable**](enable-ps-bgprouteflapdampening.md)   | Starts performing route dampening for the flapping BGP routes.<br/>              |
| [**Get**](get-ps-bgprouteflapdampening.md)         | Retrieves the configuration of BGP route dampening engine.<br/>                  |
| [**Set**](set-ps-bgprouteflapdampening.md)         | Configures the BGP route dampening engine.<br/>                                  |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>Ramgmtpsprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





