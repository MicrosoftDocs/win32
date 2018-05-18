---
title: View Memento property
description: The Memento property returns a memento for the current view. A memento is the programmatic equivalent of a favorite setting. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '25dad886-4529-432e-be2c-4b86aebb1b95'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Memento property MMC", "Memento property MMC , View object", "View object MMC , Memento property", "Memento property MMC , View interface", "View interface MMC , Memento property"]
topic_type:
- apiref
api_name:
- View.Memento
- View.Memento
api_location:
- Mmc.exe
api_type:
- COM
---

# View::Memento property

The **Memento** property returns a memento for the current view. A memento is the programmatic equivalent of a favorite setting. This property is read-only.

## Syntax


```VB
Property Memento As String
```



## Property value

An XML-readable string that represents the current view.

## Examples


```VB
' Retrieve the Memento property.
Dim strMemento As String
strMemento = objView.Memento
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

[**View.ViewMemento**](view-viewmemento.md)
</dt> </dl>

 

 





