---
title: MIDLRT and Windows Runtime components
description: Shows how to create metadata (.winmd) files that represent the API for custom Windows Runtime components.
ms.assetid: 7830A5DB-9696-4A93-948B-51DA46A5143C
keywords:
- MIDL compiler MIDL
- MIDL compiler MIDL , MIDL and Windows Runtime winrt
- Windows Runtime MIDL
ms.topic: article
ms.date: 05/31/2018
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

## Related topics

<dl> <dt>

[MDMERGE and metadata files](mdmerge-and-metadata-files.md)
</dt> </dl>

 

 




