---
title: MIDLRT and Windows Runtime components
description: Shows how to create metadata (.winmd) files that represent the API for custom Windows Runtime components.
ms.assetid: 7830A5DB-9696-4A93-948B-51DA46A5143C
keywords:
- MIDL compiler MIDL
- MIDL compiler MIDL , MIDL and Windows Runtime winrt
- Windows Runtime MIDL
ms.topic: reference
ms.date: 07/08/2026
---

# MIDLRT and Windows Runtime components

Shows how to create metadata (.winmd) files that represent the API for custom Windows Runtime components.


Use the MIDLRT compiler to build metadata (.winmd) files for your custom Windows Runtime components.

When your metadata files are generated, you can compose them into a more efficient package by using the MDMERGE utility. For more info, see [MDMERGE and metadata files](mdmerge-and-metadata-files.md).


Using MIDLRT is similar to using the MIDL compiler. Run MIDLRT from the command line using the following command:

**midlrt** *<***options***>* **filename.idl**

where *<***options***>* represents the command-line options you want to use, and Filename.idl is the name of the IDL file to compile.


The following list shows the command-line switches that MIDLRT.EXE uses.

<dl>

[**/enum\_class**](-enum-class.md)  
[**/metadata\_dir**](-metadata-dir.md)  
[**/nomidl**](-nomidl.md)  
[**/nomd**](-nomd.md)  
[**/ns\_prefix**](-ns-prefix.md)  
[**/winmd**](-winmd.md)  
[**/winrt**](-winrt.md)  
</dl>

A complete listing of MIDLRT compiler switches and options is available when you use the MIDLRT compiler [**/help**](-help-.md) and /? switches. The switches are organized by categories. For more info, see the [MIDL Command-Line Reference](midl-command-line-reference.md).

## Include XML documentation files for IntelliSense

When you distribute Windows Runtime components as NuGet packages, include XML documentation files (`.xml`) alongside the corresponding metadata (`.winmd`) files. XML doc files provide API descriptions, parameter documentation, and code examples that development tools such as Visual Studio and Visual Studio Code use to display IntelliSense tooltips.

Without XML documentation files, IntelliSense shows only the type and member names from the `.winmd` metadata, without descriptions or usage guidance.

To include XML documentation:

1. Add `///` triple-slash documentation comments to your Windows Runtime component source files.
2. Configure your build to generate XML documentation output. For C# projects, set the `GenerateDocumentationFile` property to `true` in your project file. For C++/CLI projects, use the `/doc` compiler option. For native C++/WinRT projects, generate documentation XML from your IDL or source comments using a separate documentation tool.
3. In your NuGet package, place the `.xml` files in the same directory as the corresponding `.winmd` files so that consuming projects automatically pick up the documentation.

## Related topics

<dl> <dt>

[MDMERGE and metadata files](mdmerge-and-metadata-files.md)
</dt> </dl>

 

 




