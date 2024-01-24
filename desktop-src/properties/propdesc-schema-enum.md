---
description: Used to assign enumerated text to discrete values.
ms.assetid: c8cc040e-fcce-43a0-98c1-db2b2c616ac3
title: enum
ms.topic: article
ms.date: 05/31/2018
---

# enum

Used to assign enumerated text to discrete values. Any number of these elements may exist under an [enumeratedList](./propdesc-schema-enumeratedlist.md). Programmatically, these are represented as IPropertyEnumType objects, whose [**IPropertyEnumType::GetEnumType**](/windows/win32/api/propsys/nf-propsys-ipropertyenumtype-getenumtype) method returns PET\_DISCRETEVALUE.

## Syntax


```
<!-- enum -->
<xs:element name="enum" minOccurs="0" maxOccurs="unbounded">
    <xs:complexType>
        <xs:sequence>
            <xs:element ref="image" minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="value" type="xs:string" use="required"/>
        <xs:attribute name="text" type="xs:string" use="required"/>
        <xs:attribute name="mnemonics" type="xs:string"/>
    </xs:complexType>
</xs:element>
```



## Element Information



| Parent Element                                         | Child Elements |
|--------------------------------------------------------|----------------|
| [enumeratedList](./propdesc-schema-enumeratedlist.md) | none           |



 

## Attributes



| Attribute | Description                                                                                                                                                                                                          |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| value     | Public. Required. The discrete value (string or number) to be assigned enumerated text to.                                                                                                                           |
| text      | Public. Required. The text used to display the enumerated value. The syntax allows for a direct display string or an indirect display string reference; use the indirect display string so that it can be localized. |
| mnemonics | **Windows 7 and later.** Public. Optional. A list of mnemonic values that can be used to refer to the property in search queries. The list is delimited with the '\|' character.                                     |



 

 

 
