---
title: Metadata
description: Metadata, for the purposes of this SDK, is information that describes an ASF file or the contents of the file.
ms.assetid: '4ccca0c3-52c5-4291-bdab-354705db9b10'
keywords:
- Windows Media Format SDK,metadata overview
- Advanced Systems Format (ASF),metadata overview
- ASF (Advanced Systems Format),metadata overview
- metadata,about
ms.topic: article
ms.date: 05/31/2018
---

# Metadata

Metadata, for the purposes of this SDK, is information that describes an ASF file or the contents of the file. The header section of an ASF file contains all of the metadata associated with that file. Individual items of metadata in an ASF file are called attributes. Each attribute has a name and a value. Throughout this documentation, global constants are used to identify attributes. For example, the title of an ASF file is stored in the **g\_wszWMTitle** attribute.

A number of attributes are defined in the Windows Media Format SDK to handle the most common metadata needs. In addition, you can create your own attributes. You should take care when naming custom attributes, however, because other application developers can use the same names, and conflicts can occur.

Some attributes are set by the SDK and cannot be changed manually. For example, when you index an ASF file, the SDK sets the **g\_wszWMSeekable** attribute to show that the file can now be read from any specified point.

Other attributes are purely informational and must be set manually. For example, if you want to keep track of the author of a file, you should set **g\_wszWMAuthor**.

The Windows Media Format SDK provides support for attributes that apply to the entire file, and attributes that apply to individual streams.

You can use the Windows Media Format SDK to edit the metadata in MP3 files, though you should always use ID3-compliant attributes in MP3 files to maintain compatibility with other MP3 manipulation programs.

## Related topics

<dl> <dt>

[**Concepts**](concepts.md)
</dt> <dt>

[**Metadata Editor Object**](metadata-editor-object.md)
</dt> <dt>

[**Metadata Features**](metadata-features.md)
</dt> <dt>

[**Working with Metadata**](working-with-metadata.md)
</dt> </dl>

 

 




