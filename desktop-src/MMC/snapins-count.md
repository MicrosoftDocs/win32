---
title: SnapIns Count property
description: The Count property returns the number of SnapIn objects (primary stand-alone snap-ins) that are in the SnapIns collection. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 32c6ece8-ca52-42a8-812e-3ab34559dfd4
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Count property MMC
- Count property MMC , SnapIns object
- SnapIns object MMC , Count property
- Count property MMC , SnapIns interface
- SnapIns interface MMC , Count property
topic_type:
- apiref
api_name:
- SnapIns.Count
- SnapIns.Count
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SnapIns::Count property

The **Count** property returns the number of [**SnapIn**](snapin-object.md) objects (primary stand-alone snap-ins) that are in the [**SnapIns**](snapins-collection.md) collection. This property is read-only.

## Syntax


```VB
Property Count As Long
```



## Property value

The number of [**SnapIn**](snapin-object.md) objects contained in this collection.

## Examples


```VB
' Retrieve the SnapIns property.
Dim objSnapIns As MMC20.SnapIns
Set objSnapIns = objDoc.SnapIns
 
' Retrieve the count of SnapIn objects.
Dim nSnapIns As Long
nSnapIns = objSnapIns.Count
' Display the count.
MsgBox ("There are " & nSnapIns & " snap-ins in the document.")
 
' Free the object when done.
Set objSnapIns = Nothing
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mmcobj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>Mmcobj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_SnapIns is defined as 2EF3DE1D-B12A-49D1-92C5-0B00798768F1<br/>              |



## See also

<dl> <dt>

[**SnapIns.Item**](snapins-item.md)
</dt> <dt>

[**Extensions.Count**](extensions-count.md)
</dt> </dl>

 

 





