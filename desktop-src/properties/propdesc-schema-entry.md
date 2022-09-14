---
description: This topic introduces the property description schema used by the Shell property system.
ms.assetid: cac93c31-d90d-4116-b846-0cf593d1d56e
title: Understanding the Property Description Schema
ms.topic: article
ms.date: 05/31/2018
---

# Understanding the Property Description Schema

This topic introduces the property description schema used by the Shell property system.

The introduction of new features for Windows Vista and later required that the existing Shell property system be extended to:

-   Support a rich and extensible property description system that provides information about properties including display names, type, display type, sort and group behavior, and other attributes needed to present and operate over the properties.
-   Support a stock list of property types (combined with UI that can edit those types in different views like the listview, preview pane, property dialogs, and so on) that can be associated with various properties.
-   Supply property description lists, which define the set of properties displayed in various views.
-   Provide a simplified interface, [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore), so property handlers can be written more easily and so properties can be persisted to files.
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
-   An in-memory schema cache used to store the parsed schema files, which include all property descriptions introduced to the subsystem. There is no need to reparse the .propdesc config files that describe the schema. For more information, see [**PSRegisterPropertySchema**](/windows/win32/api/propsys/nf-propsys-psregisterpropertyschema), [**PSUnregisterPropertySchema**](/windows/win32/api/propsys/nf-propsys-psunregisterpropertyschema), and [**PSRefreshPropertySchema**](/windows/win32/api/propsys/nf-propsys-psrefreshpropertyschema).
-   A subsystem object that implements [**IPropertySystem**](/windows/win32/api/propsys/nn-propsys-ipropertysystem), which is used to obtain or work with property descriptions.
-   A subsystem object that implements [**IPropertyDescription**](/windows/win32/api/propsys/nn-propsys-ipropertydescription), which is used to inform and operate based on a property description.
-   A subsystem object that implements [**IPropertyDescriptionList**](/windows/win32/api/propsys/nn-propsys-ipropertydescriptionlist), which is used as a collection of property descriptions.

> [!Note]  
> You must add `xmlns=http://schemas.microsoft.com/windows/2006/propertydescription` to the root schema element of your .propdesc files.

 

## Why Use a Schema?

Properties, by themselves, are not type-safe. A component can assign a numerical value to the System.Author property, or a [**FILETIME**](/windows/win32/api/minwinbase/ns-minwinbase-filetime) date-stamp to the System.Music.AlbumTitle property, and, without any further enforcement or guidance, the property stores will allow it. So, we needed a notion to "schematize" the properties, which brings us to the schema subsystem.

## What Are the Major Schema Parts?

The property description schema used by the Shell property system is composed of a single [propertyDescriptionList](./propdesc-schema-propertydescriptionlist.md) element, as well as a *schemaVersion* attribute, which indicates the version of this schema definition format. Note: value must be "1.0".


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



The [propertyDescriptionList](./propdesc-schema-propertydescriptionlist.md) is composed of one or more [propertyDescription](./propdesc-schema-propertydescription.md) elements, as well as *publisher* and *product* attributes.


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



A [propertyDescription](./propdesc-schema-propertydescription.md) is composed of one [searchInfo](./propdesc-schema-searchinfo.md) and zero or one [labelInfo](./propdesc-schema-labelinfo.md), [typeInfo](./propdesc-schema-typeinfo.md), and [displayInfo](./propdesc-schema-displayinfo.md) elements, as well as *formatID*, *propID*, *propstr*, and *name* attributes.

There should be one [propertyDescription](./propdesc-schema-propertydescription.md) element for every unique canonical property name that is intended to be available in the system. The string attributes have a limit of 512 characters. Values longer than 512 characters are truncated.


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

-   [relatedPropertyInfo](./propdesc-schema-relatedpropertyinfo.md) and [relatedProperty](./propdesc-schema-relatedproperty.md) elements
-   [image](./propdesc-schema-image.md) element
-   mnemonics attribute of the [searchInfo](./propdesc-schema-searchinfo.md) element
-   mnemonics attribute of the [enum](./propdesc-schema-enum.md) element
-   searchRawValue attribute of the [typeInfo](./propdesc-schema-typeinfo.md) element

The following elements and attributes have changed:

-   [enumeratedList](./propdesc-schema-enumeratedlist.md), [enum](./propdesc-schema-enum.md), and [enumRange](./propdesc-schema-enumrange.md) elements
-   [drawControl](./propdesc-schema-drawcontrol.md) element
-   [editControl](./propdesc-schema-editcontrol.md) element
-   propID attribute of the [propertyDescription](./propdesc-schema-propertydescription.md) element
-   columnIndexType attribute of the [searchInfo](./propdesc-schema-searchinfo.md) element

The following elements and attributes have been removed:

-   [queryControl](./propdesc-schema-querycontrol.md) element
-   isQueryable attribute of the [typeInfo](./propdesc-schema-typeinfo.md) element
-   includeInFullTextQuery attribute of the [typeInfo](./propdesc-schema-typeinfo.md) element

## Related topics

<dl> <dt>

[propertyDescription](./propdesc-schema-propertydescription.md)
</dt> <dt>

[searchInfo](./propdesc-schema-searchinfo.md)
</dt> <dt>

[labelInfo](./propdesc-schema-labelinfo.md)
</dt> <dt>

[typeInfo](./propdesc-schema-typeinfo.md)
</dt> <dt>

[displayInfo](./propdesc-schema-displayinfo.md)
</dt> <dt>

[stringFormat](./propdesc-schema-stringformat.md)
</dt> <dt>

[booleanFormat](./propdesc-schema-booleanformat.md)
</dt> <dt>

[numberFormat](./propdesc-schema-numberformat.md)
</dt> <dt>

[dateTimeFormat](./propdesc-schema-datetimeformat.md)
</dt> <dt>

[enumeratedList](./propdesc-schema-enumeratedlist.md)
</dt> <dt>

[drawControl](./propdesc-schema-drawcontrol.md)
</dt> <dt>

[editControl](./propdesc-schema-editcontrol.md)
</dt> <dt>

[filterControl](./propdesc-schema-filtercontrol.md)
</dt> <dt>

[queryControl](./propdesc-schema-querycontrol.md)
</dt> <dt>

[image](./propdesc-schema-image.md)
</dt> </dl>

 

 
