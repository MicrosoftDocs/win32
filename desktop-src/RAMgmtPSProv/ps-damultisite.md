---
title: PS\_DAMultiSite class
description: Represents configuration of multisite environment.
audience: developer
ms.assetid: '4fd21f3b-060b-464f-bbb8-fecc554d5d3c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DAMultiSite class", "PS_DAMultiSite class, described"]
topic_type:
- apiref
api_name:
- PS_DAMultiSite
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_DAMultiSite class

Represents configuration of multisite environment.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_DAMultiSite
{
};
```

## Members

The **PS\_DAMultiSite** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DAMultiSite** class has these methods.



| Method                                    | Description                                                                                                                                                                                                                                                    |
|:------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Disable**](disable-ps-damultisite.md) | Disables a multisite deployment that contains a single entry point. After disabling, servers in the entry point will be configured with the remote access settings that were configured before the servers were joined to the multisite deployment.<br/> |
| [**Enable**](enable-ps-damultisite.md)   | Enables and configures a multisite deployment, and adds the first entry point. A prerequisite check is performed for multi-site deployment requirements.<br/>                                                                                            |
| [**Get**](get-ps-damultisite.md)         | Retrieves global settings applied to all entry points in a multisite deployment.<br/>                                                                                                                                                                    |
| [**Set**](set-ps-damultisite.md)         | Configures global settings that are applied to all entry points in a multisite deployment.<br/>                                                                                                                                                          |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





