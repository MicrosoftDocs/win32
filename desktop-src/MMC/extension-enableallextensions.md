---
title: Extension EnableAllExtensions method
description: The EnableAllExtensions method determines whether or not all extensions for the extension snap-in are enabled. This method is the programmatic equivalent of the Add all extensions check box in the Snap-In Manager.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: eeb4a400-da1e-47b7-bbbf-a601e92ef55b
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- EnableAllExtensions method MMC
- EnableAllExtensions method MMC , Extension object
- Extension object MMC , EnableAllExtensions method
- EnableAllExtensions method MMC , Extension interface
- Extension interface MMC , EnableAllExtensions method
topic_type:
- apiref
api_name:
- Extension.EnableAllExtensions
- Extension.EnableAllExtensions
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extension::EnableAllExtensions method

The **EnableAllExtensions** method determines whether or not all extensions for the extension snap-in are enabled. This method is the programmatic equivalent of the **Add all extensions** check box in the Snap-In Manager.

## Syntax


```VB
Extension.EnableAllExtensions( _
  ByVal Enable As Long _
)
```



## Parameters

<dl> <dt>

*Enable* 
</dt> <dd>

Value that determines whether all extensions are enabled. To add all available extensions, set *Enable* to 1. To add or exclude individual extensions, set *Enable* to 0, and then call [**Extension.Enable**](extension-enable.md) to enable or disable individual extension snap-ins.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The [**Extension**](extension-object.md) object is a snap-in, and the **EnableAllExtensions** method applies to the extensions that can extend the **Extension** object.

## Examples


```VB
objExt.EnableAllExtensions (0)
' This extension's extensions can now be enabled or disabled.
' ...
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

[**Extension.Enable**](extension-enable.md)
</dt> <dt>

[**Extension.Extensions**](extension-extensions.md)
</dt> </dl>

 

 





