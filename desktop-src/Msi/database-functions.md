---
Description: This material is intended for developers who are writing their own setup programs and developers who want to learn more about the installer database tables. For general information on the installer, see About Windows Installer.
ms.assetid: 95516437-9708-4f4e-a5c2-7bcd4741c776
title: Database Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Database Functions

This material is intended for developers who are writing their own setup programs and developers who want to learn more about the installer database tables. For general information on the installer, see [About Windows Installer](about-windows-installer.md).

You can use the installer access functions to access the database and the installation process. These functions should only be used by custom installation actions and authoring tools. Some of the installer access functions require SQL query strings for querying the database. Queries must adhere to the installer [SQL syntax](sql-syntax.md).

This topic lists the installer database access functions by category.

## General Database Access Functions



| Function                                                             | Description                                                                             |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**MsiDatabaseCommit**](/windows/win32/Msiquery/nf-msiquery-msidatabasecommit?branch=master)                       | Commits changes to a database.                                                          |
| [**MsiDatabaseGetPrimaryKeys**](/windows/win32/Msiquery/nf-msiquery-msidatabasegetprimarykeysa?branch=master)       | Returns the names of all the primary key columns.                                       |
| [**MsiDatabaseIsTablePersistent**](/windows/win32/Msiquery/nf-msiquery-msidatabaseistablepersistenta?branch=master) | Returns an enumeration describing the state of a table.                                 |
| [**MsiDatabaseOpenView**](/windows/win32/Msiquery/nf-msiquery-msidatabaseopenviewa?branch=master)                   | Prepares a database query and creates a view object.                                    |
| [**MsiGetActiveDatabase**](/windows/win32/Msiquery/nf-msiquery-msigetactivedatabase?branch=master)                 | Returns the active database for the installation.                                       |
| [**MsiViewGetColumnInfo**](/windows/win32/Msiquery/nf-msiquery-msiviewgetcolumninfo?branch=master)                 | Returns column names or definitions.                                                    |
| [**MsiOpenDatabase**](/windows/win32/Msiquery/nf-msiquery-msiopendatabasea?branch=master)                           | Opens a database file for data access.                                                  |
| [**MsiViewClose**](/windows/win32/Msiquery/nf-msiquery-msiviewclose?branch=master)                                 | Releases the result set for an executed view.                                           |
| [**MsiViewExecute**](/windows/win32/Msiquery/nf-msiquery-msiviewexecute?branch=master)                             | Executes the view query and supplies required parameters.                               |
| [**MsiViewFetch**](/windows/win32/Msiquery/nf-msiquery-msiviewfetch?branch=master)                                 | Fetches the next sequential record from the view.                                       |
| [**MsiViewGetError**](/windows/win32/Msiquery/nf-msiquery-msiviewgeterrora?branch=master)                           | Returns the error that occurred in the [**MsiViewModify**](/windows/win32/Msiquery/nf-msiquery-msiviewmodify?branch=master) function. |
| [**MsiViewModify**](/windows/win32/Msiquery/nf-msiquery-msiviewmodify?branch=master)                               | Updates a fetched record.                                                               |



 

## Database Management Functions



| Function                                                               | Description                                                      |
|------------------------------------------------------------------------|------------------------------------------------------------------|
| [**MsiCreateTransformSummaryInfo**](/windows/win32/Msiquery/nf-msiquery-msicreatetransformsummaryinfoa?branch=master) | Creates summary information for an existing transform.           |
| [**MsiDatabaseApplyTransform**](/windows/win32/Msiquery/nf-msiquery-msidatabaseapplytransforma?branch=master)         | Applies a transform to a database.                               |
| [**MsiDatabaseExport**](/windows/win32/Msiquery/nf-msiquery-msidatabaseexporta?branch=master)                         | Exports a table from an open database to a text archive file.    |
| [**MsiDatabaseGenerateTransform**](/windows/win32/Msiquery/nf-msiquery-msidatabasegeneratetransforma?branch=master)   | Generates a transform file of differences between two databases. |
| [**MsiDatabaseImport**](/windows/win32/Msiquery/nf-msiquery-msidatabaseimporta?branch=master)                         | Imports an installer text archive table into an open database.   |
| [**MsiDatabaseMerge**](/windows/win32/Msiquery/nf-msiquery-msidatabasemergea?branch=master)                           | Merges two databases together.                                   |
| [**MsiGetDatabaseState**](/windows/win32/Msiquery/nf-msiquery-msigetdatabasestate?branch=master)                     | Returns the state of the database.                               |



 

## Record Processing Functions



| Function                                                 | Description                                                     |
|----------------------------------------------------------|-----------------------------------------------------------------|
| [**MsiCreateRecord**](/windows/win32/Msiquery/nf-msiquery-msicreaterecord?branch=master)               | Creates new record object with specified number of fields.      |
| [**MsiFormatRecord**](/windows/win32/Msiquery/nf-msiquery-msiformatrecorda?branch=master)               | Formats record field data and properties using a format string. |
| [**MsiRecordClearData**](/windows/win32/Msiquery/nf-msiquery-msirecordcleardata?branch=master)         | Sets all fields in a record to null.                            |
| [**MsiRecordDataSize**](/windows/win32/Msiquery/nf-msiquery-msirecorddatasize?branch=master)           | Returns the length of a record field.                           |
| [**MsiRecordGetFieldCount**](/windows/win32/Msiquery/nf-msiquery-msirecordgetfieldcount?branch=master) | Returns the number of fields in a record.                       |
| [**MsiRecordGetInteger**](/windows/win32/Msiquery/nf-msiquery-msirecordgetinteger?branch=master)       | Returns the integer value from a record field.                  |
| [**MsiRecordGetString**](/windows/win32/Msiquery/nf-msiquery-msirecordgetstringa?branch=master)         | Returns the string value of a record field.                     |
| [**MsiRecordIsNull**](/windows/win32/Msiquery/nf-msiquery-msirecordisnull?branch=master)               | Reports whether a record field is null.                         |
| [**MsiRecordReadStream**](/windows/win32/Msiquery/nf-msiquery-msirecordreadstream?branch=master)       | Reads bytes from a record stream field into a buffer.           |
| [**MsiRecordSetInteger**](/windows/win32/Msiquery/nf-msiquery-msirecordsetinteger?branch=master)       | Sets a record field to an integer field.                        |
| [**MsiRecordSetStream**](/windows/win32/Msiquery/nf-msiquery-msirecordsetstreama?branch=master)         | Sets a record stream field from a file.                         |
| [**MsiRecordSetString**](/windows/win32/Msiquery/nf-msiquery-msirecordsetstringa?branch=master)         | Copies a string into the designated field.                      |



 

## Summary Information Property Functions



| Function                                                                 | Description                                                            |
|--------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**MsiGetSummaryInformation**](/windows/win32/Msiquery/nf-msiquery-msigetsummaryinformationa?branch=master)             | Obtains handle to summary information stream of installer database.    |
| [**MsiSummaryInfoGetProperty**](/windows/win32/Msiquery/nf-msiquery-msisummaryinfogetpropertya?branch=master)           | Gets a single property from the summary information.                   |
| [**MsiSummaryInfoGetPropertyCount**](/windows/win32/Msiquery/nf-msiquery-msisummaryinfogetpropertycount?branch=master) | Returns number of properties in the summary information stream.        |
| [**MsiSummaryInfoPersist**](/windows/win32/Msiquery/nf-msiquery-msisummaryinfopersist?branch=master)                   | Writes changed summary information back to summary information stream. |
| [**MsiSummaryInfoSetProperty**](/windows/win32/Msiquery/nf-msiquery-msisummaryinfosetpropertya?branch=master)           | Sets a single summary information property.                            |



 

## Installer State Access Functions



| Function                                               | Description                                                 |
|--------------------------------------------------------|-------------------------------------------------------------|
| [**MsiGetLanguage**](/windows/win32/Msiquery/nf-msiquery-msigetlanguage?branch=master)               | Returns the numeric language of the current installation.   |
| [**MsiGetLastErrorRecord**](/windows/win32/Msiquery/nf-msiquery-msigetlasterrorrecord?branch=master) | Returns error record last returned for the calling process. |
| [**MsiGetMode**](/windows/win32/Msiquery/nf-msiquery-msigetmode?branch=master)                       | Returns one of the Boolean internal installation states.    |
| [**MsiGetProperty**](/windows/win32/Msiquery/nf-msiquery-msigetpropertya?branch=master)               | Gets the value of an installer property.                    |
| [**MsiSetProperty**](/windows/win32/Msiquery/nf-msiquery-msisetpropertya?branch=master)               | Sets the value of an installation property.                 |
| [**MsiSetMode**](/windows/win32/Msiquery/nf-msiquery-msisetmode?branch=master)                       | Sets an internal engine Boolean state.                      |



 

## Installer Action Functions



| Function                                             | Description                                                               |
|------------------------------------------------------|---------------------------------------------------------------------------|
| [**MsiDoAction**](/windows/win32/Msiquery/nf-msiquery-msidoactiona?branch=master)                   | Executes built-in action, custom action, or user-interface wizard action. |
| [**MsiEvaluateCondition**](/windows/win32/Msiquery/nf-msiquery-msievaluateconditiona?branch=master) | Evaluates a conditional expression containing property names and values.  |
| [**MsiProcessMessage**](/windows/win32/Msiquery/nf-msiquery-msiprocessmessage?branch=master)       | Sends an error record to the installer for processing.                    |
| [**MsiSequence**](/windows/win32/Msiquery/nf-msiquery-msisequencea?branch=master)                   | Executes an action sequence.                                              |



 

## Installer Location Functions



| Function                                     | Description                                                       |
|----------------------------------------------|-------------------------------------------------------------------|
| [**MsiGetSourcePath**](/windows/win32/Msiquery/nf-msiquery-msigetsourcepatha?branch=master) | Returns the full source path for a folder in the Directory table. |
| [**MsiGetTargetPath**](/windows/win32/Msiquery/nf-msiquery-msigettargetpatha?branch=master) | Returns the full target path for a folder in the Directory table. |
| [**MsiSetTargetPath**](/windows/win32/Msiquery/nf-msiquery-msisettargetpatha?branch=master) | Sets the full target path for a folder in the Directory table.    |



 

## Installer Selection Functions



| Function                                                     | Description                                                          |
|--------------------------------------------------------------|----------------------------------------------------------------------|
| [**MsiEnumComponentCosts**](/windows/win32/Msiquery/nf-msiquery-msienumcomponentcostsa?branch=master)       | Enumerates the disk-space per drive required to install a component. |
| [**MsiGetComponentState**](/windows/win32/Msiquery/nf-msiquery-msigetcomponentstatea?branch=master)         | Obtains the state of a component.                                    |
| [**MsiGetFeatureCost**](/windows/win32/Msiquery/nf-msiquery-msigetfeaturecosta?branch=master)               | Returns the disk space required by a feature.                        |
| [**MsiGetFeatureState**](/windows/win32/Msiquery/nf-msiquery-msigetfeaturestatea?branch=master)             | Gets the state of a feature.                                         |
| [**MsiGetFeatureValidStates**](/windows/win32/Msiquery/nf-msiquery-msigetfeaturevalidstatesa?branch=master) | Returns a valid installation state.                                  |
| [**MsiSetComponentState**](/windows/win32/Msiquery/nf-msiquery-msisetcomponentstatea?branch=master)         | Sets a component to the specified state.                             |
| [**MsiSetFeatureAttributes**](/windows/win32/Msiquery/nf-msiquery-msisetfeatureattributesa?branch=master)   | Modifies the default attributes of a feature at run time.            |
| [**MsiSetFeatureState**](/windows/win32/Msiquery/nf-msiquery-msisetfeaturestatea?branch=master)             | Sets a feature to a specified state.                                 |
| [**MsiSetInstallLevel**](/windows/win32/Msiquery/nf-msiquery-msisetinstalllevel?branch=master)             | Sets the installation level of a full product installation.          |
| [**MsiVerifyDiskSpace**](/windows/win32/Msiquery/nf-msiquery-msiverifydiskspace?branch=master)             | Checks for sufficient disk space.                                    |



 

## User Interface Functions



| Function                                           | Description                                                             |
|----------------------------------------------------|-------------------------------------------------------------------------|
| [**MsiEnableUIPreview**](/windows/win32/Msiquery/nf-msiquery-msienableuipreview?branch=master)   | Enables preview mode of the user interface.                             |
| [**MsiPreviewBillboard**](/windows/win32/Msiquery/nf-msiquery-msipreviewbillboarda?branch=master) | Displays a billboard with the host control in the displayed dialog box. |
| [**MsiPreviewDialog**](/windows/win32/Msiquery/nf-msiquery-msipreviewdialoga?branch=master)       | Displays a dialog box as modeless and inactive.                         |



 

All functions support both ANSI and Unicode calls. To use these functions, include MsiQuery.h and link with Msi.lib.

## Installation Functions

In addition to the database access functions listed above, you create an installation package for an application by using the installer functions listed in the [Installer Function Reference](installer-function-reference.md) section.

 

 



