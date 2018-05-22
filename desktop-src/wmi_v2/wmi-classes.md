---
title: MI Classes
description: This section provides WMI class and reference page information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '11bee4f9-c2c7-4de8-83e7-4ab5668fc3e5'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["classes Windows Management Infrastructure (MI)", "MI classes Windows Management Infrastructure (MI)"]
---

# MI Classes

This section provides WMI class and reference page information.

## Naming Conventions for WMI Classes and Properties

Property names must conform to the Managed Object Format (MOF) syntax defined by the Distributed Management Task Force (DMTF). The initial identifier characters must be from the letters a through z and the underscore character (\_). All additional characters must be from the letters a through z, the underscore character, and the numerals 0 through 9. For more information, see the Unicode Usage section of the [CIM Specification Version 2.2](http://go.microsoft.com/fwlink/p/?linkid=84403).

SQL reserve words should not be used in class and property names. For a complete list of the SQL reserve words and for more information, see the Guidelines section of the [CIM Specification Version 2.2](http://go.microsoft.com/fwlink/p/?linkid=84403).

## Document Conventions for a WMI Class Reference Page

This section identifies and describes the document conventions for a WMI class reference page.

A typical reference page contains a syntax block, methods table, and a properties list.

-   Syntax block

    A simplified version of MOF code that includes the class name, parent class (if any), and class properties, in alphabetical order, with data types.

-   Methods table

    If a class has methods, the methods are listed in the table immediately following the syntax block. Each implemented method is linked to a reference page.

-   Properties list

    Each class property is listed with a data type, access type (read-only or read/write), qualifiers, and a description of the property.

## Syntax block

``` syntax
class Win32_xyz : CIM_xyz 
{
  uint16 abc  ;
  string def  ;
};
```

## Methods table



| Win32\_xyz methods | Description                                |
|--------------------|--------------------------------------------|
| *SomeMethod*       | Brief description of what the method does. |



 

## Properties list

<dl> <dt>

<span id="abc"></span><span id="ABC"></span>abc
</dt> <dd>

Data type: **uint16**

Access type: Shows whether you have read/write or read-only access to this property.

Qualifiers: If present, shows the qualifiers for the property. For example, **KeyOverride**.

Describes the property and provides inheritance information for the property. For example, this property is inherited from CIM\_xyz. There is a link to the parent class if Microsoft provides an implementation of that class. However, the CIM classes are not available.

</dd> <dt>

<span id="def"></span><span id="DEF"></span>def
</dt> <dd>

Data type: **string**

Access type: Read-only

Description of the property.

</dd> </dl>

## Remarks

Gives more information about the class, if applicable. Also provides derivation information, if applicable.

## Related topics

<dl> <dt>

[WMI Reference](wmi-reference.md)
</dt> </dl>

 

 




