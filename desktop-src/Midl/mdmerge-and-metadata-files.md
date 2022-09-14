---
title: MDMERGE and metadata files
description: Composes multiple metadata (.winmd) files into a number of output metadata files, based on namespace.
ms.assetid: A3203627-82DF-4744-BBBC-53D13F30210E
keywords:
- metadata
- winmd file
- Windows metadata
ms.topic: article
ms.date: 05/31/2018
---

# MDMERGE and metadata files

Composes multiple metadata (.winmd) files into a number of output metadata files, based on namespace.

## Usage

Run MDMERGE from the command line using the following command:

**mdmerge** *<***options***>*

where *<***options***>* represents the command-line options you want to use.

Generate metadata files for your custom Windows Runtime components by using the MIDLRT compiler. For more info, see [MIDLRT and Windows Runtime components](midlrt-and-windows-runtime-components.md).

## Command-line switches

The following list shows the command-line switches that MDMERGE uses.

<dl>

[**/i**](-mdmerge-i.md)  
[**/metadata\_dir**](-mdmerge-metadata-dir.md)  
[**/n**](-mdmerge-n.md)  
[**/o**](-mdmerge-o.md)  
[**/partial**](-mdmerge-partial.md)  
[**/v**](-mdmerge-v.md)  
</dl>

A complete listing of MDMERGE compiler switches and options is available when you use the **-h** and **/?** switches.

## Remarks

Metadata composition enables multiple IDL files to contain definitions for Windows Runtime components in the same namespace. This frees you from defining all of the types in a namespace within a single IDL file.

You're likely to have numerous Windows Runtime components that your apps use. When you perform the final step to produce deployable Windows Runtime metadata assemblies, you can configure MDMERGE to merge components from multiple metadata directories, like those that are installed with the system (%WINDOWS%\\system32\\WinMetadata), your foundation types, and your current project’s build directory. All necessary types are merged into the correct, deployable, metadata assemblies that you can package for the Windows Store.

You can use the [**/n**](-mdmerge-n.md) option to specify the supported namespace depth for composing metadata assemblies. This enables configuring a hot split for your Windows Runtime components, so that only a single .winmd file is packaged instead of many. This reduces the load times and file I/O required by your Windows Store apps.

## Related topics

<dl> <dt>

[MIDLRT and Windows Runtime components](midlrt-and-windows-runtime-components.md)
</dt> </dl>

 

 




