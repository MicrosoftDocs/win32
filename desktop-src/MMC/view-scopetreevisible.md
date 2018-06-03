---
title: View ScopeTreeVisible property
description: The ScopeTreeVisible property sets or returns the scope tree visible state. This property is read/write.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5648ed7d-c9a9-472b-aee3-bfc80eafc087
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ScopeTreeVisible property MMC
- ScopeTreeVisible property MMC , View object
- View object MMC , ScopeTreeVisible property
- ScopeTreeVisible property MMC , View interface
- View interface MMC , ScopeTreeVisible property
topic_type:
- apiref
api_name:
- View.ScopeTreeVisible
- View.ScopeTreeVisible
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# View::ScopeTreeVisible property

The **ScopeTreeVisible** property sets or returns the scope tree visible state. This property is read/write.

## Syntax


```VB
Property ScopeTreeVisible As Long
```



## Property value

The scope tree's visible state. The visible state is 1 when the scope tree is visible, or 0 when it is hidden.

## Examples


```VB
' Determine the scope tree visibility state.
Dim nVisible As Long
nVisible = objView.ScopeTreeVisible
If (1 = nVisible) Then
    MsgBox ("The scope tree is visible")
Else
    MsgBox ("The scope tree is not visible.")
End If
 
' Make the scope tree hidden.
objView.ScopeTreeVisible = 0
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



## See also

<dl> <dt>

[**ViewOptions**](/windows/desktop/api/MmcObj/ne-mmcobj-viewoptions)
</dt> </dl>

 

 





