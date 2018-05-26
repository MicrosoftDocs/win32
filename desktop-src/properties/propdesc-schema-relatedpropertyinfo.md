---
Description: New for Windows 7. Container element for relatedProperty elements.
ms.assetid: F8BAAE5C-A7EA-487a-B829-91A27E24B58D
title: relatedPropertyInfo
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# relatedPropertyInfo

New for Windows 7. Container element for [relatedProperty](shell.propdesc_schema_relatedProperty) elements. There should be only one [relatedPropertyInfo](shell.propdesc_schema_relatedPropertyInfo) element for each [propertyDescription](shell.propdesc_schema_propertyDescription) element.

## Syntax


```
<!-- relatedPropertyInfo -->
<xs:element name="relatedPropertyInfo">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="relatedProperty" minOccurs="0" maxOccurs="unbounded">
                <xs:complexType>
                    <xs:attribute name="relationshipName" type="canonical-name" use="required"/>
                    <xs:attribute name="propertyName" type="canonical-name" use="required"/>
                </xs:complexType>
            </xs:element>
        </xs:sequence>
    </xs:complexType>

    <xs:unique name="No_two_relatedProperties_can_have_the_same_relationship_name">
        <xs:selector xpath="s:relatedProperty"/>
        <xs:field    xpath="@relationshipName"/>
    </xs:unique>
</xs:element>
```



## Element Information



| Parent Element                                                   | Child Elements                                           |
|------------------------------------------------------------------|----------------------------------------------------------|
| [propertyDescription](shell.propdesc_schema_propertyDescription) | [relatedProperty](shell.propdesc_schema_relatedProperty) |



 

## Attributes

This element has no attributes.

 

 



