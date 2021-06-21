---
description: Contains a set of elements&\#8212;Paragraph, InkWord, Drawing, Text, Image, or Flag&\#8212;that are grouped together in the Journal note.
ms.assetid: 59ee3037-7178-41c8-84d5-d5c68fa2cf9b
title: GroupNode Element
ms.topic: reference
ms.date: 05/31/2018
---

# GroupNode Element

Contains a set of elements—[**Paragraph**](paragraph-element.md), [**InkWord**](inkword-element.md), [**Drawing**](drawing-element.md), [**Text**](text-element.md), [**Image**](image-element.md), or [**Flag**](flag-element.md)—that are grouped together in the Journal note.

## Definition

``` syntax
<xs:element name="GroupNode" type="GroupNodeType" />
```

## Parent Elements

[**Content**](content-element--journal-reader.md)

## Child Elements

[**Paragraph**](paragraph-element.md)

[**InkWord**](inkword-element.md)

[**Drawing**](drawing-element.md)

[**Text**](text-element.md)

[**Image**](docimage-element.md)

[**Flag**](flag-element.md)

## Attributes



| Attribute  | Type                      | Required | Description                                                                             | Possible Values           |
|------------|---------------------------|----------|-----------------------------------------------------------------------------------------|---------------------------|
| **Left**   | **xs:integer**            | Required | The distance from the origin to the leftmost point in the bounding box for the element. | Any integer.              |
| **Top**    | **xs:integer**            | Required | The distance from the origin to the topmost point in the bounding box for the element.  | Any integer.              |
| **Width**  | **xs:nonNegativeInteger** | Required | The width of the bounding box for the element.                                          | Any non-negative integer. |
| **Height** | **xs:nonNegativeInteger** | Required | The height of the bounding box for the element.                                         | Any non-negative integer. |



 

## Element Information



|  Element     | Value                                                     |
|--------------|-----------------------------------------------------------------|
| Element type | [**GroupNodeType**](groupnodetype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink                      |
| Schema name  | Journal Reader                                                  |



 

 

 



