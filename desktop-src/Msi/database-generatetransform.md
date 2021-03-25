---
description: The GenerateTransform method of the Database object creates a transform that, when applied to the object database, results in the reference database. The transform is stored in the storage object.
ms.assetid: 51cd70a0-6eda-4ca6-b468-9cb36ad942f8
title: Database.GenerateTransform method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Database.GenerateTransform
api_type: 
- COM
api_location: 
- Msi.dll
---

# Database.GenerateTransform method

The **GenerateTransform** method of the [**Database**](database-object.md) object creates a [*transform*](t-gly.md) that, when applied to the object database, results in the reference database. The transform is stored in the storage object.

If the transform is to be applied during an installation you must use the [**CreateTransformSummaryInfo**](database-createtransformsummaryinfo.md) method to populate the summary information stream.

## Syntax


```JScript
Database.GenerateTransform(
  reference,
  storage
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

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

A transform can add non-primary key columns to the end of a table. A transform cannot be created that adds primary key columns to a table. A transform cannot be created that changes the order, names, or definitions of columns.

This method returns a Boolean value. It returns TRUE if a transform is generated. It returns FALSE if a transform is not generated because there are no differences between the two databases. If the method fails, it generates an error.

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

 

 




