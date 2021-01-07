---
description: Contains the details about an individual page in a Journal note.
ms.assetid: 8cada667-188b-42f9-8602-34e23d512b82
title: JournalPage Element
ms.topic: reference
ms.date: 05/31/2018
---

# JournalPage Element

Contains the details about an individual page in a Journal note.

## Definition

``` syntax
<xs:element name="JournalPage" type="JournalPageType" maxOccurs="unbounded" />
```

## Parent Elements

[**JournalDocument**](journaldocument-element.md)

## Child Elements

[**Stationary**](stationery-element.md)

[**DocImage**](docimage-element.md)

[**TitleInfo**](titleinfo-element.md)

[**Content**](content-element--journal-reader.md)

## Attributes



| Attribute      | Type                      | Required | Description                                                                        | Possible Values                                          |
|----------------|---------------------------|----------|------------------------------------------------------------------------------------|----------------------------------------------------------|
| **Number**     | **xs:nonNegativeInteger** | Required | The ordinal number of the page within the Journal document, starting with one (1). | Any non-negative integer.                                |
| **Width**      | **xs:nonNegativeInteger** | Required | The width of the page.                                                             | Any non-negative integer.                                |
| **Height**     | **xs:nonNegativeInteger** | Required | The height of the page.                                                            | Any non-negative integer.                                |
| **LineHeight** | **xs:nonNegativeInteger** | Optional | The height of the line used on the page.                                           | Any non-negative integer.                                |
| **LanguageId** | **xs:nonNegativeInteger** | Optional | The language id used for the page.                                                 | A non-negative integer representing a valid language id. |



 

## Element Information



|              |                                                                     |
|--------------|---------------------------------------------------------------------|
| Element type | [**JournalPageType**](journalpagetype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink                          |
| Schema name  | Journal Reader                                                      |



 

 

 



