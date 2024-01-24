---
title: Importing Files and Type Libraries
description: The MIDL keywords include, import, and importlib let you reuse code by referencing existing header, IDL, and object definition language (ODL) files, and compiled type libraries.
ms.assetid: b4571c1d-4bd7-4ab1-9ef6-14356a6c4bb4
keywords:
- Microsoft Interface Definition Language MIDL , tasks, importing files and type libraries
- importing MIDL
- type libraries MIDL , importing
ms.topic: article
ms.date: 05/31/2018
---

# Importing Files and Type Libraries

The MIDL keywords [**include**](include.md), [**import**](import.md), and [**importlib**](importlib.md) let you reuse code by referencing existing header, IDL, and object definition language (ODL) files, and compiled type libraries.

The ACF [**include**](include.md) directive lets you specify in an ACF file one or more C-language header files to be included in the MIDL-generated stub code. The generated file will have a line with a **\#include** C-preprocessor directive with the indicated header file. Use this **include** directive to bring in header files that are specific to a particular operating environment and that do not contain information necessary for the interface between client and server. Do not use **include** for header files containing data types that you want available to the IDL file; instead, use the [**import**](import.md) directive.

## Example 1

``` syntax
[
  auto_handle
] 
interface X86PC
{ 
  include "gendefs.h", "protos.h", "myfile.h"; 
  //interface typdefs and function declarations here
}
```

The IDL [**import**](import.md) directive is the standard method for bringing type and interface definitions from other IDL (or ODL) files and header files into your IDL file. All IDL statements in the imported file, such as typedefs, [**const**](const.md) declarations, and interface definitions become available to the importing IDL file.

Like the C-language preprocessor directive **\#include**, the [**import**](import.md) directive tells the compiler to include data types that were defined in the imported IDL files. Unlike the **\#include** directive, the **import** directive ignores procedure prototypes, since no stubs are generated for anything in the imported file. Because the preprocessor is invoked separately for the imported file, preprocessor directives (such as **) do not carry over to the importing IDL file.

For additional information on using [**import**](import.md) to include system header files in an IDL file, see [Importing System Header Files](importing-system-header-files.md).

## Example 2

``` syntax
[
  uuid(. . .), object
] 
interface IKnown : IUnknown
{
  import "base.idl", "unknwn.idl", "helper.idl";
  //remainder of interface definition
}
```

The ODL [**importlib**](importlib.md) directive lets you reference a compiled type library in your IDL or ODL file. The **importlib** directive must be inside a [**library**](library.md) statement, and must precede other type descriptions in the library. The imported library, as well as the generated library, must be available to the application at runtime.

## Example 3

``` syntax
library NewBrowser
{
  importlib("stdole32.tlb");
  importlib("legacy.tlb");
  //remainder of library definition
};
```

You can also use the C-preprocessor **\#include** directive to include headers and other files in your IDL or ODL file. Be aware, however, that this directive will literally include the entire contents of the specified file. If a header file contains prototypes that you do not need or want in the MIDL-generated stub files, or if it contains nonremotable type definitions, you should use the MIDL [**import**](import.md) directive instead of the **\#include** directive.

## Related topics

<dl> <dt>

[**import**](import.md)
</dt> <dt>

[**importlib**](importlib.md)
</dt> <dt>

[**include**](include.md)
</dt> <dt>

[Importing System Header Files](importing-system-header-files.md)
</dt> </dl>

 

 




