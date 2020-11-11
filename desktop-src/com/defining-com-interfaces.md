---
title: Defining COM Interfaces
description: Microsoft defines many COM interfaces. In most cases, you can reuse these generic interfaces. However, some applications have specific requirements that make it desirable or necessary to define your own object interfaces.
ms.assetid: 8a94bd7d-d101-411c-97de-9e9a46bf9591
ms.topic: article
ms.date: 05/31/2018
---

# Defining COM Interfaces

Microsoft defines many COM interfaces. In most cases, you can reuse these generic interfaces. However, some applications have specific requirements that make it desirable or necessary to define your own object interfaces.

All COM interfaces must derive, directly or indirectly, from the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface. Within that constraint, your custom interface can support almost any method or parameter, including asynchronous methods. You can also generate a type library for your custom interfaces so that clients can access information about your object's methods at run time. After you define an interface, describe it in Microsoft Interface Definition Language (MIDL), compile and register it, you use it just like any generic interface. With distributed COM, interface methods are available both to remote processes and to other processes on the same computer.

Finally, building COM interfaces requires a development environment that includes a C/C++ compiler and the Midl.exe compiler.

The steps in creating a COM interface are as follows:

-   Decide how you want to provide marshaling support for your interface; either with type-library driven marshaling or with a proxy/stub DLL. Even in-process interfaces must be marshaled if they are to be used across apartment boundaries. It is a good idea to build marshaling support into every COM interface, even if you don't think you will need it. See [Interface Marshaling](interface-marshaling.md) for more information.
-   Describe the interface or interfaces in an interface definition (IDL) file. In addition, you can specify certain local aspects of your interface in an application configuration file (ACF). If you are using type-library driven marshaling, add a [**library**](/windows/desktop/Midl/library) statement that references the interfaces for which you want to generate type information.
-   Use the MIDL compiler to generate a type library file and header file, or C-language proxy/stub files, interface identifier file, DLL data file and header file. See [MIDL Compilation](midl-compilation.md) for more information.
-   Depending on the marshaling method you chose, write a module definition (DEF) file, compile and link all the MIDL-generated files into a single proxy DLL, and register the interface in the system registry, or register the type library. See [Loading and Registering a Type Library](loading-and-registering-a-type-library.md) and [Building and Registering a Proxy DLL](building-and-registering-a-proxy-dll.md) for more information.

## Related topics

<dl> <dt>

[Anatomy of an IDL File](anatomy-of-an-idl-file.md)
</dt> <dt>

[COM Clients and Servers](com-clients-and-servers.md)
</dt> <dt>

[Interface Design Rules](interface-design-rules.md)
</dt> <dt>

[The Component Object Model](the-component-object-model.md)
</dt> </dl>

 

 