---
title: Microsoft Interface Definition Language
description: The Microsoft Interface Definition Language (MIDL) defines interfaces between client and server programs.
ms.assetid: 5ed1ff94-bbcb-4c6e-83aa-63d24eb84859
keywords:
- MIDL MIDL
- MIDL MIDL , (See Microsoft Interface Definition Language MIDL )
- Microsoft Interface Definition Language MIDL
- Microsoft Interface Definition Language MIDL , start page
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Interface Definition Language

> [!NOTE]
> This topic is about the *classic* MIDL used for creating RPC and COM interfaces. For MIDL 3.0, which is used to create Windows Runtime (WinRT) types, see [Microsoft Interface Definition Language 3.0 reference](/uwp/midl-3/).

## Purpose

The Microsoft Interface Definition Language (MIDL) defines interfaces between client and server programs. Microsoft includes the MIDL compiler with the Platform Software Development Kit (SDK) to enable developers to create the interface definition language (IDL) files and application configuration files (ACF) required for remote procedure call (RPC) interfaces and COM/DCOM interfaces. MIDL also supports the generation of type libraries for OLE Automation.

## Where applicable

MIDL can be used in all client/server applications based on Windows operating systems. It can also be used to create client and server programs for heterogeneous network environments that include such operating systems as Unix and Apple. Microsoft supports the Open Group (formerly known as the Open Software Foundation) DCE standard for RPC interoperability.

## Developer audience

When using MIDL with RPC, familiarity with C/C++ programming and the RPC paradigm is required. When using MIDL with COM, familiarity with C++ programming and the RPC paradigm as it applies to COM is required, or alternatively, familiarity with OLE Automation model scripting and type libraries is required.

## Run-time requirements

The appropriate run-time libraries for using MIDL are included with Windows. The MIDL compiler and the components of the RPC development environment are installed when you install the Windows SDK. For more information, see [Using the MIDL Compiler](using-the-midl-compiler-2.md) and [Installing the RPC Programming Environment](/windows/desktop/Rpc/installing-the-rpc-programming-environment).

## In this section



| Topic                                                                                               | Description                                                                        |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [Overview](about-this-guide-2.md)<br/>                                                       | General information about MIDL and the MIDL compiler.<br/>                   |
| [Using the MIDL Compiler](using-the-midl-compiler-2.md)<br/>                                 | Information about using the MIDL compilter to generate RPC stubs.<br/>       |
| [Interface Definitions and Type Libraries](interface-definitions-and-type-libraries.md)<br/> | Documentation of RPC-specific interface definitions and type libraries.<br/> |
| [MIDL Command-Line Reference](midl-command-line-reference.md)<br/>                           | Documentation of the MIDL compiler command-line switches.<br/>               |
| [MIDL Language Reference](midl-language-reference.md)<br/>                                   | The MIDL compiler language reference.<br/>                                   |



 

## Related topics

<dl> <dt>

[Remote Procedure Call (RPC)](/windows/desktop/Rpc/rpc-start-page)
</dt> </dl>

 

