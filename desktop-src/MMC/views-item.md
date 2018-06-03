---
title: Views Item method
description: The Item method returns the View object at a specified index.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: adf1d8e4-96cd-4af0-bbd2-ec162ca382ad
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Item method MMC
- Item method MMC , Views object
- Views object MMC , Item method
- Item method MMC , Views interface
- Views interface MMC , Item method
topic_type:
- apiref
api_name:
- Views.Item
- Views.Item
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Views::Item method

The **Item** method returns the [**View**](view-object.md) object at a specified index.

## Syntax


```VB
Views.Item( _
  ByVal Index As Long _
) As View
```



## Parameters

<dl> <dt>

*Index* 
</dt> <dd>

The index of the view being retrieved. The index is 1-based.

</dd> </dl>

## Examples


```VB
' Retrieve the number of View objects.
Dim nCount As Long
nCount = objViews.Count
 
Dim i As Long
Dim objView As MMC20.View
 
' Iterate the views.
For i = 1 To nCount
    Set objView = objViews.Item(i)
    ' Use the View object.
    ' ...
    
    ' Free the View object for the next iteration.
    Set objView = Nothing
Next i
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Views is defined as D6B8C29D-A1FF-4D72-AAB0-E381E9B9338D<br/>              |



## See also

<dl> <dt>

[**Views.Add**](views-add.md)
</dt> <dt>

[**Views.Count**](views-count.md)
</dt> </dl>

 

 





