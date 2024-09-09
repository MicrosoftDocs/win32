---
description: Specifies what control to use when editing the property.
ms.assetid: cef6d76f-664a-4808-a224-e82a5adb2d70
title: editControl
ms.topic: article
ms.date: 05/31/2018
---

# editControl

Specifies what control to use when editing the property. There should be only one [editControl]() element for each [displayInfo](./propdesc-schema-displayinfo.md) element.

If there are multiple elements, the last one is used. If no [editControl]() element is provided, then the default attribute settings are applied to the property description.

If \<typeInfo isInnate="true"\>, this element is ignored because an innate property cannot be edited.

## Syntax


```
<!-- editControl -->
<xs:element name="editControl"  minOccurs="0" maxOccurs="1">
    <xs:complexType>
        <xs:attribute name="control">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="Default"/>
                    <xs:enumeration value="Calendar"/>
                    <xs:enumeration value="CheckboxDropList"/>
                    <xs:enumeration value="DropList"/>
                    <xs:enumeration value="MultiLineText"/>
                    <xs:enumeration value="MultiValueText"/>
                    <xs:enumeration value="Rating"/>
                    <xs:enumeration value="Text"/>
                    <xs:enumeration value="IconList"/>
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
<td>Default. Uses the default control, based upon the &lt;typeInfo type=&quot;&quot;&gt; attribute. The default types are listed below. Any other type results in using the &quot;Text&quot; control. &lt;&gt;
<table>
<thead>
<tr class="header">
<th>Type</th>
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
<td>DateTime</td>
<td>Calendar</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>Calendar</td>
<td>Uses the calendar control.</td>
</tr>
<tr class="odd">
<td>CheckboxDropList</td>
<td>Uses the list control with checkboxes.</td>
</tr>
<tr class="even">
<td>DropList</td>
<td>Uses the dropdown list control.</td>
</tr>
<tr class="odd">
<td>MultiLineText</td>
<td>Uses the multi-line text edit control.</td>
</tr>
<tr class="even">
<td>MultiValueText</td>
<td>Uses the multi-value text edit control.</td>
</tr>
<tr class="odd">
<td>Rating</td>
<td>Uses the 5-star rating control.</td>
</tr>
<tr class="even">
<td>Text</td>
<td>Uses the text edit control.</td>
</tr>
<tr class="odd">
<td>IconList</td>
<td><strong>Windows 7 and later.</strong></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

 

 
