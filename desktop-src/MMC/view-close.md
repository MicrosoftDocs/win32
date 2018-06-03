---
title: View Close method
description: The Close method closes the view. You cannot close the last view of the document; instead, you must close the document.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5fe087c1-cee1-4f84-aa0c-6738af87d53e
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Close method MMC
- Close method MMC , View object
- View object MMC , Close method
- Close method MMC , View interface
- View interface MMC , Close method
topic_type:
- apiref
api_name:
- View.Close
- View.Close
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# View::Close method

The **Close** method closes the view. You cannot close the last view of the document; instead, you must close the document.

## Syntax


```VB
View.Close()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Examples


```VB
' Close the View.
objView.Close
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

[**Document.Close**](document-close.md)
</dt> </dl>

 

 





