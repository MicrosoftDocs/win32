---
Description: Describes a single unique canonical property.
ms.assetid: 1a36ec83-5d8a-4fc5-be3d-a8c2f0983057
title: propertyDescription
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# propertyDescription

Describes a single unique canonical property. Every such property intended to be available in the system must have a corresponding [propertyDescription](shell.propdesc_schema_propertyDescription) element.

## Syntax for Windows 7


```
<!-- propertyDescription for Windows 7-->
<xs:element name="propertyDescription">
    <xs:complexType>
        <xs:all>
            <xs:element ref="searchInfo"          minOccurs="0" maxOccurs="1"/>
            <xs:element ref="labelInfo"           minOccurs="0" maxOccurs="1"/>
            <xs:element ref="typeInfo"            minOccurs="0" maxOccurs="1"/>
            <xs:element ref="aliasInfo"           minOccurs="0" maxOccurs="1"/>
            <xs:element ref="displayInfo"         minOccurs="0" maxOccurs="1"/>
            <xs:element ref="relatedPropertyInfo" minOccurs="0" maxOccurs="1"/>
        </xs:all>

        <xs:attribute name="formatID"  type="uuid" use="required"/>
        <xs:attribute name="propID"    type="propid" use="required"/>
        <xs:attribute name="name"      type="canonical-name"        use="required"/>
    </xs:complexType>
</xs:element>
```



## Syntax for Vista


```
<!-- propertyDescription for Windows Vista-->
<xs:element name="propertyDescription">
    <xs:complexType>
        <xs:all>
            <xs:element ref="searchInfo"          minOccurs="0" maxOccurs="1"/>
            <xs:element ref="labelInfo"           minOccurs="0" maxOccurs="1"/>
            <xs:element ref="typeInfo"            minOccurs="0" maxOccurs="1"/>
            <xs:element ref="aliasInfo"           minOccurs="0" maxOccurs="1"/>
            <xs:element ref="displayInfo"         minOccurs="0" maxOccurs="1"/>
        </xs:all>

        <xs:attribute name="formatID"  type="uuid" use="required"/>
        <xs:attribute name="propID"    type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="name"      type="canonical-name"        use="required"/>
    </xs:complexType>
</xs:element>
```



## Element Information



| Parent Element                                                           | Child Elements                                                   |
|--------------------------------------------------------------------------|------------------------------------------------------------------|
| [propertyDescriptionList](shell.propdesc_schema_propertyDescriptionList) | [searchInfo](shell.propdesc_schema_searchInfo)                   |
|                                                                          | [labelInfo](shell.propdesc_schema_labelInfo)                     |
|                                                                          | [typeInfo](shell.propdesc_schema_typeInfo)                       |
|                                                                          | [aliasInfo](shell.propdesc_schema_aliasInfo)                     |
|                                                                          | [displayInfo](shell.propdesc_schema_displayInfo)                 |
|                                                                          | [relatedPropertyInfo](shell.propdesc_schema_relatedPropertyInfo) |



 

## Attributes



| Attribute | Description                                                                                                                                                                                                                                                                                                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name      | Required. The canonical property name, unique to the system; for example, `System.Rating`. This string is of type canonical-type and is limited to 64 characters. The name is case-sensitive and should use the following syntax: Publisher.Application.PropertyName. [**IPropertyDescription::GetCanonicalName**](shell.IPropertyDescription_GetCanonicalName) returns this value. |
| formatID  | Required. The property's format identifier (FMTID). The value must include enclosing braces; for example, `{64440492-4C8B-11D1-8B70-080036B11A03}`. [**IPropertyDescription::GetPropertyKey**](shell.IPropertyDescription_GetPropertyKey) returns this value.                                                                                                                       |
| propID    | Required. The property identifier (PID); for example, `9`. [**IPropertyDescription::GetPropertyKey**](shell.IPropertyDescription_GetPropertyKey) returns this value. This value must be greater than or equal to 2. The values 0 and 1 are reserved by the system.                                                                                                                  |



 

 

 



