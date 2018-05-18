---
title: Relationships Overview
description: This topic describes the basics of using Packaging APIs to interact with relationships, which are directional associations.
ms.assetid: '8e071847-7eb2-4528-8402-4aaa1f5cd216'
keywords: ["Packaging APIs,relationships", "packaging,relationships", "packages,relationships", "relationships,about", "relationships,objects", "parts,relationships"]
---

# Relationships Overview

This topic describes the basics of using Packaging APIs to interact with relationships, which are directional associations.

This topic contains the following sections.

-   [Introduction](#introduction)
-   [Prerequisites](#prerequisites)
-   [Relationship Objects](#relationship-objects)
-   [Relationship Set Objects](#relationship-set-objects)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## Introduction

In the analogy of a package to a real–world filing system, relationships can be used to navigate a package like information on a directory card can be used to navigate a filing system.

In the logical model of a package, relationships are the links that connect a source to a target. While the source is either the package or a part, the target can be any URI-addressable resource inside or outside of the package.

If the relationship target is inside the package, the targeted resource is a part in the package. If the target is outside of the package, the targeted resource can be any URI-addressable resource.

## Prerequisites

For a table of prerequisites, see [Packaging](packaging.md).

## Relationship Objects

Windows 7 provides the relationship object implementation of the [**IOpcRelationship**](iopcrelationship.md) interface.

A relationship object is instantiated to represent a relationship. The object is created by calling the [**IOpcRelationshipSet::CreateRelationship**](iopcrelationshipset-createrelationship.md) method and accessed by calling the [**IOpcRelationshipSet::GetRelationship**](iopcrelationshipset-getrelationship.md) or [**IOpcRelationshipEnumerator::GetCurrent**](iopcrelationshipenumerator-getcurrent.md) method.

Relationship objects are contained in a relationship set object, which represents the Relationships part where all relationships that have the same source are stored. For more information about relationship set objects, see the [Relationship Set Objects](#relationship-set-objects) section and the [**IOpcRelationshipSet**](iopcrelationshipset.md) topic.

A pointer to the [**IOpcRelationship**](iopcrelationship.md) interface of a relationship object provides to relationship information through methods that enable access to the following properties: relationship identifier, relationship type, source URI, target resource URI, and target mode. These properties are listed in the following table.

| Property                | Description                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| relationship identifier | The unique identifier of the relationship. <br/>                                                                              |
| relationship type       | The qualified name of the relationship as defined by the package designer.<br/>                                               |
| source URI              | The URI of the source of the relationship. The source URI is either the URI of the package or of a part in the package. <br/> |
| target URI              | The URI of the target resource of the relationship. <br/>                                                                     |
| target mode             | A value that indicates whether the target resource is internal or external to the package. <br/>                              |



 

The URI of the relationship source is represented by an OPC URI object, which implements the [**IOpcUri**](iopcuri.md) interface. The relative URI of the relationship target is represented by an implementation of the [IUri](http://go.microsoft.com/fwlink/p/?linkid=116163) interface. The following diagram shows a relationship object, the OPC URI object of the source, and the URI of the target URI that are retrieved from the relationship object.

![illustration showing a relationship object, the opc uri object, and the uri that can be retrieved from it](../images/relationship-object.png)

## Relationship Set Objects

Windows 7 provides the relationship set object implementation of the [**IOpcRelationshipSet**](iopcrelationshipset.md) interface.

A relationship set object represents a Relationships part that stores all relationships that have the same source. These set objects can be accessed by calling either the [**IOpcPackage::GetRelationshipSet**](iopcpackage-getrelationshipset.md) or [**IOpcPart::GetRelationshipSet**](iopcpart-getrelationshipset.md) method. If the set is retrieved using **IOpcPackage::GetRelationshipSet**, it represents the Relationships part that stores package relationships. If it is retrieved using **IOpcPart::GetRelationshipSet**, the set represents the Relationships part that stores part relationships that have the same source.

A pointer to the [**IOpcRelationshipSet**](iopcrelationshipset.md) interface of a relationship set object provides access to relationship objects that represent the relationships stored in the corresponding Relationships part, and a part content stream of the relationship markup that defines the relationships in the Relationships part.

The [**IOpcRelationshipSet**](iopcrelationshipset.md) interface provides methods to create, delete, and get enumerators for the relationship objects contained in the set.

## Additional Resources

While not required to use the Packaging API, knowledge of the following technologies will advance your understanding of the Packaging API.



| Technology                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Markup Compatibility requirements in the [ECMA-376 OpenXML](http://go.microsoft.com/fwlink/p/?linkid=123375) standard | If your application interacts with packages that comply with different editions of the ECMA-376 OpenXML, 1st Edition, Part 2: Open Packaging Conventions (OPC), familiarity with markup compatibility requirements will be helpful in developing your application. For more information, see 1st edition, Part 5: Markup Compatibility in the [ECMA-376 OpenXML](http://go.microsoft.com/fwlink/p/?linkid=123375) (http://go.microsoft.com/fwlink/p/?linkid=123375).<br/> |



 

## Related topics

<dl> <dt>

[Relationships Fundamentals](relationships.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[Getting Started with the Packaging API](packaging-api-overview.md)
</dt> <dt>

[Open Packaging Conventions Fundamentals](open-packaging-conventions-overview.md)
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

 

 





