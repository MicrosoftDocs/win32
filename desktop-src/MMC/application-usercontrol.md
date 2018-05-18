---
title: \_Application UserControl property
description: The UserControl property sets or retrieves the user control property for the application. This property determines whether the user has control of the MMC application. This property is read/write.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a146a67f-f2d4-4472-adf6-2ab67a3ce353'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["UserControl property MMC", "UserControl property MMC , Application object", "Application object MMC , UserControl property", "UserControl property MMC , _Application interface", "_Application interface MMC , UserControl property"]
topic_type:
- apiref
api_name:
- Application.UserControl
- _Application.UserControl
api_location:
- Mmc.exe
api_type:
- COM
---

# \_Application::UserControl property

The **UserControl** property sets or retrieves the user control property for the application. This property determines whether the user has control of the MMC application. This property is read/write.

## Syntax


```VB
Property UserControl As Long
```



## Property value

A value that specifies whether the user has control of the MMC application.

## Remarks

If the **UserControl** property is 1, then when the script (or using application) terminates without ending the MMC application, the MMC application remains active for the user. Additionally, if the **UserControl** property is 1, then the MMC application cannot be hidden ([**Application.Hide**](application-hide.md) will fail). The **UserControl** property default value is 0; a value of 0 results in the MMC application terminating when the script or using application terminates.

If the MMC application is hidden and the **UserControl** property is changed from 0 to 1, then the MMC application will be shown.

## Examples


```VB
' Retrieve the UserControl property.
Dim lUserCtrl As Long
lUserCtrl = objMMC.UserControl
' Use the value.
MsgBox ("UserControl = " & lUserCtrl)

' Set the UserControl property.
objMMC.UserControl = 1
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| CLSID<br/>                    | CLSID\_Application is defined as 49B2791A-B1AE-4C90-9B8E-E860BA07F889<br/>      |
| IID<br/>                      | IID\_\_Application is defined as A3AFB9CC-B653-4741-86AB-F0470EC1384C<br/>      |



## See also

<dl> <dt>

[**Application.Hide**](application-hide.md)
</dt> <dt>

[**Application.Show**](application-show.md)
</dt> <dt>

[**Application.Visible**](application-visible.md)
</dt> <dt>

[Controlling the Lifetime of an MMC Instance](controlling-the-lifetime-of-an-mmc-instance.md)
</dt> </dl>

 

 





