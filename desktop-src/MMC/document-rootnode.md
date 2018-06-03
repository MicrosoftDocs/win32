---
title: Document RootNode property
description: The RootNode property returns the console's root Node object. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d37429ac-8dfe-42e6-9d9f-4cedf8898688
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- RootNode property MMC
- RootNode property MMC , Document object
- Document object MMC , RootNode property
- RootNode property MMC , Document interface
- Document interface MMC , RootNode property
topic_type:
- apiref
api_name:
- Document.RootNode
- Document.RootNode
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Document::RootNode property

The **RootNode** property returns the console's root [**Node**](node-object.md) object. This property is read-only.

## Syntax


```VB
Property RootNode As Node
```



## Property value

The console's root node.

## Examples


```VB
' Retrieve the document's RootNode property.
Dim objRoot As MMC20.Node
Set objRoot = objDoc.RootNode
 
' Use the RootNode object.
' ...
 
' Free the object when done.
Set objRoot = Nothing
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

[**Node**](node-object.md)
</dt> </dl>

 

 





