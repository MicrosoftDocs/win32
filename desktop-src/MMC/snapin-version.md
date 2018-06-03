---
title: SnapIn Version property
description: The Version property returns the version, in string form, of the snap-in. If the version is not available, then this property returns an empty string. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 266db28e-cf57-42ae-968d-0f497648c0cf
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Version property MMC
- Version property MMC , SnapIn object
- SnapIn object MMC , Version property
- Version property MMC , SnapIn interface
- SnapIn interface MMC , Version property
topic_type:
- apiref
api_name:
- SnapIn.Version
- SnapIn.Version
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SnapIn::Version property

The **Version** property returns the version, in string form, of the snap-in. If the version is not available, then this property returns an empty string. This property is read-only.

## Syntax


```VB
Property Version As String
```



## Property value

The snap-in's version, in string form. If the version is not available, then the return value is an empty string.

## Examples


```VB
' Retrieve and display the snap-in version.
Dim strVrsn As String
strVrsn = objSnap.Version
MsgBox ("Version: " & strVrsn)
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

[**SnapIn.Name**](snapin-name.md)
</dt> <dt>

[**SnapIn.SnapinCLSID**](snapin-snapinclsid.md)
</dt> <dt>

[**SnapIn.Vendor**](snapin-vendor.md)
</dt> </dl>

 

 





