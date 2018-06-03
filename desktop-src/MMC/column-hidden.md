---
title: Column Hidden property
description: The Hidden property returns or sets the visible state for the column. When setting the Hidden property, the view is refreshed automatically. This property is read/write.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9e30fdff-aaec-4f67-94ae-3dbf5bcc7a02
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Hidden property MMC
- Hidden property MMC , Column object
- Column object MMC , Hidden property
- Hidden property MMC , Column interface
- Column interface MMC , Hidden property
topic_type:
- apiref
api_name:
- Column.Hidden
- Column.Hidden
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Column::Hidden property

The **Hidden** property returns or sets the visible state for the column. When setting the **Hidden** property, the view is refreshed automatically. This property is read/write.

## Syntax


```VB
Property Hidden As Long
```



## Property value

Visible state of the column. If **Hidden** is 0, then the column is viewable. If **Hidden** is 1, then the column is not viewable. The first column must always remain viewable and cannot be hidden.

## Examples


```VB
' Retrieve the Hidden property.
Dim nHidden As Long
nHidden = objCol.Hidden
 
' Hide the column by setting the Hidden property to 1.
objCol.Hidden = 1
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Column is defined as FD1C5F63-2B16-4D06-9AB3-F45350B940AB<br/>             |



 

 





