---
description: Contains text information from the Journal note.
ms.assetid: 09ec2e8a-bd50-4f82-8ce3-a1c61f48ddb7
title: Text Element
ms.topic: reference
ms.date: 05/31/2018
---

# Text Element

Contains text information from the Journal note.

## Definition

When used with [**Content**](content-element--journal-reader.md):

``` syntax
<xs:element name="Text" type="TextType" />
```

Or, when used with [**TitleInfo**](titleinfo-element.md) and [**GroupNode**](groupnode-element.md):

``` syntax
<xs:element name="Text" type="xs:string" />
```

## Parent Elements

[**Content**](content-element--journal-reader.md)

[**GroupNode**](groupnode-element.md)

[**TitleInfo**](titleinfo-element.md)

## Child Elements

None.

## Attributes

There are no attributes when used with [**TitleInfo**](titleinfo-element.md) and [**GroupNode**](groupnode-element.md). When used with[**Content**](content-element--journal-reader.md), the attributes are as follows.



| Attribute  | Type                      | Required | Description                                                                             | Possible Values           |
|------------|---------------------------|----------|-----------------------------------------------------------------------------------------|---------------------------|
| **Left**   | **xs:integer**            | Required | The distance from the origin to the leftmost point in the bounding box for the element. | Any integer.              |
| **Top**    | **xs:integer**            | Required | The distance from the origin to the topmost point in the bounding box for the element.  | Any integer.              |
| **Width**  | **xs:nonNegativeInteger** | Required | The width of the bounding box for the element.                                          | Any non-negative integer. |
| **Height** | **xs:nonNegativeInteger** | Required | The height of the bounding box for the element.                                         | Any non-negative integer. |



 

## Element Information



|   Element           |   Value                                |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Element type | [**TextType**](texttype-complex-type.md) complexType (with the Content element) or **xs:string** (with [**GroupNode**](groupnode-element.md) and [**TitleInfo**](titleinfo-element.md) elements) |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink<br/>                                                                                                                                               |
| Schema name  | Journal Reader<br/>                                                                                                                                                                           |



 

 

 




