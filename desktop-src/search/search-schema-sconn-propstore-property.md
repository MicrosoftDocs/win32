---
description: The optional &lt;property&gt; element specifies a property used by the search connector. These properties are specific to this search connector, so there is no predefined set of names to use. This element has no child elements.
ms.assetid: 33854123-d4c0-4385-910b-a32d6922423f
title: property Element of propertyStore (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# property Element of propertyStore (Search Connector Schema)

The optional &lt;property&gt; element specifies a property used by the search connector. These properties are specific to this search connector, so there is no predefined set of names to use. This element has no child elements.

## Syntax

```
<!-- property for propertyStore element -->
    <xs:element name="propertyBag" type="propertyStoreType" minOccurs="0">
        <xs:element name="property" minOccurs="0" maxOccurrs="unbounded">
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

## Element Information

| Parent Element                                                                           | Child Elements |
|------------------------------------------------------------------------------------------|----------------|
| [propertyStore Element (Search Connector Schema)](search-schema-sconn-propertystore.md) |                |

## Attributes

| Attribute | Description | Values |
|---|---|---|
| name | Public. Required. The display name of the property. | Default | 
| type | Public. Required. The type of property. | Any: Default. The value will not be coerced by the property subsystem. VT_NULL will be returned by GetPropertyType.<ul><li>Null: There is no value for this property. VT_NULL will be returned by GetPropertyType.</li><li>String: The value must be a VT_LPWSTR.</li><li>Boolean: The value must be a VT_BOOL.</li><li>Byte: The value must be a VT_UI1.</li><li>Buffer: The value must be a VT_UI1 | VT_VECTOR buffer of bytes.</li><li>Int16: The value must be a VT_I2.</li><li>UInt16: The value must be a VT_UI2.</li><li>Int32: The value must be a VT_I4.</li><li>UInt32: The value must be a VT_UI4.</li><li>Int64: The value must be a VT_I8.</li><li>UInt64: The value must be a VT_UI8</li><li>Double: The value must be a VT_R8.</li><li>DateTime: The value must be a VT_FILETIME.</li><li>Guid: The value must be a VT_CLSID.</li><li>Blob: The value must be a VT_BLOB.</li><li>Object: The value must be a VT_UNKNOWN.</li><li>Stream: The value must be a VT_STREAM.</li><li>Clipboard: The value must be a VT_CF.</li></ul> |
| schema | Public. Optional. The schema where the property is defined. | Default |

## Remarks

OpenSearch search connectors can use the OpenSearchHTMLRolloverTemplate property. This property identifies a template that is formatted following the OpenSearch template convention. The OpenSearchHTMLRolloverTemplate template is used when the user clicks on the "Search on website" button in the command bar.

## Example

The following example shows a &lt;propertyStore&gt; element with two &lt;property&gt; elements.

```
<propertyStore>
    <property name="OpenSearchHTMLRolloverTemplate">https://www.adventureworks.com/Search/?Query={searchTerms}</property>
    <property name="isExternal" type="boolean">true</property>
</propertyStore>
```
