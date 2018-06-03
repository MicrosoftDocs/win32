---
title: Implementing a Class Factory
description: This topics describes what you must do to expose objects for Automation.
ms.assetid: 99f761b4-3300-4f76-985c-195d9099a0f6
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a Class Factory

Before OLE can create an object, it needs access to the object's *class factory*. The class factory implements the **IClassFactory** interface. For detailed information about this interface, see the *COM Programmer's Reference* and *Inside OLE, Second Edition*, published by Microsoft Press.This topics describes what you must do to expose objects for Automation.

It is important to implement a class factory for objects that may be created explicitly through the OLE function **CoCreateInstance**, or through the Visual Basic **New** keyword. For example, an application can expose an Application object for creation, but may have many other programmable objects that can be created or destroyed by referencing a member of the Application object. In this case, only the Application object would need a class factory.

For each class factory, you need to implement the following two member functions of the **IClassFactory** interface, which provide services for OLE API functions. The prototypes for the member functions reside in the file Ole2.h.

-   [**CreateInstance**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo-createinstance) — Creates an instance of the object's class.

-   **LockServer** — Prevents the object's server from shutting down, even if the last instance of the object is released. **LockServer** can improve the performance of applications that frequently create and release objects.

In general, the [**CreateInstance**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo-createinstance) method should create a new instance of the object's class. For the Application object, however, the **CreateInstance** method should return the existing instance of the Application object, which is registered in the running object table ([ROT](glossary.md)).

The class factory object implements the **IClassFactory** and **IUnknown** interfaces. All objects must implement **IUnknown**, which allows ActiveX clients to determine which interfaces the object supports. A class factory can create instances of a class.

The object implements two interfaces: **IUnknown** and IMyInterface. The interface IMyInterface is a [dual](dual.md) interface, which supports both late binding through [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch), and early binding through the VTBL. The *dual* interface provides two ways to invoke the object's methods and properties. **IDispatch** includes the member functions [**GetIDsOfNames**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-getidsofnames), [**GetTypeInfo**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-gettypeinfo), [**GetTypeInfoCount**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-gettypeinfocount), and [**Invoke**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-invoke).

Member1 and Member2 are the members of IMyInterface. These members are available as direct entry points through the object's VTBL. They can also be accessed through [IDispatch::Invoke](https://msdn.microsoft.com/windows/desktop/964ADE8E-9D8A-4D32-BD47-AA678912A54D).

You must decide how to handle errors that occur in the exposed objects. If an object supports a *dual* interface and needs to return detailed, contextual error information, you also need to implement the Automation error interface, [**IErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-ierrorinfo).

In addition to writing code to implement objects, you must create a type library and a registration file. Describe the types of exposed objects in the library section of the .idl file or create an .odl file. Use the MIDL compiler to compile the .odl file. A type library (.tlb) file and a header (.h) file are created. The registration file provides information that the operating system and OLE need to locate objects.

 

 




