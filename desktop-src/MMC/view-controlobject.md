---
title: View ControlObject property
description: The ControlObject property returns the automation interface supplied by the control in the result view. This property is valid only when an OCX (ActiveX control) is displayed in the result view. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4babc95d-9e14-42b2-84e0-ecb225552366
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ControlObject property MMC
- ControlObject property MMC , View object
- View object MMC , ControlObject property
- ControlObject property MMC , View interface
- View interface MMC , ControlObject property
topic_type:
- apiref
api_name:
- View.ControlObject
- View.ControlObject
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# View::ControlObject property

The **ControlObject** property returns the automation interface supplied by the control in the result view. This property is valid only when an OCX (ActiveX control) is displayed in the result view. This property is read-only.

## Syntax


```VB
Property ControlObject As Object
```



## Property value

The automation interface, as provided by the OCX in the result view.

## Remarks

The functionality of the control object is dependent on the particular OCX. For details, refer to the description provided by the OCX.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_View is defined as 6EFC2DA2-B38C-457E-9ABB-ED2D189B8C38<br/>               |



 

 





