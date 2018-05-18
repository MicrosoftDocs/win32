---
title: \_Application VersionMinor property
description: The VersionMinor property returns the minor version number of MMC. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dda02f3b-b326-4181-8923-3a4ad9f62e0d'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["VersionMinor property MMC", "VersionMinor property MMC , Application object", "Application object MMC , VersionMinor property", "VersionMinor property MMC , _Application interface", "_Application interface MMC , VersionMinor property"]
topic_type:
- apiref
api_name:
- Application.VersionMinor
- _Application.VersionMinor
api_location:
- Mmc.exe
api_type:
- COM
---

# \_Application::VersionMinor property

The **VersionMinor** property returns the minor version number of MMC. This property is read-only.

## Syntax


```VB
Property VersionMinor As Long
```



## Property value

Long value that represents the minor version number of the MMC application. For example, if this property returned the value 0, then MMC version x.0 is running.

## Examples


```VB
Dim VerMinor As Long
VerMinor = objMMC.VersionMinor
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



 

 





