---
title: Type Libraries and the Object Description Language
description: Type libraries enable others to use ActiveX objects you have created.
ms.assetid: c4061d23-b6bd-43f4-adf0-5980dae7a059
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Type Libraries and the Object Description Language

When you expose ActiveX objects, it allows interoperability with the programs of other vendors. For vendors to use these objects, they must have access to the characteristics of the objects (properties and methods). To make this information available developers must:

-   Publish object and type definitions (for example, as printed documentation).

-   Code objects into a binary application so they can be accessed using [IDispatch::GetTypeInfo](https://msdn.microsoft.com/windows/desktop/CC1EC9AA-6C40-4E70-819C-A7C6DD6B8C99) or implementations of the [**ITypeInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypeinfo) and [**ITypeLib**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-itypelib) interfaces.

-   Use the Microsoft Interface Definition Language (MIDL) compiler to create a type library that contains the objects, and then make the type library available.

The MIDL compiler compiles scripts that are written in the Object Description Language (ODL). Microsoft has expanded the Interface Definition Language (IDL) to contain the complete ODL syntax.

For more information about the MIDL compiler, refer to the *MIDL Programmer's Guide and Reference*.

This section contains the following descriptions and references:

## In this section

-   [Contents of a Type Library](contents-of-a-type-library.md)
-   [Using MIDL](using-midl.md)
-   [Using Type Building Interfaces and Functions](using-type-building-interfaces-and-functions.md)
-   [ODL File Syntax](odl-file-syntax.md)
-   [ODL Reference](odl-reference.md)

## Related topics

<dl> <dt>

[Automation Programming Reference](automation-programming-reference.md)
</dt> </dl>

 

 




