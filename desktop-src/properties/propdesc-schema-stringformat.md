---
description: Specifies how IPropertyDescription::FormatForDisplay should format the stringFormat property's value as a string.
ms.assetid: 7c38bc15-be86-4260-b2e4-13afc90de6d7
title: stringFormat
ms.topic: article
ms.date: 05/31/2018
---

# stringFormat

Specifies how [**IPropertyDescription::FormatForDisplay**](/windows/win32/api/propsys/nf-propsys-ipropertydescription-formatfordisplay) should format the property's value as a string. This is applicable only if \<displayInfo displayType="String"\>. There should be only one [stringFormat]() element for each [displayInfo](./propdesc-schema-displayinfo.md) element.

If there are multiple elements, the last one is used. If no [stringFormat]() element is provided, then the default attribute settings are applied to the property description.

## Syntax


```
<!-- stringFormat -->
<xs:element name="stringFormat"  minOccurs="0" maxOccurs="1">
    <xs:complexType>
        <xs:attribute name="formatAs">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="General"/>
                    <xs:enumeration value="FileName"/>
                    <xs:enumeration value="FilePath"/>
                    <xs:enumeration value="Hyperlink"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
    </xs:complexType>
</xs:element>
```



## Element Information



| Parent Element                                   | Child Elements |
|--------------------------------------------------|----------------|
| [displayInfo](./propdesc-schema-displayinfo.md) | None           |



 

## Attributes



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>formatAs</td>
<td>Public. Optional. Default is &quot;General&quot;. The following are valid values. 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>General</td>
<td>Default. Returns the value as an unformatted string.</td>
</tr>
<tr class="even">
<td>FileName</td>
<td>Formats the value as a file name. Hides the extension according to user settings. Requires the property type to be String.</td>
</tr>
<tr class="odd">
<td>FilePath</td>
<td>Formats the value as a file path. Hides the extension according to user settings. Requires the property type to be String.</td>
</tr>
<tr class="even">
<td>Hyperlink</td>
<td>Formats the value as a hyperlink.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

 

 
