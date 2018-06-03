---
title: Document Views property
description: The Views property returns the Views object for the document. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2f553dcc-6315-41ae-99d7-bd9ee45f7ecf
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Views property MMC
- Views property MMC , Document object
- Document object MMC , Views property
- Views property MMC , Document interface
- Document interface MMC , Views property
topic_type:
- apiref
api_name:
- Document.Views
- Document.Views
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Document::Views property

The **Views** property returns the [**Views**](views-collection.md) object for the document. This property is read-only.

## Syntax


```VB
Property Views As Views
```



## Property value

The [**Views**](views-collection.md) collection for the document.

## Examples


```VB
' Retrieve the Views property.
Dim objViews As MMC20.Views
Set objViews = objDoc.Views
 
' Use the Views collection.
'...
' Free collection when done.
Set objViews = Nothing
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

[**Views collection**](views-collection.md)
</dt> </dl>

 

 





