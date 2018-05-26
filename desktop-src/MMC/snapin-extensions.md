---
title: SnapIn Extensions property
description: The Extensions property returns the Extensions collection for the snap-in. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d7504a23-937e-4180-9c63-62601791529c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Extensions property MMC
- Extensions property MMC , SnapIn object
- SnapIn object MMC , Extensions property
- Extensions property MMC , SnapIn interface
- SnapIn interface MMC , Extensions property
topic_type:
- apiref
api_name:
- SnapIn.Extensions
- SnapIn.Extensions
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SnapIn::Extensions property

The **Extensions** property returns the [**Extensions**](extensions-collection.md) collection for the snap-in. This property is read-only.

## Syntax


```VB
Property Extensions As Extensions
```



## Property value

The [**Extensions collection**](extensions-collection.md) for the snap-in.

## Examples


```VB
' Retrieve the Extensions property.
Dim objExts As MMC20.Extensions
Set objExts = objSnap.Extensions
 
' Use the Extensions object.
' This code displays the Extensions count.
MsgBox ("Number of Extensions: " & objExts.Count)
 
' Free the object when done.
Set objExts = Nothing
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_SnapIn is defined as 3BE910F6-3459-49C6-A1BB-41E6BE9DF3EA<br/>               |



## See also

<dl> <dt>

[**SnapIn.EnableAllExtensions**](snapin-enableallextensions.md)
</dt> <dt>

[**Extensions collection**](extensions-collection.md)
</dt> </dl>

 

 





