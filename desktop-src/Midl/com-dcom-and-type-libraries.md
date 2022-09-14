---
title: COM, DCOM, and Type Libraries
description: Component Object Model (COM) and Distributed Component Object Model (DCOM) use Remote Procedure Calls (RPC) to enable distributed component objects to communicate with each other.
ms.assetid: 7bade397-676e-43be-82f4-b23cd768fd16
keywords:
- interfaces MIDL , COM
- interfaces MIDL , DCOM
- interfaces MIDL , type libraries
ms.topic: article
ms.date: 05/31/2018
---

# COM, DCOM, and Type Libraries

Component Object Model (COM) and Distributed Component Object Model (DCOM) use Remote Procedure Calls (RPC) to enable distributed component objects to communicate with each other. Thus, a COM or DCOM interface defines the identity and external characteristics of a COM object. It forms the means by which clients can gain access to an object's methods and data. With DCOM, this access is possible regardless of whether the objects exist in the same process, different processes on the same machine, or on different machines. As with RPC client/server interfaces, a COM or DCOM object can expose its functionality in a number of different ways and through multiple interfaces.

## Type Library

A type library (.tlb) is a binary file that stores information about a COM or DCOM object's properties and methods in a form that is accessible to other applications at runtime. Using a type library, an application or browser can determine which interfaces an object supports, and invoke an object's interface methods. This can occur even if the object and client applications were written in different programming languages. The COM/DCOM run-time environment can also use a type library to provide automatic cross-apartment, cross-process, and cross-machine marshaling for interfaces described in type libraries.

## Characteristics of an Interface

You define the characteristics of an interface in an interface definition (IDL) file and an optional application configuration file (ACF):

-   The IDL file specifies the characteristics of the application's interfaces on the wire — that is, how data is to be transmitted between client and server, or between COM objects.
-   The ACF file specifies interface characteristics, such as binding handles, that pertain only to the local operating environment. The ACF file can also specify how to marshal and transmit a complex data structure in a machine-independent form.

For more information on IDL and ACF files, see [The IDL and ACF Files](/windows/desktop/Rpc/the-idl-and-acf-files).

The IDL and ACF files are scripts written in Microsoft Interface Definition Language (MIDL), which is the Microsoft implementation and extension of the OSF-DCE interface definition language (IDL). The Microsoft extensions to the IDL language enable you to create COM interfaces and type libraries. The compiler, Midl.exe, uses these scripts to generate C-language stubs and header files as well as type library files.

## The MIDL Compiler

Depending on the contents of your IDL file, the MIDL compiler will generate any of the following files.

A C-language proxy/stub file, an interface identifier file, a DLL data file, and a related header file for a custom COM interface. The MIDL compiler generates these files when it encounters the object attribute in an interface attribute list. For more detailed information on these files, see [Files Generated for a COM Interface](files-generated-for-a-com-interface.md).

A compiled type library (.tlb) file and related header file. MIDL generates these files when it encounters a [**library**](library.md) statement in the IDL file. For general information about type libraries, see [Contents of a Type Library](/previous-versions/windows/desktop/automat/contents-of-a-type-library), in the Automation Programmer's Reference.

C/C++-language client and server stub files and related header file for an RPC interface. These files are generated when there are interfaces in the IDL file that do not have the [**object**](object.md) attribute. For an overview of the stub and header files, see [General Build Procedure](/windows/desktop/Rpc/general-build-procedure). For more detailed information, see [Files Generated for an RPC Interface](files-generated-for-an-rpc-interface.md).

 

 