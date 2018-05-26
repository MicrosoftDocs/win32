---
title: '\_Application VersionMajor property'
description: The VersionMajor property returns the major version number of MMC. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6e1ca2c0-ef37-49fb-8358-66c60589a20e
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- VersionMajor property MMC
- VersionMajor property MMC , Application object
- Application object MMC , VersionMajor property
- VersionMajor property MMC , _Application interface
- _Application interface MMC , VersionMajor property
topic_type:
- apiref
api_name:
- Application.VersionMajor
- _Application.VersionMajor
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# \_Application::VersionMajor property

The **VersionMajor** property returns the major version number of MMC. This property is read-only.

## Syntax


```VB
Property VersionMajor As Long
```



## Property value

Long value that represents the major version number of the MMC application. For example, if this property returned the value 2, then MMC version 2.x is running.

## Examples


```VB
Dim VerMajor As Long
VerMajor = objMMC.VersionMajor
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



 

 





