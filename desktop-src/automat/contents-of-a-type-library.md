---
title: Contents of a Type Library
description: Type libraries are binary files (.tlb files) that include information about types and objects exposed by an ActiveX application.
ms.assetid: 76b062d4-1a08-47f5-b4d4-064237cb1372
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Contents of a Type Library

Type libraries are binary files (.tlb files) that include information about types and objects exposed by an ActiveX application. A type library can contain any of the following:

-   Information about data types, such as aliases, enumerations, structures, or unions.

-   Descriptions of one or more objects, such as a module, interface, IDispatch interface (dispinterface), or component object class (coclass). Each of these descriptions is commonly referred to as a *typeinfo*.

-   References to type descriptions from other type libraries.

By including the type library with a product, the information about the objects in the library can be made available to the users of the applications and programming tools. Type libraries can be shipped in any of the following forms:

-   A stand-alone binary file. The .tlb (type library) file output by the MIDL utility is a binary file.

-   A resource in a dynamic link library (DLL). This resource should have the type TypeLib and an integer identifier. It must be declared in the resource (.rc) file as follows:

    ```C++
    1 typelib mylib1.tlb
    2 typelib mylib2.tlb
    ```

    

-   There can be multiple type library resources in a DLL. Application developers should use the resource compiler to add the .tlb file to their own DLL. A DLL with one or more type library resources typically has the file extension .olb (object library).

-   A resource in an .exe file. The .exe file can contain multiple type library resources.

Object browsers, compilers, and similar tools access type libraries through the interfaces [**ITypeLib**](/windows/previous-versions/oaidl/nn-oaidl-itypelib?branch=master), [**ITypeLib2**](/windows/previous-versions/oaidl/nn-oaidl-itypelib2?branch=master), [**ITypeInfo**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo?branch=master), [**ITypeInfo2**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo2?branch=master) and [**ITypeComp**](/windows/previous-versions/oaidl/nn-oaidl-itypecomp?branch=master). Type library tools (such as MIDL) can be created using the interfaces [**ICreateTypeLib**](/windows/previous-versions/oaidl/nn-oaidl-icreatetypelib?branch=master), [**ICreateTypeLib2**](/windows/previous-versions/oaidl/nn-oaidl-icreatetypelib2?branch=master), [**ICreateTypeInfo**](/windows/previous-versions/oaidl/nn-oaidl-icreatetypeinfo?branch=master) and [**ICreateTypeInfo2**](/windows/previous-versions/oaidl/nn-oaidl-icreatetypeinfo2?branch=master).

## Related topics

<dl> <dt>

[Type Libraries and the Object Description Language](type-libraries-and-the-object-description-language.md)
</dt> </dl>

 

 




