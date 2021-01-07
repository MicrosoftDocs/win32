---
description: The Registry table holds the registry information that the application needs to set in the system registry.
ms.assetid: 809ffd02-cf97-42d8-aed9-c13a14dcd8b4
title: Registry Table
ms.topic: article
ms.date: 05/31/2018
---

# Registry Table

The Registry table holds the registry information that the application needs to set in the system registry.

The Registry table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Registry    | [Identifier](identifier.md) | Y   | N        |
| Root        | [Integer](integer.md)       | N   | N        |
| Key         | [RegPath](regpath.md)       | N   | N        |
| Name        | [Formatted](formatted.md)   | N   | Y        |
| Value       | [Formatted](formatted.md)   | N   | Y        |
| Component\_ | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="Registry"></span><span id="registry"></span><span id="REGISTRY"></span>Registry
</dt> <dd>

Primary key used to identify a registry record.

</dd> <dt>

<span id="Root"></span><span id="root"></span><span id="ROOT"></span>Root
</dt> <dd>

The predefined root key for the registry value. Enter a value of -1 in this field to make the root key dependent on the type of installation. Enter one of the other values in the following table to force the registry value to be written under a particular root key.



| Constant                          | Hexadecimal | Decimal | Root key                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------|-------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| (none)                            | \- 0x001    | -1      | If this is a per-user installation, the registry value is written under **HKEY\_CURRENT\_USER**. If this is a per-machine installation, the registry value is written under **HKEY\_LOCAL\_MACHINE**. Note that a per-machine installation is specified by setting the [**ALLUSERS**](allusers.md) property to 1.<br/>                |
| **msidbRegistryRootClassesRoot**  | 0x000       | 0       | **HKEY\_CLASSES\_ROOT**The installer writes or removes the value from the **HKCU\\Software\\Classes** hive during installation in the per-user [installation context](installation-context.md).<br/> The installer writes or removes the value from the **HKLM\\Software\\Classes** hive during per-machine installations.<br/> |
| **msidbRegistryRootCurrentUser**  | 0x001       | 1       | **HKEY\_CURRENT\_USER**                                                                                                                                                                                                                                                                                                                      |
| **msidbRegistryRootLocalMachine** | 0x002       | 2       | **HKEY\_LOCAL\_MACHINE**                                                                                                                                                                                                                                                                                                                     |
| **msidbRegistryRootUsers**        | 0x003       | 3       | **HKEY\_USERS**                                                                                                                                                                                                                                                                                                                              |



 

Note that it is recommended that registry entries written to the **HKCU** hive reference a component having the RegistryKeyPath bit set in the Attributes column of the [Component table](component-table.md). This ensures that the installer writes the necessary registry entries when there are multiple users on the same computer.

</dd> <dt>

<span id="Key"></span><span id="key"></span><span id="KEY"></span>Key
</dt> <dd>

The localizable key for the registry value.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

This column contains the registry value name (localizable). If this is Null, then the data entered into the Value column are written to the default registry key.

If the Value column is Null, then the strings shown in the following table in the Name column have special significance.



| String | Meaning                                                                                                                                                                                          |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \+     | The key is to be created, if absent, when the component is installed.                                                                                                                            |
| \-     | The key is to be deleted, if present, with all of its values and subkeys, when the component is uninstalled.                                                                                     |
| \*     | The key is to be created, if absent, when the component is installed. Additionally, the key is to be deleted, if present, with all of its values and subkeys, when the component is uninstalled. |



 

Note that the [RemoveRegistry table](removeregistry-table.md) must be used if an installed registry key is to be deleted, with its values and subkeys, when the component is installed.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

This column is the localizable registry value. The field is [Formatted](formatted.md). If the value is attached to one of the following prefixes (i.e. \#%*value*) then the value is interpreted as described in the table. Note that each prefix begins with a number sign (\#). If the value begins with two or more consecutive number signs (\#), the first \# is ignored and value is interpreted and stored as a string.



| Prefix | Meaning                                                                        |
|--------|--------------------------------------------------------------------------------|
| \#x    | The value is interpreted and stored as a hexadecimal value (REG\_BINARY).      |
| \#%    | The value is interpreted and stored as an expandable string (REG\_EXPAND\_SZ). |
| \#     | The value is interpreted and stored as an integer (REG\_DWORD).                |



 

-   If the value contains the sequence tilde \[~\], then the value is interpreted as a Null-delimited list of strings (REG\_MULTI\_SZ). For example, to specify a list containing the three strings a, b and c, use "a\[~\]b\[~\]c".
-   The sequence \[~\] within the value separates the individual strings and is interpreted and stored as a Null character.
-   If a \[~\] precedes the string list, the strings are to be appended to any existing registry value strings. If an appending string already occurs in the registry value, the original occurrence of the string is removed.
-   If a \[~\] follows the end of the string list, the strings are to be prepended to any existing registry value strings. If a prepending string already occurs in the registry value, the original occurrence of the string is removed.
-   If a \[~\] is at both the beginning and the end or at neither the beginning nor the end of the string list, the strings are to replace any existing registry value strings.
-   Otherwise, the value is interpreted and stored as a string (REG\_SZ).

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key into the first column of the [Component table](component-table.md) referencing the component that controls the installation of the registry value.

</dd> </dl>

## Remarks

The [WriteRegistryValues](writeregistryvalues-action.md) and [RemoveRegistryValues](removeregistryvalues-action.md) actions in [*sequence tables*](s-gly.md) process the information in this table. For information about using *sequence tables*, see [Using a Sequence Table](using-a-sequence-table.md).

The registry information is written out to the system registry when the corresponding component has been selected to be installed locally or run from source.

Note that the installer removes a registry key after removing the last value or subkey under the key. To prevent an empty registry key from being removed when uninstalling, write a dummy value under the key you need to keep and enter + in the Name column. If \* is in the Name column, the key is deleted, with all of its values and subkeys, when the component is removed.

A custom action can be used to add rows to the Registry table during an installation, uninstallation, or repair transaction. These rows do not persist in the Registry table and the information is only available during the current transaction. The custom action must therefore be run in every installation, uninstallation, or repair transaction that requires the information in these additional rows. The custom action must come before the [RemoveRegistryValues](removeregistryvalues-action.md) and [WriteRegistryValues](writeregistryvalues-action.md) actions in the action sequence.

For information on how to secure a registry key see the [MsiLockPermissionsEx Table](msilockpermissionsex-table.md) and [LockPermissions Table](lockpermissions-table.md).

## Validation

<dl>

[ICE02](ice02.md)  
[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE38](ice38.md)  
[ICE43](ice43.md)  
[ICE46](ice46.md)  
[ICE49](ice49.md)  
[ICE53](ice53.md)  
[ICE55](ice55.md)  
[ICE57](ice57.md)  
[ICE70](ice70.md)  
[ICE80](ice80.md)  
</dl>

 

 




