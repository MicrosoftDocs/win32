---
title: View ViewMemento method
description: The ViewMemento method sets the view to the specified memento's state. A memento is the programmatic equivalent of a favorite setting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9027c6fe-7a09-457a-859f-652f9e83dabd'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["ViewMemento method MMC", "ViewMemento method MMC , View object", "View object MMC , ViewMemento method", "ViewMemento method MMC , View interface", "View interface MMC , ViewMemento method"]
topic_type:
- apiref
api_name:
- View.ViewMemento
- View.ViewMemento
api_location:
- Mmc.exe
api_type:
- COM
---

# View::ViewMemento method

The **ViewMemento** method sets the view to the specified memento's state. A memento is the programmatic equivalent of a favorite setting.

## Syntax


```VB
View.ViewMemento( _
  ByVal Memento As String _
)
```



## Parameters

<dl> <dt>

*Memento* 
</dt> <dd>

The XML-readable string that represents the view's state.

</dd> </dl>

## Return value

This method does not return a value.

## Examples


```VB
' Restore the view.
' strMemento was created by previously
' retrieving the View.Memento property.
objView.ViewMemento (strMemento)
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_View is defined as 6EFC2DA2-B38C-457E-9ABB-ED2D189B8C38<br/>               |



## See also

<dl> <dt>

[**View.Memento**](view-memento.md)
</dt> </dl>

 

 





