---
description: The Session object controls the installation process.
ms.assetid: 013959d9-900c-45f7-b742-17b0365d6107
title: Session object (Windows Installer)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session object (Windows Installer)

The **Session** object controls the installation process. It opens the Installer database, which contains the installation tables and data. This object is associated with a standard set of action functions, each performing particular operations on data from one or more tables. Additional custom actions may be added for particular product installations. The basic engine function is a sequencer that fetches sequential records from a designated sequence table, evaluates any specified condition expression, and executes the designated action. Actions not recognized by the engine are deferred to the UI handler object for processing, usually dialog box sequences.

Note that only one **Session** object can be opened by a single process.

## Members

The **Session** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Session** object has these methods.



| Method                                                 | Description                                                                                                                                                                                                                                                               |
|:-------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DoAction**](session-doaction.md)                   | Executes the specified action. <br/>                                                                                                                                                                                                                                |
| [**EvaluateCondition**](session-evaluatecondition.md) | Evaluates a logical expression containing symbols and values and returns an integer of the enumeration msiEvaluateConditionErrorEnum.<br/>                                                                                                                          |
| [**FeatureInfo**](session-featureinfo.md)             | Returns a [**FeatureInfo**](featureinfo-object.md) object containing descriptive information for the specified feature.<br/>                                                                                                                                       |
| [**FormatRecord**](session-formatrecord.md)           | Returns a formatted string from template and record data.<br/>                                                                                                                                                                                                      |
| [**Message**](session-message.md)                     | Performs any enabled logging operations and defers execution to the UI handler object associated with the engine.<br/>                                                                                                                                              |
| [**Sequence**](session-sequence.md)                   | Opens a query on the specified table, ordering the actions by the numbers in the Sequence column. For each row fetched, the [**DoAction**](session-doaction.md) method is called, provided that any supplied condition expression does not evaluate to False.<br/> |
| [**SetInstallLevel**](session-setinstalllevel.md)     | Sets the install level for the current installation to a specified value and recalculates the Select and Installed states for all features.<br/>                                                                                                                    |



 

### Properties

The **Session** object has these properties.



| Property                                                                  | Access type           | Description                                                                                                                                                                |
|:--------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ComponentCosts**](session-componentcosts.md)<br/>               |                       | Returns a [**RecordList**](recordlist-object.md) object enumerating the disk space per drive required to install a component.<br/>                                  |
| [**ComponentCurrentState**](session-componentcurrentstate.md)<br/> |                       | Returns the current installed state of the designated component.<br/>                                                                                                |
| [**ComponentRequestState**](session-componentrequeststate.md)<br/> |                       | Obtains or requests a change in the Action state of a row in the Component table.<br/>                                                                               |
| [**Database**](session-database.md)<br/>                           |                       | Returns the database for the current installation session.<br/>                                                                                                      |
| [**FeatureCost**](session-featurecost.md)<br/>                     |                       | Returns the total amount of disk space (in units of 512 bytes) required by the specified feature and its parent features (up to the root of the Feature table).<br/> |
| [**FeatureCurrentState**](session-featurecurrentstate.md)<br/>     |                       | Returns the current installed state of the designated feature.<br/>                                                                                                  |
| [**FeatureRequestState**](session-featurerequeststate.md)<br/>     | Read/write<br/> | Obtains or requests a change in the Select state of a feature's record and subrecords.<br/>                                                                          |
| [**FeatureValidStates**](session-featurevalidstates.md)<br/>       |                       | Returns an integer representing bit flags with each relevant bit representing a valid installation state for the specified feature.<br/>                             |
| [**Installer**](session-installer.md)<br/>                         |                       | Returns the active installer object.<br/>                                                                                                                            |
| [**Language (Session Object)**](session-language.md)<br/>          |                       | Represents the numeric language identifier used by the current installation session.<br/>                                                                            |
| [**Mode**](session-mode.md)<br/>                                   |                       | This property is a value representing the designated mode flag for the current installation session.<br/>                                                            |
| [**ProductProperty**](session-productproperty.md)<br/>             |                       | Represents the string value of a named installer property.<br/>                                                                                                      |
| [**Property (Session Object)**](session-session.md)<br/>           | Read/write<br/> | Retrieves product properties from the product database.<br/>                                                                                                         |
| [**SourcePath**](session-sourcepath.md)<br/>                       |                       | Provides the full path to the designated folder on the source media or server image.<br/>                                                                            |
| [**TargetPath**](session-targetpath.md)<br/>                       | Read/write<br/> | Provides the full path to the designated folder on the installation target drive.<br/>                                                                               |
| [**VerifyDiskSpace**](session-verifydiskspace.md)<br/>             |                       | Returns true if enough disk space exists, and false if the disk is full.<br/>                                                                                        |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



## See also

<dl> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




