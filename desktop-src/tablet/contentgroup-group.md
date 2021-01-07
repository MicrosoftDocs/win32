---
description: Defines a group that contains a set of grouped content in a Journal note.
ms.assetid: e2561be1-03ce-41f7-9ad4-197d75411c48
title: ContentGroup Group
ms.topic: reference
ms.date: 05/31/2018
---

# ContentGroup Group

Defines a group that contains a set of grouped content in a Journal note.

## Definition

``` syntax
<xs:group name="ContentGroup" >
  <xs:choice>
    <xs:element name="GroupNode" type="GroupNodeType" />
    <xs:element name="Paragraph" type="ParagraphType" />
    <xs:element name="InkWord" type="InkWordType" />
    <xs:element name="Drawing" type="DrawingType" />
    <xs:element name="Text" type="TextType" />
    <xs:element name="Image" type="ImageType" />
    <xs:element name="Flag" type="FlagType" />
    <xs:element name="Reflow" type="ReflowType" />
  </xs:choice>
</xs:group>
```

## Child Elements

[**GroupNode**](groupnode-element.md)

[**Paragraph**](paragraph-element.md)

[**InkWord**](inkword-element.md)

[**Drawing**](drawing-element.md)

[**Text**](text-element.md)

[**Image**](docimage-element.md)

[**Flag**](flag-element.md)

## Attributes



| Attribute  | Type                      | Required | Description                                                                                        | PossibleValues                       |
|------------|---------------------------|----------|----------------------------------------------------------------------------------------------------|--------------------------------------|
| **Left**   | **xs:integer**            | Required | The distance from the origin to the leftmost point in the bounding box for the element.<br/> | Any integer.<br/>              |
| **Top**    | **xs:integer**            | Required | The distance from the origin to the topmost point in the bounding box for the element.<br/>  | Any integer.<br/>              |
| **Width**  | **xs:nonNegativeInteger** | Required | The width of the bounding box for the element.<br/>                                          | Any non-negative integer.<br/> |
| **Height** | **xs:nonNegativeInteger** | Required | The height of the bounding box for the element.<br/>                                         | Any non-negative integer.<br/> |



 

## Type Information



|             |                                            |
|-------------|--------------------------------------------|
| Namespace   | urn:schemas-microsoft-com:tabletpc:richink |
| Schema name | Journal Reader                             |



 

 

 




