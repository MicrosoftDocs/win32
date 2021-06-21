---
description: Contains location and bounding information for the note Title, if present.
ms.assetid: b193f6c2-5f26-41f9-acc8-d734c426b069
title: TitleArea Element
ms.topic: reference
ms.date: 05/31/2018
---

# TitleArea Element

Contains location and bounding information for the note Title, if present.

## Definition

``` syntax
<xs:element name="TitleArea" type="TitleAreaType" minOccurs="0" />
```

## Parent Elements

[**Title**](title-element.md)

## Child Elements

None.

## Attributes



| Attribute  | Type                      | Required | Description                                                                             | Possible Values           |
|------------|---------------------------|----------|-----------------------------------------------------------------------------------------|---------------------------|
| **Left**   | **xs:integer**            | Required | The distance from the origin to the leftmost point in the bounding box for the element. | Any integer.              |
| **Top**    | **xs:integer**            | Required | The distance from the origin to the topmost point in the bounding box for the element.  | Any integer.              |
| **Width**  | **xs:nonNegativeInteger** | Required | The width of the bounding box for the element.                                          | Any non-negative integer. |
| **Height** | **xs:nonNegativeInteger** | Required | The height of the bounding box for the element.                                         | Any non-negative integer. |



 

## Element Information



|   Element    | Value                                                           |
|--------------|-----------------------------------------------------------------|
| Element type | [**TitleAreaType**](titleareatype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink                      |
| Schema name  | Journal Reader                                                  |



 

 

 



