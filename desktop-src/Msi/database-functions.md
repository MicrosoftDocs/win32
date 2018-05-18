---
Description: 'This material is intended for developers who are writing their own setup programs and developers who want to learn more about the installer database tables. For general information on the installer, see About Windows Installer.'
ms.assetid: '95516437-9708-4f4e-a5c2-7bcd4741c776'
title: Database Functions
---

# Database Functions

This material is intended for developers who are writing their own setup programs and developers who want to learn more about the installer database tables. For general information on the installer, see [About Windows Installer](about-windows-installer.md).

You can use the installer access functions to access the database and the installation process. These functions should only be used by custom installation actions and authoring tools. Some of the installer access functions require SQL query strings for querying the database. Queries must adhere to the installer [SQL syntax](sql-syntax.md).

This topic lists the installer database access functions by category.

## General Database Access Functions



| Function                                                             | Description                                                                             |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**MsiDatabaseCommit**](msidatabasecommit.md)                       | Commits changes to a database.                                                          |
| [**MsiDatabaseGetPrimaryKeys**](msidatabasegetprimarykeys.md)       | Returns the names of all the primary key columns.                                       |
| [**MsiDatabaseIsTablePersistent**](msidatabaseistablepersistent.md) | Returns an enumeration describing the state of a table.                                 |
| [**MsiDatabaseOpenView**](msidatabaseopenview.md)                   | Prepares a database query and creates a view object.                                    |
| [**MsiGetActiveDatabase**](msigetactivedatabase.md)                 | Returns the active database for the installation.                                       |
| [**MsiViewGetColumnInfo**](msiviewgetcolumninfo.md)                 | Returns column names or definitions.                                                    |
| [**MsiOpenDatabase**](msiopendatabase.md)                           | Opens a database file for data access.                                                  |
| [**MsiViewClose**](msiviewclose.md)                                 | Releases the result set for an executed view.                                           |
| [**MsiViewExecute**](msiviewexecute.md)                             | Executes the view query and supplies required parameters.                               |
| [**MsiViewFetch**](msiviewfetch.md)                                 | Fetches the next sequential record from the view.                                       |
| [**MsiViewGetError**](msiviewgeterror.md)                           | Returns the error that occurred in the [**MsiViewModify**](msiviewmodify.md) function. |
| [**MsiViewModify**](msiviewmodify.md)                               | Updates a fetched record.                                                               |



 

## Database Management Functions



| Function                                                               | Description                                                      |
|------------------------------------------------------------------------|------------------------------------------------------------------|
| [**MsiCreateTransformSummaryInfo**](msicreatetransformsummaryinfo.md) | Creates summary information for an existing transform.           |
| [**MsiDatabaseApplyTransform**](msidatabaseapplytransform.md)         | Applies a transform to a database.                               |
| [**MsiDatabaseExport**](msidatabaseexport.md)                         | Exports a table from an open database to a text archive file.    |
| [**MsiDatabaseGenerateTransform**](msidatabasegeneratetransform.md)   | Generates a transform file of differences between two databases. |
| [**MsiDatabaseImport**](msidatabaseimport.md)                         | Imports an installer text archive table into an open database.   |
| [**MsiDatabaseMerge**](msidatabasemerge.md)                           | Merges two databases together.                                   |
| [**MsiGetDatabaseState**](msigetdatabasestate.md)                     | Returns the state of the database.                               |



 

## Record Processing Functions



| Function                                                 | Description                                                     |
|----------------------------------------------------------|-----------------------------------------------------------------|
| [**MsiCreateRecord**](msicreaterecord.md)               | Creates new record object with specified number of fields.      |
| [**MsiFormatRecord**](msiformatrecord.md)               | Formats record field data and properties using a format string. |
| [**MsiRecordClearData**](msirecordcleardata.md)         | Sets all fields in a record to null.                            |
| [**MsiRecordDataSize**](msirecorddatasize.md)           | Returns the length of a record field.                           |
| [**MsiRecordGetFieldCount**](msirecordgetfieldcount.md) | Returns the number of fields in a record.                       |
| [**MsiRecordGetInteger**](msirecordgetinteger.md)       | Returns the integer value from a record field.                  |
| [**MsiRecordGetString**](msirecordgetstring.md)         | Returns the string value of a record field.                     |
| [**MsiRecordIsNull**](msirecordisnull.md)               | Reports whether a record field is null.                         |
| [**MsiRecordReadStream**](msirecordreadstream.md)       | Reads bytes from a record stream field into a buffer.           |
| [**MsiRecordSetInteger**](msirecordsetinteger.md)       | Sets a record field to an integer field.                        |
| [**MsiRecordSetStream**](msirecordsetstream.md)         | Sets a record stream field from a file.                         |
| [**MsiRecordSetString**](msirecordsetstring.md)         | Copies a string into the designated field.                      |



 

## Summary Information Property Functions



| Function                                                                 | Description                                                            |
|--------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**MsiGetSummaryInformation**](msigetsummaryinformation.md)             | Obtains handle to summary information stream of installer database.    |
| [**MsiSummaryInfoGetProperty**](msisummaryinfogetproperty.md)           | Gets a single property from the summary information.                   |
| [**MsiSummaryInfoGetPropertyCount**](msisummaryinfogetpropertycount.md) | Returns number of properties in the summary information stream.        |
| [**MsiSummaryInfoPersist**](msisummaryinfopersist.md)                   | Writes changed summary information back to summary information stream. |
| [**MsiSummaryInfoSetProperty**](msisummaryinfosetproperty.md)           | Sets a single summary information property.                            |



 

## Installer State Access Functions



| Function                                               | Description                                                 |
|--------------------------------------------------------|-------------------------------------------------------------|
| [**MsiGetLanguage**](msigetlanguage.md)               | Returns the numeric language of the current installation.   |
| [**MsiGetLastErrorRecord**](msigetlasterrorrecord.md) | Returns error record last returned for the calling process. |
| [**MsiGetMode**](msigetmode.md)                       | Returns one of the Boolean internal installation states.    |
| [**MsiGetProperty**](msigetproperty.md)               | Gets the value of an installer property.                    |
| [**MsiSetProperty**](msisetproperty.md)               | Sets the value of an installation property.                 |
| [**MsiSetMode**](msisetmode.md)                       | Sets an internal engine Boolean state.                      |



 

## Installer Action Functions



| Function                                             | Description                                                               |
|------------------------------------------------------|---------------------------------------------------------------------------|
| [**MsiDoAction**](msidoaction.md)                   | Executes built-in action, custom action, or user-interface wizard action. |
| [**MsiEvaluateCondition**](msievaluatecondition.md) | Evaluates a conditional expression containing property names and values.  |
| [**MsiProcessMessage**](msiprocessmessage.md)       | Sends an error record to the installer for processing.                    |
| [**MsiSequence**](msisequence.md)                   | Executes an action sequence.                                              |



 

## Installer Location Functions



| Function                                     | Description                                                       |
|----------------------------------------------|-------------------------------------------------------------------|
| [**MsiGetSourcePath**](msigetsourcepath.md) | Returns the full source path for a folder in the Directory table. |
| [**MsiGetTargetPath**](msigettargetpath.md) | Returns the full target path for a folder in the Directory table. |
| [**MsiSetTargetPath**](msisettargetpath.md) | Sets the full target path for a folder in the Directory table.    |



 

## Installer Selection Functions



| Function                                                     | Description                                                          |
|--------------------------------------------------------------|----------------------------------------------------------------------|
| [**MsiEnumComponentCosts**](msienumcomponentcosts.md)       | Enumerates the disk-space per drive required to install a component. |
| [**MsiGetComponentState**](msigetcomponentstate.md)         | Obtains the state of a component.                                    |
| [**MsiGetFeatureCost**](msigetfeaturecost.md)               | Returns the disk space required by a feature.                        |
| [**MsiGetFeatureState**](msigetfeaturestate.md)             | Gets the state of a feature.                                         |
| [**MsiGetFeatureValidStates**](msigetfeaturevalidstates.md) | Returns a valid installation state.                                  |
| [**MsiSetComponentState**](msisetcomponentstate.md)         | Sets a component to the specified state.                             |
| [**MsiSetFeatureAttributes**](msisetfeatureattributes.md)   | Modifies the default attributes of a feature at run time.            |
| [**MsiSetFeatureState**](msisetfeaturestate.md)             | Sets a feature to a specified state.                                 |
| [**MsiSetInstallLevel**](msisetinstalllevel.md)             | Sets the installation level of a full product installation.          |
| [**MsiVerifyDiskSpace**](msiverifydiskspace.md)             | Checks for sufficient disk space.                                    |



 

## User Interface Functions



| Function                                           | Description                                                             |
|----------------------------------------------------|-------------------------------------------------------------------------|
| [**MsiEnableUIPreview**](msienableuipreview.md)   | Enables preview mode of the user interface.                             |
| [**MsiPreviewBillboard**](msipreviewbillboard.md) | Displays a billboard with the host control in the displayed dialog box. |
| [**MsiPreviewDialog**](msipreviewdialog.md)       | Displays a dialog box as modeless and inactive.                         |



 

All functions support both ANSI and Unicode calls. To use these functions, include MsiQuery.h and link with Msi.lib.

## Installation Functions

In addition to the database access functions listed above, you create an installation package for an application by using the installer functions listed in the [Installer Function Reference](installer-function-reference.md) section.

 

 



