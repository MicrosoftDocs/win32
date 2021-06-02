---
description: Specifies what control to use when simply displaying the property.
ms.assetid: 0fb8afc4-d16b-4c2e-80b3-da9935b11bb5
title: drawControl
ms.topic: article
ms.date: 05/31/2018
---

# drawControl

Specifies what control to use when simply displaying the property. There should be only one [drawControl]() element for each [displayInfo](./propdesc-schema-displayinfo.md) element.

If there are multiple elements, the last one is used. If no [drawControl]() element is provided, then the default attribute settings are applied to the property description.

This form of the control does not allow for property editing.

## Syntax


```
<!-- drawControl -->
<xs:element name="drawControl"  minOccurs="0" maxOccurs="1">
    <xs:complexType>
        <xs:attribute name="control">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="Default"/>
                    <xs:enumeration value="MultiLineText"/>
                    <xs:enumeration value="MultiValueText"/>
                    <xs:enumeration value="PercentBar"/>
                    <xs:enumeration value="ProgressBar"/>
                    <xs:enumeration value="Rating"/>
                    <xs:enumeration value="StaticText"/>
                    <xs:enumeration value="IconList"/>
                    <xs:enumeration value="BooleanCheckMark"/>
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
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>control</td>
<td>Public. Optional. Default is &quot;Default&quot;. The following are valid values. 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Default</td>
<td>Default. Uses the default control, based upon the <typeInfo type=&quot;&quot;> attribute. The default type is &quot;String&quot; (multi-value) and the default control is &quot;MultiValueText&quot;. Any other type results in using the &quot;StaticText&quot; control.</td>
</tr>
<tr class="even">
<td>MultiLineText</td>
<td>Uses the multi-line text control.</td>
</tr>
<tr class="odd">
<td>MultiValueText</td>
<td>Uses the multi-value text control.</td>
</tr>
<tr class="even">
<td>PercentBar</td>
<td>Uses the percent bar control.</td>
</tr>
<tr class="odd">
<td>ProgressBar</td>
<td>Uses the progress bar control.</td>
</tr>
<tr class="even">
<td>Rating</td>
<td>Uses the 5-star rating control.</td>
</tr>
<tr class="odd">
<td>StaticText</td>
<td>Uses <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-formatfordisplay"><strong>IPropertyDescription::FormatForDisplay</strong></a> to display the property value.</td>
</tr>
<tr class="even">
<td>IconList</td>
<td><strong>Windows 7 and later.</strong> An enumeration of icons.</td>
</tr>
<tr class="odd">
<td>BooleanCheckMark</td>
<td><strong>Windows 7 and later.</strong></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

 

 
