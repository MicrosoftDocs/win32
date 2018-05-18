---
Description: 'Specifies how IPropertyDescription::FormatForDisplay should format the property''s value as a string. This is applicable only if &lt;displayInfo displayType=&\#0034;String&\#0034;&gt;.'
ms.assetid: 'f6384910-4411-4ac2-884d-3476c1b6ff96'
title: booleanFormat
---

# booleanFormat

Specifies how [**IPropertyDescription::FormatForDisplay**](shell.IPropertyDescription_FormatForDisplay) should format the property's value as a string. This is applicable only if &lt;displayInfo displayType="String"&gt;. There should be only one [booleanFormat](shell.propdesc_schema_booleanFormat) element for each [displayInfo](shell.propdesc_schema_displayInfo) element.

If there are multiple elements, the last one is used. If no [booleanFormat](shell.propdesc_schema_booleanFormat) element is provided, then the default attribute settings are applied to the property description.

## Syntax


```
      <!-- booleanFormat -->
      <xs:element name="booleanFormat"  minOccurs="0" maxOccurs="1">
        <xs:complexType>
          <xs:attribute name="formatAs">
            <xs:simpleType>
              <xs:restriction base="xs:string">
                <xs:enumeration value="YesNo"/>
                <xs:enumeration value="OnOff"/>
                <xs:enumeration value="TrueFalse"/>
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
<td>formatAs</td>
<td>Public. Optional. Default is &quot;YesNo&quot;. The following are valid values. 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YesNo</td>
<td>Default. Formats the value as either &quot;Yes&quot; or &quot;No&quot;. Requires the property type to be Boolean.</td>
</tr>
<tr class="even">
<td>OnOff</td>
<td>Formats the value as either &quot;On&quot; or &quot;Off&quot;. Requires the property type to be Boolean.</td>
</tr>
<tr class="odd">
<td>TrueFalse</td>
<td>Formats the value as either &quot;True&quot; or &quot;False&quot;. Requires the property type to be Boolean.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

 

 



