---
title: Extensions Count property
description: The Count property returns the number of Extension objects that are in the Extensions collection. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f4e025ab-d856-4706-978c-628198f6bd63
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Count property MMC
- Count property MMC , Extensions object
- Extensions object MMC , Count property
- Count property MMC , Extensions interface
- Extensions interface MMC , Count property
topic_type:
- apiref
api_name:
- Extensions.Count
- Extensions.Count
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extensions::Count property

The **Count** property returns the number of [**Extension**](extension-object.md) objects that are in the [**Extensions**](extensions-collection.md) collection. This property is read-only.

## Syntax


```VB
Property Count As Long
```



## Property value

The number of [**Extension**](extension-object.md) objects contained in this collection.

## Examples


```VB
' Retrieve the count of Extension objects.
Dim nCount As Long
nCount = objExts.Count
MsgBox ("Number of Extension objects: " & nCount)
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Extensions is defined as 82DBEA43-8CA4-44bc-A2CA-D18741059EC8<br/>           |



## See also

<dl> <dt>

[**Extensions.Item**](extensions-item.md)
</dt> <dt>

[**SnapIns.Count**](snapins-count.md)
</dt> </dl>

 

 





