---
description: Specifies how IPropertyDescription::FormatForDisplay should format the property's value as a string. This is applicable only if <displayInfo displayType=&\#0034;DateTime&\#0034;>.
ms.assetid: c290fb2e-ef5b-4dea-ba42-7c9e273a89dc
title: dateTimeFormat
ms.topic: article
ms.date: 05/31/2018
---

# dateTimeFormat

Specifies how [**IPropertyDescription::FormatForDisplay**](/windows/win32/api/propsys/nf-propsys-ipropertydescription-formatfordisplay) should format the property's value as a string. This is applicable only if <displayInfo displayType="DateTime">. There should be only one [dateTimeFormat]() element for each [displayInfo](./propdesc-schema-displayinfo.md) element.

If there are multiple elements, the last one is used. If no [dateTimeFormat]() element is provided, then the default attribute settings are applied to the property description.

## Syntax


```
      <!-- dateTimeFormat -->
      <xs:element name="dateTimeFormat"  minOccurs="0" maxOccurs="1">
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
<td>Default. Formats the date-time value using <a href="/windows/desktop/api/shlwapi/nf-shlwapi-shformatdatetimea"><strong>SHFormatDateTime</strong></a>. Use the <em>formatTimeAs</em> and <em>formatDateAs</em> attributes to specify how the time and date are formatted. Requires the property type to be DateTime.</td>
</tr>
<tr class="even">
<td>Month</td>
<td>Formats the value as one of the months of the year. Requires the property type to be Int32. The value must be stored as a numeric value with 1 representing the first month of the year.</td>
</tr>
<tr class="odd">
<td>YearMonth</td>
<td>Formats the value as &quot;Year - Month&quot;. Requires the property type to be Int32. The value must be stored such that the two highest bytes specify the year and the lower two bytes specify the month.</td>
</tr>
<tr class="even">
<td>Year</td>
<td>Formats the value as a simple string.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>formatTimeAs</td>
<td>Public. Optional. Default is &quot;ShortTime&quot;. Specifies the format in which to display time. Applies when <strong>formatAs=&quot;General&quot;</strong>. The following are valid values. 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ShortTime</td>
<td>Default. Show the time like &quot;7:48 PM&quot;.</td>
</tr>
<tr class="even">
<td>LongTime</td>
<td>Show the time like &quot;7:48:33 PM&quot;.</td>
</tr>
<tr class="odd">
<td>HideTime</td>
<td>Do not display the time portion of the date.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td>formatDateAs</td>
<td>Public. Optional. Default is &quot;ShortDate&quot;. Specifies the format in which to display the date. Applies when <strong>formatAs=&quot;General&quot;</strong>. The following are valid values. 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ShortDate</td>
<td>Default. Show the date like &quot;5/13/59&quot;.</td>
</tr>
<tr class="even">
<td>LongDate</td>
<td>Show the date like &quot;Wednesday, May 13, 1959&quot;.</td>
</tr>
<tr class="odd">
<td>HideDate</td>
<td>Do not display the date portion.</td>
</tr>
<tr class="even">
<td>RelativeShortDate</td>
<td>Show the date like &quot;ShortDate&quot;, but use relative descriptions, such as &quot;yesterday&quot;, whenever possible.</td>
</tr>
<tr class="odd">
<td>RelativeLongDate</td>
<td>Show the date like &quot;LongDate&quot;, but use relative descriptions, such as &quot;yesterday&quot;, whenever possible.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

 

 
