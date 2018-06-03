---
title: Type Description Functions
description: The following functions are provided for loading, registering, and querying type libraries.
ms.assetid: 883cd5ab-7952-4b00-b72a-669c96141f1d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Type Description Functions

The following functions are provided for loading, registering, and querying type libraries.

## In this section



| Topic                                                                                 | Description                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**LHashValOfName**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-lhashvalofname)<br/>                                   | Computes a hash value for a name.<br/>                                                                                                                                                                         |
| [**LHashValOfNameSys**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-lhashvalofnamesys)<br/>                             | Computes a hash value for a name.<br/>                                                                                                                                                                         |
| [**LHashValOfNameSysA**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-lhashvalofnamesysa)<br/>                           | Computes a hash value for the specified name.<br/>                                                                                                                                                             |
| [**LoadRegTypeLib**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-loadregtypelib)<br/>                                   | Uses registry information to load a type library.<br/>                                                                                                                                                         |
| [**LoadTypeLib**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-loadtypelib)<br/>                                         | Loads and registers a type library.<br/>                                                                                                                                                                       |
| [**LoadTypeLibEx**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-loadtypelibex)<br/>                                     | Loads a type library and (optionally) registers it in the system registry.   <br/>                                                                                                                             |
| [**OaEnablePerUserTLibRegistration**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-oaenableperusertlibregistration)<br/> | Enables the [**RegisterTypeLib**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registertypelib) function to override default registry mappings under Windows Vista Service Pack 1 (SP1), Windows Server 2008, and later operating system versions.<br/> |
| [**QueryPathOfRegTypeLib**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-querypathofregtypelib)<br/>                     | Retrieves the path of a registered type library.<br/>                                                                                                                                                          |
| [**RegisterTypeLib**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registertypelib)<br/>                                 | Adds information about a type library to the system registry.<br/>                                                                                                                                             |
| [**RegisterTypeLibForUser**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registertypelibforuser)<br/>                   | Registers a type library for use by the calling user.<br/>                                                                                                                                                     |
| [**UnRegisterTypeLib**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-unregistertypelib)<br/>                             | Removes type library information from the system registry. Use this API to allow applications to properly uninstall themselves.<br/>                                                                           |
| [**UnRegisterTypeLibForUser**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-unregistertypelibforuser)<br/>               | Removes type library information that was registered by using [**RegisterTypeLibForUser**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registertypelibforuser).<br/>                                                                                   |



 

## Related topics

<dl> <dt>

[Type Description Interfaces](type-description-interfaces.md)
</dt> </dl>

 

 





