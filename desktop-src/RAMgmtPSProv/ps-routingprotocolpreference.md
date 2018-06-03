---
title: PS\_RoutingProtocolPreference class
description: Manages routing protocol preferences.
audience: developer
ms.assetid: 4ea2ea36-ef27-4c51-846b-16c728f738e9
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_RoutingProtocolPreference class
- PS_RoutingProtocolPreference class, described
topic_type:
- apiref
api_name:
- PS_RoutingProtocolPreference
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_RoutingProtocolPreference class

Manages routing protocol preferences.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_RoutingProtocolPreference
{
};
```

## Members

The **PS\_RoutingProtocolPreference** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RoutingProtocolPreference** class has these methods.



| Method                                          | Description                                                                  |
|:------------------------------------------------|:-----------------------------------------------------------------------------|
| [**Get**](get-ps-routingprotocolpreference.md) | Retrieves the preference level of the specified routing protocol.<br/> |
| [**Set**](set-ps-routingprotocolpreference.md) | Updates the preference level of the specified routing protocol.<br/>   |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





