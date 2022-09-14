---
title: importlib attribute
description: The \ importlib\ directive makes types that have already been compiled into another type library available to the type library being created.
ms.assetid: d5f15a77-c6b1-4918-be86-07d2995ca2d4
keywords:
- importlib attribute MIDL
topic_type:
- apiref
api_name:
- importlib
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# importlib attribute

The **\[importlib\]** directive makes types that have already been compiled into another type library available to the type library being created.

``` syntax
[
    library-attributes
]
library (library-name)
{
    importlib(file-to-import); 
    ... 
}
```

## Parameters

<dl> <dt>

*library-attributes* 
</dt> <dd>

Zero or more attributes that will be applied to the library.

</dd> <dt>

*library-name* 
</dt> <dd>

The identifier that software components will use to denote this [**library**](library.md).

</dd> <dt>

*file-to-import* 
</dt> <dd>

The name and location of the imported file at MIDL compile-time.

</dd> </dl>

## Remarks

All **\[importlib\]** directives must precede the other type descriptions in the library. Note that the imported library, as well as the generated library, must be distributed with the application so that it is available at run time.

In most cases you should use the MIDL **\[**[**import**](import.md)**\]** directive to reference definitions from another .IDL file in your .IDL file. This method provides your type library with all the information from the original file, whereas **\[importlib\]** only brings in the contents of the type library.

> [!Note]  
> The **\[importlib\]** directive makes any type defined in the imported library accessible from within the library being compiled. To avoid ambiguity when there are duplicate references, we recommend that you qualify each such reference with the appropriate library name, as follows:

 

``` syntax
library_name.type
```

In the absence of such qualification, MIDL resolves duplicate reference ambiguity as follows:

-   Effective with version 3.1, MIDL uses the first reference it finds.
-   Version 3.0 of MIDL, the first version of MIDL that could generate type libraries, uses the last reference it found.

## Examples

``` syntax
library BrowseHelper 
{ 
    importlib("stdole32.tlb"); 
    importlib("mydisp.tlb"); 
    //Remainder of library definition 
};
```

## See also

<dl> <dt>

[**library**](library.md)
</dt> <dt>

[**import**](import.md)
</dt> <dt>

[Importing System Header Files](importing-system-header-files.md)
</dt> <dt>

[Importing Files and Type Libraries](importing-files-and-type-libraries.md)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 