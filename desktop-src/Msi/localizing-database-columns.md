---
description: Modify any of the other localizable columns in the MNPFren.msi database using a table editor such as Orca or SQL queries.
ms.assetid: b62cf529-71a0-47ff-99ea-a182c0fe4479
title: Localizing Database Columns
ms.topic: article
ms.date: 05/31/2018
---

# Localizing Database Columns

Modify any of the other localizable columns in the MNPFren.msi database using a table editor such as Orca or SQL queries. To determine which columns of a particular table may be localized to another language, see the reference topic for that database table. See [Database Tables](database-tables.md) for a list of all database tables.

For example, the Text field of some records in the [Control table](control-table.md) may need to be localized into French. The string "Are you sure you want to cancel \[ProductName\] installation?" in the [Cancel Dialog](cancel-dialog.md) may be modified in this table to be displayed in French. The original record in .msi file appears as follows.

[Control Table](control-table.md) (partial) of the original .msi file



| Dialog\_  | Control | Type | X   | Y   | Width | Height | Attributes | Property | Text                                                          | Control\_Next | Help |
|-----------|---------|------|-----|-----|-------|--------|------------|----------|---------------------------------------------------------------|---------------|------|
| CancelDlg | Text    | Text | 48  | 15  | 194   | 30     | 3          |          | Are you sure you want to cancel \[ProductName\] installation? |               |      |



 

You may use a table editor to modify the Text field, such as the Orca table editor provided with the SDK or another table editor, or use a SQL query to change the Text field of the Control table record. An example demonstrating script-driven database queries is provided in the Windows Installer SDK as the utility WiRunSQL.vbs. Use the following command line to modify the field with WiRunSQL.vbs and the Windows Script Host. See also [Examples of Database Queries Using SQL and Script](examples-of-database-queries-using-sql-and-script.md).

**Cscript WiRunSQL.vbs MNPFren.msi "UPDATE Control SET Control.Text='Etes-vous sur de vouloir annuler l'installation de \[ProductName\]?' WHERE Control.Dialog\_='CancelDlg' AND Control.Control='Text'"**

[Control Table](control-table.md) (partial) in MNPFren.msi



| Dialog\_  | Control | Type | X   | Y   | Width | Height | Attributes | Property | Text                                                                | Control\_Next | Help |
|-----------|---------|------|-----|-----|-------|--------|------------|----------|---------------------------------------------------------------------|---------------|------|
| CancelDlg | Text    | Text | 48  | 15  | 194   | 30     | 3          |          | Êtes-vous sûr de vouloir annuler l'installation de \[ProductName\]? |               |      |



 

If the installation of MNPFren.msi is canceled by the user, the **Cancel Dialog** appears displaying the text: "Êtes-vous sûr de vouloir annuler l'installation de MNP2000?"

When using this method to localize UI text to a different language, the localized UI must be tested to ensure that the size of controls are large enough to display the entire localized text. This should be tested using all font size settings that are available for display. Localized text can require more space than the original text and may be truncated if displayed in a control that is too small.

[Continue](updating-productlanguage-and-productcode-properties.md)

 

 



