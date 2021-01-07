---
description: Specifies a property's type information.
ms.assetid: ae1f8835-ef6c-42bb-b44f-ad374337a012
title: typeInfo
ms.topic: article
ms.date: 05/31/2018
---

# typeInfo

Specifies a property's type information. There should be only one [typeInfo]() element for each [propertyDescription](./propdesc-schema-propertydescription.md). This element has changed for Windows 7.

If there are multiple elements, the last one is used. If no [typeInfo]() element is provided, then the default attribute settings are applied to the property description.

## Syntax for Windows 7


```
<!-- typeInfo for Windows 7-->
<xs:element name="typeInfo">
    <xs:complexType>
        <xs:attribute name="type" default="Any">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="Any"/>
                    <xs:enumeration value="Null"/>
                    <xs:enumeration value="String"/>
                    <xs:enumeration value="Boolean"/>
                    <xs:enumeration value="Byte"/>
                    <xs:enumeration value="Buffer"/>
                    <xs:enumeration value="Int16"/>
                    <xs:enumeration value="UInt16"/>
                    <xs:enumeration value="Int32"/>
                    <xs:enumeration value="UInt32"/>
                    <xs:enumeration value="Int64"/>
                    <xs:enumeration value="UInt64"/>
                    <xs:enumeration value="Double"/>
                    <xs:enumeration value="DateTime"/>
                    <xs:enumeration value="Guid"/>
                    <xs:enumeration value="Blob"/>
                    <xs:enumeration value="Stream"/>
                    <xs:enumeration value="Clipboard"/>
                    <xs:enumeration value="Object"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="groupingRange">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="Discrete"/>
                    <xs:enumeration value="Alphanumeric"/>
                    <xs:enumeration value="Size"/>
                    <xs:enumeration value="Date"/>
                    <xs:enumeration value="Dynamic"/>
                    <xs:enumeration value="Percent"/>
                    <xs:enumeration value="Enumerated"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="isInnate" type="xs:boolean" default="false"/>
        <xs:attribute name="canBePurged" type="xs:boolean"/>
        <xs:attribute name="multipleValues" type="xs:boolean" default="false"/>
        <xs:attribute name="isGroup" type="xs:boolean" default="false"/>
        <xs:attribute name="aggregationType">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="Default"/>
                    <xs:enumeration value="First"/>
                    <xs:enumeration value="Sum"/>
                    <xs:enumeration value="Average"/>
                    <xs:enumeration value="DateRange"/>
                    <xs:enumeration value="Union"/>
                    <xs:enumeration value="Maximum"/>
                    <xs:enumeration value="Minimum"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="isTreeProperty" type="xs:boolean" default="false"/>
        <xs:attribute name="isViewable" type="xs:boolean" default="false"/>
        <xs:attribute name="isQueryable" type="xs:boolean" default="false"/>
        <xs:attribute name="includeInFullTextQuery" type="xs:boolean" default="false"/>
        <xs:attribute name="searchRawValue" type="xs:boolean" default="false"/>
        <xs:attribute name="conditionType">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="None"/>
                    <xs:enumeration value="String"/>
                    <xs:enumeration value="Number"/>
                    <xs:enumeration value="DateTime"/>
                    <xs:enumeration value="Boolean"/>
                    <xs:enumeration value="Size"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="defaultOperation">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="Equal"/>
                    <xs:enumeration value="NotEqual"/>
                    <xs:enumeration value="LessThan"/>
                    <xs:enumeration value="GreaterThan"/>
                    <xs:enumeration value="Contains"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
    </xs:complexType>
</xs:element>
```



## Element Information



| Parent Element                                                   | Child Elements |
|------------------------------------------------------------------|----------------|
| [propertyDescription](./propdesc-schema-propertydescription.md) | None           |



 

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
<td>type</td>
<td>Public. Optional. Default is &quot;Any&quot;. Indicates the type of the property. The following are valid types and their associated variant types are retrieved by <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-getpropertytype"><strong>IPropertyDescription::GetPropertyType</strong></a>. 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Any</td>
<td>Default. The property subsystem will not enforce or coerce the property value. <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-getpropertytype"><strong>IPropertyDescription::GetPropertyType</strong></a> returns VT_NULL. Independent software vendors (ISVs) are strongly encouraged to provide a type rather than fall back on this default.</td>
</tr>
<tr class="even">
<td>Null</td>
<td>There is no value for this property. <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-getpropertytype"><strong>IPropertyDescription::GetPropertyType</strong></a> returns VT_NULL.</td>
</tr>
<tr class="odd">
<td>String</td>
<td>The value must be a VT_LPWSTR, which is a Unicode string terminated by a null reference.</td>
</tr>
<tr class="even">
<td>Boolean</td>
<td>The value must be a VT_BOOL, which is a boolean.</td>
</tr>
<tr class="odd">
<td>Byte</td>
<td>The value must be a VT_UI1, which is a byte.</td>
</tr>
<tr class="even">
<td>Buffer</td>
<td>The value must be a VT_UI1 | VT_VECTOR buffer of bytes.</td>
</tr>
<tr class="odd">
<td>Int16</td>
<td>The value must be a VT_I2, which is a 16-bit integer.</td>
</tr>
<tr class="even">
<td>UInt16</td>
<td>The value must be a VT_UI2, which is a 16-bit unsigned integer.</td>
</tr>
<tr class="odd">
<td>Int32</td>
<td>The value must be a VT_I4, which is a 32-bit integer.</td>
</tr>
<tr class="even">
<td>UInt32</td>
<td>The value must be a VT_UI4, which is a 32-bit unsigned integer.</td>
</tr>
<tr class="odd">
<td>Int64</td>
<td>The value must be a VT_I8, which is a 64-bit integer.</td>
</tr>
<tr class="even">
<td>UInt64</td>
<td>The value must be a VT_UI8, which is a 64-bit unsigned integer.</td>
</tr>
<tr class="odd">
<td>Double</td>
<td>The value must be a VT_R8, which is a double.</td>
</tr>
<tr class="even">
<td>DateTime</td>
<td>The value must be a VT_FILETIME, which is a <a href="/windows/desktop/api/minwinbase/ns-minwinbase-filetime"><strong>FILETIME</strong></a>.</td>
</tr>
<tr class="odd">
<td>Guid</td>
<td>The value must be a VT_CLSID, which is a class identifier (CLSID).</td>
</tr>
<tr class="even">
<td>Blob</td>
<td>The value must be a VT_BLOB, which are length-prefixed bytes.</td>
</tr>
<tr class="odd">
<td>Stream</td>
<td>The value must be a VT_STREAM, which is an object that implements <a href="/windows/desktop/api/objidl/nn-objidl-istream"><strong>IStream</strong></a>.</td>
</tr>
<tr class="even">
<td>Clipboard</td>
<td>The value must be a VT_CF, which is a clipboard format.</td>
</tr>
<tr class="odd">
<td>Object</td>
<td>The value must be a VT_UNKNOWN, which is an object that implements <a href="/windows/desktop/api/unknwn/nn-unknwn-iunknown"><strong>IUnknown</strong></a>.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>groupingRange</td>
<td>Optional. Default is &quot;Discrete&quot;. Specifies how the property is displayed when a view is grouped by this property. Once set here, these values are retrieved by <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-getgroupingrange"><strong>IPropertyDescription::GetGroupingRange</strong></a>. The following are valid types.

<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Discrete</td>
<td>Default. Displays individual values.</td>
</tr>
<tr class="even">
<td>Alphanumeric</td>
<td>Displays static alphanumeric ranges for values.</td>
</tr>
<tr class="odd">
<td>Size</td>
<td>Displays static size ranges for values.</td>
</tr>
<tr class="even">
<td>Date</td>
<td>Displays month/year groups. Default for properties of type=&quot;DateTime&quot;.</td>
</tr>
<tr class="odd">
<td>TimeRelative</td>
<td>Displays in time-relative groups.</td>
</tr>
<tr class="even">
<td>Dynamic</td>
<td>Displays dynamically created ranges for the values.</td>
</tr>
<tr class="odd">
<td>Percent</td>
<td>Displays percent buckets.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td>isInnate</td>
<td>Public. Optional. Default is &quot;false&quot;. Specifies whether the property is considered innate. An innate property is one which is either calculated from the content of a file, or from other resources or systems. For example, System.Size is an innate property provided by the file system; changing the value of the property in and of itself does nothing. Other examples are System.Image.Dimensions and System.Document.PageCount, which are calculated by programs based upon the content of the file, not based upon a user-changeable setting. Setting isInnate=&quot;true&quot; means the user cannot edit this property directly via a property control. This value maps to the PDTF_ISINNATE flag defined in <a href="/windows/win32/api/propsys/ne-propsys-propdesc_type_flags"><strong>PROPDESC_TYPE_FLAGS</strong></a> and used in <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-gettypeflags"><strong>IPropertyDescription::GetTypeFlags</strong></a>.</td>
</tr>
<tr class="even">
<td>canBePurged</td>
<td><strong>Windows Vista with Service Pack 1 (SP1) and later only</strong>. Public. Optional. When set to &quot;true&quot;, allows an innate property to be deleted. Innate properties, which are calculated from other properties, are read-only by definition. The default value for this attribute depends on the <em>isInnate</em> value.

<table>
<thead>
<tr class="header">
<th>isInnate</th>
<th>canBePurged Default Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>true</td>
<td>false</td>
</tr>
<tr class="even">
<td>false</td>
<td>true</td>
</tr>
</tbody>
</table>

<p> </p>
<div class="alert">
<blockquote>
[!Note]<br />
A property whose <em>isInnate</em> value is &quot;false&quot; (meaning that the property is read/write) cannot also set the <em>canBePurged</em> value to &quot;false&quot;. This restriction is enforced by the operating system.
</blockquote>
</div>
<div>
 
</div>
<p>Although this attribute was introduced in Windows Vista with Service Pack 1 (SP1), a .propdesc file that includes this attribute is compatible with Windows Vista prior to Windows Vista with SP1. The <em>canBePurged</em> attribute is simply ignored in that situation.</p></td>
</tr>
<tr class="odd">
<td>multipleValues</td>
<td>Public. Optional. Default is &quot;false&quot;. Specifies whether this property can have multiple values. This value maps to the PDTF_MULTIPLEVALUES flag defined in <a href="/windows/win32/api/propsys/ne-propsys-propdesc_type_flags"><strong>PROPDESC_TYPE_FLAGS</strong></a> and used in <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-gettypeflags"><strong>IPropertyDescription::GetTypeFlags</strong></a>. This also influences whether VT_VECTOR is OR'd to the VARTYPE of the property value.</td>
</tr>
<tr class="even">
<td>isGroup</td>
<td>Public. Optional. Default is &quot;false&quot;. Specifies whether the property is a group heading. A group heading is strictly used in proplists, has no value, is never stored in a file, and should also have <typeInfo type=&quot;Null&quot;>. Some UI in the system use proplists to indicate the sequence of the properties to display. These proplists may include references to group headings (eg, System.PropGroup.Camera), which tell the UI to start a new group section (eg, &quot;Camera Settings&quot;). A property description with isGroup=&quot;true&quot; should specify a <labelInfo label=&quot;Some localized label&quot;>, otherwise it isn't a useful property. This value maps to the PDTF_ISGROUP flag defined in <a href="/windows/win32/api/propsys/ne-propsys-propdesc_type_flags"><strong>PROPDESC_TYPE_FLAGS</strong></a> and used in <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-gettypeflags"><strong>IPropertyDescription::GetTypeFlags</strong></a>.</td>
</tr>
<tr class="odd">
<td>aggregationType</td>
<td>Public. Optional. Default is &quot;Default&quot;. Specifies how aggregate properties are displayed when multiple items are selected. Once set here, these values are retrieved by <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-getaggregationtype"><strong>IPropertyDescription::GetAggregationType</strong></a> as an <a href="/windows/win32/api/propsys/ne-propsys-propdesc_aggregation_type"><strong>PROPDESC_AGGREGATION_TYPE</strong></a>. The following are valid types.

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
<td>Default. Displays a <strong>Multiple Values</strong> placeholder in the UI. This is the default if the <em>type</em> is incompatible with the specified <em>aggregationType</em>.</td>
</tr>
<tr class="even">
<td>First</td>
<td>Displays the property value of the first item in the selection or collection.</td>
</tr>
<tr class="odd">
<td>Sum</td>
<td>Displays the sum of the numerical values. Useful for properties such as System.Media.Duration or System.Size. This value is not compatible with non-numeric types.</td>
</tr>
<tr class="even">
<td>Average</td>
<td>Displays the average of the numerical values. Useful for properties such as System.Rating. This value is not compatible with non-numeric types.</td>
</tr>
<tr class="odd">
<td>DateRange</td>
<td>Displays a range of dates. Useful for properties like System.Photo.DateTaken. This value is not compatible with anything except type=&quot;DateTime&quot; and is the default for properties of that type.</td>
</tr>
<tr class="even">
<td>Union</td>
<td>Displays a union of all the values in the selection or collection. The order in which the values are shown is undefined. This value is the default for properties of type=&quot;String&quot; and multipleValues=&quot;true&quot;.</td>
</tr>
<tr class="odd">
<td>Maximum</td>
<td>Displays the maximum value in the collection. Useful for properties like System.DateModified. Not compatible with non-numeric or non-date types.</td>
</tr>
<tr class="even">
<td>Minimum</td>
<td>Displays the minimum value in the collection. Not compatible with non-numeric or non-date types.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>isTreeProperty</td>
<td>Public. Optional. Default value is &quot;false&quot;.</td>
</tr>
<tr class="odd">
<td>isViewable</td>
<td>Public. Optional. Default value is &quot;false&quot;. Specifies whether this property is intended to be viewable to the user. For example, the Column Chooser UI only shows the properties that have isViewable=&quot;true&quot;. The exception is UI that is driven by a proplist, which will always show the property. If you have a property that is only meant to shuttle data between two objects, and never intended to be viewed by the user, this attribute should be false. This value maps to the PDTF_ISVIEWABLE flag defined in <a href="/windows/win32/api/propsys/ne-propsys-propdesc_type_flags"><strong>PROPDESC_TYPE_FLAGS</strong></a> and used in <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-gettypeflags"><strong>IPropertyDescription::GetTypeFlags</strong></a>.</td>
</tr>
<tr class="even">
<td>isQueryable</td>
<td>Windows Vista only. Not supported in Windows 7 and later. Public. Optional. Default value is &quot;false&quot;. Specifies whether this property is intended to be available in the Search Query Builder UI. A property must have isViewable=&quot;true&quot; before isQueryable=&quot;true&quot; is respected. This value maps to the PDTF_ISQUERYABLE flag defined in <a href="/windows/win32/api/propsys/ne-propsys-propdesc_type_flags"><strong>PROPDESC_TYPE_FLAGS</strong></a> and used in <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-gettypeflags"><strong>IPropertyDescription::GetTypeFlags</strong></a>.</td>
</tr>
<tr class="odd">
<td>searchRawValue</td>
<td><strong>Windows 7 and later.</strong> Public. Optional. Default value is &quot;false&quot;.</td>
</tr>
<tr class="even">
<td>includeInFullTextQuery</td>
<td>Windows Vista only. Not supported in Windows 7 and later. Public. Optional. Default value is &quot;false&quot;.</td>
</tr>
<tr class="odd">
<td>conditionType</td>
<td>Public. Optional. Default is &quot;String&quot;. Specifies a hint to the Search Query Builder UI so that it can determine the list of possible condition operators inside a predicate. The following are recognized values. 
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
<td>Default. The following operators will be used: &quot;is&quot;, &quot;is not&quot;, &quot;&lt;&quot;, &quot;&gt;&quot;, &quot;<=&quot;, &quot;>=&quot;, &quot;starts with&quot;, &quot;ends with&quot;, &quot;contains&quot;, &quot;doesn't contain&quot;, &quot;is like&quot;.</td>
</tr>
<tr class="even">
<td>Number</td>
<td>Default for numeric properties. The following operators will be used: &quot;equals&quot;, &quot;doesn't equal&quot;, &quot;is less than&quot;, &quot;is greater than&quot;, &quot;is less than or equal to&quot;, &quot;is greater than or equal to&quot;.</td>
</tr>
<tr class="odd">
<td>DateTime</td>
<td>Default for properties of type=&quot;DateTime&quot;. The following operators will be used: &quot;is&quot;, &quot;is not&quot;, &quot;is before&quot;, &quot;is after&quot;, &quot;is before but includes&quot;, &quot;is after but includes&quot;.</td>
</tr>
<tr class="even">
<td>Boolean</td>
<td>Default for properties of type=&quot;Boolean&quot;. Same as Number.</td>
</tr>
<tr class="odd">
<td>Size</td>
<td>Same as Number.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>defaultOperation</td>
<td>Public. Optional. Default is &quot;Equal&quot;. Specifies a hint to the Search Query Builder tool so that it can determine the default operator. The possible values are as follows:

<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Equal</td>
<td>Default. Indicates equivalent.</td>
</tr>
<tr class="even">
<td>NotEqual</td>
<td>Indicates not equivalent.</td>
</tr>
<tr class="odd">
<td>LessThan</td>
<td>Indicates less than.</td>
</tr>
<tr class="even">
<td>GreaterThan</td>
<td>Default for properties of conditionType=&quot;Size&quot;. Indicates greater than.</td>
</tr>
<tr class="odd">
<td>Contains</td>
<td>Default for properties of conditionType=&quot;String&quot;. Indicates inclusion.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

 

 
