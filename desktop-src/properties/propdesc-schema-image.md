---
description: image
ms.assetid: 89893C4E-4F4E-4d85-9623-08607B4383E5
title: image Element (Property Description Schema)
ms.topic: article
ms.date: 05/31/2018
---

# image

There should be only one [image]() element for each parent element.

## Syntax


```
<!-- image -->
<xs:element name="image">
    <xs:complexType>
        <xs:attribute name="res" use="required">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:maxLength value="260"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
    </xs:complexType>
</xs:element>
```



## Element Information



| Parent Elements                                                                  | Child Elements |
|----------------------------------------------------------------------------------|----------------|
| [enum](./propdesc-schema-enum.md), [enumRange](./propdesc-schema-enumrange.md) | None           |



 

## Attributes



| Attribute | Description       |
|-----------|-------------------|
| res       | Public. Required. |



 

 

 
