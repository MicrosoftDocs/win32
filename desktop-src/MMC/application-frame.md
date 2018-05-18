---
title: \_Application Frame property
description: The Frame property returns a Frame object that represents the application frame. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a8784123-2efb-4f99-881a-27ccb2e00a0f'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Frame property MMC", "Frame property MMC , Application object", "Application object MMC , Frame property", "Frame property MMC , _Application interface", "_Application interface MMC , Frame property"]
topic_type:
- apiref
api_name:
- Application.Frame
- _Application.Frame
api_location:
- Mmc.exe
api_type:
- COM
---

# \_Application::Frame property

The **Frame** property returns a [**Frame object**](frame-object.md) that represents the application frame. This property is read-only.

## Syntax


```VB
Property Frame As Frame
```



## Property value

The **Frame** object for the application.

## Examples


```VB
' Retrieve the Frame property.
Dim objFrm As MMC20.Frame
Set objFrm = objMMC.Frame
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

[**Frame object**](frame-object.md)
</dt> </dl>

 

 





