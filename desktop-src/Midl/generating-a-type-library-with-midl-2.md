---
title: Generating a Type Library with MIDL
description: The top-level element of the ODL syntax is the library statement (library block).
ms.assetid: e21a9e6e-4e10-4280-af8f-24534cb2ab90
keywords:
- Microsoft Interface Definition Language MIDL , tasks, generating a type library
ms.topic: article
ms.date: 05/31/2018
---

# Generating a Type Library with MIDL

The top-level element of the ODL syntax is the library statement (library block). Every other ODL statement, with the exception of the attributes that are applied to the library statement, must be defined within the library block. When the MIDL compiler sees a library block, it generates a type library in much the same way that MkTypLib does. With a few exceptions, described in [Differences Between MIDL and MKTYPLIB](differences-between-midl-and-mktyplib.md), the statements within the library block should follow the same syntax as in the ODL language and MkTypLib.

> [!Note]  
> The Mktyplib.exe tool is obsolete. Use the MIDL compiler instead.

 

You can apply ODL attributes to elements that are defined either inside or outside the library block. These attributes have no effect outside the library block unless the element they are applied to is referenced from within the library block. Statements inside the library block can reference an outside element either by using it as a base type, inheriting from it, or by referencing it on a line as shown:

``` syntax
<some IDL definitions including definitions for interface IFace and struct bar>
[<some attributes>]
library a
{
    interface IFace;
    struct this_struct;
...
};
```

If an element defined outside the library block is referenced within the library block, then its definition will be put into the generated type library. The MIDL compiler treats the statements outside of a library block as a typical IDL file and parses those statements as it has always done. Normally, this means generating C-language stubs for an RPC application.

For more information about the general syntax for an ODL file see [ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax).

 

 