---
title: Open Packaging Conventions Fundamentals
description: Introduces the OPC concepts that are required for using Packaging APIs.
ms.assetid: 115430f2-8e1f-46ba-ae6e-b7f3689048ff
keywords:
- Open Packaging Conventions (OPC)
- OPC (Open Packaging Conventions)
- Packaging APIs,Open Packaging Conventions
- packaging,Open Packaging Conventions (OPC)
- packages,Open Packaging Conventions (OPC)
- packages,about
- packaging,logical model
- packages,logical model
- logical model
- packaging,physical model
- packages,physical model
- physical model
- packaging,ZIP-based formats
- packages,ZIP-based formats
- ZIP-based package formats
- packaging,parts
- packages,parts
- parts,Open Packaging Conventions (OPC)
- parts,about
- packaging,relationships
- packages,relationships
- relationships,Open Packaging Conventions (OPC)
- packaging,digital signatures
- packages,digital signatures
- digital signatures
- signatures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Open Packaging Conventions Fundamentals

Introduces the OPC concepts that are required for using Packaging APIs.

This topic contains the following sections.

-   [Introduction](#introduction)
-   [What are the Open Packaging Conventions (OPC)?](#what-are-the-open-packaging-conventions-opc)
-   [Packages](#packages)
    -   [Logical Model](#logical-model)
    -   [Physical Model](#physical-model)
    -   [Existing ZIP-Based Package Formats](#existing-zip-based-package-formats)
-   [Parts](#storing-relationships-relationships-parts)
-   [Relationships](#storing-relationships-relationships-parts)
    -   [Storing Relationships: Relationships Parts](#storing-relationships-relationships-parts)
-   [Digital Signatures](#digital-signatures)
-   [Related topics](#related-topics)

## Introduction

The *ECMA-376 OpenXML, 1st Edition, Part 2: Open Packaging Conventions (OPC)* can be more easily understood through an analogy with real world filing systems. People and businesses need to organize their information. Often, this information is tracked by using paperwork that is stored in folders, which are in turn, stored in filing cabinets. For each person and business, someone had to design a system to fit their needs, a system that would allow information to be accessed as needed.

A personalized filing system provides great advantages when used by someone who understands how the system works, but when someone new needs to access the system, how do they know where to find the information they need? Suddenly, the personalized filing system becomes less convenient. Applications face similar challenges in organizing data: what information is most important and how can developers ensure that it is easily accessible?

The *OPC* specification provides an answer to this question. A package, as described in the *OPC*, enables different applications to access key information from an OPC based file in a standardized and predictable way. A package is like a filing cabinet whose basic organization is known to all the people and businesses that interact with it.

## What are the Open Packaging Conventions (OPC)?

The Open Packaging Conventions (*OPC*) describes a new file technology that is documented in the ISO/IEC 29500 and ECMA 376 standards. Rather than a specific file format, *OPC* is a file technology for designing file formats with a shared, base architecture.

The *OPC* integrates elements of Zip, XML, and the Web technologies into an open, industry standard that makes it easier to organize, store, and transport application data.

*OPC* is the file technology base for many new formats supported by Microsoft products and a growing number of other new Microsoft and third-party applications. While these formats share *OPC* as a foundation, the data contained in a package file depends on the specific format.

## Packages

A package is an aggregate of data components, like the filing cabinet (which is shown in the following illustration) is an aggregate of an individual or business's paperwork.

![illustration showing a generic filing cabinet](../images/closed-cabinet.png)

Unlike real world filing systems, packages must conform to a predictable, conceptual organizational system (called the logical model), and predicatable physical characteristics (called the physical model). These standardized conformance requirements are described in the *OPC*.

### Logical Model

The logical model describes a package as an aggregate of data structured as a directed graph. A generic directed graph is shown in the following diagram.

![illustration showing a generic directed graph with 5 circles: 1 points to 3, 2 points to 1 and 4, 3 points to 1 and 4, and 4 and 5 point to nothing](../images/directed-graph.png)

The vertices of a package graph are all URI-addressable resources, and the edges are links between those resources. The links of a package graph are relationships. In a package graph, the two resources connected by a relationship are known as the source and target of the relationship; in a generic graph, these would be known as the initial and terminal vertices, respectively.

The resource that is a source must be either the package itself or a data component (called a part) inside of the package. The target resource of a relationship can be any URI-addressable resource inside or outside of the package.

This model provides a format-independent way of structuring and accessing package data.

### Physical Model

While the logical model describes the data structure of a package in the abstract, the physical model maps those logical concepts to a physical format. The result of this mapping is a physical package format. For example, the OPC provides a mapping of package concepts to the ZIP archive format; parts are treated as file items and appear in a directory-like hierarchy that is derived from part names. The result of this mapping is the physical, ZIP-based package format. To view the physical organization of any ZIP-based package, append the .zip extension to the package file name and open the archive using Windows Explorer or a ZIP utility. The following screen shot illustrates an XPS file that was opened for browsing:

![screen shot showing an xps file that was opened for browsing, with a folders view in the left pane, and three folders and two files in the right pane](../images/browse-package.png)

Any individual or organization can design a physical package format by mapping logical package concepts to a desired physical format. As a result, package format designers can design and optimize a physical format for the specific needs of an application without compromising the logical structure of the package.

Currently, nearly all package formats are based on ZIP archives.

### Existing ZIP-Based Package Formats

Examples of ZIP-based package formats include:


    -   Office Word 2007 documents (.docx)
    -   Office Excel 2007 worksheets (.xlsx)
    -   Office PowerPoint 2007 presentations (.pptx)
-   XPS documents (.xps)

## Parts

In the analogy of a package to a real world filing system, the parts in a package are like the folders in a filing cabinet. Parts store application data, like folders (which are shown in the following illustration) store personal or business information.

![illustration showing a generic, empty file-folder](../images/folder-empty.png)

To further extend the analogy, the content of a part is data in the form of a byte stream like the content of a folder is information in the form of paperwork, as shown in the following illustration.

![illustration showing a generic file-folder that contains information in the form of paperwork](../images/folder-full.png)

In the logical model of a package, parts are resources that are URI-addressable data components inside a package. A part consists of a byte stream of data and properties. The properties are specified in the *OPC*. The part's content type property uses a MIME-style media type to describe part content. The content types for parts are identified in a package-specific stream, called the Content Types stream. This stream contains XML markup that maps parts and extensions to content types. This XML markup is specified by the package format designer or in the *OPC*.

Parts also have the part name property: the URI of the part, relative to the root of the package. However, the part name depends on the physical mapping of the package format and, therefore, cannot be predicted reliably from one package format to another. A part that exists in more than one package format may not have the same part name in different package files. To find the current part name of a part in the current package, regardless of the package format, identify a relationship that targets the part and use the relationship to resolve the current part name.

For more information about parts and about finding their current part names, see the [Parts Overview](parts-overview.md) and the [Finding the Core Properties Part](finding-the-core-properties-part.md) how-to topic.

## Relationships

In the analogy of a package to a real world filing system, relationships can be used to navigate a package like information on a directory card can be used to navigate a filing system.

In the logical model of a package, relationships are the links that connect a source to a target. While the source is either the package or a part, the target can be any URI-addressable resource inside or outside of the package.

If the relationship target is inside the package, the targeted resource is a part in the package. If the target is outside of the package, the targeted resource can be any URI-addressable resource.

Only two kinds of resources can be the source of a relationship: the package itself and a part. If the source is the package, the relationship is called a package relationship; if the source is a part, the relationship is called a part relationship.

The relationship's properties provide access to the type of the relationship (the relationship type), target mode, and the relative URI of its target. The relationship type describes the connection between the relationship source and target. Relationship types are specified by the package format designer or in the OPC. The target mode of a relationship indicates whether its target is inside or outside of the package; if inside, the target is a part. The relative URI of a relationship target uses the URI of the source as its base.

If the target of a relationship is a part, the relative URI of the target can be resolved to its part name. For an example, see [Resolving a Part Name from a Target URI](resolving-a-part-name-from-a-relationship-s-target-uri.md). The resolution of a part name from the URI of a relationship's target is not contingent on the physical mapping of the package.

Relationships are serialized by using specialized XML markup, called relationship markup. An example of a serialized relationship is shown in the following markup.


```XML
<Relationship Id="rId1"
    Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"
    Target="word/document.xml" />
```



### Storing Relationships: Relationships Parts

Relationships are stored in a specialized part, called a Relationships part. There is one Relationships part for each distinct relationship source in a package. All relationships that have the same source are stored in the same Relationships part.

The part name of a Relationships part is derived from the source URI of the relationships that are stored in the part. The part content of a Relationships part is the relationship markup, which is the serialized form of the stored relationships.

## Digital Signatures

In a package, a digital signature (signature) can be validated, confirming that the signed contents of the package have not been modified since the signature was generated.

> \[!Important\]  
> Although signatures can be used to validate the identity of the package signer and originator, this must be performed by the package consumer.

 

A package signature can reference package components that have been signed. These components include XML markup that has been signed in application-specific **Object** elements. The signature can also include certificates (or links to them), which may be used in signature validation.

A package can have more than one signature, and each signature can reference any package component or application-specific content in an **Object** element that exists inside the signature markup.

The following table describes common package signature concepts. 

| Signature concepts                    | Description                                                                                                                                                                                   |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| signature                             | A package digital signature. A digital signature generated for a package.<br/>                                                                                                          |
| reference to a part                   | A reference to one part that has been signed. <br/>                                                                                                                                     |
| reference to relationships            | A reference to one or more relationships that have been signed and that are all stored in the same Relationships part. <br/>                                                            |
| reference to application data         | A reference to application-specific data that has been signed and is contained in a specified object. <br/>                                                                             |
| object that contains application data | An application-specific object that contains application data that may be signed when the signature is generated. This object is serialized as an element in the signature markup.<br/> |
| certificate                           | An X.509 certificate that is included when the signature is created and can be used in signature validation.<br/>                                                                       |



 

For more information about digital signatures, see the W3C recommendation [XML Signature Syntax and Processing](http://go.microsoft.com/fwlink/p/?linkid=132847) (http://go.microsoft.com/fwlink/p/?linkid=132847).

## Related topics

<dl> <dt>

[Packaging API Programming Guide](packaging-programming-guide.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[Getting Started with the Packaging API](packaging-api-overview.md)
</dt> <dt>

**External**
</dt> <dt>

[ECMA-376 OpenXML](http://go.microsoft.com/fwlink/p/?linkid=123375)
</dt> </dl>

 

 





