---
title: Generating a Proxy DLL and a Type Library from a Single IDL File
description: You can use a single IDL file to generate both the proxy stubs and header files for marshaling code, and a type library.
ms.assetid: faa647ac-765a-45bd-8193-b6ea90d064ff
keywords:
- Microsoft Interface Definition Language MIDL , tasks, generating a proxy DLL and a type library
ms.topic: article
ms.date: 05/31/2018
---

# Generating a Proxy DLL and a Type Library from a Single IDL File

You can use a single IDL file to generate both the proxy stubs and header files for marshaling code, and a type library. You do this by defining an interface outside the library block and then referencing that interface from inside the library block, as shown in this example:

``` syntax
//file: AllKnown.idl

[
    object, uuid(. . .), <other interface attributes>
]
interface IKnown : IUnknown 
{
    import "unknwn.idl";
    <declarations, etc. for IKnown interface go here>
};

[
    <library attributes>
]
library KnownLibrary 
{

    //reference interface IKnown:
    interface IKnown;

    //or create a new class:
    [
        <coclass attributes>
    ] 
    coclass KnowMore 
    {
       interface IKnown;
    };
};
```

For more information, see [Marshaling OLE Data Types](marshaling-ole-data-types.md) and [Additional Files Required To Generate a Type Library](additional-files-required-to-generate-a-type-library-2.md).

 

 




