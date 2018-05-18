---
title: Creating the IDispatch Interface
description: The IDispatch interface provides a late-bound mechanism to access and retrieve information about an object's methods and properties.
ms.assetid: '0606fe11-59e3-4ce1-bde1-a34cfbf0b093'
---

# Creating the IDispatch Interface

The [**IDispatch**](idispatch.md) interface provides a [late-bound](glossary.md) mechanism to access and retrieve information about an object's methods and properties. In addition to the member functions inherited from **IUnknown**, the following member functions should be implemented within the class definition of each object that will be exposed through Automation.

-   [GetTypeInfoCount](DA876D53-CB8A-465C-A43E-C0EB272E2A12) — Returns the number of type descriptions for the object. For objects that support [**IDispatch**](idispatch.md), the type information count is always 1.

-   [GetTypeInfo](CC1EC9AA-6C40-4E70-819C-A7C6DD6B8C99) — Retrieves a description of the object's programmable interface.

-   [GetIDsOfNames](6F6CF233-3481-436E-8D6A-51F93BF91619) — Maps the name of a method or property to a DISPID, which can later be used to invoke the method or property.

-   [Invoke](964ADE8E-9D8A-4D32-BD47-AA678912A54D) — Calls one of the object's methods, or gets or sets one of its properties.

You can implement [**IDispatch**](idispatch.md) by any of the following means:

-   Delegating to the [**DispInvoke**](dispinvoke.md) and [**DispGetIDsOfNames**](dispgetidsofnames.md) functions, or to [**ITypeInfo::Invoke**](itypeinfo-invoke.md) and [**ITypeInfo::GetIDsOfNames**](itypeinfo-getidsofnames.md). This is the recommended approach, because it supports multiple locales and allows exceptions to be returned.

-   Calling the [**CreateStdDispatch**](createstddispatch.md) function. This approach is the simplest, but it does not provide for rich error handling or multiple national languages.

-   Implementing the member functions without delegating to the dispatch functions. This approach is seldom necessary. Because **Invoke** is a complex interface with many subtle semantics that are difficult to emulate, it is strongly recommended that code delegate to[**ITypeInfo::Invoke**](itypeinfo-invoke.md) to implement this mechanism.

 

 




