---
description: The UIPreview object is used to view user interface dialog boxes and billboards during authoring. This object is created by the EnableUIPreview method of the Database object.
ms.assetid: 5df2a4f3-6352-4575-b822-1811150a86be
title: UIPreview object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UIPreview
api_type: 
- COM
api_location: 
- Msi.dll
---

# UIPreview object

The **UIPreview** object is used to view user interface dialog boxes and billboards during authoring. This object is created by the [**EnableUIPreview**](database-enableuipreview.md) method of the [**Database**](database-object.md) object.

## Members

The **UIPreview** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **UIPreview** object has these methods.



| Method                                           | Description                                                                                             |
|:-------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
| [**ViewBillboard**](uipreview-viewbillboard.md) | Displays an authored billboard using the host control in the currently displayed dialog box.<br/> |
| [**ViewDialog**](uipreview-viewdialog.md)       | Displays an authored UI dialog box stored in the current database.<br/>                           |



 

### Properties

The **UIPreview** object has these properties.



| Property                                          | Access type           | Description                                                                                                                                                                       |
|:--------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Property**](uipreview-property.md)<br/> | Read/write<br/> | Represents the string value of a named installer property or, if prefixed with a percent sign (%), the value of a system environment variable for the current process.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IUIPreview is defined as 000C109A-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




