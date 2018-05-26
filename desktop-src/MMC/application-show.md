---
title: '\_Application Show method'
description: The Show method causes the MMC application to be viewable. This method sets the Visible property to 1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 17875b21-e102-4755-a1d3-cde141ffe57d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Show method MMC
- Show method MMC , Application object
- Application object MMC , Show method
- Show method MMC , _Application interface
- _Application interface MMC , Show method
topic_type:
- apiref
api_name:
- Application.Show
- _Application.Show
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# \_Application::Show method

The **Show** method causes the MMC application to be viewable. This method sets the [**Visible**](application-visible.md) property to 1.

## Syntax


```VB
Application.Show()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Examples


```VB
' Show the MMC application.
objMMC.Show
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

[**Application.Hide**](application-hide.md)
</dt> <dt>

[**Application.Visible**](application-visible.md)
</dt> <dt>

[Controlling the Lifetime of an MMC Instance](controlling-the-lifetime-of-an-mmc-instance.md)
</dt> </dl>

 

 





