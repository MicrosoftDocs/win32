---
description: The ProductLanguage property specifies the language the installer should use for any strings in the user interface that are not authored into the database.
ms.assetid: 5d798825-c70b-4d5a-b88c-a9db40663f6a
title: ProductLanguage property
ms.topic: reference
ms.date: 05/31/2018
---

# ProductLanguage property

The **ProductLanguage** property specifies the language the installer should use for any strings in the user interface that are not authored into the database. This property must be a numeric language identifier (LANGID). If a transform changes the language of the user interface in the database, then it should also change the value of this property to reflect the new language.

This property is REQUIRED.

## Remarks

The value of the **ProductLanguage** property must be one of the languages listed in the [**Template Summary**](template-summary.md) property.

When authoring a package as language-neutral, set the **ProductLanguage** property to 0 and use the MS Shell Dlg font as the text style for all authored dialogs. Because some fonts do not support all the character sets, by using this font you can ensure that the text is correctly displayed on all localized versions of the operating system.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




