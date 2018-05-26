---
title: Extension SnapinCLSID property
description: The SnapinCLSID property returns the CLSID, in string form, for the snap-in. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 64e461cf-c631-4735-957c-57e612b0fb11
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- SnapinCLSID property MMC
- SnapinCLSID property MMC , Extension object
- Extension object MMC , SnapinCLSID property
- SnapinCLSID property MMC , Extension interface
- Extension interface MMC , SnapinCLSID property
topic_type:
- apiref
api_name:
- Extension.SnapinCLSID
- Extension.SnapinCLSID
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Extension::SnapinCLSID property

The **SnapinCLSID** property returns the CLSID, in string form, for the snap-in. This property is read-only.

## Syntax


```VB
Property SnapinCLSID As String
```



## Property value

The CLSID, as a string, for the snap-in.

## Examples


```VB
' Retrieve and display the extension CLSID.
Dim strCLSID As String
strCLSID = objExt.SnapinCLSID
MsgBox ("CLSID: " & strCLSID)
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Extension is defined as AD4D6CA6-912F-409b-A26E-7FD234AEF542<br/>            |



## See also

<dl> <dt>

[**Extension.Name**](extension-name.md)
</dt> <dt>

[**Extension.Vendor**](extension-vendor.md)
</dt> <dt>

[**Extension.Version**](extension-version.md)
</dt> </dl>

 

 





