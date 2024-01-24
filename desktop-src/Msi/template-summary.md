---
description: For an installation package, the Template Summary property indicates the platform and language versions that are compatible with this installation database.
ms.assetid: a1015ddb-8d5c-40f7-97ac-4a1347644ae6
title: Template Summary property
ms.topic: reference
ms.date: 05/31/2018
---

# Template Summary property

For an installation package, the **Template Summary** property indicates the platform and language versions that are compatible with this installation database. The syntax of the **Template Summary** property information for an installation database is the following:

\[*platform property*\];\[*language id*\]\[,*language id*\]\[,...\].

The following examples are valid values for the **Template Summary** property:

-   x64;1033
-   Intel;1033
-   Intel64;1033
-   ;1033
-   Intel ;1033,2046
-   Intel64;1033,2046
-   Intel;0
-   Arm;1033,2046
-   Arm;0
-   Arm64;1033,2046
-   Arm64;0

The **Template Summary** property of a transform indicates the platform and language versions compatible with the transform. In a transform file, only one language may be specified. The specified platform and language determine whether a transform can be applied to a particular database. The platform property and the language property can be left blank if no transform restriction relies on them to validate the transform.

The **Template Summary** property of a patch package is a semicolon-delimited list of the product codes that can accept the patch. If you use [Msimsp.exe](msimsp-exe.md) and [Patchwiz.dll](patchwiz-dll.md) to generate the patch package, this list is obtained from the [TargetImages table](targetimages-table-patchwiz-dll-.md) of the patch creation file.

This summary property is required.

## Remarks

If the current platform does not match one of the platforms specified in the **Template Summary** property then the installer does not process the package.

If the platform specification is missing in the **Template Summary** property value, the installer assumes the Intel architecture.

If this is a 64-bit Windows Installer package being run on an Intel64 (Itanium) platform, enter Intel64 in the **Template Summary** property.

If this is a 64-bit Windows Installer package being run on a x64 platform, enter x64 in the **Template Summary** property.

If this is a 64-bit Windows Installer package being run on an Arm64 platform, enter Arm64 in the **Template Summary** property.

A Windows Installer package cannot be marked as supporting both Intel64 and x64; for example, the **Template Summary** property value of Intel64,x64 is invalid.

A Windows Installer package cannot be marked as supporting both 32-bit and 64-bit platforms; for example, **Template Summary** property values such as Intel,x64 or Intel,Intel64 are invalid.

Entering 0 (zero) in the language ID field of the **Template Summary** property, or leaving this field empty, indicates that the package is language neutral.

If this is a Windows Installer package being run on Windows RT, enter the value Arm in the **Template Summary** property.

Merge Modules are the only packages that may have multiple languages. Only one language can be specified in a source installer database. For more information, see [Multiple Language Merge Modules](multiple-language-merge-modules.md).

The Alpha platform is not supported by Windows Installer.

**Windows Installer:** The following syntax is not supported:

\[*platform property*\]\[,*platform property*\]\[,...\]\[*language id*\]\[,*language id*\]\[,...\].

The following examples are not valid values for the **Template Summary** property:

-   Alpha,Intel;1033
-   Intel,Alpha;1033
-   Alpha;1033
-   Alpha;1033,2046

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |



## See also

<dl> <dt>

[Summary Property Descriptions](summary-property-descriptions.md)
</dt> </dl>

 

 




