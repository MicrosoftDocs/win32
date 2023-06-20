---
description: Specifies a property's display information.
ms.assetid: 27c03ced-a5fa-4ab4-b88e-5b78701da878
title: displayInfo
ms.topic: article
ms.date: 05/31/2018
---

# displayInfo

Specifies a property's display information. There should be only one [displayInfo]() element for each [propertyDescription](./propdesc-schema-propertydescription.md).

If there are multiple elements, the last one is used. If no [displayInfo]() element is provided, then the default attribute settings are applied to the property description.

## Syntax


```
<!-- displayInfo -->
<xs:element name="displayInfo">
    <xs:complexType>
        <xs:all>
            <xs:element name="stringFormat" minOccurs="0" maxOccurs="1">
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
            <xs:element name="booleanFormat" minOccurs="0" maxOccurs="1">
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
            <xs:element name="numberFormat" minOccurs="0" maxOccurs="1">
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
                        <xs:simpleType>
                            <xs:restriction base="xs:string">
                                <xs:enumeration value="hh:mm"/>
                                <xs:enumeration value="hh:mm:ss"/>
                                <xs:enumeration value="hh:mm:ss.fff"/>
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="dateTimeFormat" minOccurs="0" maxOccurs="1">
                <xs:complexType>
                    <xs:attribute name="formatAs">
                        <xs:simpleType>
                            <xs:restriction base="xs:string">
                                <xs:enumeration value="General"/>
                                <xs:enumeration value="Month"/>
                                <xs:enumeration value="YearMonth"/>
                                <xs:enumeration value="Year"/>
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="formatTimeAs">
                        <xs:simpleType>
                            <xs:restriction base="xs:string">
                                <xs:enumeration value="ShortTime"/>
                                <xs:enumeration value="LongTime"/>
                                <xs:enumeration value="HideTime"/>
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="formatDateAs">
                        <xs:simpleType>
                            <xs:restriction base="xs:string">
                                <xs:enumeration value="ShortDate"/>
                                <xs:enumeration value="LongDate"/>
                                <xs:enumeration value="HideDate"/>
                                <xs:enumeration value="RelativeShortDate"/>
                                <xs:enumeration value="RelativeLongDate"/>
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="enumeratedList" minOccurs="0" maxOccurs="1">
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
                                <xs:attribute name="minValue" type="xs:string" use="required"/>
                                <xs:attribute name="setValue" type="xs:string"/>
                                <xs:attribute name="text" type="xs:string"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>

                    <xs:attribute name="defaultText" type="xs:string"/>
                    <xs:attribute name="useValueForDefault" type="xs:boolean"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="drawControl" minOccurs="0" maxOccurs="1">
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
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="editControl" minOccurs="0" maxOccurs="1">
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
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="filterControl" minOccurs="0" maxOccurs="1">
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
            <xs:element name="queryControl" minOccurs="0" maxOccurs="1">
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
        </xs:all>

        <xs:attribute name="defaultColumnWidth" type="xs:nonNegativeInteger" default="20"/>
        <xs:attribute name="displayType">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="String"/>
                    <xs:enumeration value="Number"/>
                    <xs:enumeration value="Boolean"/>
                    <xs:enumeration value="DateTime"/>
                    <xs:enumeration value="Enumerated"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        
        <xs:attribute name="alignment" default="Left">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="Left"/>
                    <xs:enumeration value="Center"/>
                    <xs:enumeration value="Right"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="relativeDescriptionType">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="General"/>
                    <xs:enumeration value="Date"/>
                    <xs:enumeration value="Size"/>
                    <xs:enumeration value="Count"/>
                    <xs:enumeration value="Revision"/>
                    <xs:enumeration value="Length"/>
                    <xs:enumeration value="Duration"/>
                    <xs:enumeration value="Speed"/>
                    <xs:enumeration value="Rate"/>
                    <xs:enumeration value="Rating"/>
                    <xs:enumeration value="Priority"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="defaultSortDirection" default="Ascending">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                  <xs:enumeration value="Ascending"/>
                  <xs:enumeration value="Descending"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
    </xs:complexType>
</xs:element>
```



## Element Information



| Parent Element                                                   | Child Elements                                                                                                 |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [propertyDescription](./propdesc-schema-propertydescription.md) | [stringFormat](./propdesc-schema-stringformat.md)                                                             |
|                                                                  | [booleanFormat](./propdesc-schema-booleanformat.md)                                                           |
|                                                                  | [numberFormat](./propdesc-schema-numberformat.md)                                                             |
|                                                                  | [dateTimeFormat](./propdesc-schema-datetimeformat.md)                                                         |
|                                                                  | [enumeratedList](./propdesc-schema-enumeratedlist.md)                                                         |
|                                                                  | [drawControl](./propdesc-schema-drawcontrol.md)                                                               |
|                                                                  | [editControl](./propdesc-schema-editcontrol.md)                                                               |
|                                                                  | [filterControl](./propdesc-schema-filtercontrol.md)                                                           |
|                                                                  | [queryControl](./propdesc-schema-querycontrol.md) (Windows Vista only. Not supported in Windows 7 and later.) |



 

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
<td>defaultColumnWidth</td>
<td>Public. Optional. Default is &quot;20&quot;.</td>
</tr>
<tr class="even">
<td>displayType</td>
<td>Public. Optional. Default is &quot;String&quot;. Specifies the type of the display string. Once set here, the associated <strong>PROPDESC_DISPLAYTYPE</strong> values are retrieved by <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-getdisplaytype"><strong>IPropertyDescription::GetDisplayType</strong></a>. The following are valid types. 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>String</td>
<td>Default. Value is displayed as a string. Use &quot;stringFormat&quot; to format. Method returns PDDT_STRING.</td>
</tr>
<tr class="even">
<td>Number</td>
<td>Default for numeric properties. Value is displayed as a number. Use &quot;numberFormat&quot; to format. Method returns PDDT_NUMBER.</td>
</tr>
<tr class="odd">
<td>Boolean</td>
<td>Default if &lt;typeInfo type=&quot;Boolean&quot;&gt;. Value is displayed as a boolean. Use &quot;booleanFormat&quot; to format. Method returns PDDT_BOOLEAN.</td>
</tr>
<tr class="even">
<td>DateTime</td>
<td>Default if &lt;typeInfo type=&quot;DateTime&quot;&gt;. Value is displayed as a date or time. Use &quot;dateTimeFormat&quot; to format. Method returns PDDT_DATETIME.</td>
</tr>
<tr class="odd">
<td>Enumeration</td>
<td>Value is displayed as a display string mapping provided by the &quot;enumeratedList&quot; element. Method returns PDDT_ENUMERATED.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td>alignment</td>
<td>Optional. Default is &quot;Left&quot;. 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Left</td>
<td>Default. Align left.</td>
</tr>
<tr class="even">
<td>Center</td>
<td>Align center.</td>
</tr>
<tr class="odd">
<td>Right</td>
<td>Align right.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>relativeDescriptionType</td>
<td>Optional. Default is &quot;General&quot;. Specifies how two values of this property should be described when they are compared with one another. In the case of equivalency, &quot;Same&quot; is always used. <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-getrelativedescription"><strong>IPropertyDescription::GetRelativeDescription</strong></a> and <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-getrelativedescriptiontype"><strong>IPropertyDescription::GetRelativeDescriptionType</strong></a> use this value to determine what relative description display names to use. 
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
<td>Default. Uses &quot;Different&quot; / &quot;Same&quot; / &quot;Different&quot;.</td>
</tr>
<tr class="even">
<td>Date</td>
<td>Default if &lt;typeInfo type=&quot;DateTime&quot;&gt;. Uses &quot;Earlier&quot; / &quot;Same&quot; / &quot;Later&quot;, or uses &quot;Older&quot; / &quot;Same&quot; / &quot;Newer&quot;, or uses &quot;Sooner&quot; / &quot;Same&quot; / &quot;Later&quot;.</td>
</tr>
<tr class="odd">
<td>Size</td>
<td>Uses &quot;Smaller&quot; / &quot;Same&quot; / &quot;Larger&quot;</td>
</tr>
<tr class="even">
<td>Count</td>
<td>Uses &quot;Smaller&quot; / &quot;Same&quot; / &quot;Larger&quot;</td>
</tr>
<tr class="odd">
<td>Revision</td>
<td>Uses &quot;Earlier&quot; / &quot;Same&quot; / &quot;Later&quot;</td>
</tr>
<tr class="even">
<td>Length</td>
<td>Uses &quot;Shorter&quot; / &quot;Same&quot; / &quot;Longer&quot;</td>
</tr>
<tr class="odd">
<td>Duration</td>
<td>Uses &quot;Shorter&quot; / &quot;Same&quot; / &quot;Longer&quot;</td>
</tr>
<tr class="even">
<td>Speed</td>
<td>Uses &quot;Slower&quot; / &quot;Same&quot; / &quot;Faster&quot;</td>
</tr>
<tr class="odd">
<td>Rate</td>
<td>Uses &quot;Slower&quot; / &quot;Same&quot; / &quot;Faster&quot;</td>
</tr>
<tr class="even">
<td>Rating</td>
<td>Uses &quot;Lower&quot; / &quot;Same&quot; / &quot;Higher&quot;</td>
</tr>
<tr class="odd">
<td>Priority</td>
<td>Uses &quot;Lower&quot; / &quot;Same&quot; / &quot;Higher&quot;</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td>defaultSortDirection</td>
<td>Specifies sort direction. Default is &quot;Ascending&quot;. 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Ascending</td>
<td>Sorts ascending.</td>
</tr>
<tr class="even">
<td>Descending</td>
<td>Sorts descending.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

 

 
