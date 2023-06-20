---
description: Not supported in Windows 7 and later. Specifies what control to use in the query builder.
ms.assetid: 7d79c2fe-c63d-4ac5-8dd6-1a6103e53245
title: queryControl
ms.topic: article
ms.date: 05/31/2018
---

# queryControl

Not supported in Windows 7 and later. Specifies what control to use in the query builder. There should be only one [queryControl]() element for each [displayInfo](./propdesc-schema-displayinfo.md) element.

If there are multiple elements, the last one is used. If no [queryControl]() element is provided, then the default attribute settings are applied to the property description.

## Syntax


```
<!-- queryControl -->
<xs:element name="queryControl"  minOccurs="0" maxOccurs="1">
    <xs:complexType>
        <xs:attribute name="control">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="Default"/>
                    <xs:enumeration value="Boolean"/>
                    <xs:enumeration value="Calendar"/>
                    <xs:enumeration value="CheckboxDropList"/>
                    <xs:enumeration value="DropList"/>
                    <xs:enumeration value="MultiValueText"/>
                    <xs:enumeration value="NumericText"/>
                    <xs:enumeration value="Rating"/>
                    <xs:enumeration value="Text"/>
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
<td>control</td>
<td>Public. Optional. Default is &quot;Default&quot;. The following are valid values. 
<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Default</td>
<td>Default. Uses the default control, based upon the &lt;typeInfo type=&quot;&quot;&gt; attribute. The default types are listed below. Any other type results in using the &quot;Text&quot; control. 
<table>
<thead>
<tr class="header">
<th>ConditionType</th>
<th>Control</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>String</td>
<td>Text</td>
</tr>
<tr class="even">
<td>String (multi-value)</td>
<td>MultiValueText</td>
</tr>
<tr class="odd">
<td>Number or Size</td>
<td>NumericText</td>
</tr>
<tr class="even">
<td>Number or Size (enum)</td>
<td>List</td>
</tr>
<tr class="odd">
<td>DateTime</td>
<td>Calendar</td>
</tr>
<tr class="even">
<td>Boolean</td>
<td>Boolean</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>Boolean</td>
<td>Uses the boolean control.</td>
</tr>
<tr class="odd">
<td>Calendar</td>
<td>Uses the dropdown calendar control.</td>
</tr>
<tr class="even">
<td>CheckboxDropList</td>
<td>Uses the list control with checkboxes.</td>
</tr>
<tr class="odd">
<td>DropList</td>
<td>Uses the dropdown list control.</td>
</tr>
<tr class="even">
<td>MultiValueText</td>
<td>Uses the multi-value text edit control.</td>
</tr>
<tr class="odd">
<td>NumericText</td>
<td>Uses the numeric text edit control.</td>
</tr>
<tr class="even">
<td>Rating</td>
<td>Uses the 5-star rating control.</td>
</tr>
<tr class="odd">
<td>Text</td>
<td>Uses the text edit control.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

 

 
