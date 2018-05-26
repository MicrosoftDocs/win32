---
title: SnapIns Item method
description: The Item method returns the SnapIn object at a specified index.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f6b1c347-cec4-407a-96fd-71b2d0a070e0
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Item method MMC
- Item method MMC , SnapIns object
- SnapIns object MMC , Item method
- Item method MMC , SnapIns interface
- SnapIns interface MMC , Item method
topic_type:
- apiref
api_name:
- SnapIns.Item
- SnapIns.Item
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SnapIns::Item method

The **Item** method returns the [**SnapIn**](snapin-object.md) object at a specified index.

## Syntax


```VB
SnapIns.Item( _
  ByVal Index As Long _
) As SnapIn
```



## Parameters

<dl> <dt>

*Index* 
</dt> <dd>

The index of the [**SnapIn**](snapin-object.md) being retrieved. The index is 1-based.

</dd> </dl>

## Examples


```VB
' Retrieve the count of SnapIn objects.
Dim nSnapIns As Long
nSnapIns = objSnapIns.Count
 
Dim i As Long
Dim objSnap As MMC20.SnapIn
' Iterate the SnapIn objects.
For i = 1 To nSnapIns
    ' Obtain the SnapIn
    Set objSnap = objSnapIns.Item(i)
    
    ' Use the SnapIn object.
    ' This example will display the SnapIn name.
    MsgBox (objSnap.Name)
    
    ' Free the SnapIn object for the next iteration.
    Set objSnap = Nothing
Next i
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

[**SnapIns.Count**](snapins-count.md)
</dt> </dl>

 

 





