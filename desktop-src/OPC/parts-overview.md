---
title: Parts Overview
description: This topic describes the basics of using Packaging APIs to interact with parts.
ms.assetid: 95da581d-3d30-4cd7-bd20-f44bf505ac0a
keywords:
- Packaging APIs,parts
- packaging,parts
- packages,parts
- parts,about
- parts,objects
- parts,physical model
- physical model
- parts,finding
- parts,relationship types
- relationships,parts
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Parts Overview

This topic describes the basics of using Packaging APIs to interact with parts.

This topic contains the following sections.

-   [Introduction](#introduction)
-   [Prerequisites](#prerequisites)
-   [Part Objects](#part-objects)
-   [Mapping Parts to a Physical Model](#mapping-parts-to-a-physical-model)
-   [Finding a Part by Relationship Type](#finding-a-part-by-relationship-type)
    -   [Why use a relationship type?](#why-use-a-relationship-type)
    -   [Procedure for Finding a Part](#procedure-for-finding-a-part)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## Introduction

In the analogy of a package to a real world filing system, the parts in a package are like the folders in a filing cabinet. Parts store application data, like folders store personal or business information. To further extend the analogy, the content of a part is data in the form of a byte stream like the content of a folder is information in the form of paperwork.

In the logical model of a package, parts are resources that are URI-addressable data components inside a package. A part consists of a byte stream of data and properties which are specified in the *ECMA-376 OpenXML, 1st Edition, Part 2: Open Packaging Conventions (OPC)*.

To interact with a specific part, the caller uses the Packaging APIs to get a pointer to a part object that represents the part (a conceptual file-folder). All interactions are performed using this part object.

## Prerequisites

For a table of prerequisites, see [Packaging](packaging.md).

## Part Objects

Windows 7 provides the part object implementation of the [**IOpcPart**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcpart) interface.

A part object is instantiated to represent a part. The object is created by calling the [**IOpcPartSet::CreatePart**](/previous-versions/windows/desktop/api/msopc/nf-msopc-iopcpartset-createpart) method and accessed by calling the [**IOpcPartSet::GetPart**](/previous-versions/windows/desktop/api/msopc/nf-msopc-iopcpartset-getpart) or [**IOpcPartEnumerator::GetCurrent**](/previous-versions/windows/desktop/api/msopc/nf-msopc-iopcpartenumerator-getcurrent) method.

A part object is contained in a part set object that implements the [**IOpcPartSet**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcpartset) interface. This set can be retrieved by calling the [**IOpcPackage::GetPartSet**](/previous-versions/windows/desktop/api/msopc/nf-msopc-iopcpackage-getpartset) method, and it represents all the parts that are not Relationships parts in a package. In addition to providing support for creating part objects, the set also provides support for deleting part objects and for getting an enumerator of the part objects contained in the set. For more information about part set objects, see the **IOpcPartSet** topic.

A pointer to the [**IOpcPart**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcpart) interface of a part object provides access to part information and an [**IOpcRelationshipSet**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcrelationshipset) interface. An **IOpcPart** provides access to part information through methods that allow access to the following properties: content, content type, name, and compression option. These properties are listed in the table that follows.

| Property     | Description                                                                          |
|--------------|--------------------------------------------------------------------------------------|
| content      | The stream of bytes that makes up a part, as it is defined in the *OPC*. <br/> |
| content type | The media type, specified by the format designer, of part content. <br/>       |
| name         | The URI to a part in the package, relative to the package root.<br/>           |
| compression  | The degree to which the part content is compressed. <br/>                      |



 

The part name is represented by a part URI object, which implements the [**IOpcPartUri**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcparturi) interface. The following diagram shows a part object and the part URI and relationship set objects that can be retrieved from it.

![illustration showing a part object and the part uri and relationship set objects that can be retrieved from it](https://www.bing.com/search?q=illustration showing a part object and the part uri and relationship set objects that can be retrieved from it)

The relationship set object retrieved with the [**IOpcPart::GetRelationshipSet**](/previous-versions/windows/desktop/api/msopc/nf-msopc-iopcpart-getrelationshipset) represents the Relationships part that stores relationships that have the current part as their source. The object is an unordered set of [**IOpcRelationship**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcrelationship) interface pointers to relationship objects. Each relationship object represents one part relationship. For more information about relationship objects, see the [Relationships Overview](relationships-overview.md) topic.

## Mapping Parts to a Physical Model

In the logical model of a package, parts are data components that are URI-addressable resources inside the package. When a package format is designed, the package format designer defines how parts are mapped to physical features of the physical format. How a part is mapped can influence the part name. For example, in a ZIP-based physical package, parts map to ZIP file items and part names map to the path of the part, which is relative to the root of the ZIP archive.

## Finding a Part by Relationship Type

To find a part in a package, use a relationship type to identify a relationship that targets the part. Then, resolve the part name from the relationship target's URI and retrieve the part.

### Why use a relationship type?

The part name is closely tied with the package format in use. This name varies according to how the logical package model is mapped to a physical format. Mapping allows package format designers to optimize the package format to the necessary software. As a side effect, the part name is unpredictable from one package to another. For this reason, a part is found by first identifying a relationship, which is a logical link to the part, and then resolving the name of the part to be found in the current package.

Relationship information is tracked with several properties, which are represented as attributes in the following example of a **Relationship** element. The relationship identifier property (the **Id** attribute) is arbitrary and local to a Relationships part. The target URI property (the **Target** attribute) is a relative URI to the target part and is not known before a relationship is identified. The relationship type property (the **Type** attribute), however, is defined by the package format designer or in the OPC and is, therefore, known and predictable across a package format.

The following code shows example markup for a relationship, including the relationship identifier, target URI, and relationship type properties.

> [!Note]  
> The example uses the default **TargetMode**: "Internal".

 


```XML
                <Relationship
                Id="rId1"
                Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"
                Target="word/document.xml" />
              
```



### Procedure for Finding a Part

Use the following steps to find a part by using a relationship type.

For an example of how an application can use a relationship type to find a part, see the [Finding the Core Properties Part](finding-the-core-properties-part.md) topics or the [Set Author Sample](set-author-sample.md).

1.  Identify and define a constant for the relationship type and, if required, for the content type of the part to be found. For definitions and requirements for the relationship type and content type, see the specification provided by the package format designer or the OPC.

    The content type can be used to ensure that part content is the expected content type, which is described in the package-format specification or the OPC.

2.  Access the package where the part to be found is stored.

3.  Find the part.

    1.  Get the Relationships part that contains relationships that target the part.

        -   If the part is targeted by a package relationship, identify the Relationships part that stores all package relationships.

        -   If the part is targeted by a part relationship, identify the Relationships part that stores a part relationship that targets the part.

    2.  Identify the relationships of the specified relationship type in the set.

        > \[!Important\]  
        > If the package format designer describes an expected number of relationships of the specified relationship type that can be stored in a Relationships part, check that the number of relationships retrieved conforms to that expectation. For information about the expected number of relationships for a specified relationship type, see the specification provided by the package format designer or the OPC.

         

4.  To find the part, iterate through relationships of the specified relationship type.

    1.  If the target of a retrieved relationship is a part, resolve the part name against the URI of the relationship's source.

        For an example of how to resolve a part name from the URI targeted by a relationship, see [Resolving a Part Name from a Target URI](resolving-a-part-name-from-a-relationship-s-target-uri.md).

    2.  Ensure that a part with the resolved part name exists in the package.

    3.  Get the part.

    4.  If an expected content type is defined for the part by the package designer or the OPC, ensure that the part has the correct content type. If the part has the expected content type, or if no expected content type is defined, the part has been found.

## Additional Resources

While not required to use the Packaging API, knowledge of the following technologies will advance your understanding of the Packaging API.



| Technology                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Markup Compatibility requirements in the [ECMA-376 OpenXML](http://go.microsoft.com/fwlink/p/?linkid=123375) standard | If your application interacts with packages that comply with different editions of the OPC, familiarity with markup compatibility requirements will be helpful in developing your application. For more information, see 1st edition, Part 5: Markup Compatibility in the [ECMA-376 OpenXML](http://go.microsoft.com/fwlink/p/?linkid=123375) (http://go.microsoft.com/fwlink/p/?linkid=123375).<br/> |



 

## Related topics

<dl> <dt>

[Parts Fundamentals](parts.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[Open Packaging Conventions Fundamentals](open-packaging-conventions-overview.md)
</dt> <dt>

[Parts How-To Topics](parts-how-to-topics.md)
</dt> <dt>

[Getting Started with the Packaging API](packaging-api-overview.md)
</dt> <dt>

**Reference**
</dt> <dt>

[Packaging API Reference](packaging-programming-reference.md)
</dt> <dt>

[Packaging API Samples](packaging-programming-samples.md)
</dt> <dt>

**External**
</dt> <dt>

[ECMA-376 OpenXML](http://go.microsoft.com/fwlink/p/?linkid=123375)
</dt> </dl>

 

 





