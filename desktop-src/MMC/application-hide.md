---
title: \_Application Hide method
description: The Hide method hides the MMC application. This method sets the Visible property to False.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0ac59101-61ee-48a6-85f8-7aff0ba466b6'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Hide method MMC", "Hide method MMC , Application object", "Application object MMC , Hide method", "Hide method MMC , _Application interface", "_Application interface MMC , Hide method"]
topic_type:
- apiref
api_name:
- Application.Hide
- _Application.Hide
api_location:
- Mmc.exe
api_type:
- COM
---

# \_Application::Hide method

The **Hide** method hides the MMC application. This method sets the [**Visible**](application-visible.md) property to False.

## Syntax


```VB
Application.Hide()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method will fail if the MMC application is under user control. If the [**Application.UserControl**](application-usercontrol.md) property is 1, then the MMC application is under user control.

## Examples


```VB
' Hide the MMC application.
objMMC.Hide
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

[**Application.Show**](application-show.md)
</dt> <dt>

[**Application.Visible**](application-visible.md)
</dt> <dt>

[**Application.UserControl**](application-usercontrol.md)
</dt> <dt>

[Controlling the Lifetime of an MMC Instance](controlling-the-lifetime-of-an-mmc-instance.md)
</dt> </dl>

 

 





