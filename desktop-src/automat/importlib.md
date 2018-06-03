---
title: importlib
description: This directive makes types that have already been compiled into another type library available to the library currently being created. All importlib directives must precede the other type descriptions in the library.
ms.assetid: 6bba3d5d-5526-4b53-be6f-258918b30e9c
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# importlib

This directive makes types that have already been compiled into another type library available to the library currently being created. All importlib directives must precede the other type descriptions in the library.

## Syntax

``` syntax
importlib(filename);
```

<dl> <dt>

<span id="filename"></span><span id="FILENAME"></span>*filename*
</dt> <dd>

The location of the type library file when MIDL is executed.

</dd> </dl>

## Remarks

The importlib directive makes any type defined in the imported library accessible from within the library being compiled. Ambiguity is resolved as the current library is searched for the type. If the type cannot be found, MIDL searches the imported library that is lexically first, and then the next, and so on. To import a type name in code, the name should be entered as *libname*.*typename*, where *libname* is the library name as it appeared in the library statement when the library was compiled.

The imported type library should be distributed with the library being compiled.

## Example

The following example imports the libraries Stdole.tlb and Mydisp.tlb.


```C++
library BrowseHelper
{
   importlib("stdole.tlb");
   importlib("mydisp.tlb");
}
```



 

 




