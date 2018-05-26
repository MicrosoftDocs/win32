---
title: SnapIn Name property
description: The Name property returns the name of the snap-in. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9339976d-c021-496c-9a5b-4538ade27ac6
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Name property MMC
- Name property MMC , SnapIn object
- SnapIn object MMC , Name property
- Name property MMC , SnapIn interface
- SnapIn interface MMC , Name property
topic_type:
- apiref
api_name:
- SnapIn.Name
- SnapIn.Name
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SnapIn::Name property

The **Name** property returns the name of the snap-in. This property is read-only.

## Syntax


```VB
Property Name As String
```



## Property value

The name of the snap-in.

## Examples


```VB
' Retrieve and display the snap-in name.
Dim strName As String
strName = objSnap.Name
MsgBox ("Name: " & strName)
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

[**SnapIn.SnapinCLSID**](snapin-snapinclsid.md)
</dt> <dt>

[**Snapin.Vendor**](snapin-vendor.md)
</dt> <dt>

[**SnapIn.Version**](snapin-version.md)
</dt> </dl>

 

 





