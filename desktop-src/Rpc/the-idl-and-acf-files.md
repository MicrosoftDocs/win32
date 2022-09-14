---
title: The IDL and ACF Files
description: The syntax of the Microsoft Interface Definition Language (MIDL) is based on the syntax of the C programming language. When a language concept in this description of MIDL is not fully defined, the C-language definition of that term is implied.
ms.assetid: f99f5934-750d-4c30-9970-803a891cacb7
keywords:
- Remote Procedure Call RPC , described, IDL and ACF files
ms.topic: article
ms.date: 05/31/2018
---

# The IDL and ACF Files

The syntax of the Microsoft Interface Definition Language (MIDL) is based on the syntax of the C programming language. When a language concept in this description of MIDL is not fully defined, the C-language definition of that term is implied.

The MIDL design specifies two distinct files: the Interface Definition Language (IDL) file and the application configuration file (ACF). These files contain attributes that direct the generation of the C-language stub files that manage the remote procedure call (RPC). The IDL file contains a description of the interface between the client and the server programs. RPC applications use the ACF file to describe the characteristics of the interface that are specific to the hardware and operating system that make up a particular operating environment. The purpose of dividing this information into two files is to keep the software interface separate from characteristics that affect only the operating environment.

The IDL file specifies a network contract between the client and server—that is, the IDL file specifies what is transmitted between the client and the server. Keeping this information distinct from the information about the operating environment makes the IDL file portable to other environments. The IDL file consists of two parts: an [interface header](the-idl-interface-header.md) and an [interface body](the-idl-interface-body.md).

The ACF specifies attributes that affect only local performance rather than the network contract. Microsoft RPC allows you to combine the ACF and IDL attributes in a single IDL file. You can also combine multiple interfaces in a single IDL file (and its ACF).

This section summarizes the attributes that are specified in the IDL and ACF files. It is intended to only provide an overview. For more detailed information, see the [MIDL Language Reference](/windows/desktop/Midl/midl-language-reference), and the [MIDL Command-Line Reference](/windows/desktop/Midl/midl-command-line-reference). The discussion in this section is presented in the following topics:

-   [The Interface Definition Language (IDL) File](the-interface-definition-language-idl-file.md)
-   [The Application Configuration File (ACF)](the-application-configuration-file-acf-.md)
-   [MIDL Compiler Output](midl-compiler-output.md)

 

 