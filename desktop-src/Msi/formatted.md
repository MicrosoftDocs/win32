---
description: The Formatted data type is a text string that is processed to resolve embedded property names, table keys, environment variable references, and other special substrings.
ms.assetid: 7a1bc160-a06c-4d57-b429-e39167893a45
title: Formatted
ms.topic: article
ms.date: 05/31/2018
---

# Formatted

The Formatted data type is a text string that is processed to resolve embedded property names, table keys, environment variable references, and other special substrings. The following conventions are recognized to resolve the string:

-   Square brackets (\[ \]) or curly braces ({ }) with no matching pair are left in the text.
-   If a substring of the form \[*propertyname*\] is encountered, it is replaced by the value of the property. If *propertyname* is not a valid property name, then the substring resolves as blank. For example, the Description column of the [LaunchCondition Table](launchcondition-table.md) takes a Formatted string. If ERRORTXT has been set to "Please contact your support personnel." then the text displayed for failing the launch condition would include this string. If ERRORTXT is not set then the text displayed for failing the launch condition would be just "System does not meet installation requirements."

    

    | Condition | Description                                                  |
    |-----------|--------------------------------------------------------------|
    | Version9X | System does not meet installation requirements. \[ERRORTXT\] |

    

     

-   The square brackets may be iterated and the property names are resolved from inside out. For example, suppose the substring \[\[PropertyA\]\] appears in the text. First, the value of property PropertyA is retrieved. If the value is a valid property name, such as PropertyB, then the value of PropertyB is retrieved, and the entire substring \[\[PropertyA\]\] is substituted with the value of PropertyB. If PropertyA is not a valid property name, or if the value of PropertyA is not a valid property name, then the substring is blank.
-   If a substring of the form \[%*environmentvariable*\] is found, the value of the environment variable is substituted for the substring.
-   If a substring of the form \[\\*x*\] is found, it is replaced by the character *x* , where *x* is one character, without any further processing. Only the first character after the backslash is kept; everything else is removed. For example, to include a literal left bracket (\[), use \[\\\[\]. The text \[\\\[\]Bracket Text\[\\\]\] resolves to \[Bracket Text\].
-   If a substring is enclosed in curly braces ({ }), and it contains no property names enclosed in square brackets (\[ \]), the substring is left unchanged, including the curly braces.
-   If a substring is enclosed in curly braces ({ }) and it contains one or more property names enclosed in square brackets (\[ \]) then, if all the property names are valid, the text (with the resolved substitutions) is displayed without the curly braces.
-   If a substring of the form \[~\] is found, it is replaced with the null character. This is used to author **REG\_MULTI\_SZ** character strings in the [Registry table](registry-table.md). Note that \[~\] is also used to append or prefix values to environment variables using the [Environment table](environment-table.md).
-   If a substring of the form \[\#*filekey*\] is found, it is replaced by the full path of the file, with the value *filekey* used as a key into the [File table](file-table.md). The value of \[\#*filekey*\] remains blank and is not replaced by a path until the installer runs the [CostInitialize action](costinitialize-action.md), [FileCost action](filecost-action.md), and [CostFinalize action](costfinalize-action.md). The value of \[\#*filekey*\] depends upon the installation state of the component to which the file belongs. If the component is run from the source, the value is the path to the source location of the file. If the component is run locally, the value is the path to the target location of the file after installation. If the component has an action state of absent, the installed state of the component is used to determine the \[\).
-   If a substring of the form \[$*componentkey*\] is found, it is replaced by the install directory of the component, with the value *componentkey* used as a key into the [Component table](component-table.md). The value of \[$*componentkey*\] remains blank and is not replaced by a directory until the installer runs the [CostInitialize action](costinitialize-action.md), [FileCost action](filecost-action.md), and [CostFinalize action](costfinalize-action.md). The value of \[$*componentkey*\] depends upon the installation state of the component and where it occurs. In the Value column of the [Registry Table](registry-table.md), this substring may refer to the action state or the requested action state of the component. In all other cases, this substring refers to the action state of the component. For example, if the component is run from the source, the value is the source directory of the file. If the component is run locally, the value is the target directory after installation. If the component is absent, the value is left blank. Windows Installer tracks both the action and requested installation states of components. For example, if a component is already installed, it may have a requested state of local and an action state of null. For more information about checking the installation state of components, see [Checking the Installation of Features, Components, Files](checking-the-installation-of-features-components-files.md).
-   Note that if a component is already installed, and is not reinstalled, removed, or moved during the current installation, the action state of the component is null and the string \[$*componentkey*\] evaluates to Null.
-   If a substring of the form \[!*filekey*\] is found, it is replaced by the full short path of the file, with the value *filekey* used as a key into the [File table](file-table.md).

    This syntax is valid only when used in the Value column of the Registry or the IniFile tables. When used in other columns this syntax is treated the same as \[\#*filekey*\] .

 

 



