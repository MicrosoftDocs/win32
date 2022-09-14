---
description: The &lt;propertyStore&gt; element specifies a set of one or more properties used by this library. This element is optional and has no attributes.
ms.assetid: 19532C1F-686F-4c14-8BA8-0043E77BE594
title: propertyStore Element (Library Schema)
ms.topic: article
ms.date: 05/31/2018
---

# propertyStore Element (Library Schema)

The &lt;propertyStore&gt; element specifies a set of one or more properties used by this library. This element is optional and has no attributes.

## Syntax

``` syntax
<!-- propertyStore -->
<xs:element name="propertyStore" minOccurs="0">
    <xs:complexType>
        <xs:complexContent>
            <!-- properties are extensions of propertyStoreType -->
            <xs:extension base="propertyStoreType"/>        
        </xs:complexContent>
    </xs:complexType>
</xs:element>
```

## Element Information



| Parent Element                                                               | Child Elements                                                   |
|------------------------------------------------------------------------------|------------------------------------------------------------------|
| [libraryDescription Element (Library Schema)](schema-librarydescription.md) | [property Element (Library Schema)](schema-library-property.md) |



 

## Remarks

The &lt;propertyStore&gt; element can have one or more &lt;property&gt; child elements.

## Related topics

<dl> <dt>

[Library Description Schema](library-schema-entry.md)
</dt> <dt>

[Search Connector Description Schema](../search/search-sconn-desc-schema-entry.md)
</dt> </dl>

 

 
