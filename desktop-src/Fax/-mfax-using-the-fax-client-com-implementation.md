---
Description: 'In addition to the Fax Service Client API Microsoft Win32 functions, Microsoft supplies an implementation of Component Object Model (COM) interfaces for developing fax client applications.'
ms.assetid: '80b70d79-0f59-4758-916d-aa321ec15c6a'
title: Using the Fax Client COM Implementation
---

# Using the Fax Client COM Implementation

In addition to the Fax Service Client API Microsoft Win32 functions, Microsoft supplies an implementation of Component Object Model (COM) interfaces for developing fax client applications. These are implemented as dual interfaces to provide access to programmers working in Microsoft Visual Basic, Microsoft Visual Basic Scripting Edition (VBScript), Microsoft JScript, and Java. VTable access is provided for C/C++ programmers. The interfaces use the Microsoft ActiveX Template Library to enhance performance and minimize size requirements.

The overview section, [About the Fax Service Client API](-mfax-about-the-fax-service-client-api.md), addresses the differences between fax client applications that run in the Win32 environment, and those that run in the COM implementation environment.

The COM implementation reference material for C/C++ developers is organized around the individual COM interfaces. You will find reference topics for each interface and for each interface method in [Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md).

The reference material for Visual Basic developers is organized around [the fax client object model](-mfax-the-fax-client-object-model.md). You will find reference topics for each object in the [Fax Service Client API Visual Basic Reference](-mfax-fax-service-client-api-visual-basic-reference.md). For more information, see [Using the Fax Client COM Implementation with Visual Basic](-mfax-using-the-fax-client-com-implementation-with-visual-basic.md).

> [!Note]  
> If you are programming in C/C++, do not implement any interface that begins with **IFax**. If you are programming in Visual Basic, do not implement any class that begins with **Fax**. The Microsoft standard implementation provides complete functionality.

 

To support the functionality of the fax client COM implementation, the following files are required.

-   FaxCom.h
-   FaxCom.dll

 

 



