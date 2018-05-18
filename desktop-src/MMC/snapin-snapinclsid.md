---
title: SnapIn SnapinCLSID property
description: The SnapinCLSID property returns the CLSID, in string form, for the snap-in. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9f0ca0ee-139a-4328-99db-71f80aad823a'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["SnapinCLSID property MMC", "SnapinCLSID property MMC , SnapIn object", "SnapIn object MMC , SnapinCLSID property", "SnapinCLSID property MMC , SnapIn interface", "SnapIn interface MMC , SnapinCLSID property"]
topic_type:
- apiref
api_name:
- SnapIn.SnapinCLSID
- SnapIn.SnapinCLSID
api_location:
- Mmcndmgr.dll
api_type:
- COM
---

# SnapIn::SnapinCLSID property

The **SnapinCLSID** property returns the CLSID, in string form, for the snap-in. This property is read-only.

## Syntax


```VB
Property SnapinCLSID As String
```



## Property value

The CLSID, as a string, for the snap-in.

## Examples


```VB
' Retrieve and display the snap-in CLSID.
Dim strCLSID As String
strCLSID = objSnap.SnapinCLSID
MsgBox ("CLSID: " & strCLSID)
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_SnapIn is defined as 3BE910F6-3459-49C6-A1BB-41E6BE9DF3EA<br/>               |



## See also

<dl> <dt>

[**SnapIn.Name**](snapin-name.md)
</dt> <dt>

[**SnapIn.Vendor**](snapin-vendor.md)
</dt> <dt>

[**SnapIn.Version**](snapin-version.md)
</dt> </dl>

 

 





