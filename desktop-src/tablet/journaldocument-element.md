---
description: The top-level element in a Journal note XML file.
ms.assetid: 3887667c-67a7-416a-b94d-c30bb02a7985
title: JournalDocument Element
ms.topic: reference
ms.date: 05/31/2018
---

# JournalDocument Element

The top-level element in a Journal note XML file.

## Definition

``` syntax
<xs:element name="JournalDocument">
  <xs:complexType>
   <xs:sequence>
    <xs:element name="Stationery" type="StationeryType" minOccurs="0" maxOccurs="unbounded" />
    <xs:element name="JournalPage" type="JournalPageType" maxOccurs="unbounded" />
   </xs:sequence>
   <xs:attribute name="Version" type="xs:string" use="required" fixed="1.0" />
   <xs:attribute name="DefaultPageWidth" type="xs:nonNegativeInteger" use="required" />
   <xs:attribute name="DefaultPageHeight" type="xs:nonNegativeInteger" use="required" />
  </xs:complexType>
</xs:element>/>
```

## Parent Elements

None.

## Child Elements

[**Stationery**](stationery-element.md)

[**JournalPage**](journalpage-element.md)

## Attributes



| Attribute             | Type                      | Required | Description                                                      | Possible Values           |
|-----------------------|---------------------------|----------|------------------------------------------------------------------|---------------------------|
| **Version**           | **xs:string**             | Required | The version of the Journal document represented in the XML file. | 1.0                       |
| **DefaultPageWidth**  | **xs:nonNegativeInteger** | Required | The default width of the page for the Journal document.          | Any non-negative integer. |
| **DefaultPageHeight** | **xs:nonNegativeInteger** | Required | The default height of the page for the Journal document.         | Any non-negative integer. |



 

## Element Information



|  Element     | Value                                                     |
|--------------|--------------------------------------------|
| Element type | **JournalDocument**                        |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink |
| Schema name  | Journal Reader                             |



 

 

 



