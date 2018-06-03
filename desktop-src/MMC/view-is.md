---
title: View Is method
description: The Is method determines whether the view is the same as a specified view.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 41627d45-501e-4be3-a721-78b10de078f6
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Is method MMC
- Is method MMC , View object
- View object MMC , Is method
- Is method MMC , View interface
- View interface MMC , Is method
topic_type:
- apiref
api_name:
- View.Is
- View.Is
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# View::Is method

The **Is** method determines whether the view is the same as a specified view.

## Syntax


```VB
View.Is( _
  ByVal View As View _
) As Boolean
```



## Parameters

<dl> <dt>

*View* 
</dt> <dd>

[**View**](view-object.md) object to compare to this view.

</dd> </dl>

## Examples


```VB
' Determine if objView is the same object as objOtherView.
Dim nSame As Boolean
 
nSame = objView.Is(objOtherView)
If (True = nSame) Then
    MsgBox ("The View objects are the same")
Else
    MsgBox ("The View objects are not the same")
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
| IID<br/>                      | IID\_View is defined as 6EFC2DA2-B38C-457E-9ABB-ED2D189B8C38<br/>               |



 

 





