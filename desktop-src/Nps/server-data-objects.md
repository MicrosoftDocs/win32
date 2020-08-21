---
title: Server Data Objects
description: The Server Data Objects (SDO) API makes it possible to programmatically configure and administer a system running NPS.
ms.assetid: 9d159e15-f534-4ab1-9641-db70064beb51
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Server Data Objects

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008. The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

 

The Server Data Objects (SDO) API makes it possible to programmatically configure and administer a system running NPS. Using SDO, a developer can also write applications that administer remote access policies and profiles. The remote access policies and profiles are used by the Routing and Remote Access Service (RRAS) as well as NPS to determine whether a remote client is allowed to connect to a network access server (NAS).

The SDO API is applicable in any environment that uses NPS or Remote Access Policies.

With the SDO API, a developer can manipulate any element of the NPS configuration that is accessible through the NPS user interface.

The SDO API also makes it possible to set or retrieve any of the values accessible through the user dial-in settings property page.

The SDO API is composed of COM interfaces. Each of the interfaces in the SDO API inherits from the COM [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. The **IDispatch** interface enables developers to call the SDO interface methods from Visual Basic or any Automation client, as well as from C/C++.

Developers can also call the SDO API from scripting languages such as VBScript. However, because VBScript is limited to using VARIANT-type parameters only, not all the functionality of SDO is available.

## In This Section

[Overview](/windows/desktop/Nps/sdo-about-server-data-objects)

General information about the Server Data Objects API.

[Using](/windows/desktop/Nps/sdo-using-server-data-objects)

Sample code that demonstrates how to use the Server Data Objects API.

[Reference](/windows/desktop/Nps/sdo-server-data-objects-reference)

Documentation of the enumerated types and interfaces that compose the Server Data Objects API.

## Related topics

<dl> <dt>

[Network Policy Server (Internet Authentication Service)](portal.md)
</dt> <dt>

[Remote Access Service](/windows/desktop/RRAS/portal)
</dt> </dl>

 

 