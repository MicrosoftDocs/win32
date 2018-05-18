---
title: MenuItem Execute method
description: The Execute method executes the context menu item command.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5ae3957a-c4d6-4f1e-b0df-f4ed6bd60ca5'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Execute method MMC", "Execute method MMC , MenuItem object", "MenuItem object MMC , Execute method", "Execute method MMC , MenuItem interface", "MenuItem interface MMC , Execute method"]
topic_type:
- apiref
api_name:
- MenuItem.Execute
- MenuItem.Execute
api_location:
- Mmcndmgr.dll
api_type:
- COM
---

# MenuItem::Execute method

The **Execute** method executes the context menu item command.

## Syntax


```VB
MenuItem.Execute()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Examples


```VB
' Execute the MenuItem.
objMenuItem.Execute
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_MenuItem is defined as 0178FAD1-B361-4B27-96AD-67C57EBF2E1D<br/>             |



## See also

<dl> <dt>

[**Application.OnContextMenuExecuted**](application-oncontextmenuexecuted.md)
</dt> </dl>

 

 





