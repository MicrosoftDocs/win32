---
title: SnapIns Remove method
description: The Remove method removes a SnapIn object from the collection. Removing the snap-in from the collection removes it from the console as well.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a75fda6c-701f-4d68-8f91-8781fc412a0d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Remove method MMC
- Remove method MMC , SnapIns object
- SnapIns object MMC , Remove method
- Remove method MMC , SnapIns interface
- SnapIns interface MMC , Remove method
topic_type:
- apiref
api_name:
- SnapIns.Remove
- SnapIns.Remove
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SnapIns::Remove method

The **Remove** method removes a [**SnapIn**](snapin-object.md) object from the collection. Removing the snap-in from the collection removes it from the console as well.

## Syntax


```VB
SnapIns.Remove( _
  ByVal SnapIn As SnapIn _
)
```



## Parameters

<dl> <dt>

*SnapIn* 
</dt> <dd>

The [**SnapIn**](snapin-object.md) object that represents the snap-in to remove from the collection.

</dd> </dl>

## Return value

This method does not return a value.

## Examples


```VB
' This example removes the Snap-In if it is named "Folder".
Dim strName As String
' objSnap was set by a previous call to objSnapIns.Item
strName = objSnap.Name
If ("Folder" = strName) Then
    objSnapIns.Remove objSnap
End If
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

[**SnapIns.Add**](snapins-add.md)
</dt> <dt>

[**Application.OnSnapInRemoved**](application-onsnapinremoved.md)
</dt> </dl>

 

 





