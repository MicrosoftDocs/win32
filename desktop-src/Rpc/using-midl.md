---
title: Using MIDL
description: Creating and compiling a Microsoft Interface Definition Language (MIDL) interface and Remote Procedure Call (RPC).
ms.assetid: 2594e3d6-d44a-4e12-8286-b9700e67702e
ms.topic: article
ms.date: 05/31/2018
---

# Using MIDL

All interfaces for programs using RPC must be defined in Microsoft Interface Definition Language (MIDL) and compiled with the MIDL compiler. The following topics present a brief overview of creating and compiling a MIDL interface:

-   [Defining an Interface with MIDL](#defining-an-interface-with-midl)
-   [Compiling a MIDL File](#compiling-a-midl-file)

For a detailed discussion of these topics, see [The IDL and ACF Files](the-idl-and-acf-files.md).

## Defining an Interface with MIDL

MIDL files are text files that you can create and edit with a text editor. If you generate a UUID for your interface, you will typically store the output in a template MIDL file. For more information on UUIDs, see [Generating Interface UUIDs](generating-interface-uuids.md).

All interfaces in MIDL follow the same format. They begin with a header that contains a list of interface attributes and the interface name. The attributes are enclosed in square brackets. The interface header is followed by its body, which is enclosed in curly brackets. A simple interface is shown in the following example:

``` syntax
[
  uuid(ba209999-0c6c-11d2-97cf-00c04f8eea45),
  version(1.0)
]
interface MyInterface
{
  const unsigned short INT_ARRAY_LEN = 100;

  void MyRemoteProc( 
      [in] int param1,
      [out] int outArray[INT_ARRAY_LEN]
  );
}
```

Some of the attributes that typically appear in a MIDL interface definition are the UUID and the interface version number. The body of the interface definition must contain the procedure declarations of all of the remote procedures in the interface. It can also contain the declarations of data types and constants required by the interface.

All parameters in the remote procedure declarations must be declared as \[[**in**](/windows/desktop/Midl/in)\], \[[**out**](/windows/desktop/Midl/out-idl)\], or \[**in**, **out**\]. These declarations specify that the client program passes data into a remote procedure, gets data out of a remote procedure, or both. For more detailed information about interface parameter declarations, see [The IDL Interface Body](the-idl-interface-body.md).

## Compiling a MIDL File

The MIDL compiler is a command-line tool that is automatically installed with the Platform Software Development Kit (SDK). Invoke it in a command window by typing the command **midl**, followed by the name of a MIDL file, at the command line. Make sure that the directory containing the MIDL compiler is in your path. The following example illustrates its use:

**midl MyApp.idl**

Note that you do not have to include the extension if the file name has the .idl extension. You can also use the MIDL compiler [command-line switches](/windows/desktop/Midl/midl-command-line-reference) by inserting them between the **midl** command and the file name. This is demonstrated in the following example:

**midl /acf MyApp.acf MyApp.idl**

In this example, the MIDL compiler is executed using the file MyApp.idl as the input file. The command line switch **/acf** instructs the compiler to use an application configuration file (ACF) for input as well. Application configuration files are discussed more thoroughly in [The IDL and ACF Files](the-idl-and-acf-files.md).

For more detailed information on using the MIDL compiler, see the [Microsoft Interface Definition Language (MIDL)](/windows/desktop/Midl/midl-start-page), which contains information on the following topics:

-   [C-Preprocessor Requirements for MIDL](/windows/desktop/Midl/c-preprocessor-requirements-for-midl)
-   [C/C++-Compiler Considerations](/windows/desktop/Midl/c-c-compiler-considerations)
-   [Files Generated for an RPC Interface](/windows/desktop/Midl/files-generated-for-an-rpc-interface)
-   [MIDL Command-line Reference](/windows/desktop/Midl/midl-command-line-reference)
-   [MIDL Language Reference](/windows/desktop/Midl/midl-language-reference)
-   [MIDL Compiler Errors and Warnings](/windows/desktop/Midl/midl-compiler-errors-and-warnings)

 

 