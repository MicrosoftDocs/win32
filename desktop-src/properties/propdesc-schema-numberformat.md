---
description: Specifies how IPropertyDescription::FormatForDisplay should format the property's value as a string. This is applicable only if <displayInfo displayType=&\#0034;Number&\#0034;>.
ms.assetid: 9e8cfe5c-e17a-40d6-958f-a1bd1130c699
title: numberFormat
ms.topic: article
ms.date: 05/31/2018
---

# numberFormat

Specifies how [**IPropertyDescription::FormatForDisplay**](/windows/win32/api/propsys/nf-propsys-ipropertydescription-formatfordisplay) should format the property's value as a string. This is applicable only if <displayInfo displayType="Number">. There should be only one [numberFormat]() element for each [displayInfo](./propdesc-schema-displayinfo.md) element.

If there are multiple elements, the last one is used. If no [numberFormat]() element is provided, then the default attribute settings are applied to the property description.

## Syntax


```
      <!-- numberFormat -->
      <xs:element name="numberFormat"  minOccurs="0" maxOccurs="1">
        <xs:complexType>
          <xs:attribute name="formatAs">
            <xs:simpleType>
              <xs:restriction base="xs:string">
                <xs:enumeration value="General"/>
                <xs:enumeration value="Percentage"/>
                <xs:enumeration value="ByteSize"/>
                <xs:enumeration value="KBSize"/>
                <xs:enumeration value="SampleSize"/>
                <xs:enumeration value="Bitrate"/>
                <xs:enumeration value="SampleRate"/>
                <xs:enumeration value="FrameRate"/>
                <xs:enumeration value="Pixels"/>
                <xs:enumeration value="DPI"/>
                <xs:enumeration value="Duration"/>
              </xs:restriction>
            </xs:simpleType>
          </xs:attribute>
          <xs:attribute name="formatDurationAs">
              <xs:restriction base="xs:string">
                <xs:enumeration value="hh:mm"/>
                <xs:enumeration value="hh:mm:ss"/>
                <xs:enumeration value="hh:mm:ss.fff"/>
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
<td>Public. Optional. Default is &quot;General&quot;. Specifies the display format. The following are valid values. 
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
<td>Default. Displays the value as an unformatted number.</td>
</tr>
<tr class="even">
<td>Percentage</td>
<td>Formats the value as a percentage. Requires the property to be UInt32.</td>
</tr>
<tr class="odd">
<td>ByteSize</td>
<td>Formats the value as a byte, &quot;KB&quot;, &quot;MB&quot;, or &quot;GB&quot; as appropriate. Requires the property to be UInt64.</td>
</tr>
<tr class="even">
<td>KBSize</td>
<td>Formats the value as a &quot;KB&quot;, no matter what the value is. Requires the property to be UInt64.</td>
</tr>
<tr class="odd">
<td>SampleSize</td>
<td>Formats the value as a number of bits. Requires the property to be UInt32.</td>
</tr>
<tr class="even">
<td>BitRate</td>
<td>Formats the value in &quot;Kbps&quot;. Requires the property to be UInt32. The value must be stored in &quot;bits-per-second&quot; units.</td>
</tr>
<tr class="odd">
<td>SampleRate</td>
<td>Formats the value in &quot;KHz&quot;. Requires the property to be UInt32. The value must be stored in &quot;Hertz&quot; units.</td>
</tr>
<tr class="even">
<td>FrameRate</td>
<td>Formats the value in frames/second. Requires the property to be UInt32. The value must be stored in &quot;kilo-frames-per-second&quot; units.</td>
</tr>
<tr class="odd">
<td>Pixels</td>
<td>Formats the value in pixel units. Requires the property to be UInt32.</td>
</tr>
<tr class="even">
<td>DPI</td>
<td>Formats the value in dots-per-inch. Requires the property to be UInt32.</td>
</tr>
<tr class="odd">
<td>Duration</td>
<td>Formats the value as a duration. Use &lt;formatDurationAs&gt; to specify the duration format. Requires the property to be UInt64.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>formatDurationAs</td>
<td>Public. Optional. Default is &quot;hh:mm:ss&quot;. Only applies if <em>formatAs=&quot;Duration&quot;</em>. Requires the property to be UInt64. The following are valid values. 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>hh:mm</td>
<td>Formats the value in hours and minutes.</td>
</tr>
<tr class="even">
<td>hh:mm:ss</td>
<td>Default. Formats the value in hours, minutes, and seconds.</td>
</tr>
<tr class="odd">
<td>hh:mm:ss.fff</td>
<td>Formats the value in hours, minutes, seconds, and milliseconds.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

 

 
