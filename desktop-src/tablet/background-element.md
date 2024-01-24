---
description: Contains the background for a JournalDocument element or JournalPage element.
ms.assetid: 48527c4e-50fb-4800-ac87-1646234783ba
title: Background Element
ms.topic: reference
ms.date: 05/31/2018
---

# Background Element

Contains the background for a [**JournalDocument**](journaldocument-element.md) element or [**JournalPage**](journalpage-element.md) element.

## Definition

``` syntax
<xs:element name="Background" type="BackgroundType" minOccurs="0" />
```

## Parent Elements

[**Stationery**](stationery-element.md)

## Child Elements

[**Image**](image-element.md)

## Attributes




| Attribute | Type | Required | Description | Possible Values | 
|-----------|------|----------|-------------|-----------------|
| <strong>Style</strong> | <strong>xs:string</strong> | Required | Specifies the style of the background. | <ul><li>None</li><li>Solid</li></ul> | 
| <strong>Color</strong> | <a href="colortype-simple-type.md"><strong>ColorType</strong></a> simpleType | Optional | Specifies the color of the background. | See <a href="colortype-simple-type.md"><strong>ColorType</strong></a> simpleType. | 




 

## Element Information



|                  | Value                                                             |
|------------------|-------------------------------------------------------------------|
| **Element type** | [**BackgroundType**](backgroundtype-complex-type.md) complexType |
| **Namespace**    | urn:schemas-microsoft-com:tabletpc:richink                        |
| **Schema name**  | Journal Reader                                                    |



 

 

 



