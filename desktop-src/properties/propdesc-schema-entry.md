---
Description: This topic introduces the property description schema used by the Shell property system.
ms.assetid: cac93c31-d90d-4116-b846-0cf593d1d56e
title: Understanding the Property Description Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Understanding the Property Description Schema

This topic introduces the property description schema used by the Shell property system.

The introduction of new features for Windows Vista and later required that the existing Shell property system be extended to:

-   Support a rich and extensible property description system that provides information about properties including display names, type, display type, sort and group behavior, and other attributes needed to present and operate over the properties.
-   Support a stock list of property types (combined with UI that can edit those types in different views like the listview, preview pane, property dialogs, and so on) that can be associated with various properties.
-   Supply property description lists, which define the set of properties displayed in various views.
-   Provide a simplified interface, [**IPropertyStore**](https://msdn.microsoft.com/library/Bb761474(v=VS.85).aspx), so property handlers can be written more easily and so properties can be persisted to files.
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
-   An in-memory schema cache used to store the parsed schema files, which include all property descriptions introduced to the subsystem. There is no need to reparse the .propdesc config files that describe the schema. For more information, see [**PSRegisterPropertySchema**](https://msdn.microsoft.com/library/Bb762087(v=VS.85).aspx), [**PSUnregisterPropertySchema**](https://msdn.microsoft.com/library/Bb762090(v=VS.85).aspx), and [**PSRefreshPropertySchema**](https://msdn.microsoft.com/library/Bb762086(v=VS.85).aspx).
-   A subsystem object that implements [**IPropertySystem**](https://msdn.microsoft.com/library/Bb761437(v=VS.85).aspx), which is used to obtain or work with property descriptions.
-   A subsystem object that implements [**IPropertyDescription**](https://msdn.microsoft.com/library/Bb761561(v=VS.85).aspx), which is used to inform and operate based on a property description.
-   A subsystem object that implements [**IPropertyDescriptionList**](https://msdn.microsoft.com/library/Bb761511(v=VS.85).aspx), which is used as a collection of property descriptions.

> [!Note]  
> You must add `xmlns=http://schemas.microsoft.com/windows/2006/propertydescriptio`n to the root schema element of your .propdesc files.

 

## Why Use a Schema?

Properties, by themselves, are not type-safe. A component can assign a numerical value to the System.Author property, or a [**FILETIME**](https://msdn.microsoft.com/en-us/library/ms724284(v=VS.85).aspx) date-stamp to the System.Music.AlbumTitle property, and, without any further enforcement or guidance, the property stores will allow it. So, we needed a notion to "schematize" the properties, which brings us to the schema subsystem.

## What Are the Major Schema Parts?

The property description schema used by the Shell property system is composed of a single [propertyDescriptionList](https://msdn.microsoft.com/library/Bb773882(v=VS.85).aspx) element, as well as a *schemaVersion* attribute, which indicates the version of this schema definition format. Note: value must be "1.0".


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



The [propertyDescriptionList](https://msdn.microsoft.com/library/Bb773882(v=VS.85).aspx) is composed of one or more [propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx) elements, as well as *publisher* and *product* attributes.


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



A [propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx) is composed of one [searchInfo](https://msdn.microsoft.com/library/Bb773885(v=VS.85).aspx) and zero or one [labelInfo](https://msdn.microsoft.com/library/Bb773876(v=VS.85).aspx), [typeInfo](https://msdn.microsoft.com/library/Bb773889(v=VS.85).aspx), and [displayInfo](https://msdn.microsoft.com/library/Bb773865(v=VS.85).aspx) elements, as well as *formatID*, *propID*, *propstr*, and *name* attributes.

There should be one [propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx) element for every unique canonical property name that is intended to be available in the system. The string attributes have a limit of 512 characters. Values longer than 512 characters are truncated.


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

-   [relatedPropertyInfo](https://msdn.microsoft.com/library/Dd798385(v=VS.85).aspx) and [relatedProperty](https://msdn.microsoft.com/library/Dd798384(v=VS.85).aspx) elements
-   [image](https://msdn.microsoft.com/library/Dd798383(v=VS.85).aspx) element
-   mnemonics attribute of the [searchInfo](https://msdn.microsoft.com/library/Bb773885(v=VS.85).aspx) element
-   mnemonics attribute of the [enum](https://msdn.microsoft.com/library/Bb773869(v=VS.85).aspx) element
-   searchRawValue attribute of the [typeInfo](https://msdn.microsoft.com/library/Bb773889(v=VS.85).aspx) element

The following elements and attributes have changed:

-   [enumeratedList](https://msdn.microsoft.com/library/Bb773871(v=VS.85).aspx), [enum](https://msdn.microsoft.com/library/Bb773869(v=VS.85).aspx), and [enumRange](https://msdn.microsoft.com/library/Bb773873(v=VS.85).aspx) elements
-   [drawControl](https://msdn.microsoft.com/library/Bb773866(v=VS.85).aspx) element
-   [editControl](https://msdn.microsoft.com/library/Bb773868(v=VS.85).aspx) element
-   propID attribute of the [propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx) element
-   columnIndexType attribute of the [searchInfo](https://msdn.microsoft.com/library/Bb773885(v=VS.85).aspx) element

The following elements and attributes have been removed:

-   [queryControl](https://msdn.microsoft.com/library/Bb773883(v=VS.85).aspx) element
-   isQueryable attribute of the [typeInfo](https://msdn.microsoft.com/library/Bb773889(v=VS.85).aspx) element
-   includeInFullTextQuery attribute of the [typeInfo](https://msdn.microsoft.com/library/Bb773889(v=VS.85).aspx) element

## Related topics

<dl> <dt>

[propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx)
</dt> <dt>

[searchInfo](https://msdn.microsoft.com/library/Bb773885(v=VS.85).aspx)
</dt> <dt>

[labelInfo](https://msdn.microsoft.com/library/Bb773876(v=VS.85).aspx)
</dt> <dt>

[typeInfo](https://msdn.microsoft.com/library/Bb773889(v=VS.85).aspx)
</dt> <dt>

[displayInfo](https://msdn.microsoft.com/library/Bb773865(v=VS.85).aspx)
</dt> <dt>

[stringFormat](https://msdn.microsoft.com/library/Bb773886(v=VS.85).aspx)
</dt> <dt>

[booleanFormat](https://msdn.microsoft.com/library/Bb773862(v=VS.85).aspx)
</dt> <dt>

[numberFormat](https://msdn.microsoft.com/library/Bb773877(v=VS.85).aspx)
</dt> <dt>

[dateTimeFormat](https://msdn.microsoft.com/library/Bb773863(v=VS.85).aspx)
</dt> <dt>

[enumeratedList](https://msdn.microsoft.com/library/Bb773871(v=VS.85).aspx)
</dt> <dt>

[drawControl](https://msdn.microsoft.com/library/Bb773866(v=VS.85).aspx)
</dt> <dt>

[editControl](https://msdn.microsoft.com/library/Bb773868(v=VS.85).aspx)
</dt> <dt>

[filterControl](https://msdn.microsoft.com/library/Bb773874(v=VS.85).aspx)
</dt> <dt>

[queryControl](https://msdn.microsoft.com/library/Bb773883(v=VS.85).aspx)
</dt> <dt>

[image](https://msdn.microsoft.com/library/Dd798383(v=VS.85).aspx)
</dt> </dl>

 

 



