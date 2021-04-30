---
description: The Shortcut table holds the information the application needs to create shortcuts on the user's computer.
ms.assetid: 86b5b51e-e5f4-4f42-84f9-1faa29ea7a84
title: Shortcut Table
ms.topic: article
ms.date: 05/31/2018
---

# Shortcut Table

The Shortcut table holds the information the application needs to create shortcuts on the user's computer.

The Shortcut table has the following columns.



| Column                 | Type                         | Key | Nullable |
|------------------------|------------------------------|-----|----------|
| Shortcut               | [Identifier](identifier.md) | Y   | N        |
| Directory\_            | [Identifier](identifier.md) | N   | N        |
| Name                   | [Filename](filename.md)     | N   | N        |
| Component\_            | [Identifier](identifier.md) | N   | N        |
| Target                 | [Shortcut](shortcut.md)     | N   | N        |
| Arguments              | [Formatted](formatted.md)   | N   | Y        |
| Description            | [Text](text.md)             | N   | Y        |
| Hotkey                 | [Integer](integer.md)       | N   | Y        |
| Icon\_                 | [Identifier](identifier.md) | N   | Y        |
| IconIndex              | [Integer](integer.md)       | N   | Y        |
| ShowCmd                | [Integer](integer.md)       | N   | Y        |
| WkDir                  | [Identifier](identifier.md) | N   | Y        |
| DisplayResourceDLL     | [Formatted](formatted.md)   | N   | Y        |
| DisplayResourceId      | [Integer](integer.md)       | N   | Y        |
| DescriptionResourceDLL | [Formatted](formatted.md)   | N   | Y        |
| DescriptionResourceId  | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Shortcut"></span><span id="shortcut"></span><span id="SHORTCUT"></span>Shortcut
</dt> <dd>

The key value for this table.

</dd> <dt>

<span id="Directory_"></span><span id="directory_"></span><span id="DIRECTORY_"></span>Directory\_
</dt> <dd>

The external key into the first column of the [Directory table](directory-table.md). This column specifies the directory in which the Shortcut file is created.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

The localizable name of the shortcut to be created.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

The external key into the first column of the [Component table](component-table.md). The installer uses the installation state of the component specified in this column to determine whether the shortcut is created or deleted. This component must have a valid key path for the shortcut to be installed. If the Target column contains the name of a feature, the file launched by the shortcut is the key file of the component listed in this column.

</dd> <dt>

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>Target
</dt> <dd>

The shortcut target.

For an advertised shortcut, this column must be an external key into the first column of the [Feature table](feature-table.md). The installer evaluates the entry in the Target field as an [Identifier](identifier.md) and the entry must be a valid foreign key into the [Feature Table](feature-table.md). The file launched by the shortcut in this case is the key file of the component listed in the Component\_ column. When the shortcut is activated, the installer verifies that all the components in the feature are installed before launching this file.

For a non-advertised shortcut, the installer evaluates this field as a [Formatted](formatted.md) string. The field should contains a property identifier enclosed by square brackets (\[ \]), that is expanded into the file or a folder pointed to by the shortcut. For more information, see the [CreateShortcuts action](createshortcuts-action.md).

</dd> <dt>

<span id="Arguments"></span><span id="arguments"></span><span id="ARGUMENTS"></span>Arguments
</dt> <dd>

The command-line arguments for the shortcut.

Note that the resolution of properties in the Arguments field is limited. A property formatted as \[*Property*\] in this field can only be resolved if the property already has the intended value when the component that owns the shortcut is installed. For example, to resolve to the correct value for the argument "\[\#MyDoc.doc\]", the same process must be installing the file MyDoc.doc and the component that owns the shortcut.

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

The localizable description of the shortcut.

</dd> <dt>

<span id="Hotkey"></span><span id="hotkey"></span><span id="HOTKEY"></span>Hotkey
</dt> <dd>

The hotkey for the shortcut. The low-order byte contains the virtual-key code for the key, and the high-order byte contains modifier flags. This must be a non-negative number. Authors of installation packages are generally recommended not to set this option, because the setting of this option can add duplicate hotkeys to a user's desktop. In addition, the practice of assigning hotkeys to shortcuts can be problematic for users using hotkeys for [accessibility](accessibility.md).

</dd> <dt>

<span id="Icon_"></span><span id="icon_"></span><span id="ICON_"></span>Icon\_
</dt> <dd>

The external key to column one of the [Icon table](icon-table.md).

</dd> <dt>

<span id="IconIndex"></span><span id="iconindex"></span><span id="ICONINDEX"></span>IconIndex
</dt> <dd>

The icon index for the shortcut. This must be a non-negative number.

</dd> <dt>

<span id="ShowCmd"></span><span id="showcmd"></span><span id="SHOWCMD"></span>ShowCmd
</dt> <dd>

The Show command for the application window.

The following values may be used. The values are as defined for the Windows API function ShowWindow.



| Value | Meaning             |
|-------|---------------------|
| 1     | SW\_SHOWNORMAL      |
| 3     | SW\_SHOWMAXIMIZED   |
| 7     | SW\_SHOWMINNOACTIVE |



 

</dd> <dt>

<span id="WkDir"></span><span id="wkdir"></span><span id="WKDIR"></span>WkDir
</dt> <dd>

The name of the property that has the path of the working directory for the shortcut. The value can use the Windows format to reference environment variables, for example %USERPROFILE%. The references are resolved to an actual path when the installer resolves the working directory to create the shortcut.

</dd> </dl>

<dl> <dt>

<span id="DisplayResourceDLL"></span><span id="displayresourcedll"></span><span id="DISPLAYRESOURCEDLL"></span>DisplayResourceDLL
</dt> <dd>

This field contains a [Formatted](formatted.md) string value for the full path to the language-neutral portable executable (LN file) that contains the resource configuration (RC Config) data. The formatted string can use the \[\#filekey\] convention. If this field contains a value, the Name column is ignored. If this field is empty, the installer uses the value in the Name column. When this field contains a value, the **DisplayResourceId** field is also required to contain a value, or the installation fails.

This column of the Shortcut table is used only when running on Windows Vista or Windows Server 2008 and is otherwise ignored. This column is available with versions not earlier than Windows Installer 4.0.

For information about how to add shortcuts to Shortcut table for use with MUI resources see [A MUI Shortcut Example](a-mui-shortcut-example.md).

</dd> <dt>

<span id="DisplayResourceId"></span><span id="displayresourceid"></span><span id="DISPLAYRESOURCEID"></span>DisplayResourceId
</dt> <dd>

The display name index for the shortcut. This must be a non-negative number. When this field contains a value, the **DisplayResourceDLL** field is required to also contain a value or the installation fails.

This column of the Shortcut table is used only when running on Windows Vista or Windows Server 2008 and is otherwise ignored. This column is available with versions not earlier than Windows Installer 4.0.

</dd> <dt>

<span id="DescriptionResourceDLL"></span><span id="descriptionresourcedll"></span><span id="DESCRIPTIONRESOURCEDLL"></span>DescriptionResourceDLL
</dt> <dd>

This field contains a [Formatted](formatted.md) string value for the full path to the language-neutral portable executable (LN file) that contains the resource configuration (RC Config) data. The formatted string can use the \[\#filekey\] convention. If this field contains a value, the Name column is ignored. If this field is empty, the installer uses the value in the Description column. When this field contains a value, the **DescriptionResourceId** field is also required to contain a value, or the installation fails.

This column of the Shortcut table is used only when running on Windows Vista or Windows Server 2008 and is otherwise ignored. This column is available with versions not earlier than Windows Installer 4.0.

For information about how to add shortcuts to Shortcut table for use with MUI resources see [A MUI Shortcut Example](a-mui-shortcut-example.md).

</dd> <dt>

<span id="DescriptionResourceId"></span><span id="descriptionresourceid"></span><span id="DESCRIPTIONRESOURCEID"></span>DescriptionResourceId
</dt> <dd>

The description name index for the shortcut. This must be a non-negative number. When this field contains a value, the **DescriptionResourceDLL** field is required to also contain a value or the installation fails.

This column of the Shortcut table is used only when running on Windows Vista or Windows Server 2008 and is otherwise ignored. This column is available with versions not earlier than Windows Installer 4.0.

</dd> </dl>

## Remarks

The enabling of a feature creates an advertised shortcut only if the system's IShellLink interface supports installer descriptor resolution. This is supported by Microsoft Windows 2000 and systems running Microsoft Internet Explorer 4.01. If unsupported, the installer creates a non-advertised shortcut upon the installation of the feature's component, either locally or run from source.

Note that advertised shortcuts always point at a particular application, identified by a [**ProductCode**](productcode.md), and should not be shared between applications. Advertised shortcuts only work for the most recently installed application, and are removed when that application is removed.

This table is referred to when the [CreateShortcuts action](createshortcuts-action.md) and the [RemoveShortcuts action](removeshortcuts-action.md) is executed.

See also the [**DISABLEADVTSHORTCUTS**](disableadvtshortcuts.md) property.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE19](ice19.md)  
[ICE32](ice32.md)  
[ICE36](ice36.md)  
[ICE46](ice46.md)  
[ICE50](ice50.md)  
[ICE57](ice57.md)  
[ICE59](ice59.md)  
[ICE67](ice67.md)  
[ICE69](ice69.md)  
[ICE80](ice80.md)  
[ICE90](ice90.md)  
[ICE91](ice91.md)  
[ICE94](ice94.md)  
</dl>

 

 



