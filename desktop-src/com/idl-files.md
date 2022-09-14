---
title: IDL Files
description: IDL Files
ms.assetid: 94a6752d-fcf3-47ce-ac3f-be1d1c9768e6
ms.topic: article
ms.date: 05/31/2018
---

# IDL Files

COM uses the Microsoft Interface Definition Language (MIDL) to describe COM objects. MIDL is an extension of the IDL for distributed computing environments defined by the Open Software Foundation, which was developed to define interfaces for remote procedure calls in traditional client/server applications. MIDL includes most of the attributes and statements of Object Definition Language (ODL), the language originally used to generate type libraries for OLE Automation.

In C++ and Java, a developer building a COM object creates an IDL file that the MIDL compiler then processes to create a type library or header and proxy files, or both. A *type library* is a binary file that describes the COM object or COM interfaces, or both. A type library is the compiled version of the IDL file. However, type libraries support ODL semantics only. In particular, they cannot represent all the information from an IDL file related to IDL attributes like \[[**size\_is**](/windows/desktop/Midl/size-is)\]. You need to create and use proxy files for IDL files affected by information loss in the type library.

In Visual Basic, a developer creating a COM object does not create an IDL file. Instead, Visual Basic gathers information using class and project properties and directly creates the type library.

 

 