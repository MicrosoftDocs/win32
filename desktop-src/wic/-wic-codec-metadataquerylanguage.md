---
description: This topic introduces the metadata query language for Windows Imaging Component (WIC).
ms.assetid: 5ffa0a69-b53d-4be3-b802-deaaa743e6bd
title: Metadata Query Language Overview
ms.topic: article
ms.date: 05/31/2018
---

# Metadata Query Language Overview

This topic introduces the metadata query language for Windows Imaging Component (WIC). You use the metadata query language to create expressions that find specific data (metadata items) and locations (metadata blocks) within the metadata of an image.

This topic contains the following sections.

-   [Prerequisites](#prerequisites)
-   [Introduction](#introduction)
-   [Anatomy of a Path Expression](#anatomy-of-a-path-expression)
    -   [Block Selection](#block-selection)
    -   [Item Selection](#item-selection)
    -   [Escape Character](#escape-character)
    -   [Sample Expressions](#sample-expressions)
-   [Photo Metadata Policy Expressions](#photo-metadata-policy-expressions)
-   [Metadata Query Language Summary](#metadata-query-language-summary)
-   [Related topics](#related-topics)

## Prerequisites

To understand this topic, you should be familiar with the WIC metadata system as described in the [WIC Metadata Overview](-wic-about-metadata.md) and accessing metadata, as described in the [Overview of Reading and Writing Image Metadata](-wic-codec-readingwritingmetadata.md).

## Introduction

You interact with the metadata platform primarily through two Component Object Model (COM) components: a query reader, represented by the [**IWICMetadataQueryReader**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataqueryreader) interface, and a query writer, represented by the [**IWICMetadataQueryWriter**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataquerywriter) interface. These components enable you to read or write metadata using the metadata query language. The query language describes the syntax of a path expression and the query components use this path expression to access the desired metadata. This path expression describes the location of a metadata block or item.

A metadata block is a named group of metadata in a specific format. A metadata block can contain individual metadata items such as an author or creation time and additional metadata blocks. A metadata block's name is determined by its format. For example, a metadata block containing App1 metadata would be named "app1". Common metadata formats include App1, Exif, IFD, and XMP.

A metadata item is a name/value pair that describes characteristics like author, title, and rating.

A path expression contains one or more metadata block names. It can also specify a metadata item within a metadata block. The following path expression represents an App1 block which contains an IFD block which contains the metadata item:

-   /app1/ifd/{ushort=18249}

The following diagram illustrates the makeup of an example JPEG image with four root metadata blocks: App0, App1, XMP, and an unknown block. Each highlighted item notes the type of metadata (block or item) and the query expression used to retrieve the data.

![jpeg image with metadata callouts](graphics/jpegwithcallouts.png)

> [!Note]  
> The contents of this diagram are referenced throughout this document and are used in many of the examples.

 

## Anatomy of a Path Expression

To access metadata using the WIC APIs, a fully qualified query expression must be used in most cases. This topic discusses fully qualified expressions for accessing metadata. If you need information about the cases in which non-fully qualified expressions are used, refer to the Photo Metadata Policy Expression section later in this document.

What is a fully qualified query expression? In WIC, a fully qualified expression is a string that begins with the path character slash (/), followed by a navigation path to a metadata block or a specific metadata item. Each step within the navigation path is separated by a slash, forming an expression for accessing a metadata block or a metadata item. For example, the following is a fully qualified query expression that accesses the Microsoft Photo Rating in an IFD block that is nested in an App1 block:

-   /app1/ifd/{ushort=18249}

When WIC parses this expression, it first searches for the App1 metadata block within the image's metadata. If the App1 block is found, it continues its search looking for the nested IFD metadata block. If the IFD block is found, it then looks for the specific metadata item, in this case the MicrosoftPhoto rating under the tag 18249, within the IFD metadata block. If at any time WIC does not find a metadata block or item, it aborts the query.

### Block Selection

The simplest WIC metadata query expression is an expression to obtain a query reader/writer for a specific metadata block. Obtaining a query reader/writer enables you to direct subsequent queries directly to a nested metadata block without dealing with its parent block. A block selection query expression is a navigation path to the desired metadata block. For example, in the previous illustration there are five metadata blocks, two of which are nested in other metadata blocks. The following are the path expressions to each metadata block in the JPEG example:

-   /app0
-   /app1
-   /app1/ifd
-   /app1/ifd/exif
-   /xmp

When you use a query reader/writer to execute a query, it returns a new query reader/writer that services queries within the scope of the specified metadata block. For instance, if you execute the query "/app1" , a new query reader is obtained and queries to the new reader are relative to the App1 block. This means that the query "/ifd" is valid for the new reader because the App1 block contains an IFD block. However, "/xmp" would not work because this App1 block does not contain an XMP metadata block.

The query language also supports an index notation. Index notation provides access to a specific metadata block when multiple blocks of the same type exist. For the JPEG example, the following indexed path expression can be used:

-   /\[0\]app1/\[0\]ifd

In the query language, all indexes start at zero. In the previous expression, the first zero queries for the first App1 block and the second zero queries the first nested IFD block. Index notation can still be used even when multiple blocks of the same type do not exist. If the example JPEG included a second App1 block with an embedded IFD block, the expression "/\[1\]app1/ifd" would be used to access the second App1 block.

Index notation becomes more common when dealing with PNG tEXt chunks because it is likely that the PNG image will have more than one tEXt chunk.

> [!Note]  
> Multidimensional array indexes are not supported.

 

### Item Selection

You can access the metadata items in a metadata block by building on the block selection expressions. Consider the XMP and Microsoft Photo rating properties in the JPEG example. This metadata exists in two metadata blocks: the App1/IFD and XMP blocks. Therefore, more than one expression can be used to access the same data. The following expression accesses the MicrosoftPhoto rating in the XMP block:

-   /xmp/xmp:Rating

The "xmp:" part of the expression is a schema friendly identifier. XMP is an extensible standard and allows third party entities to publish their own schemas which define how to store certain metadata items. An XMP schema is fully identified by a URL, but WIC provides a set of friendly identifiers for well-known schemas. For more information, see the [Native Image Format Metadata Queries](-wic-native-image-format-metadata-queries.md) topic.

For JPEG images, rating information can also be stored within the App1 nested IFD block. However, unlike the XMP rating example, the IFD block does not use a schema name to access the rating information. You use a data expression instead. The following expression is used to access the MicrosoftPhoto rating in the App1 nested IFD block:

-   /app1/ifd/{ushort=18249}

In this expression, the "/app1/ifd" part of the expression is the navigation path to the IFD block (as discussed previously in the Block Selection section). The second part of the expression "/{ushort=18249}" accesses the data. This part of the expression instructs the query parser to find the data embedded in the unsigned short tag that has the tag identifier 18249.

> [!Note]  
> For a list of common metadata formats supported by each image format at, see the [Native Image Format Metadata Queries](-wic-native-image-format-metadata-queries.md) topic.

 

The {ushort=18249} is a data expression and can take several forms. A data expression is a two part expression containing the requested metadata tag or key, in this case "18249", and the data type of the key, in this case "ushort". The two parts are separated by an equal sign (=). WICsupports a majority of the common C/C++ data types. The following data types are accepted by the query language:

-   char
-   uchar
-   short
-   ushort
-   long
-   ulong
-   int
-   uint
-   longlong
-   float
-   double
-   str
-   wstr
-   guid
-   bool

> [!Note]  
> This list only specifies the data types supported by the metadata query language. Use these data types when creating a metadata query data expression such as {ushort=18249}. The WIC returns the metadata item's value in the form of PROPVARIANT, which defines its own type system.

 

The "18249" in the example is the data tag. This particular number is defined by Microsoft to contain the MicrosoftPhoto rating. The data tag can be any number, string, or GUID depending on the data item you are looking for

Unlike the XMP Rating example, there is no name collision for the rating value in the App1/IFD block. This is because the XMP rating value is actually stored under a different ushort tag, 18246. Thus, the expression to access the XMP rating in the App1/IFD block is:

-   /app1/ifd/{ushort=18246}

> [!Note]  
> For a formal description of the metadata query language, see the Metadata Query Language Summary section later in this document.

 

### Escape Character

The query language is not case sensitive and treats all characters as lowercase. However, some metadata formats (such as XMP) are case sensitive. When working with a case-sensitive metadata format, use the backslash (\\) character when you want to specify an uppercase character.

The escape character is consumed by the language parser and the following character that follows it is interpreted directly. For example, the expression {char=\\\\} is resolved as '\\'and {char=\\C} is resolved as an uppercase C. Without the escape character, {char=\\} would be an invalid expression and {char=C} would be interpreted as a lowercase c. Be sure to use the backslash escape character before all uppercase letters in metadata formats that are case sensitive.

### Sample Expressions

The following table provides some example expressions and descriptions of their interpretations by the query language parser. 

| Expression                     | Description                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ifd/xmp/exif:Author            | Corresponds to the following navigation path: IFD block -> XMP block -> "Author" property in the "Exif" schema.                                                                                                                                                                                                                                            |
| /\[1\]ifd/\[0\]xmp/exif:Author | Same as the first item in this table except that the \[\#\] prefix describes which item to navigate in event of a name collision.                                                                                                                                                                                                                                |
| /ifd/{ushort=700}/Author       | Same as the first item in this table except that it uses a data expression to reference the XMP block instead of the block name "xmp" (XMP block is embedded under the unsigned short tag identifier 700). Also, the "Author" property does not specify a schema. The query parser will try to match the property across all schemas and return the first match. |
| /ifd/xmp                       | Provides a navigation path to a metadata block. If the block is found, a new metadata reader/writer is returned.                                                                                                                                                                                                                                                 |
| /\[\*\]tEXt/Keyword            | Gets or sets the Keyword property for a PNG chunk. Because the PNG metadata specification allows for multiple chunks of a particular type, the \[\*\] notation gets/sets the data PNG chunk with the appropriate property. Per the PNG specification, no two chunks can have the same properties.                                                                |



 

Each metadata block is also uniquely identified by the metadata GUID which can be used in place of the friendly block name. The following syntax can be used in place of providing block names: "/{guid=GUID}/\[n\]{guid=GUID}/schema:tagidentifier"

The following table provides some invalid examples and the reasons they would be rejected. 

| Invalid Expression         | Rejection description                                                                                                                                                  |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /ifd/\[0\]\[2\]exif/       | Rejected because multi dimensional array indexes are not supported.                                                                                                    |
| /ifd/{ushort=1}/{ushort=2} | Rejected unless the IFD has a tagID=1 which is a metadata handler that contains a metadata item with a tagID=2.                                                        |
| /{ushort=1}                | Rejected if the query processing is relative to a top level of the metadata hierarchy. This is because the top level contains only metadata blocks and not data items. |



 

## Photo Metadata Policy Expressions

As noted previously, a fully qualified query expression starts with a slash (/). Expressions that do not begin with the slash are evaluated as policy expressions. A policy expression enables you to query the photo metadata for image-related Windows [Shell Properties](https://msdn.microsoft.com/library/ms788673(VS.85).aspx). In the Data Selection section earlier in this document, the expression "/xmp/xmp:Rating" was used to access the XMP rating property. This property can also be queried using the following policy expression:

-   System.SimpleRating

To access the rating property from the MicrosoftPhoto schema, the following query expression can be used:

-   System.Rating

Photo metadata policy expressions behave differently from fully qualified metadata queries in a few notable ways.

First, when accessing metadata using a policy expression, WIC performs arbitration and conflict resolution in the case that the same property is available in multiple metadata blocks. For instance, both the MicrosoftPhoto and the XMP rating values are stored in both the App1/IFD block and the XMP block. The photo metadata policy determines the precedence for which block value is returned when reading metadata. When you are writing metadata, the photo metadata policy ensures that the same properties in different blocks are consistent. If you use a metadata query such as "/xmp/xmp:Rating", you are responsible for arbitrating between the various metadata locations.

> [!Note]  
> For a list of the supported policy expressions and their mapping policies, see the [Photo Metadata Policies](photo-metadata-policies.md) topic.

 

Second, photo metadata policy expressions are independent of the image format, while fully qualified metadata queries are not. For example, the "/xmp/xmp:Rating" query is specific to the JPEG format. TIFF images also support XMP metadata, but it is stored differently compared to JPEG, so the TIFF query would be “/ifd/xmp/xmp:Rating”. However, in both cases the policy expression would be “System.SimpleRating”.

Photo metadata policy expressions provide a higher level of abstraction and simplicity when compared to fully qualified metadata queries, and so should be preferred in cases where low-level metadata access is not needed. However, policy expressions only provide access to a limited set of image metadata, whereas the metadata query language provides access to nearly all of the metadata stored within an image file.

## Metadata Query Language Summary

The following table is a formal definition of the WIC metadata query language. Each grammar symbol represents an expression made up of other symbols. The expression can be another symbol or a sequence of other symbols separated by the vertical bar (\|), indicating an "or" choice. The whole expression on the right is a possible substitution for the specified symbol on the left. 

| Symbol                   | Expression                                                                                                                                                                  |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \<path>             | \<name> \| '/' \<property path>                                                                                                                                   |
| \<property path>    | \<metadata item> \| \<property path> '/' \<property path>                                                                                                    |
| \<metadata item>    | \<index name> \| \<item name> \| \<schema name> ':' \<item name>                                                                                        |
| \<schema name>      | \<item name>                                                                                                                                                           |
| \<item name>        | \<metadata item> \| \<indexed item\>&lt;index&gt;                                                                                                                  |
| \<indexed item>     | \<item> \| \<implied metadata>\<item>                                                                                                                        |
| \<implied metadata> | '<'\<name>'>'                                                                                                                                                    |
| \<item>             | \<name> \| \&lt;index&gt; \<data> \| \<data>                                                                                                                  |
| \<data>             | '{' \<data type> '=' \<value> '}'                                                                                                                                 |
| \&lt;index&gt;            | '\[' \<number> \| \<star> '\]'                                                                                                                                    |
| \<data type>        | 'char' \| 'uchar' \| 'short' \| 'ushort' \| 'long' \| 'ulong' \| 'int' \| 'uint' \| 'longlong' \| 'ulonglong' \| 'float' \| 'double' \| 'str' \| 'wstr' \| 'guid' \| 'bool' |
| \<data value>       | \<number> \| \<name> \| \<guid>                                                                                                                              |
| \<star>             | '\*'                                                                                                                                                                        |
| \<number>           | number                                                                                                                                                                      |
| \<name>             | string                                                                                                                                                                      |
| \<guid>             | guid                                                                                                                                                                        |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[WIC Metadata Overview](-wic-about-metadata.md)
</dt> <dt>

[Overview of Reading and Writing Image Metadata](-wic-codec-readingwritingmetadata.md)
</dt> <dt>

[Metadata Extensibility Overview](-wic-codec-metadatahandlers.md)
</dt> <dt>

[How-to: Re-encode a JPEG Image with Metadata](-wic-codec-jpegmetadataencoding.md)
</dt> </dl>

 

 



