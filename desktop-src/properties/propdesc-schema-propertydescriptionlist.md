---
description: Container for one or many individual propertyDescription elements.
ms.assetid: b54aaa85-6928-470e-9630-44b094205106
title: propertyDescriptionList
ms.topic: article
ms.date: 05/31/2018
---

# propertyDescriptionList

Container for one or many individual [propertyDescription](./propdesc-schema-propertydescription.md) elements. A .propdesc property description schema file should contain at least one [propertyDescriptionList]() element.

## Syntax


```
<!-- propertyDescriptionList -->
<xs:element name="propertyDescriptionList">
    <xs:complexType>
        <xs:sequence>
            <xs:element ref="s:propertyDescription" minOccurs="1" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:attribute name="publisher" type="xs:string" use="required"/>
        <xs:attribute name="product"   type="xs:string" use="required"/>
    </xs:complexType>

    <xs:unique name="No_two_propertyDescriptions_can_have_the_same_formatid_and_propid">
        <xs:selector xpath="s:propertyDescription"/>
        <xs:field    xpath="@formatID"/>
        <xs:field    xpath="@propID"/>
    </xs:unique>

    <xs:unique name="No_two_propertyDescriptions_can_have_the_same_canonical_name">
        <xs:selector xpath="s:propertyDescription"/>
        <xs:field    xpath="@name"/>
    </xs:unique>
</xs:element>
```



## Element Information



| Parent Element                        | Child Elements                                                   |
|---------------------------------------|------------------------------------------------------------------|
| [schema](./propdesc-schema-entry.md) | [propertyDescription](./propdesc-schema-propertydescription.md) |



 

## Attributes



| Attribute | Description                                                               |
|-----------|---------------------------------------------------------------------------|
| publisher | Public. Required. The display name of the publisher providing the schema. |
| product   | Public. Required. The display name of the product providing the schema.   |



 

## Remarks

The [propertyDescriptionList]() should not be confused with "property lists" and [**IPropertyDescriptionList**](/windows/win32/api/propsys/nn-propsys-ipropertydescriptionlist), which are completely separate.

 

 
