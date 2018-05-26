---
Description: Specifies what control to use in the header filter menu.
ms.assetid: a3117e16-20d0-4637-b726-9fa49516ad5c
title: filterControl
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# filterControl

Specifies what control to use in the header filter menu. There should be only one [filterControl](shell.propdesc_schema_filterControl) element for each [displayInfo](shell.propdesc_schema_displayInfo) element.

If there are multiple elements, the last one is used. If no [filterControl](shell.propdesc_schema_filterControl) element is provided, then the default attribute settings are applied to the property description.

## Syntax


```
      <!-- filterControl -->
      <xs:element name="filterControl"  minOccurs="0" maxOccurs="1">
        <xs:complexType>
          <xs:attribute name="control">
            <xs:simpleType>
              <xs:restriction base="xs:string">
                <xs:enumeration value="Default"/>
                <xs:enumeration value="Calendar"/>
                <xs:enumeration value="Rating"/>
              </xs:restriction>
            </xs:simpleType>
          </xs:attribute>
        </xs:complexType>
      </xs:element>
```



## Element Information



| Parent Element                                   | Child Elements |
|--------------------------------------------------|----------------|
| [displayInfo](shell.propdesc_schema_displayInfo) | None           |



 

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
<td>Default. Uses the default control, based upon the &lt;typeInfo type=&quot;&quot;&gt; attribute. The default type is &quot;DateTime&quot; and the default control is &quot;Calendar&quot;. Any other type results in no special filter control.</td>
</tr>
<tr class="even">
<td>Calendar</td>
<td>Uses the calendar control.</td>
</tr>
<tr class="odd">
<td>Rating</td>
<td>Uses the 5-star rating control.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

 

 



