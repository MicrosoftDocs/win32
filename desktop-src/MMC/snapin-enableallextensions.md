---
title: SnapIn EnableAllExtensions method
description: The EnableAllExtensions method determines whether or not all extensions for the snap-in are enabled. This method is the programmatic equivalent of the \ 0034;Add all extensions \ 0034; check box in the Snap-In Manager.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9aee0bb9-ad2c-4bd5-97be-e38cc2425d70
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- EnableAllExtensions method MMC
- EnableAllExtensions method MMC , SnapIn object
- SnapIn object MMC , EnableAllExtensions method
- EnableAllExtensions method MMC , SnapIn interface
- SnapIn interface MMC , EnableAllExtensions method
topic_type:
- apiref
api_name:
- SnapIn.EnableAllExtensions
- SnapIn.EnableAllExtensions
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SnapIn::EnableAllExtensions method

The **EnableAllExtensions** method determines whether or not all extensions for the snap-in are enabled. This method is the programmatic equivalent of the "Add all extensions" check box in the Snap-In Manager.

## Syntax


```VB
SnapIn.EnableAllExtensions( _
  ByVal Enable As Long _
)
```



## Parameters

<dl> <dt>

*Enable* 
</dt> <dd>

Value that determines whether all extensions are enabled. To add all available extensions, set *Enable* to 1. To add or exclude individual extensions, call this method with *Enable* set to 0 and then call [**Extension.Enable**](extension-enable.md) to enable or disable individual extension snap-ins.

</dd> </dl>

## Return value

This method does not return a value.

## Examples


```VB
' Add all extensions.
objSnap.EnableAllExtensions (1)
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

[**SnapIn.Extensions**](snapin-extensions.md)
</dt> <dt>

[**Extensions collection**](extensions-collection.md)
</dt> </dl>

 

 





