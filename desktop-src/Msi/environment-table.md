---
description: The Environment table is used to set the values of environment variables.
ms.assetid: f7106ed6-706f-4e57-989f-030066bcecd3
title: Environment Table
ms.topic: article
ms.date: 05/31/2018
---

# Environment Table

The Environment table is used to set the values of environment variables.

The Environment table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Environment | [Identifier](identifier.md) | Y   | N        |
| Name        | [Text](text.md)             | N   | N        |
| Value       | [Formatted](formatted.md)   | N   | Y        |
| Component\_ | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment
</dt> <dd>

This is the primary key of the table and is a non-localized token.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

This column is the localizable name of the environment variable. The key values are written or removed depending upon which of the characters in the following table are prefixed to the name. There is no effect in the ordering of the symbols used in a prefix.



| Prefix                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| =                              | Create the environment variable if it does not exist, and then set it during installation. If the environment variable exists, set it during the installation.                                                                                                                                                                                                                                                                                                                                   |
| \+                             | Create the environment variable if it does not exist, then set it during installation. This has no effect on the value of the environment variable if it already exists.                                                                                                                                                                                                                                                                                                                         |
| \-                             | Remove the environment variable when the component is removed. This symbol can be combined with any prefix.                                                                                                                                                                                                                                                                                                                                                                                      |
| !                              | Remove the environment variable during an installation. The installer only removes an environment variable during an installation if the name and value of the variable match the entries in the Name and Value fields of the Environment table. If you want to remove an environment variable, regardless of its value, use the '!' syntax, and leave the Value field empty.                                                                                                                    |
| \*                             | This prefix is used with Windows 2000 to indicate that the name refers to a system environment variable. If no asterisk is present, the installer writes the variable to the user's environment. This symbol can be combined with any prefix. A package that is used for installation in the per-machine [installation context](installation-context.md) should write environment variables to the machine's environment by including \* in the Name column. For more information, see Remarks. |
| =-                             | The environment variable is set on install and removed on uninstall. This is the usual behavior.                                                                                                                                                                                                                                                                                                                                                                                                 |
| !-                             | Removes an environment variable during an install or uninstall.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| =+ !+<br/> !=<br/> | These are not a valid prefixes                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |



 

If the Value field in the table includes a \[~\], then the prefix characters apply to only the specified portion of the string. The use of \[~\] is described below in the Value column section.

The environment variable is removed if the Value field of the table is blank. Therefore, with a blank in the Value field, an = prefix deletes the environment variable on install and a - prefix deletes any current values on uninstall.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

This column contains the localizable value that is to be set as a formatted string. See [Formatted](formatted.md). If this field is left blank, the variable is removed. If the field is blank and the string in the Name field is prefixed by the - symbol, the variable is removed only when the component is removed.

To append a value to the end of an existing variable, prefix the string in this field by the Null character \[~\] and the separator character. For example, if the semicolon is the chosen separator: \[~\];*Value*.

To prefix a value to the front of an existing variable, append the string in this field by the separator character and the Null character \[~\]. For example, if the semicolon is the chosen separator: *Value*;\[~\] .

If no \[~\] is present in the field, the string represents the entire value to be set or deleted.

Each row can contain only one value. For example, the entry *Value*;*Value*;\[~\] is more than one value and should not be used because it causes unpredictable results. The entry *Value*;\[~\] is just one value.

If Name is prefixed with +, then \[~\] must not be used in Value column. This is because the meaning of "+" and "\[~\]" are clearly exclusive of one another.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

An external key to the first column of the [Component table](component-table.md). This column references the component that controls the installation of the environment values.

</dd> </dl>

## Remarks

For the installer to set environment variables, the [WriteEnvironmentStrings action](writeenvironmentstrings-action.md) and [RemoveEnvironmentStrings action](removeenvironmentstrings-action.md) need to be listed in the [InstallExecuteSequence Table](installexecutesequence-table.md).

Note that environment variables do not change for the installation in progress when either the [WriteEnvironmentStrings action](writeenvironmentstrings-action.md) or [RemoveEnvironmentStrings action](removeenvironmentstrings-action.md) are run. On Windows 2000, this information is stored in the registry and a message notifies the system of changes when the installation completes. A new process, or another process that checks for these messages, uses the new environment variables.

When modifying the path environment variable with the Environment table, do not attempt to enter the entire new path explicitly into the Value field. Instead, extend the existing path by prefixing or appending a value and delimiter (;) to \[~\]. If \[~\] is not present in the Value field, the existing path information is lost and installing the .msi file may prevent the computer from booting. The path variable is mostly commonly set using the syntax: \[~\];Value.

When performing per-machine installations from a terminal server, the installer writes per-user environment variables to **HKU\\.Default\\Environment**. Because Terminal Services does not replicate this section of the registry, the installation does not set the per-user environment variables. A package used for per-machine installations should write environment variables to the computer's environment by including \* in the Name column. If the package can be installed per-user or per-machine, create two components: (1) a per-user component with the Environment table entries authored for user settings, and (2) a per-machine component with the Environment table authored for computer settings. Condition the installation of this component using the [**Privileged**](privileged.md) property.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE46](ice46.md)  
[ICE65](ice65.md)  
[ICE69](ice69.md)  
[ICE80](ice80.md)  
</dl>

 

 




