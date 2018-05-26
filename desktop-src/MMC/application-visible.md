---
title: '\_Application Visible property'
description: The Visible property returns whether the MMC application is viewable or hidden. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 438757ad-0ca3-4aab-b955-7c7564028f9f
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Visible property MMC
- Visible property MMC , Application object
- Application object MMC , Visible property
- Visible property MMC , _Application interface
- _Application interface MMC , Visible property
topic_type:
- apiref
api_name:
- Application.Visible
- _Application.Visible
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# \_Application::Visible property

The **Visible** property returns whether the MMC application is viewable or hidden. This property is read-only.

## Syntax


```VB
Property Visible As Long
```



## Property value

Value of 1 if the application is visible, or 0 if the application is hidden. This property can be set by calling the [**Show**](application-show.md) or [**Hide**](application-hide.md) methods.

## Examples


```VB
' If the MMC application is hidden, make it visible.
If (0 = objMMC.Visible) Then
    objMMC.Show
End If
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| CLSID<br/>                    | CLSID\_Application is defined as 49B2791A-B1AE-4C90-9B8E-E860BA07F889<br/>      |
| IID<br/>                      | IID\_\_Application is defined as A3AFB9CC-B653-4741-86AB-F0470EC1384C<br/>      |



## See also

<dl> <dt>

[Controlling the Lifetime of an MMC Instance](controlling-the-lifetime-of-an-mmc-instance.md)
</dt> </dl>

 

 





