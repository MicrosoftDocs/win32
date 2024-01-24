---
description: Contains a base64 encoded bitmap of a flag associated with section of a Journal note.
ms.assetid: 612f8814-ab3c-4a3e-9791-525788d4cc72
title: Flag Element
ms.topic: reference
ms.date: 05/31/2018
---

# Flag Element

Contains a base64 encoded bitmap of a flag associated with section of a Journal note.

## Definition

``` syntax
<xs:element name="Flag" type="FlagType" minOccurs="0" maxOccurs="unbounded" />
```

## Parent Elements

[**Content**](content-element--journal-reader.md)

[**GroupNode**](groupnode-element.md)

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



|  Element     | Value                                                     |
|--------------|-------------------------------------------------------|
| Element type | [**FlagType**](flagtype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink            |
| Schema name  | Journal Reader                                        |



 

 

 



