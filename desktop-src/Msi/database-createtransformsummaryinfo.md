---
description: The CreateTransformSummaryInfo method of the Database object creates and populates the summary information stream of an existing transform file. This method fills in the properties with the base and reference ProductCode and ProductVersion.
ms.assetid: 67df9b9c-0e7c-49a6-a35e-5196327d6aff
title: Database.CreateTransformSummaryInfo method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Database.CreateTransformSummaryInfo
api_type: 
- COM
api_location: 
- Msi.dll
---

# Database.CreateTransformSummaryInfo method

The **CreateTransformSummaryInfo** method of the [**Database**](database-object.md) object creates and populates the summary information stream of an existing transform file. This method fills in the properties with the base and reference [**ProductCode**](productcode.md) and [**ProductVersion**](productversion.md).

## Syntax


```JScript
Database.CreateTransformSummaryInfo(
  reference,
  storage,
  errorConditions,
  validation
)
```



## Parameters

<dl> <dt>

*reference* 
</dt> <dd>

Required database that does not include the changes.

</dd> <dt>

*storage* 
</dt> <dd>

The name of the generated transform file. This is optional.

</dd> <dt>

*errorConditions* 
</dt> <dd>

Required error conditions that should be suppressed when the transform is applied. Combine one or more of the following error condition values.



| Error condition name                                                                                                                                                                                                                                                                                                                                        | Meaning                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <span id="msiTransformErrorNone"></span><span id="msitransformerrornone"></span><span id="MSITRANSFORMERRORNONE"></span><dl> <dt>**msiTransformErrorNone**</dt> <dt>0</dt> </dl>                                                                         | None of the following conditions.<br/>                                                |
| <span id="msiTransformErrorAddExistingRow"></span><span id="msitransformerroraddexistingrow"></span><span id="MSITRANSFORMERRORADDEXISTINGROW"></span><dl> <dt>**msiTransformErrorAddExistingRow**</dt> <dt>1</dt> </dl>                                 | Adds a row that already exists.<br/>                                                  |
| <span id="msiTransformErrorDeleteNonExistingRow"></span><span id="msitransformerrordeletenonexistingrow"></span><span id="MSITRANSFORMERRORDELETENONEXISTINGROW"></span><dl> <dt>**msiTransformErrorDeleteNonExistingRow**</dt> <dt>2</dt> </dl>         | Deletes a row that does not exist.<br/>                                               |
| <span id="msiTransformErrorAddExistingTable"></span><span id="msitransformerroraddexistingtable"></span><span id="MSITRANSFORMERRORADDEXISTINGTABLE"></span><dl> <dt>**msiTransformErrorAddExistingTable**</dt> <dt>4</dt> </dl>                         | Adds a table that already exists.<br/>                                                |
| <span id="msiTransformErrorDeleteNonExistingTable"></span><span id="msitransformerrordeletenonexistingtable"></span><span id="MSITRANSFORMERRORDELETENONEXISTINGTABLE"></span><dl> <dt>**msiTransformErrorDeleteNonExistingTable**</dt> <dt>8</dt> </dl> | Deletes a table that does not exist.<br/>                                             |
| <span id="msiTransformErrorUpdateNonExistingRow"></span><span id="msitransformerrorupdatenonexistingrow"></span><span id="MSITRANSFORMERRORUPDATENONEXISTINGROW"></span><dl> <dt>**msiTransformErrorUpdateNonExistingRow**</dt> <dt>16</dt> </dl>        | Updates a row that does not exist.<br/>                                               |
| <span id="msiTransformErrorChangeCodepage"></span><span id="msitransformerrorchangecodepage"></span><span id="MSITRANSFORMERRORCHANGECODEPAGE"></span><dl> <dt>**msiTransformErrorChangeCodepage**</dt> <dt>32</dt> </dl>                                | Transform and database code pages do not match and neither code page is neutral.<br/> |



 

</dd> <dt>

*validation* 
</dt> <dd>

Required when the transform is applied to a database; shows which properties should be validated to verify that this transform can be applied to the database. The properties are all contained in the [Summary Information Stream Property Set](summary-information-stream-property-set.md).

Combine one or more of the following values.



| Validation flag                                                                                                                                                                                                                                                                                                         | Meaning                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <span id="msiTransformValidationNone"></span><span id="msitransformvalidationnone"></span><span id="MSITRANSFORMVALIDATIONNONE"></span><dl> <dt>**msiTransformValidationNone**</dt> <dt>0</dt> </dl>                 | No validation done.<br/>                        |
| <span id="msiTransformValidationLanguage"></span><span id="msitransformvalidationlanguage"></span><span id="MSITRANSFORMVALIDATIONLANGUAGE"></span><dl> <dt>**msiTransformValidationLanguage**</dt> <dt>1</dt> </dl> | Default language must match base database.<br/> |
| <span id="msiTransformValidationProduct"></span><span id="msitransformvalidationproduct"></span><span id="MSITRANSFORMVALIDATIONPRODUCT"></span><dl> <dt>**msiTransformValidationProduct**</dt> <dt>2</dt> </dl>     | Product must match base database.<br/>          |



 

To validate product version, first choose one or more of these three flags to indicate how much of the version is to be verified.



| Validation flag                                                                                                                                                                                                                                                                                                              | Meaning                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <span id="msiTransformValidationMajorVer"></span><span id="msitransformvalidationmajorver"></span><span id="MSITRANSFORMVALIDATIONMAJORVER"></span><dl> <dt>**msiTransformValidationMajorVer**</dt> <dt>8</dt> </dl>      | Checks major version only.<br/>                |
| <span id="msiTransformValidationMinorVer"></span><span id="msitransformvalidationminorver"></span><span id="MSITRANSFORMVALIDATIONMINORVER"></span><dl> <dt>**msiTransformValidationMinorVer**</dt> <dt>16</dt> </dl>     | Checks major and minor version only.<br/>      |
| <span id="msiTransformValidationUpdateVer"></span><span id="msitransformvalidationupdatever"></span><span id="MSITRANSFORMVALIDATIONUPDATEVER"></span><dl> <dt>**msiTransformValidationUpdateVer**</dt> <dt>32</dt> </dl> | Checks major, minor, and update versions.<br/> |



 

Then choose one of the following to indicate the required relationship between the product version of the database the transform is being applied to and that of the base database.



| Validation flag                                                                                                                                                                                                                                                                                                                                   | Meaning                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <span id="msiTransformValidationLess"></span><span id="msitransformvalidationless"></span><span id="MSITRANSFORMVALIDATIONLESS"></span><dl> <dt>**msiTransformValidationLess**</dt> <dt>64</dt> </dl>                                          | Applied version < base version<br/>  |
| <span id="msiTransformValidationLessOrEqual"></span><span id="msitransformvalidationlessorequal"></span><span id="MSITRANSFORMVALIDATIONLESSOREQUAL"></span><dl> <dt>**msiTransformValidationLessOrEqual**</dt> <dt>128</dt> </dl>             | Applied version <= base version<br/> |
| <span id="msiTransformValidationEqual"></span><span id="msitransformvalidationequal"></span><span id="MSITRANSFORMVALIDATIONEQUAL"></span><dl> <dt>**msiTransformValidationEqual**</dt> <dt>256</dt> </dl>                                     | Applied version = base version<br/>     |
| <span id="msiTransformValidationGreaterOrEqual"></span><span id="msitransformvalidationgreaterorequal"></span><span id="MSITRANSFORMVALIDATIONGREATEROREQUAL"></span><dl> <dt>**msiTransformValidationGreaterOrEqual**</dt> <dt>512</dt> </dl> | Applied version >= base version<br/> |
| <span id="msiTransformValidationGreater"></span><span id="msitransformvalidationgreater"></span><span id="MSITRANSFORMVALIDATIONGREATER"></span><dl> <dt>**msiTransformValidationGreater**</dt> <dt>1024</dt> </dl>                            | Applied version > base version<br/>  |



 

To validate that the transform is being applied to a package having the appropriate [**UpgradeCode**](upgradecode.md), set the following flag.



| Validation flag                                                                                                                                                                                                                                                                                                                        | Meaning                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <span id="msiTransformValidationUpgradeCode"></span><span id="msitransformvalidationupgradecode"></span><span id="MSITRANSFORMVALIDATIONUPGRADECODE"></span><dl> <dt>**msiTransformValidationUpgradeCode**</dt> <dt>2048</dt> </dl> | Validates that the transform is the appropriate [**UpgradeCode**](upgradecode.md).<br/> |



 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To create a summary information stream for a transform, the [**ProductCode**](productcode.md) and [**ProductVersion**](productversion.md) properties must be defined in the [Property](property-table.md) tables of both the base and reference databases. If msiTransformValidationUpgradeCode is used, the [**UpgradeCode**](upgradecode.md) property must be defined in both databases.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IDatabase is defined as 000C109D-0000-0000-C000-000000000046<br/>                                                                                                                                                                            |



## See also

<dl> <dt>

[Database Transforms](database-transforms.md)
</dt> </dl>

 

 




