---
description: The optional <dateCreated> element identifies the date and the time when this search connector was created, using the ISO 8601 standard. It has no child elements and no attributes.
ms.assetid: 96d8b067-b5ab-4d36-a8d7-1d084a9f661d
title: dateCreated Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# dateCreated Element (Search Connector Schema)

The optional <dateCreated> element identifies the date and the time when this search connector was created, using the ISO 8601 standard. It has no child elements and no attributes.

## Syntax


```
<!-- dateCreated -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="dateCreated" type="xs:dateTime" minOccurs="0"/>
            ...
        </xs:all>
        <xs:attribute name="publisher" type="xs:string"/>
        <xs:attribute name="product" type="xs:string"/>
    </xs:complexType>
```



## Element Information



| Parent Element                                                                                                   | Child Elements |
|------------------------------------------------------------------------------------------------------------------|----------------|
| [searchConnectorDescriptionType Element (Search Connector Schema)](search-schema-searchconnectordescription.md) |                |



 

## Remarks

The format of the value of this element follows the ISO 8601 standard. A common use would be either of the following:

-   \[YYYY\]-\[MM\]-\[DD\]T\[hh\]:\[mm\]:\[ss\]±\[hh\]:\[mm\] ("1981-04-05T14:30:30-05:00")
-   \[YYYY\]\[MM\]\[DD\]T\[hh\]\[mm\]\[ss\]Z ("19810405T193030Z")

## Example


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="https://schemas.adventureworks.com/searchConnector">
    ...
    <dateCreated>2009-04-05T12:00:00-05:00</dateCreated>
    ...
</searchConnectionDescription>
```



 

 



