---
description: This section provides WMI class and reference page information.
ms.assetid: 0110677a-bbba-42f7-8e59-55d83758f70a
ms.tgt_platform: multiple
title: WMI Classes
ms.topic: article
ms.date: 05/31/2018
---

# WMI Classes

This section provides WMI class and reference page information. For more information about how to retrieve class or instance data, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md). The following list lists, describes, and provides links to specific WMI class information. For more information and script code examples of using WMI classes to obtain a variety of operating system and hardware data, see [WMI Tasks for Scripts and Applications](wmi-tasks-for-scripts-and-applications.md). For examples in C++, see [WMI C++ Application Examples](wmi-c---application-examples.md). [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md) shows how to obtain remote data. You can also use PowerShell do access WMI objects; for a list of WMI classes that include PowerShell code samples, see [here](https://msdn.microsoft.com/library/tags-cloud.aspx?tag=powershell+code+wmi).



| Section                                                    | Description                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [WMI System Classes](wmi-system-classes.md)               | Predefined classes that are included in every namespace in the Windows Management Instrumentation (WMI) core. You can recognize a WMI system class because the name begins with a double underscore (\_\_). These classes provide much of the basic functionality for WMI. The WMI system classes are similar in purpose to the system tables in SQL server. |
| [MSFT Classes](msft-classes.md)                           | Other Microsoft classes that offer the means to manipulate several operating system features, such as remote events and policy extensions. The [WMI Troubleshooting](wmi-troubleshooting.md) classes are MSFT classes that provide data about WMI operations.                                                                                               |
| [CIM Classes](cimclas.md)                                 | [*Common Information Model (CIM)*](gloss-c.md) schema classes. If you want to write your own WMI classes then you can inherit from one or more of these classes. The WMI [Win32 Classes](/windows/desktop/CIMWin32Prov/win32-provider) inherit from the CIM classes.                                                                          |
| [Standard Consumer Classes](standard-consumer-classes.md) | A set of WMI event consumers which trigger an action upon receipt of an arbitrary event. For more information, see [Monitoring Events](monitoring-events.md).                                                                                                                                                                                               |



 

## WMI Class Scripting Center Code Examples

The following Scripting Center code samples affect multiple WMI classes across multiple namespaces.



| Link                                                                                                                                      | Description                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GUI WMI Explorer and WMI Method Help Generator](https://Gallery.TechNet.Microsoft.Com/scriptcenter/89c759b7-20b4-49e8-98a8-3c8fbdb2dd69) | Sample script that provides a GUI WMI Explorer and WMI Method Help Generator.                                                                                                                                                        |
| [WMI Explorer Search WMI NameSpaces](https://Gallery.TechNet.Microsoft.Com/scriptcenter/WMI-Explorer-Search-WMI-cd87e309)                 | Allows users to search for classes in all of the available namespaces on the specified computers. This sample is the command-line verison of the GUI WMI Explorer sample, and may be considered an extension of Get-WmiObject -List. |
| [Arposh Windows System Administration tool](https://Gallery.TechNet.Microsoft.Com/scriptcenter/Arposh-Windows-System-a1beb102)            | AWSA was built with the System Administrator in mind. Troubleshooting Windows issues requires a vast array of tools and knowledge. AWSA brings those tools together in one central location and adds additional functionality.       |



 

## Naming Conventions for WMI Classes and Properties

Property names must conform to the Managed Object Format (MOF) syntax defined by the Distributed Management Task Force (DTMF). The initial identifier characters must be from the letters a through z and the underscore character (\_). All additional characters must be from the letters a through z, the underscore character, and the numerals 0 through 9. For more information, see the Unicode Usage section of the [CIM Specification Version 2.2](https://www.dmtf.org/standards/cim).

SQL reserve words should not be used in class and property names. For a complete list of the SQL reserve words and for more information, see the Guidelines section of the [CIM Specification Version 2.2](https://www.dmtf.org/standards/cim).

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

Qualifiers: If present, shows the qualifiers for the property. For example, **Key**, **Override**.

Describes the property and provides inheritance information for the property. For example, this property is inherited from **CIM\_*xyz***. There is a link to the parent class if Microsoft provides an implementation of that class. However, the CIM classes are not available.

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

 

 
