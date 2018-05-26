---
title: Document CreateProperties method
description: The CreateProperties method makes a new Properties collection for the document.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b1f742b9-aae4-4d63-880c-7c3c310442f5
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CreateProperties method MMC
- CreateProperties method MMC , Document object
- Document object MMC , CreateProperties method
- CreateProperties method MMC , Document interface
- Document interface MMC , CreateProperties method
topic_type:
- apiref
api_name:
- Document.CreateProperties
- Document.CreateProperties
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Document::CreateProperties method

The **CreateProperties** method makes a new [**Properties**](snapin-properties.md) collection for the document.

## Syntax


```VB
Document.CreateProperties() As Properties
```



## Parameters

This method has no parameters.

## Examples


```VB
' Create a Properties collection for the document.
Dim objProps As MMC20.Properties
Set objProps = objDoc.CreateProperties()
 
' Use the Properties collection.
' ...
 
' Free the object when done.
Set objProps = Nothing
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Document<br/>                                                              |



## See also

<dl> <dt>

[**Properties collection**](properties-collection.md)
</dt> </dl>

 

 





