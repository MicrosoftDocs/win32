---
description: The CustomAction table provides the means of integrating custom code and data into the installation. The source of the code that is executed can be a stream contained within the database, a recently installed file, or an existing executable file.
ms.assetid: '0f47abc1-4e06-4ddc-9ea1-9afb9f27d499'
title: CustomAction Table
ms.topic: article
ms.date: 05/31/2018
---

# CustomAction Table

The CustomAction table provides the means of integrating custom code and data into the installation. The source of the code that is executed can be a stream contained within the database, a recently installed file, or an existing executable file.

The CustomAction table has the following columns.



| Column       | Type                               | Key | Nullable |
|--------------|------------------------------------|-----|----------|
| Action       | [Identifier](identifier.md)       | Y   | N        |
| Type         | [Integer](integer.md)             | N   | N        |
| Source       | [CustomSource](customsource.md)   | N   | Y        |
| Target       | [Formatted](formatted.md)         | N   | Y        |
| ExtendedType | [DoubleInteger](doubleinteger.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Action"></span><span id="action"></span><span id="ACTION"></span>Action
</dt> <dd>

Name of the action. The action normally appears in a sequence table unless it is called by another custom action. If the name matches any built-in action, then the custom action is never called.

Primary table key.

</dd> <dt>

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>Type
</dt> <dd>

A field of flag bits specifying the basic type of custom action and options. See [Summary List of All Custom Action Types](summary-list-of-all-custom-action-types.md) for a list of the basic types. See [Custom Action Return Processing Options](custom-action-return-processing-options.md), [Custom Action Execution Scheduling Options](custom-action-execution-scheduling-options.md), [Custom Action Hidden Target Option](custom-action-hidden-target-option.md), and [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md).

</dd> <dt>

<span id="Source"></span><span id="source"></span><span id="SOURCE"></span>Source
</dt> <dd>

A property name or external key into another table. For a discussion of the possible custom action sources, see [Custom Action Sources](custom-action-sources.md) and the [Summary List of All Custom Action Types](summary-list-of-all-custom-action-types.md). For example, the Source column may contain an external key into the first column of one of the following tables containing the source of the custom action code.

[Directory table](directory-table.md) for calling existing executables.

[File table](file-table.md) for calling executables and DLLs that have just been installed.

[Binary table](binary-table.md) for calling executables, DLLs, and data stored in the database.

[Property table](property-table.md) for calling executables whose paths are held by a property.

</dd> <dt>

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>Target
</dt> <dd>

An execution parameter that depends on the basic type of custom action. See the [Summary List of All Custom Action Types](summary-list-of-all-custom-action-types.md) for a description of what should be entered in this field for each type of custom action. For example, this field may contain the following depending on the custom action.



| Target                                    | Custom action                         |
|-------------------------------------------|---------------------------------------|
| Entry point (required)                    | Calling a DLL.                        |
| Executable name with arguments (required) | Calling an existing executable.       |
| Command line arguments (optional)         | Calling an executable just installed. |
| Target file name (required)               | Creating a file from custom data.     |
| Null                                      | Executing script code.                |



 

</dd> <dt>

<span id="ExtendedType"></span><span id="extendedtype"></span><span id="EXTENDEDTYPE"></span>ExtendedType
</dt> <dd>

Enter the **msidbCustomActionTypePatchUninstall** value in this field to specify a custom action with the [Custom Action Patch Uninstall Option](custom-action-patch-uninstall-option.md).

**[Windows Installer 4.0 and earlier](not-supported-in-windows-installer-4-0.md):** Not supported. This option is available beginning with Windows Installer 4.5.

</dd> </dl>

For more information, see all the topics under [Custom Actions](custom-actions.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE12](ice12.md)  
[ICE27](ice27.md)  
[ICE46](ice46.md)  
[ICE63](ice63.md)  
[ICE68](ice68.md)  
[ICE72](ice72.md)  
[ICE75](ice75.md)  
[ICE77](ice77.md)  
[ICE80](ice80.md)  
[ICE88](ice88.md)  
[ICE93](ice93.md)  
</dl>

 

 



