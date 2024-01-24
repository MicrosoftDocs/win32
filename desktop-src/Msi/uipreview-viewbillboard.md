---
description: The ViewBillboard method of the UIPreview object displays an authored billboard using the host control in the currently displayed dialog box.
ms.assetid: c51c1a5b-af53-47a8-9281-e790efadcfc4
title: UIPreview.ViewBillboard method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UIPreview.ViewBillboard
api_type: 
- COM
api_location: 
- Msi.dll
---

# UIPreview.ViewBillboard method

The **ViewBillboard** method of the [**UIPreview**](uipreview-object.md) object displays an authored billboard using the host control in the currently displayed dialog box.

## Syntax


```JScript
UIPreview.ViewBillboard(
  control,
  billboard
)
```



## Parameters

<dl> <dt>

*control* 
</dt> <dd>

Required name of the control hosting the billboard, case-sensitive, along with the dialog box, and the primary keys of the Control database table.

</dd> <dt>

*billboard* 
</dt> <dd>

Required name of the billboard to display using the specified control and current dialog box, and the primary key of the Billboard database table.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IUIPreview is defined as 000C109A-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




