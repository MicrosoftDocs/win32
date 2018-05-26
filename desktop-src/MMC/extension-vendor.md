---
title: Extension Vendor property
description: The Vendor property returns the name of the snap-in vendor. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2ac31864-4970-421e-8eef-d6a8db9300f9
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Vendor property MMC
- Vendor property MMC , Extension object
- Extension object MMC , Vendor property
- Vendor property MMC , Extension interface
- Extension interface MMC , Vendor property
topic_type:
- apiref
api_name:
- Extension.Vendor
- Extension.Vendor
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Extension::Vendor property

The **Vendor** property returns the name of the snap-in vendor. This property is read-only.

## Syntax


```VB
Property Vendor As String
```



## Property value

The snap-in vendor's name, or an empty string if the vendor's name is unavailable.

## Examples


```VB
' Retrieve and display the extension vendor.
Dim strVndr As String
strVndr = objExt.Vendor
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
| IID<br/>                      | IID\_Extension is defined as AD4D6CA6-912F-409b-A26E-7FD234AEF542<br/>            |



## See also

<dl> <dt>

[**Extension.Name**](extension-name.md)
</dt> <dt>

[**Extension.SnapinCLSID**](extension-snapinclsid.md)
</dt> <dt>

[**Extension.Version**](extension-version.md)
</dt> </dl>

 

 





