---
Description: .
ms.assetid: 89893C4E-4F4E-4d85-9623-08607B4383E5
title: image
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# image

There should be only one [image](shell.propdesc_schema_image) element for each parent element.

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
| [enum](shell.propdesc_schema_enum), [enumRange](shell.propdesc_schema_enumRange) | None           |



 

## Attributes



| Attribute | Description       |
|-----------|-------------------|
| res       | Public. Required. |



 

 

 



