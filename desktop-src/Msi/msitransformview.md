---
description: This temporary table enables the Custom Action Patch Uninstall Option for custom actions added or updated by a patch.
ms.assetid: 2d4a934f-e245-4d0a-b8bf-52457107ac08
title: MsiTransformView
ms.topic: article
ms.date: 05/31/2018
---

# MsiTransformView

This temporary table enables the [Custom Action Patch Uninstall Option](custom-action-patch-uninstall-option.md) for custom actions added or updated by a patch.

If a patch adds or updates a custom action having the **msidbCustomActionTypePatchUninstall** attribute, Windows Installer runs the new or updated custom action when the patch is uninstalled. Windows Installer makes the updates within the patch being uninstalled available to the patch uninstall custom action. The patch must include a MsiTransformView*<PatchGUID>* table to provide this information to Windows Installer. The information in this table is available to any immediate custom action, and is unavailable to deferred custom actions.

**[Windows Installer 4.0 and earlier](not-supported-in-windows-installer-4-0.md):** Not supported. The [Custom Action Patch Uninstall Option](custom-action-patch-uninstall-option.md) is available beginning with Windows Installer 4.5.

This table should be named MsiTransformView*<PatchGUID>* Table, where *<PatchGUID>* is the GUID that uniquely identifies the patch. The MsiTransformView*<PatchGUID>* Table has the following columns.



| Column  | Type                         | Key | Nullable |
|---------|------------------------------|-----|----------|
| Table   | [Identifier](identifier.md) | Y   | N        |
| Column  | [Text](text.md)             | Y   | N        |
| Row     | [Text](text.md)             | Y   | Y        |
| Data    | [Text](text.md)             | N   | Y        |
| Current | [Text](text.md)             | N   | Y        |



 

## Column

<dl> <dt>

<span id="Table"></span><span id="table"></span><span id="TABLE"></span>Table
</dt> <dd>

Name of an altered database table.

</dd> <dt>

<span id="Column"></span><span id="column"></span><span id="COLUMN"></span>Column
</dt> <dd>

Name of an altered table column or INSERT, DELETE, CREATE, or DROP.

</dd> <dt>

<span id="Row"></span><span id="row"></span><span id="ROW"></span>Row
</dt> <dd>

A list of the primary key values separated by tabs. Null primary key values are represented by a single space character. A Null value in this column indicates a schema change.

</dd> <dt>

<span id="Data"></span><span id="data"></span><span id="DATA"></span>Data
</dt> <dd>

Data, name of a data stream, or a column definition.

</dd> <dt>

<span id="Current"></span><span id="current"></span><span id="CURRENT"></span>Current
</dt> <dd>

Current value from reference database, or column a number.

</dd> </dl>

## Remarks

Patch uninstall custom actions run when the patch is uninstalled. They do not run when the product is uninstalled. Use the [Custom Action Patch Uninstall Option](custom-action-patch-uninstall-option.md) and this table to run a custom only when the patch is being uninstalled.

A patch can update a custom action provided in the original package (.msi file.) To run the updated version of the custom action when the patch is uninstalled, mark the custom action with the **msidbCustomActionTypePatchUninstall** attribute in the original package.

 

 



