---
title: Type Libraries and ActiveX Objects
description: You must create a type library for each set of exposed objects.
ms.assetid: c9c06682-842c-4e62-8788-f0f264821ab6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Type Libraries and ActiveX Objects

You must create a type library for each set of exposed objects. Because [VTBL](glossary.md) references are bound at compile time, exposed objects that support VTBL binding must be described in a type library.

Type libraries provide these important benefits:

-   Type checking can be performed at compile time. This may help developers of ActiveX clients to write fast, correct code to access objects.

-   You can describe an interface with type information and implement [**IDispatch::Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master) for the interface using a single call to [**DispInvoke**](/windows/previous-versions/OleAuto/nf-oleauto-dispinvoke?branch=master).

-   Visual Basic applications can create objects with specific interface types, rather than the generic **Object** type, to take advantage of early binding.

-   ActiveX clients that do not support VTBLs can read and cache DISPIDs at compile time, improving run-time performance.

-   Type browsers can scan the library, allowing others to see the characteristics of objects.

-   The [**RegisterTypeLib**](/windows/previous-versions/OleAuto/nf-oleauto-registertypelib?branch=master) function can be used to register exposed objects in the registration database.

-   The [**UnRegisterTypeLib**](/windows/previous-versions/OleAuto/nf-oleauto-unregistertypelib?branch=master) function can be used to completely uninstall an application from the system registry.

-   Local server access is improved because Automation uses information from the type library to package the parameters that are passed to an object in another process.

## In this section



| Topic                                                                   | Description                                                                                                                                                                                            |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Creating a Type Library](creating-a-type-library.md)<br/>       | Demonstrates how to create a type library.<br/>                                                                                                                                                  |
| [Building a Type Library](building-a-type-library.md)<br/>       | Demonstrates how to build a type library.<br/>                                                                                                                                                   |
| [Registering a Type Library](registering-a-type-library.md)<br/> | Demonstrates how to register a type library.<br/>                                                                                                                                                |
| [Returning an Error](returning-an-error.md)<br/>                 | ActiveX objects typically return rich contextual error information, which includes an error number, a description of the error, and the path of a Help file that supplies more information.<br/> |



 

 

 





