---
title: Adding ODL to an IDL Definition
description: The .odl files provide object definitions that are added to the type descriptions in a type library.
ms.assetid: 16e2f064-1636-47b1-a838-d7e41b69c613
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Adding ODL to an IDL Definition

The .odl files provide object definitions that are added to the type descriptions in a type library. The MIDL compiler parses files written in ODL syntax, generates the type libraries, and optionally creates C++ header files that contain the same definitions.

The top-level element of ODL syntax is the [library](library.md) statement (or library block). Every other ODL statement (with the exception of the attributes that can be applied to the **library** statement) must be defined in the library block.

The MIDL compiler generates a type library when it sees a **library** statement. The statements found in the library block follow essentially the same syntax as earlier versions of ODL.

ODL attributes can be applied to an element both inside and outside of the library block. Outside the block, they typically do nothing, unless the element is referenced from within the block by using it as a base type, inheriting from it, or referencing it on a line such as this:


```C++
library a
{
   interface [xyz]];
   struct bar;
   ...
};
```



If an element defined outside of the block is referenced in the block, its definition is put into the generated type library.

Anything outside of the library block is an .idl file, and the MIDL compiler processes it as usual. Typically, this means generating proxy stubs for it.

 

 




