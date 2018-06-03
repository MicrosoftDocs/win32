---
title: '\_Application Quit method'
description: The Quit method causes the MMC application to quit.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 59eaaa60-457b-4f5a-84c7-2c704850749e
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Quit method MMC
- Quit method MMC , Application object
- Application object MMC , Quit method
- Quit method MMC , _Application interface
- _Application interface MMC , Quit method
topic_type:
- apiref
api_name:
- Application.Quit
- _Application.Quit
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# \_Application::Quit method

The **Quit** method causes the MMC application to quit.

## Syntax


```VB
Application.Quit()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Examples


```VB
' Terminate the MMC application.
objMMC.Quit
' Free the Application object.
Set objMMC = Nothing
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

[**Application.OnQuit**](application-onquit.md)
</dt> </dl>

 

 





