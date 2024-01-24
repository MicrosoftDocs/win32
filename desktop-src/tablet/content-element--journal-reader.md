---
description: Contains the content for a Journal page.
ms.assetid: 1df78a17-1cd4-4e98-aed1-b09d2b357703
title: Content Element [Journal Reader]
ms.topic: reference
ms.date: 05/31/2018
---

# Content Element \[Journal Reader\]

Contains the content for a Journal page.

## Definition

``` syntax
<xs:element name="Content" type="ContentType" minOccurs="0" maxOccurs="unbounded" />
```

## Parent Elements

[**JournalPage**](journalpage-element.md)

## Child Elements

[**GroupNode**](groupnode-element.md)

[**Paragraph**](paragraph-element.md)

[**Drawing**](drawing-element.md)

[**Text**](text-element.md)

[**Image**](image-element.md)

[**Flag**](flag-element.md)

## Attributes




| Attribute | Type | Required | Description | PossibleValues | 
|-----------|------|----------|-------------|----------------|
| <strong>Type</strong> | <a href="contenttype-complex-type.md"><strong>ContentType complexType</strong></a> | Required | If the type is "Inert", then the content cannot be modified.<br /> | <ul><li>Normal</li><li>Inert</li></ul> | 




 

## Element Information



|  Element     | Value                                                     |
|--------------|-------------------------------------------------------------|
| Element type | [**ContentType**](contenttype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink                  |
| Schema name  | Journal Reader                                              |



 

 

 




