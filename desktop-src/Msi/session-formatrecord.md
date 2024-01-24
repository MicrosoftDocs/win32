---
description: The FormatRecord method of the Session object returns a formatted string from a template and record data.
ms.assetid: 2018ac75-ea18-4256-8d56-0527069ce24b
title: Session.FormatRecord method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.FormatRecord
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.FormatRecord method

The **FormatRecord** method of the [**Session**](session-object.md) object returns a formatted string from a template and record data.

## Syntax


```JScript
Session.FormatRecord(
  record
)
```



## Parameters

<dl> <dt>

*record* 
</dt> <dd>

Required **Record** object containing a template and data to be formatted. The template string must be set in field 0 followed by any referenced data parameters.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The **FormatRecord** method uses the following format process.

Parameters to be [formatted](formatted.md) are enclosed in square brackets \[..\]. The square brackets can be iterated because the substitutions are resolved from inside out.

If a part of the string is enclosed in curly braces { } and contains no square brackets, the part is left unchanged, including the curly braces.

If a part of the string is enclosed in curly braces and contains one or more property names, and if all the properties are found, the text (with the resolved substitutions) is displayed without the curly braces. If any of the properties are not found, all the text in the curly braces and the braces themselves are removed.

**To format strings using the FormatRecord method**

1.  The numeric parameters are substituted by replacing the marker with the value of the corresponding record field, with missing or Null values producing no text.
2.  The string that results is processed by replacing the non-record parameters with the corresponding values, as noted in the following descriptions.
    -   If a substring of the form "\[propertyname\]" is encountered, it is replaced by the value of the property.
    -   If a substring of the form "\[%environmentvariable\]" is found, the value of the environment variable is substituted.
    -   If a substring of the form \[\#*filekey*\] is found, it is replaced by the full path of the file, with the value *filekey* used as a key into the [File table](file-table.md). The value of \[\#*filekey*\] remains blank and is not replaced by a path until the installer runs the [CostInitialize action](costinitialize-action.md), [FileCost action](filecost-action.md), and [CostFinalize action](costfinalize-action.md). The value of \[\#*filekey*\] depends upon the installation state of the component to which the file belongs. If the component is being run from source, the value is the path to the source location of the file. If the component is being run locally, the value is the path to the target location of the file after installation. If the component is absent, the path is blank. For more information about checking the installation state of components, see [Checking the Installation of Features, Components, Files](checking-the-installation-of-features-components-files.md).
    -   If a substring of the form \[*$componentkey*\] is found, it is replaced by the install directory of the component, with the value *componentkey* used as a key into the [Component table](component-table.md). The value of \[$*componentkey*\] remains blank and is not replaced by a directory until the installer runs the [CostInitialize action](costinitialize-action.md), [FileCost action](filecost-action.md), and [CostFinalize action](costfinalize-action.md). The value of \[$*componentkey*\] depends upon the installation state of the component. If the component is being run from source, the value is the source directory of the file. If the component is being run locally, the value is the target directory after installation. If the component is absent, the value is left blank. For more information about checking the installation state of components, see [Checking the Installation of Features, Components, Files](checking-the-installation-of-features-components-files.md).
    -   If a substring of the form "\[\\c\]" is found, it is replaced by the character without any further processing. Only the first character after the backslash is kept; everything else is removed.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



## See also

<dl> <dt>

[Formatted](formatted.md)
</dt> <dt>

[Column Data Types](column-data-types.md)
</dt> </dl>

 

 




