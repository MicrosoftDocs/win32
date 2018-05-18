---
title: \_Application Help method
description: The Help method displays the Help contents for the console.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b23962c2-8850-4c45-b601-76ff9d1bf9c8'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Help method MMC", "Help method MMC , Application object", "Application object MMC , Help method", "Help method MMC , _Application interface", "_Application interface MMC , Help method"]
topic_type:
- apiref
api_name:
- Application.Help
- _Application.Help
api_location:
- Mmc.exe
api_type:
- COM
---

# \_Application::Help method

The **Help** method displays the Help contents for the console.

## Syntax


```VB
Application.Help()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Examples


```VB
' Display help for the MMC console.
objMMC.Help
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



 

 





