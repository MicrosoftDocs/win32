---
description: Package authors can reduce the size of their installation packages by compressing the source files and including them in cabinet files. The source file image can be compressed, uncompressed, or a mixture of both types.
ms.assetid: e84c52ca-a1c4-4c81-9c24-31ea435054db
title: Compressed and Uncompressed Sources
ms.topic: article
ms.date: 05/31/2018
---

# Compressed and Uncompressed Sources

Package authors can reduce the size of their installation packages by compressing the source files and including them in [cabinet files](cabinet-files.md). The source file image can be compressed, uncompressed, or a mixture of both types.

<dl> <dt>

<span id="_____Compressed_Sources"></span><span id="_____compressed_sources"></span><span id="_____COMPRESSED_SOURCES"></span> Compressed Sources
</dt> <dd>

A source consisting entirely of compressed files should include the compressed flag bit in the [**Word Count Summary**](word-count-summary.md) Property. The compressed source files must be stored in cabinet files located in a data stream inside the .msi file or in a separate cabinet file located at the root of the source tree. All of the cabinets in the source must be listed in the [Media table](media-table.md).

</dd> <dt>

<span id="Uncompressed_Sources"></span><span id="uncompressed_sources"></span><span id="UNCOMPRESSED_SOURCES"></span>Uncompressed Sources
</dt> <dd>

A source consisting entirely of uncompressed source files should omit the compressed flag bit from the [**Word Count Summary**](word-count-summary.md) Property. All of the uncompressed files in the source must exist in the source tree specified by the [Directory table](directory-table.md).

</dd> <dt>

<span id="Mixed_Sources_____"></span><span id="mixed_sources_____"></span><span id="MIXED_SOURCES_____"></span>Mixed Sources 
</dt> <dd>

To mix compressed and uncompressed source files in the same package, override the [**Word Count Summary**](word-count-summary.md) property default by setting the msidbFileAttributesCompressed or msidbFileAttributesNoncompressed bit flags on particular files. These bit flags are set in the Attributes column of the [File table](file-table.md) if the compression state of the file does not match the default specified by the [**Word Count Summary**](word-count-summary.md) property.

For example, if the [**Word Count Summary**](word-count-summary.md) property has the compressed flag bit set, all files are treated as compressed into a cabinet. Any uncompressed files in the source must include msidbFileAttributesNoncompressed in the Attributes column of the [File table](file-table.md). The uncompressed files must be located at the root of the source tree.

If the [**Word Count Summary**](word-count-summary.md) property has the uncompressed flag set, files are treated as uncompressed by default and any compressed files must include msidbFileAttributesCompressed in the Attributes column of the File table. All of the compressed files must be stored in cabinet files located in a data stream inside the .msi file or in a separate cabinet file located at the root of the source tree.

For more information, see [Using Cabinets and Compressed Sources](using-cabinets-and-compressed-sources.md).

</dd> </dl>

 

 



