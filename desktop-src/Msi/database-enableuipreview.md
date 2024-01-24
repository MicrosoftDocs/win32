---
description: The EnableUIPreview method of the Database object facilitates the authoring of dialog boxes and billboards by providing the support needed to view user interface dialog boxes stored in the installer database.
ms.assetid: c4687de7-8ab4-4377-ac5c-1fed7c915519
title: Database.EnableUIPreview method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Database.EnableUIPreview
api_type: 
- COM
api_location: 
- Msi.dll
---

# Database.EnableUIPreview method

The **EnableUIPreview** method of the [**Database**](database-object.md) object facilitates the authoring of dialog boxes and billboards by providing the support needed to view user interface dialog boxes stored in the installer database. The method starts the preview mode by returning a preview **Database** object. The preview mode ends when the preview object is released.

## Syntax


```JScript
Database.EnableUIPreview()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IDatabase is defined as 000C109D-0000-0000-C000-000000000046<br/>                                                                                                                                                                            |



 

 




