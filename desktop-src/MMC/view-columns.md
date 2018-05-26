---
title: View Columns property
description: The Columns property returns the columns in the view. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ea88bcbd-52c6-48ff-839b-74c647d8cffc
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Columns property MMC
- Columns property MMC , View object
- View object MMC , Columns property
- Columns property MMC , View interface
- View interface MMC , Columns property
topic_type:
- apiref
api_name:
- View.Columns
- View.Columns
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# View::Columns property

The **Columns** property returns the columns in the view. This property is read-only.

## Syntax


```VB
Property Columns As Columns
```



## Property value

The [**Columns collection**](columns-collection.md) made up of the columns in the view.

## Examples


```VB
' Retrieve the Columns object for the View.
Dim objCols As MMC20.Columns
Set objCols = objView.Columns
 
' Use the Columns object.
' ...
 
' Free the object when done.
Set objCols = Nothing
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

[**Columns collection**](columns-collection.md)
</dt> </dl>

 

 





