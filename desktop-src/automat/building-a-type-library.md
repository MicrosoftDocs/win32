---
title: Building a Type Library
description: Demonstrates how to build a type library.
ms.assetid: 089eb146-9f24-4b15-a768-1706614667a9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Building a Type Library

The MIDL compiler builds type libraries and is described in [Type Libraries and the Object Description Language](type-libraries-and-the-object-description-language.md).

## To create a type library from an object description script

Run the MIDL compiler tool on the script. For example:


```C++
MIDL /tlb output.tlb /h output.h inscript.odl
```



Based on the object description script inscript.odl, the example creates a type library named output.tlb and a header file named output.h.

After creating the type library, you can include it in the resource step of building your application, or leave it as a stand-alone file. In either case, be sure to specify the file name and path of the library in the application's registration (.reg) file, so Automation can find the type library when necessary. See the following section for information on registering the type library.

## To build an application that uses a type library

1.  Include the header file in the project.

2.  Compile the project.

3.  Optionally, use the Resource Compiler (RC) to bind the type library with the compiled project. The type library can bind with DLLs or executable files. For example, to bind a type library named output.tlb with a DLL, use the following statement in the .rc file for the DLL:

    ```C++
    1 typelib output.tlb
    ```

    

    A DLL that contains a type library resource usually has the .olb (object library) extension.

 

 




