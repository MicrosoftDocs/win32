---
Description: 'This topic introduces the property description schema used by the Shell property system.'
ms.assetid: 'cac93c31-d90d-4116-b846-0cf593d1d56e'
title: Understanding the Property Description Schema
---

# Understanding the Property Description Schema

This topic introduces the property description schema used by the Shell property system.

The introduction of new features for Windows Vista and later required that the existing Shell property system be extended to:

-   Support a rich and extensible property description system that provides information about properties including display names, type, display type, sort and group behavior, and other attributes needed to present and operate over the properties.
-   Support a stock list of property types (combined with UI that can edit those types in different views like the listview, preview pane, property dialogs, and so on) that can be associated with various properties.
-   Supply property description lists, which define the set of properties displayed in various views.
-   Provide a simplified interface, [**IPropertyStore**](shell.IPropertyStore), so property handlers can be written more easily and so properties can be persisted to files.
-   Support for non-file property handlers to expose properties in the view.

These features are achieved on an architecture that provides abstract access to the properties of a Shell item. This abstraction is called the Shell property system.

-   [What Is the Property Description Schema?](#what-is-the-property-description-schema)
-   [Why Use a Schema?](#why-use-a-schema)
-   [What Are the Major Schema Parts?](#what-are-the-major-schema-parts)
-   [Changes for Windows 7](#changes-for-windows-7)
-   [Related topics](#related-topics)

## What Is the Property Description Schema?

The schema subsystem consists of the following:

-   One or more .propdesc schema files that define property descriptions. The property description schema is defined in a collection of XML schema files (using the .propdesc file extension) at runtime on the system. These files are lazy-loaded when a part of the property system requires them.
-   An in-memory schema cache used to store the parsed schema files, which include all property descriptions introduced to the subsystem. There is no need to reparse the .propdesc config files that describe the schema. For more information, see [**PSRegisterPropertySchema**](shell.PSRegisterPropertySchema), [**PSUnregisterPropertySchema**](shell.PSUnregisterPropertySchema), and [**PSRefreshPropertySchema**](shell.PSRefreshPropertySchema).
-   A subsystem object that implements [**IPropertySystem**](shell.IPropertySystem), which is used to obtain or work with property descriptions.
-   A subsystem object that implements [**IPropertyDescription**](shell.IPropertyDescription), which is used to inform and operate based on a property description.
-   A subsystem object that implements [**IPropertyDescriptionList**](shell.IPropertyDescriptionList), which is used as a collection of property descriptions.

> [!Note]  
> You must add `xmlns=http://schemas.microsoft.com/windows/2006/propertydescriptio`n to the root schema element of your .propdesc files.

 

## Why Use a Schema?

Properties, by themselves, are not type-safe. A component can assign a numerical value to the System.Author property, or a [**FILETIME**](base.filetime_str) date-stamp to the System.Music.AlbumTitle property, and, without any further enforcement or guidance, the property stores will allow it. So, we needed a notion to "schematize" the properties, which brings us to the schema subsystem.

## What Are the Major Schema Parts?

The property description schema used by the Shell property system is composed of a single [propertyDescriptionList](shell.propdesc_schema_propertyDescriptionList) element, as well as a *schemaVersion* attribute, which indicates the version of this schema definition format. Note: value must be "1.0".


```
<!-- schema -->
    <xs:element name="schema">
      <xs:complexType>
        <xs:sequence>
          <xs:element ref="propertyDescriptionList" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="schemaVersion"  type="xs:string"/>
      </xs:complexType>
    </xs:element>
```



The [propertyDescriptionList](shell.propdesc_schema_propertyDescriptionList) is composed of one or more [propertyDescription](shell.propdesc_schema_propertyDescription) elements, as well as *publisher* and *product* attributes.


```
<!-- propertyDescriptionList -->
    <xs:element name="propertyDescriptionList">
      <xs:complexType>
        <xs:sequence>
          <xs:element ref="propertyDescription" minOccurs="1" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:attribute name="publisher" type="xs:string"/>
        <xs:attribute name="product"   type="xs:string"/>
      </xs:complexType>
    </xs:element>
```



A [propertyDescription](shell.propdesc_schema_propertyDescription) is composed of one [searchInfo](shell.propdesc_schema_searchInfo) and zero or one [labelInfo](shell.propdesc_schema_labelInfo), [typeInfo](shell.propdesc_schema_typeInfo), and [displayInfo](shell.propdesc_schema_displayInfo) elements, as well as *formatID*, *propID*, *propstr*, and *name* attributes.

There should be one [propertyDescription](shell.propdesc_schema_propertyDescription) element for every unique canonical property name that is intended to be available in the system. The string attributes have a limit of 512 characters. Values longer than 512 characters are truncated.


```
<!-- propertyDescription -->
    <xs:element name="propertyDescription">
      <xs:complexType>
        <xs:all>
          <xs:element name="description"    type="xs:string" minOccurs="0" maxOccurs="1"/>
          <xs:element ref="searchInfo"   minOccurs="1" maxOccurs="1"/>
          <xs:element ref="labelInfo"    minOccurs="0" maxOccurs="1"/>
          <xs:element ref="typeInfo"     minOccurs="0" maxOccurs="1"/>
          <xs:element ref="displayInfo"  minOccurs="0" maxOccurs="1"/>
        </xs:all>
        <xs:attribute name="formatID"  type="upcase-uuid" use="required""/>
        <xs:attribute name="propID"    type="xs:nonNegativeInteger" use="required""/>
        <xs:attribute name="name"      type="canonical-name" use="required"/>
      </xs:complexType>
    </xs:element>
```



## Changes for Windows 7

The property description schema has been changed for Windows 7. These are non-breaking changes. If a property element or attribute is no longer supported in Windows 7, the Windows 7 operating system ignores the Windows Vista element or attributes. Similarly, Windows Vista ignores new Windows 7 property elements or attributes as well.

However, updating custom properties for Windows 7 is recommended for a better and more consistent user experience.

The following are new elements and attributes:

-   [relatedPropertyInfo](shell.propdesc_schema_relatedPropertyInfo) and [relatedProperty](shell.propdesc_schema_relatedProperty) elements
-   [image](shell.propdesc_schema_image) element
-   mnemonics attribute of the [searchInfo](shell.propdesc_schema_searchInfo) element
-   mnemonics attribute of the [enum](shell.propdesc_schema_enum) element
-   searchRawValue attribute of the [typeInfo](shell.propdesc_schema_typeInfo) element

The following elements and attributes have changed:

-   [enumeratedList](shell.propdesc_schema_enumeratedList), [enum](shell.propdesc_schema_enum), and [enumRange](shell.propdesc_schema_enumRange) elements
-   [drawControl](shell.propdesc_schema_drawControl) element
-   [editControl](shell.propdesc_schema_editControl) element
-   propID attribute of the [propertyDescription](shell.propdesc_schema_propertyDescription) element
-   columnIndexType attribute of the [searchInfo](shell.propdesc_schema_searchInfo) element

The following elements and attributes have been removed:

-   [queryControl](shell.propdesc_schema_queryControl) element
-   isQueryable attribute of the [typeInfo](shell.propdesc_schema_typeInfo) element
-   includeInFullTextQuery attribute of the [typeInfo](shell.propdesc_schema_typeInfo) element

## Related topics

<dl> <dt>

[propertyDescription](shell.propdesc_schema_propertyDescription)
</dt> <dt>

[searchInfo](shell.propdesc_schema_searchInfo)
</dt> <dt>

[labelInfo](shell.propdesc_schema_labelInfo)
</dt> <dt>

[typeInfo](shell.propdesc_schema_typeInfo)
</dt> <dt>

[displayInfo](shell.propdesc_schema_displayInfo)
</dt> <dt>

[stringFormat](shell.propdesc_schema_stringFormat)
</dt> <dt>

[booleanFormat](shell.propdesc_schema_booleanFormat)
</dt> <dt>

[numberFormat](shell.propdesc_schema_numberFormat)
</dt> <dt>

[dateTimeFormat](shell.propdesc_schema_dateTimeFormat)
</dt> <dt>

[enumeratedList](shell.propdesc_schema_enumeratedList)
</dt> <dt>

[drawControl](shell.propdesc_schema_drawControl)
</dt> <dt>

[editControl](shell.propdesc_schema_editControl)
</dt> <dt>

[filterControl](shell.propdesc_schema_filterControl)
</dt> <dt>

[queryControl](shell.propdesc_schema_queryControl)
</dt> <dt>

[image](shell.propdesc_schema_image)
</dt> </dl>

 

 



