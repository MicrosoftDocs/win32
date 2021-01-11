---
description: The ActionText Table contains text to be displayed in a progress dialog box, and written to the log for actions that take a long time to execute. The displayed text consists of the action description and optionally formatted data from the action.
ms.assetid: 88d18422-77d0-4929-9341-d078843cb2a9
title: ActionText Table
ms.topic: article
ms.date: 05/31/2018
---

# ActionText Table

The ActionText Table contains text to be displayed in a progress dialog box, and written to the log for actions that take a long time to execute. The displayed text consists of the action description and optionally formatted data from the action.

The ActionText Table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Action      | [Identifier](identifier.md) | Y   | N        |
| Description | [Text](text.md)             | N   | Y        |
| Template    | [Template](template.md)     | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Action"></span><span id="action"></span><span id="ACTION"></span>Action
</dt> <dd>

Name of the action.

Primary table key.

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

Localized description that is displayed in the progress dialog box, or written to the log when the action is executing.

</dd> <dt>

<span id="Template"></span><span id="template"></span><span id="TEMPLATE"></span>Template
</dt> <dd>

A localized format template that is used to format action data records to display during action execution. If a template is not supplied, then the action data is not displayed.

</dd> </dl>

## Remarks

Typically, the entries in the ActionText table refer to actions in sequence tables. There are other actions the installer performs that are not listed in the sequence table, but still need to be specified in the table. The following table identifies the required table entries where the action name and template must be authored exactly as shown, but the description can be customized.



| Action          | Description                             | Template |
|-----------------|-----------------------------------------|----------|
| Rollback        | Undoes actions.                         | \[1\]    |
| RollbackCleanup | Removes old files.                      | \[1\]    |
| GenerateScript  | Generates system operations for action. | \[1\]    |



 

> [!Note]  
> Action text is only displayed for actions that run within the installation script. Therefore, action text is only displayed for actions that are sequenced between the [InstallInitialize](installinitialize-action.md) and [InstallFinalize](installfinalize-action.md) actions.

 

You can import a localized ActionText table into your database by using Msidb.exe or [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta). The SDK includes a localized ActionText Table for each of the languages listed in the [Localizing the Error and ActionText Tables](localizing-the-error-and-actiontext-tables.md) section. If the ActionText table is not populated, the installer loads localized strings for the language specified by the [**ProductLanguage**](productlanguage.md) property.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE46](ice46.md)  
</dl>

 

 



