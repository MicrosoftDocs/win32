---
description: The Close method of the View object terminates query execution and releases database resources.
ms.assetid: 677377be-38be-47c0-9a58-a0d08cc05770
title: View.Close method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- View.Close
api_type: 
- COM
api_location: 
- Msi.dll
---

# View.Close method

The **Close** method of the [**View**](view-object.md) object terminates query execution and releases database resources.

## Syntax


```JScript
View.Close()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method must be called before the [**Execute**](view-execute.md) method is called again on the [**View**](view-object.md) object unless all rows of the result set have been obtained with the [**Fetch**](view-fetch.md) method. It is called internally when the view is destroyed.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IView is defined as 000C109C-0000-0000-C000-000000000046<br/>                                                                                                                                                                                |



 

 




