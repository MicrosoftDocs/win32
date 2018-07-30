---
Description: Specifies how IPropertyDescription::FormatForDisplay should format the property's value as a string.
ms.assetid: 49ba57b8-3e08-425f-98b2-52ed2c41a488
title: enumeratedList
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# enumeratedList

Specifies how [**IPropertyDescription::FormatForDisplay**](https://msdn.microsoft.com/library/Bb761521(v=VS.85).aspx) should format the property's value as a string. It also influences how the property may be grouped, or what values to show in the list if the "editControl" is a listblox. This is applicable only if &lt;displayInfo displayType="Enumerated"&gt;. There should be only one [enumeratedList](https://msdn.microsoft.com/library/Bb773871(v=VS.85).aspx) element for each [displayInfo](https://msdn.microsoft.com/library/Bb773865(v=VS.85).aspx) element.

If there are multiple elements, the last one is used. If no [enumeratedList](https://msdn.microsoft.com/library/Bb773871(v=VS.85).aspx) element is provided, then the default attribute settings are applied to the property description.

## Syntax


```
<!-- enumeratedList -->
<xs:element name="enumeratedList"  minOccurs="0" maxOccurs="1">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="enum" minOccurs="0" maxOccurs="unbounded">
                <xs:complexType>
                    <xs:attribute name="value" type="xs:string" use="required"/>
                    <xs:attribute name="text" type="xs:string" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="enumRange" minOccurs="0" maxOccurs="unbounded">
                <xs:complexType>
                    <xs:attribute name="minValue" type="xs:integer" use="required"/>
                    <xs:attribute name="setValue" type="xs:integer"/>
                    <xs:attribute name="text" type="xs:string"/>
                </xs:complexType>
            </xs:element>
        </xs:sequence>
        <xs:attribute name="defaultText" type="xs:string"/>
        <xs:attribute name="useValueForDefault" type="xs:boolean"/>
    </xs:complexType>
</xs:element>
```



## Element Information



| Parent Element                                   | Child Elements                               |
|--------------------------------------------------|----------------------------------------------|
| [displayInfo](https://msdn.microsoft.com/library/Bb773865(v=VS.85).aspx) | [enum](https://msdn.microsoft.com/library/Bb773869(v=VS.85).aspx)           |
|                                                  | [enumRange](https://msdn.microsoft.com/library/Bb773873(v=VS.85).aspx) |



 

## Attributes



| Attribute          | Description                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| defaultText        | Public. Optional. Specify default text to use if a value is given to [**IPropertyDescription::FormatForDisplay**](https://msdn.microsoft.com/library/Bb761521(v=VS.85).aspx) that does not map to one of the enumerated elements in the list. The syntax allows for a direct display string or an indirect display string reference; use the reference, so it can be localized.                              |
| useValueForDefault | Public. Optional. Setting this to "true" will inform [**IPropertyDescription::FormatForDisplay**](https://msdn.microsoft.com/library/Bb761521(v=VS.85).aspx) to use the value as-is if the value does not map to one of the enumerated elements in the list. For **IPropertyDescription::FormatForDisplay**, setting this to "true" takes precedence over setting the "defaultText". The default is "false". |



 

 

 



