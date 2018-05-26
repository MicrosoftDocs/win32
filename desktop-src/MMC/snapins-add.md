---
title: SnapIns Add method
description: The Add method adds a snap-in to the collection. The snap-in being added must be referenced by its name, CLSID, or ProgID.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0bc52408-21d2-40d9-9050-56398572df28
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Add method MMC
- Add method MMC , SnapIns object
- SnapIns object MMC , Add method
- Add method MMC , SnapIns interface
- SnapIns interface MMC , Add method
topic_type:
- apiref
api_name:
- SnapIns.Add
- SnapIns.Add
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SnapIns::Add method

The **Add** method adds a snap-in to the collection. The snap-in being added must be referenced by its name, CLSID, or ProgID.

## Syntax


```VB
SnapIns.Add( _
  ByVal SnapinNameOrCLSID As String, _
  ByVal ParentSnapin As Variant, _
  ByVal Properties As Variant _
) As SnapIn
```



## Parameters

<dl> <dt>

*SnapinNameOrCLSID* 
</dt> <dd>

The name, CLSID, or ProgID for the registered snap-in being added to the collection.

</dd> <dt>

*ParentSnapin* 
</dt> <dd>

Optional [**SnapIn object**](snapin-object.md) under which the new **SnapIn** object is added.

</dd> <dt>

*Properties* 
</dt> <dd>

Optional properties to be used by the snap-in. The snap-in must implement the [**ISnapinProperties**](/windows/win32/Mmcobj/nn-mmcobj-isnapinproperties?branch=master) interface for the *Properties* parameter to be useful. The *Properties* parameter can be created by the [**Document.CreateProperties**](document-createproperties.md) method.

</dd> </dl>

## Examples


```VB
Dim objSnap As MMC20.SnapIn
' Add the "Folder" snap-in.
' Optional parameters for SnapIns.Add are not used.
Set objSnap = objSnapIns.Add("Folder")
 
' Use the SnapIn object.
' ...
 
' Free the SnapIn object when done.
Set objSnap = Nothing
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

[**SnapIns.Remove**](snapins-remove.md)
</dt> <dt>

[**Application.OnSnapInAdded**](application-onsnapinadded.md)
</dt> <dt>

[**ISnapinProperties**](/windows/win32/Mmcobj/nn-mmcobj-isnapinproperties?branch=master)
</dt> <dt>

[**Document.CreateProperties**](document-createproperties.md)
</dt> </dl>

 

 





