---
Description: New for Windows 7. Container element for relatedProperty elements.
ms.assetid: F8BAAE5C-A7EA-487a-B829-91A27E24B58D
title: relatedPropertyInfo
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# relatedPropertyInfo

New for Windows 7. Container element for [relatedProperty](https://msdn.microsoft.com/library/Dd798384(v=VS.85).aspx) elements. There should be only one [relatedPropertyInfo](https://msdn.microsoft.com/library/Dd798385(v=VS.85).aspx) element for each [propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx) element.

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
| [propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx) | [relatedProperty](https://msdn.microsoft.com/library/Dd798384(v=VS.85).aspx) |



 

## Attributes

This element has no attributes.

 

 



