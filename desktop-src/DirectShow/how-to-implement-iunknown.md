---
description: How to Implement IUnknown
ms.assetid: 4e363ccb-9725-4be6-bb31-283bf1d658f5
title: How to Implement IUnknown
ms.topic: article
ms.date: 05/31/2018
---

# How to Implement IUnknown

Microsoft DirectShow is based on the Component Object Model (COM). If you write your own filter, you must implement it as a COM object. The DirectShow base classes provide a framework from which to do this. Using the base classes is not required, but it can simplify the development process. This article describes some of the internal details of COM objects and their implementation in the DirectShow base classes.

This article assumes that you know how to program COM client applications—in other words, that you understand the methods in **IUnknown**—but does not assume any prior experience developing COM objects. DirectShow handles many of the details of developing a COM object. If you have experience developing COM objects, you should read the section [Using CUnknown](using-cunknown.md), which describes the [**CUnknown**](cunknown.md) base class.

COM is a specification, not an implementation. It defines the rules that a component must follow; putting those rules into effect is left to the developer. In DirectShow, all objects derive from a set of C++ base classes. The base class constructors and methods do most of the COM "bookkeeping" work, such as keeping a consistent reference count. By deriving your filter from a base class, you inherit the functionality of the class. To use base classes effectively, you need a general understanding of how they implement the COM specification.

This article contains the following topics.

-   [How IUnknown Works](how-iunknown-works.md)
-   [Using CUnknown](using-cunknown.md)

## Related topics

<dl> <dt>

[DirectShow and COM](directshow-and-com.md)
</dt> </dl>

 

 



