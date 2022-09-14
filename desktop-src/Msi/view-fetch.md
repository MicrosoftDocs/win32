---
description: The Fetch method of the View object retrieves the next row of column data if more rows are available in the result set, otherwise it is Null. Call the Execute method before the Fetch method.
ms.assetid: d51bf60d-5725-41eb-9002-1d0e5b9f50a3
title: View.Fetch method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- View.Fetch
api_type: 
- COM
api_location: 
- Msi.dll
---

# View.Fetch method

The **Fetch** method of the [**View**](view-object.md) object retrieves the next row of column data if more rows are available in the result set, otherwise it is Null. Call the [**Execute**](view-execute.md) method before the **Fetch** method.

## Syntax


```JScript
View.Fetch()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The same [**Record**](record-object.md) object should be used to retrieve the data in multiple rows, or else the object should be released by going out of scope. The record can be tested for the end of the result set using the syntax "If FetchRecord Is Nothing".

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IView is defined as 000C109C-0000-0000-C000-000000000046<br/>                                                                                                                                                                                |



 

 




