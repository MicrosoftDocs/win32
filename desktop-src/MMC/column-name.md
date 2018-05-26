---
title: Column Name method
description: The Name method returns the name of the column.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cdd3cdc0-f84a-4c0c-8e76-bebdbc7b2e8d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Name method MMC
- Name method MMC , Column object
- Column object MMC , Name method
- Name method MMC , Column interface
- Column interface MMC , Name method
topic_type:
- apiref
api_name:
- Column.Name
- Column.Name
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Column::Name method

The **Name** method returns the name of the column.

## Syntax


```VB
Column.Name() As String
```



## Parameters

This method has no parameters.

## Examples


```VB
' Determine the column's name.
Dim strColName As String
strColName = objCol.Name
MsgBox ("Column name is '" & strColName & "'")
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

[**Column.DisplayPosition**](column-displayposition.md)
</dt> </dl>

 

 





