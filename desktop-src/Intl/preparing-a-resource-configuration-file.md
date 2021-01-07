---
description: Preparing a Resource Configuration File
ms.assetid: 292b57ea-1c7e-49b6-876c-4ad307a2ec43
title: Preparing a Resource Configuration File
ms.topic: article
ms.date: 05/31/2018
---

# Preparing a Resource Configuration File

Both the MUIRCT and the RC Compiler utilities described in [Resource Utilities](resource-utilities.md) provide a command line option that allows you to specify a resource configuration file for the base language resources. Use of this public, human-readable XML file allows more control over the splitting of resources than can be obtained using the regular command line switches of the utilities. However, even if you do not provide a resource configuration file as an input, the LN and language-specific resource files will contain resource configuration data.

All resource configuration files for Win32 applications begin and end identically:


```C++
<?xml version="1.0" encoding="utf-8"?> 
<localization>

<resources>
        
        <!-- a single win32Resources element goes here -->

</resources>
</localization>
```



This topic focuses on the aspects of the XML schema that are useful in building unmanaged code on Windows Vista and later. In particular, it is only concerned with the behavior of the win32Resources element.

## win32Resources Element

The win32Resources element has the attributes described in the following table.



| Attribute name           | Mandatory | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fileType                 | No        | Type of file. Should always be "Application".                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| checksum                 | No        | Checksum value to appear in the resource configuration data of the LN file and language-specific resource files. For example, this attribute allows you to copy the checksum from a single language-specific resource file, by convention the one for English (United States), and place the checksum in a different language-specific resource file. The checksum can be specified as a hexadecimal number string that is no longer than 32 characters. The numerical value must be containable in a 128-bit number. |
| language                 | No        | Language specified using a name format compliant with RFC 4646 (Windows Vista and later), for example, en-US for English (United States).                                                                                                                                                                                                                                                                                                                                                                             |
| ultimateFallbackLanguage | No        | Language to insert into the resource configuration data for the LN file, representing the ultimate fallback language to use in a search for a corresponding language-specific resource file. If the resource loader fails to load a requested resource file from the thread preferred UI languages, it uses an ultimate fallback language as its last attempt. The language is specified using a name format compliant with RFC 4646 (Windows Vista and later), for example, en-US for English (United States).       |
| ultimateFallbackLocation | No        | Fallback location. Specify "internal" if ultimate fallback resources are compiled into the LN file. Specify "external" (default) if the LN file is to reference a language-specific resource file for its ultimate fallback resources.                                                                                                                                                                                                                                                                                |



 

In the resource configuration file, the win32Resources element has the sub-elements described in the next table.



| Element Name       | Description                                                                                                                              |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| localizedResources | Resources that encapsulate information about the resource types and individual resources contained in a language-specific resource file. |
| neutralResources   | Resources that encapsulate information about the resource types contained in an LN file.                                                 |



 

## localizedResources Element

Localized resources element. By default, this element has no attributes and only one type of sub-element. It is just a container for resourceType elements.



| Attribute Name | Description                                                                    |
|----------------|--------------------------------------------------------------------------------|
| resourceType   | Type of an individual resource contained in a language-specific resource file. |



 

## neutralResources Element

Neutral resources element. This element is just a container for resourceType elements.



| Attribute Name | Description                                        |
|----------------|----------------------------------------------------|
| resourceType   | Type of a single resource contained in an LN file. |



 

## resourceType Element

The resourceType element encapsulates information about a single resource type or individual resource. It has the attributes listed below.

> [!Caution]  
> Some resource configuration defects are caught only by RC Compiler or MUIRCT, depending on the input resource file or binary file content. The resourceType errors in the resource configuration file that do not exist in the input file are not caught, resulting in unexpected behavior. Users can be using a defective resource configuration file and do not know until they introduce binaries that use the broken parts of the resource configuration file, which creates the appearance that the breaks are from the current binaries.

 



| Attribute name | Mandatory | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| typeNameId     | Yes       | Type name or identifier for the resource. Specify a string name or a number. If using a number, prepend the string with a "\#" to indicate that it represents a number. Each resourceType element must have only one *typeNameId* attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| itemName       | No        | Item name string for the resource, to be placed in the language-specific resource file. You can specify multiple names, separated by white spaces, for example, "HTML MOFDATA".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| itemId         | No        | Identifier of individual resource item, to be placed in the language-specific resource file. The item can be specified as a range (for example, "1-12") or by individual identifiers separated by white spaces (for example, "1 3 4").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| stringId       | No        | String identifier for individual resource item, to be placed in the language-specific resource file. The string can be specified as a range (for example, "1-12") or by individual identifiers separated by white spaces (for example, "1 3 4").This attribute allows the specification of both localizable and nonlocalizable string table entries. It must be used in conjunction with the *typeNameId* value of "6", denoting a string table entry resource type.<br/> Strings are stored in blocks of 16 in a string table. For example, strings 0 to 15 are stored in a single resource item block and can be referenced in the resource configuration file as *itemId* 1, or as *stringId* "0-15". For example, if there are five localizable strings and three nonlocalizable strings, you should assign string identifiers 0-4 for the localizable strings, and string identifiers 16-18 for the nonlocalizable strings. If you do not organize strings this way, the affected blocks of strings are placed in both the LN file and the language-specific resource file.<br/> |



 

If you specify the *itemName*, *itemId*, and/or *stringId* attributes for a particular resource type under the localizedResource element, only these specified items or strings for the designated resource type are placed in the language-specific resource file. If a resourceType element is specified without any explicit item name, item identifier, or string identifier, all items of the specified resource type are placed in the language-specific resource file. Items or types not listed in any localizedResource element are placed in the LN file.

The following are the standard resource types and their numeric identifiers:

-   CURSOR(1)
-   BITMAP(2)
-   ICON(3)
-   MENU(4)
-   DIALOG(5)
-   STRING(6)
-   FONTDIR(7)
-   FONT(8)
-   ACCELERATORS(9)
-   RCDATA(10)
-   MESSAGETABLE(11)
-   GROUP\_CURSOR(12)
-   GROUP\_ICON(14)
-   VERSION(16)
-   HTML(23)

## Example


```C++
<?xml version="1.0" encoding="utf-8"?> 
<localization>
  <resources>
    <win32Resources fileType="Application">
      <neutralResources>
        <resourceType
           typeNameId="#16"
        />
      </neutralResources>
      <localizedResources> 
         <resourceType
                typeNameId="#2"
                itemId="5 6 7 8 9 10 11 12"
                itemName="HTML PRI"
         />
         <resourceType
                typeNameId="#4"
         />
         <resourceType
                typeNameId="#5"
         />
         <resourceType
                typeNameId="#6"
         />
         <resourceType
                typeNameId="#9"
         />
         <resourceType
                typeNameId="#11"
         />
         <resourceType
                typeNameId="#16"
         />
         <resourceType
                typeNameId="HTML"
         />
         <resourceType
                typeNameId="#23"
         />
         <resourceType
                typeNameId="#240"
         />
         <resourceType
                typeNameId="#1024"
         />
         <resourceType
                typeNameId="MY_TYPE"
         />
      </localizedResources> 
    </win32Resources>
  </resources>
</localization>
```



## Remarks

If you include any ICON(3), DIALOG(5), STRING(6), or VERSION(16) resource type in the neutralResources element, then you have to duplicate that entry in the localizedResources element. You can see this illustrated in the example above, where resource type 16 appears in both neutral and localized resources sections.

## Related topics

<dl> <dt>

[Preparing Resources](preparing-resources.md)
</dt> </dl>

 

 




