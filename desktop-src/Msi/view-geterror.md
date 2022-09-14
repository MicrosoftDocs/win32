---
description: The GetError method of the View object returns the Validation error and the column name for which the error occurred.
ms.assetid: ca90dfa5-8e15-490c-835b-c5c225c3cc7b
title: View.GetError method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- View.GetError
api_type: 
- COM
api_location: 
- Msi.dll
---

# View.GetError method

The **GetError** method of the [**View**](view-object.md) object returns the Validation error and the column name for which the error occurred. In automation, the returned value is a string of the form \#\#ColumnName, where the \#\# represents a 2-digit error code. It returns the first error in the view's error array; subsequent calls return the next value in the error array. Once a value of '00' is returned, no more errors exist, and subsequent calls merely loop through the array again.

## Syntax


```JScript
View.GetError()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IView is defined as 000C109C-0000-0000-C000-000000000046<br/>                                                                                                                                                                                |



 

 




