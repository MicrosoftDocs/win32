---
title: Extension Name property
description: The Name property returns the extension's name. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e3e5338d-ffdd-4608-b333-cf3ce1027b8b
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Name property MMC
- Name property MMC , Extension object
- Extension object MMC , Name property
- Name property MMC , Extension interface
- Extension interface MMC , Name property
topic_type:
- apiref
api_name:
- Extension.Name
- Extension.Name
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extension::Name property

The **Name** property returns the extension's name. This property is read-only.

## Syntax


```VB
Property Name As String
```



## Property value

The name of the extension.

## Examples


```VB
' Retrieve and display the extension name.
Dim strName As String
strName = objExt.Name
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
| IID<br/>                      | IID\_Extension is defined as AD4D6CA6-912F-409b-A26E-7FD234AEF542<br/>            |



## See also

<dl> <dt>

[**Extension.SnapinCLSID**](extension-snapinclsid.md)
</dt> <dt>

[**Extension.Vendor**](extension-vendor.md)
</dt> <dt>

[**Extension.Version**](extension-version.md)
</dt> </dl>

 

 





