---
description: Use this table to author a multiple-package installation.
ms.assetid: ac1e9c7b-bb83-4e1e-9108-211374c7d878
title: MsiEmbeddedChainer Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiEmbeddedChainer Table

Use this table to author a [multiple-package installation](multiple-package-installations.md). Each row in the MsiEmbeddedChainer table references a different user-defined function that can be used to install multiple Windows Installer packages from a single package. The [executable files](executable-files.md) for the user-defined functions are stored inside the Windows Installer package.

**[Windows Installer 4.0 or earlier](not-supported-in-windows-installer-4-0.md):** Not supported. This table is available beginning with Windows Installer 4.5.

**Windows Server 2008 R2 with the [Remote Desktop Services](../termserv/terminal-services-portal.md) role enabled:** Not supported. A multiple package installation using the MsiEmbeddedChainer table fails if the [Remote Desktop Services](../termserv/terminal-services-portal.md) role is enabled.

To install multiple packages from a single package, one of the user-defined functions listed in the MsiEmbeddedChainer table must have a conditional statment in the Condition field that evaluates to run the action. If more than one function has a condition that evaluates to run, only one function can run. This case is an error, and it cannot be guaranteed which function will run. If other custom actions are needed by the installation, these should be authored into the [CustomAction table](customaction-table.md) and sequence tables.

The functions must join the current installation by calling the [**MsiJoinTransaction**](/windows/desktop/api/Msi/nf-msi-msijointransaction) function and must call the [**MsiEndTransaction**](/windows/desktop/api/Msi/nf-msi-msiendtransaction) function to commit the installation of multiple packages. If the functions return before calling **MsiEndTransaction**, the installer rolls back all installations.

The MsiEmbeddedChainer table has the following columns.



| Column             | Type                             | Key | Nullable |
|--------------------|----------------------------------|-----|----------|
| MsiEmbeddedChainer | [Identifier](identifier.md)     | Y   | N        |
| Condition          | [Condition](condition.md)       | N   | Y        |
| CommandLine        | [Formatted](formatted.md)       | N   | Y        |
| Source             | [CustomSource](customsource.md) | N   | N        |
| Type               | [Integer](integer.md)           | N   | N        |



 

## Columns

<dl> <dt>

<span id="MsiEmbeddedChainer"></span><span id="msiembeddedchainer"></span><span id="MSIEMBEDDEDCHAINER"></span>MsiEmbeddedChainer
</dt> <dd>

The primary key for the table. This value is a unique identifier for the user-defined function described by this row.

</dd> <dt>

<span id="Condition"></span><span id="condition"></span><span id="CONDITION"></span>Condition
</dt> <dd>

A conditional statement for running the user-defined function. You can enable or disable the functions listed in the MsiEmbeddedChainer table using a transform that modifies property values evaluated by this field. For more information, see [Using Properties in Conditional Statements](using-properties-in-conditional-statements.md).

</dd> <dt>

<span id="CommandLine"></span><span id="commandline"></span><span id="COMMANDLINE"></span>CommandLine
</dt> <dd>

The value in this field is a part of the command line string passed to the executable file identified in the Source column. The installer appends the value in this field to the transaction handle to generate the command line. If the value in this column is null, the command line consists of only the transaction handle.

</dd> <dt>

<span id="Source"></span><span id="source"></span><span id="SOURCE"></span>Source
</dt> <dd>

The location of the executable file for the user-defined function. If the value in the Type column is 2, this column can contain an external key into the [Binary table](binary-table.md). If the value in the Type column is 18, this column can contain an external key into the [File table](file-table.md). If the value in the Type column is 50, this column can contain an external key into the [Property table](property-table.md).

</dd> <dt>

<span id="Type"></span><span id="type"></span><span id="TYPE"></span>Type
</dt> <dd>

The functions listed in the MsiEmbeddedChainer table are described using the following custom action numeric types. This column can contain the values for the following three numeric types only; any other combination of custom action flags is ignored.



| Custom action type                                 | Custom action flags                                                | Hexadecimal | Decimal |
|----------------------------------------------------|--------------------------------------------------------------------|-------------|---------|
| [Custom Action Type 2](custom-action-type-2.md)   | **msidbCustomActionTypeExe** + **msidbCustomActionTypeBinaryData** | 0x002       | 2       |
| [Custom Action Type 18](custom-action-type-18.md) | **msidbCustomActionTypeExe** + **msidbCustomActionTypeSourceFile** | 0x012       | 18      |
| [Custom Action Type 50](custom-action-type-50.md) | **msidbCustomActionTypeExe** + **msidbCustomActionTypeProperty**   | 0x032       | 50      |



 

</dd> </dl>

## Remarks

The Windows Installer does not prevent the user-defined functions in this table from running during the advertisement of the application. You can use a conditional statement in the Condition column to prevent a function from being run during advertisement.

The Windows Installer also provides a non-embedded external UI handler to build a rich user interface on top of the Windows Installer package. For more information about using an external UI handler with the Windows Installer, see [Monitoring an Installation Using MsiSetExternalUI](monitoring-an-installation-using-msisetexternalui.md).

The [MsiPackageCertificate Table](msipackagecertificate-table.md) lists digital signature certificates used to verify the identity of the installation packages that make a multiple-package installation. You can use this table to reduce the number of times your multiple-package installation displays a [*User Account Control*](u-gly.md) (UAC) prompt that requires a response by an administrator.

 

 
