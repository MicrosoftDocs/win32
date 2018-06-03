---
title: Column Width property
description: The Width property sets or returns the width (in pixels) of the column. This property is read/write.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 29c06b30-aa49-49eb-8d88-b5b1a1578e86
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Width property MMC
- Width property MMC , Column object
- Column object MMC , Width property
- Width property MMC , Column interface
- Column interface MMC , Width property
topic_type:
- apiref
api_name:
- Column.Width
- Column.Width
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Column::Width property

The **Width** property sets or returns the width (in pixels) of the column. This property is read/write.

## Syntax


```VB
Property Width As Long
```



## Property value

The width of the column, in pixels.

## Examples


```VB
' Retrieve the column's width.
Dim nWidth As Long
nWidth = objCol.Width
MsgBox (nWidth)
 
' Set the column's width to 120 pixels.
objCol.Width = 120
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



## See also

<dl> <dt>

[**Column.Hidden**](column-hidden.md)
</dt> </dl>

 

 





