---
description: The optional &lt;property&gt; element specifies the properties used by the location provider.
ms.assetid: c1120dea-cb0b-4746-a5c1-4c83cda6dd7c
title: property Element of locationProvider (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# property Element of locationProvider (Search Connector Schema)

The optional &lt;property&gt; element specifies the properties used by the location provider. These properties are specific to this location provider, so there is no predefined set of names to use. The &lt;property&gt; element has two attributes, as described in this topic.

## Syntax


```
<!-- property element -->
    <xs:element name="propertyBag" type="propertyStoreType" minOccurs="0">
        <xs:element name="property" minOccurs="0" maxOccurrs="unbounded"/>
            <xs:complexType>
                <xs:complexContent>
                    <xs:extension base="xs:anyType">
                        <xs:attribute name="name" type="canonical-name" use="required"/>
                        <xs:attribute name="type"/>
                    </xs:extension>
                </xs:complexContent>
            </xs:complexType>
        </xs:element>
    </xs:element>
```



## &lt;property&gt; Element Information



| Parent Element                                                                                 | Child Elements                     |
|------------------------------------------------------------------------------------------------|------------------------------------|
| [locationProvider Element (Search Connector Schema)](search-schema-sconn-locationprovider.md) | property, described in this topic. |



 


## &lt;property&gt; Attributes




| Attribute | Description | Value | 
|-----------|-------------|--------|
| name | Required. The display name of the property. |   | 
| type | Required. The type of property. | Any: Default. The value will not be coerced by the property subsystem. VT_NULL will be returned by GetPropertyType.<ul><li>Null: There is no value for this property. VT_NULL will be returned by GetPropertyType.</li><li>String: The value must be a VT_LPWSTR.</li><li>Boolean: The value must be a VT_BOOL.</li><li>Byte: The value must be a VT_UI1.</li><li>Buffer: The value must be a VT_UI1 <li> VT_VECTOR buffer of bytes.</li><li>Int16: The value must be a VT_I2.</li><li>UInt16: The value must be a VT_UI2.</li><li>Int32: The value must be a VT_I4.</li><li>UInt32: The value must be a VT_UI4.</li><li>Int64: The value must be a VT_I8.</li><li>UInt64: The value must be a VT_UI8</li><li>Double: The value must be a VT_R8.</li><li>DateTime: The value must be a VT_FILETIME.</li><li>Guid: The value must be a VT_CLSID.</li><li>Blob: The value must be a VT_BLOB.</li><li>Object: The value must be a VT_UNKNOWN.</li><li>Stream: The value must be a VT_STREAM.</li><li>Clipboard: The value must be a VT_CF.</li></ul> | 




 

## Remarks

For the OpenSearch provider, the following properties are used:

-   OpenSearchShortName: Short name of the search service
-   OpenSearchQueryTemplate: Template, formatted following the OpenSearch template convention, for the query service
-   MaximumResultCount: (number) Maximum number of results returned by the search service
-   LinkIsFilePath: (Boolean) If true, the provider tries to interpret returned items as files, using their extensions to create the proper ShellItem in the view. If false, items are treated as URL shortcuts.

 

 



