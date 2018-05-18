---
Description: 'Specifies how IPropertyDescription::FormatForDisplay should format the property''s value as a string.'
ms.assetid: '49ba57b8-3e08-425f-98b2-52ed2c41a488'
title: enumeratedList
---

# enumeratedList

Specifies how [**IPropertyDescription::FormatForDisplay**](shell.IPropertyDescription_FormatForDisplay) should format the property's value as a string. It also influences how the property may be grouped, or what values to show in the list if the "editControl" is a listblox. This is applicable only if &lt;displayInfo displayType="Enumerated"&gt;. There should be only one [enumeratedList](shell.propdesc_schema_enumeratedList) element for each [displayInfo](shell.propdesc_schema_displayInfo) element.

If there are multiple elements, the last one is used. If no [enumeratedList](shell.propdesc_schema_enumeratedList) element is provided, then the default attribute settings are applied to the property description.

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
| [displayInfo](shell.propdesc_schema_displayInfo) | [enum](shell.propdesc_schema_enum)           |
|                                                  | [enumRange](shell.propdesc_schema_enumRange) |



 

## Attributes



| Attribute          | Description                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| defaultText        | Public. Optional. Specify default text to use if a value is given to [**IPropertyDescription::FormatForDisplay**](shell.IPropertyDescription_FormatForDisplay) that does not map to one of the enumerated elements in the list. The syntax allows for a direct display string or an indirect display string reference; use the reference, so it can be localized.                              |
| useValueForDefault | Public. Optional. Setting this to "true" will inform [**IPropertyDescription::FormatForDisplay**](shell.IPropertyDescription_FormatForDisplay) to use the value as-is if the value does not map to one of the enumerated elements in the list. For **IPropertyDescription::FormatForDisplay**, setting this to "true" takes precedence over setting the "defaultText". The default is "false". |



 

 

 



