---
title: Extension Version property
description: The Version property returns the version, in string form, of the snap-in. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 442abacb-4a80-4efe-9848-59e7c3ba3ee2
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Version property MMC
- Version property MMC , Extension object
- Extension object MMC , Version property
- Version property MMC , Extension interface
- Extension interface MMC , Version property
topic_type:
- apiref
api_name:
- Extension.Version
- Extension.Version
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Extension::Version property

The **Version** property returns the version, in string form, of the snap-in. This property is read-only.

## Syntax


```VB
Property Version As String
```



## Property value

The snap-in's version, in string form, or an empty string if the vendor's version is unavailable.

## Examples


```VB
' Retrieve and display the extension version.
Dim strVrsn As String
strVrsn = objExt.Version
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
| IID<br/>                      | IID\_Extension is defined as AD4D6CA6-912F-409b-A26E-7FD234AEF542<br/>            |



## See also

<dl> <dt>

[**Extension.Name**](extension-name.md)
</dt> <dt>

[**Extension.SnapinCLSID**](extension-snapinclsid.md)
</dt> <dt>

[**Extension.Vendor**](extension-vendor.md)
</dt> </dl>

 

 





