---
title: Accessing an Object by Using IDispatch
description: ActiveX clients can use the IDispatch interface to access objects that implement the interface.
ms.assetid: 44c050aa-4c4b-4910-b501-fb6177e950b6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Accessing an Object by Using IDispatch

ActiveX clients can use the [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interface to access objects that implement the interface. The client must first create the object, and then query the object's **IUnknown** interface for a pointer to its [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interface.

Although programmers might know objects, methods, and properties by name, [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) keeps track of them internally with a number called the *dispatch identifier* ([DISPID](glossary.md)). Before an ActiveX client can access a property or method, it must have the DISPID that maps to the name of the member.

With the DISPID, a client can call the member [IDispatch::Invoke](964ADE8E-9D8A-4D32-BD47-AA678912A54D) to access the property or invoke the method, and then package the parameters for the property or method into one of the [**Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master) parameters.

The object's implementation of [**Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master) must then unpackage the parameters, call the property or method, and handle any errors that occur. When the property or method returns, the object passes its return value back to the client through an **Invoke** parameter.

DISPIDs are available at run time, and, in some circumstances, at compile time. At run time, clients get DISPIDs by calling the [IDispatch::GetIDsOfNames](6F6CF233-3481-436E-8D6A-51F93BF91619) function. This is called *late binding* because the controller binds to the property or method at run time instead of compile time.

The DISPID of each property or method is fixed, and is part of the object's type description. If the object is described in a type library, an ActiveX client can read the DISPIDs from the type library at compile time, and avoid calling **IDispatch::GetIDsOfNames** at run time. This is called *ID binding*. Because it requires only one call to [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) (the call to [**Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master)) at run time, rather than the two calls required by late binding, it is generally about twice as fast. Late-binding clients can improve performance by caching DISPIDs after retrieving them, so that **IDispatch::GetIDsOfNames** is called only once for each property or method.

 

 




