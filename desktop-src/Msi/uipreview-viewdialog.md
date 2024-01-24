---
description: The ViewDialog method of the UIPreview object displays an authored user interface dialog box stored in the current database.
ms.assetid: 5bc935ac-38ca-4a51-a1dc-6879dee97b05
title: UIPreview.ViewDialog method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UIPreview.ViewDialog
api_type: 
- COM
api_location: 
- Msi.dll
---

# UIPreview.ViewDialog method

The **ViewDialog** method of the [**UIPreview**](uipreview-object.md) object displays an authored user interface dialog box stored in the current database.

## Syntax


```JScript
UIPreview.ViewDialog(
  dialog
)
```



## Parameters

<dl> <dt>

*dialog* 
</dt> <dd>

Required name of the dialog box, case-sensitive, and the primary key of the Dialog database table.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IUIPreview is defined as 000C109A-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




