---
title: SnapIn Vendor property
description: The Vendor property returns the name of the snap-in vendor if available, or an empty string if not available. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a0808409-1837-40e3-9131-90f00a976688
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Vendor property MMC
- Vendor property MMC , SnapIn object
- SnapIn object MMC , Vendor property
- Vendor property MMC , SnapIn interface
- SnapIn interface MMC , Vendor property
topic_type:
- apiref
api_name:
- SnapIn.Vendor
- SnapIn.Vendor
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SnapIn::Vendor property

The **Vendor** property returns the name of the snap-in vendor if available, or an empty string if not available. This property is read-only.

## Syntax


```VB
Property Vendor As String
```



## Property value

The snap-in vendor's name. If the vendor's name is not available, then the return value is an empty string.

## Examples


```VB
' Retrieve and display the snap-in vendor.
Dim strVndr As String
strVndr = objSnap.Vendor
MsgBox ("Vendor: " & strVndr)
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

[**SnapIn.Version**](snapin-version.md)
</dt> </dl>

 

 





