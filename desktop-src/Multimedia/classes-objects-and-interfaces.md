---
title: Classes, Objects, and Interfaces
description: Classes, Objects, and Interfaces
ms.assetid: 52e48402-32d5-46b0-8eb9-46432e59e36a
ms.topic: article
ms.date: 05/31/2018
---

# Classes, Objects, and Interfaces

In the C++ programming language, a *class* consists of *properties* (or member data) and *methods* (or member functions). The properties are data elements, such as those contained in a structure. The methods are used for a variety of purposes, such as initialization, assignment, operations, and data access. You use a class declaration in the same way that you use a structure declaration. Memory is allocated for a class when you define a class *object*. Each class object has a data area for its properties and a table of pointers to the methods it supports.

In OLE, an object consists of data and methods, as it does in C++. However, an OLE object adheres to stricter rules. The data is strictly internal. An object only exposes interfaces. An *interface* is a set of related methods for an object. Each object can support multiple interfaces. All OLE interfaces support the [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface.

 

 




