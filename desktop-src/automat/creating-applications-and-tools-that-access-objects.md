---
title: Creating Applications and Tools that Access Objects
description: Automation provides interfaces for accessing exposed objects from an application or programming tool written in C or C++.
ms.assetid: 56c0fab8-7695-4374-b51f-cafc8ab080eb
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating Applications and Tools that Access Objects

Automation provides interfaces for accessing exposed objects from an application or programming tool written in C or C++. The following sections show C++ code that uses the same type of access method as the Visual Basic code, which is described in [Creating Scripts Using Visual Basic](creating-scripts-using-visual-basic.md). Although the process is more complex with C++ than with Visual Basic, the approach is similar. This section shows the minimum code necessary to access and manipulate a remote object.

You can use the [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interface to access ActiveX objects, or you can access objects directly through the VTBL. Because VTBL references can be bound at compile time, VTBL access is generally faster than through **IDispatch**. Whenever possible, use the **ITypeInfo** or [**ITypeInfo2**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo2?branch=master) interfaces to get information about an object, including the VTBL addresses of the object's members. Then, use this information to access ActiveX objects through the VTBL.

To create compilers and other programming tools that use information from type libraries, use the **ITypeComp** interface. This interface binds to exposed objects at compile time. For details on [**ITypeComp**](/windows/previous-versions/oaidl/nn-oaidl-itypecomp?branch=master) see [Type Description Interfaces](387D44B7-407B-44A9-9239-A4CB20E88CAC).

## In this section



| Topic                                                                                     | Description                                                          |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [Accessing Members Through VTBLs](accessing-members-through-vtbls.md)<br/>         | Demonstrates how to access a member through its vtable.<br/>   |
| [Accessing Members Through IDispatch](accessing-members-through-idispatch.md)<br/> | Demonstrates how to access members through **IDispatch**.<br/> |



 

 

 





