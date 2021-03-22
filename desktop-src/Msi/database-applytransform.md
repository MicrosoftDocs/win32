---
description: The ApplyTransform method of the Database object applies the transform to this database.
ms.assetid: bcf1ea78-54ad-49d9-8fba-7b88ced236eb
title: Database.ApplyTransform method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Database.ApplyTransform
api_type: 
- COM
api_location: 
- Msi.dll
---

# Database.ApplyTransform method

The **ApplyTransform** method of the [**Database**](database-object.md) object applies the transform to this database.

## Syntax


```JScript
Database.ApplyTransform(
  storage,
  errorConditions
)
```



## Parameters

<dl> <dt>

*storage* 
</dt> <dd>

Path to the transform file being applied. This parameter is required.

</dd> <dt>

*errorConditions* 
</dt> <dd>

Specifies the error conditions that are to be suppressed. Specify as a combination of the following integer values.



| Error condition                                                                                                                                                                                                                                                                                                                                                  | Meaning                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <span id="msiTransformErrorAddExistingRow"></span><span id="msitransformerroraddexistingrow"></span><span id="MSITRANSFORMERRORADDEXISTINGROW"></span><dl> <dt>**msiTransformErrorAddExistingRow**</dt> <dt>0x0001</dt> </dl>                                 | Adds a row that already exists.<br/>                                                     |
| <span id="msiTransformErrorDeleteNonExistingRow"></span><span id="msitransformerrordeletenonexistingrow"></span><span id="MSITRANSFORMERRORDELETENONEXISTINGROW"></span><dl> <dt>**msiTransformErrorDeleteNonExistingRow**</dt> <dt>0x0002</dt> </dl>         | Deletes a row that does not exist.<br/>                                                  |
| <span id="msiTransformErrorAddExistingTable"></span><span id="msitransformerroraddexistingtable"></span><span id="MSITRANSFORMERRORADDEXISTINGTABLE"></span><dl> <dt>**msiTransformErrorAddExistingTable**</dt> <dt>0x0004</dt> </dl>                         | Adds a table that already exists.<br/>                                                   |
| <span id="msiTransformErrorDeleteNonExistingTable"></span><span id="msitransformerrordeletenonexistingtable"></span><span id="MSITRANSFORMERRORDELETENONEXISTINGTABLE"></span><dl> <dt>**msiTransformErrorDeleteNonExistingTable**</dt> <dt>0x0008</dt> </dl> | Deletes a table that does not exist.<br/>                                                |
| <span id="msiTransformErrorUpdateNonExistingRow"></span><span id="msitransformerrorupdatenonexistingrow"></span><span id="MSITRANSFORMERRORUPDATENONEXISTINGROW"></span><dl> <dt>**msiTransformErrorUpdateNonExistingRow**</dt> <dt>0x0010</dt> </dl>         | Updates a row that does not exist.<br/>                                                  |
| <span id="msiTransformErrorChangeCodePage"></span><span id="msitransformerrorchangecodepage"></span><span id="MSITRANSFORMERRORCHANGECODEPAGE"></span><dl> <dt>**msiTransformErrorChangeCodePage**</dt> <dt>0x0020</dt> </dl>                                 | Transform and database code pages do not match and neither has a neutral code page.<br/> |
| <span id="msiTransformErrorViewTransform"></span><span id="msitransformerrorviewtransform"></span><span id="MSITRANSFORMERRORVIEWTRANSFORM"></span><dl> <dt>**msiTransformErrorViewTransform**</dt> <dt>0x0100</dt> </dl>                                     | Creates the temporary [\_TransformView table](-transformview-table.md).<br/>            |



 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The **ApplyTransform** method delays transforming tables until the last possible moment. The steps taken in **ApplyTransform** are to immediately transform the table and column catalogs for the database. The table and column catalogs are updated according to which table is added or deleted and which column is added (no deletion of columns is allowed). If a table is currently loaded in memory and needs to be transformed, it is transformed. Otherwise, the table state is set to that requiring a transform so that when the table is loaded, or when the database is committed, the transform is applied. Transform in this instance means that the actual (row) data of the table is added, deleted, or updated.

If the method fails, you can obtain extended error information by using the [**LastErrorRecord**](installer-lasterrorrecord.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IDatabase is defined as 000C109D-0000-0000-C000-000000000046<br/>                                                                                                                                                                            |



## See also

<dl> <dt>

[**Database**](database-object.md)
</dt> <dt>

[Database Transforms](database-transforms.md)
</dt> </dl>

 

 




