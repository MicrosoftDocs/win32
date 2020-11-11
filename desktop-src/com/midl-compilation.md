---
title: MIDL Compilation
description: MIDL Compilation
ms.assetid: 2797ee3b-82fd-4cb5-9e95-23b2f2a8f011
ms.topic: article
ms.date: 05/31/2018
---

# MIDL Compilation

Given an IDL file, such as [Example2.idl](anatomy-of-an-idl-file.md), that defines one or more COM interfaces and a type library, the MIDL compiler (Midl.exe) generates the files described in the following table as the default output.



| Filename                 | Description                                                                                                                                                                                           |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Example2.h<br/>    | The header file, containing type definitions and function declarations for all of the interfaces defined in the IDL file as well as forward declarations for routines that the stubs call.<br/> |
| Example2\_p.c<br/> | The proxy/stub file, which includes the surrogate entry points both for clients and for servers.<br/>                                                                                           |
| Example2\_i.c<br/> | The interface ID file, which defines the GUID for every interface specified in the IDL file.<br/>                                                                                               |
| Example2.tlb<br/>  | A compound document file that contains information about types and objects.<br/>                                                                                                                |
| Dlldata.c<br/>     | Contains the data you need to create a proxy/stub DLL.<br/>                                                                                                                                     |



 

You use the header file and all of the .c files to [create a proxy DLL](building-and-registering-a-proxy-dll.md) that can support the interface when used both by client applications and by object servers. You use the interface header file (Example2.h) and the interface ID (Example2\_i.c) file when creating the executable file for a client application that uses the interface. You can choose to include the type library file as a resource in your EXE or DLL, or you can ship it as a separate file.

## Related topics

<dl> <dt>

[Files Generated for a COM Interface](/windows/desktop/Midl/files-generated-for-a-com-interface)
</dt> <dt>

[MIDL Compiler Options](midl-compiler-options.md)
</dt> </dl>

 

