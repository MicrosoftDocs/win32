---
title: Extension Enable method
description: The Enable method enables or disables the extension.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7e060b12-880d-4639-8571-63e237446847
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Enable method MMC
- Enable method MMC , Extension object
- Extension object MMC , Enable method
- Enable method MMC , Extension interface
- Extension interface MMC , Enable method
topic_type:
- apiref
api_name:
- Extension.Enable
- Extension.Enable
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extension::Enable method

The **Enable** method enables or disables the extension.

## Syntax


```VB
Extension.Enable( _
  ByVal Enable As Long _
)
```



## Parameters

<dl> <dt>

*Enable* 
</dt> <dd>

If this parameter is 1, then the extension is enabled and available for use. If this parameter is 0, the extension is disabled.

</dd> </dl>

## Return value

This method does not return a value.

## Examples


```VB
' Enable this extension.
objExt.Enable (1)
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

[**Extension.EnableAllExtensions**](extension-enableallextensions.md)
</dt> </dl>

 

 





