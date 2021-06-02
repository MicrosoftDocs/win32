---
description: Contains encoded binary data for an image in the Journal document, if present.
ms.assetid: 'fbb86bef-68f7-4aad-8a98-1c68e79ea2de'
title: Image Element
ms.topic: article
ms.date: 05/31/2018
---

# Image Element

Contains encoded binary data for an image in the Journal document, if present.

## Definition

``` syntax
 Copy Code<xs:element name="Image" type="ImageType" />
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



|              |                                                         |
|--------------|---------------------------------------------------------|
| Element type | [**ImageType**](imagetype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink              |
| Schema name  | Journal Reader                                          |



 

## See also

<dl> <dt>

[**Background**](background-element.md)
</dt> </dl>

 

 



