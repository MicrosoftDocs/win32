---
title: View CopySelection method
description: The CopySelection method copies the selected item's data object to the clipboard.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0ffdbdf5-4c76-495f-bf87-f656f7e9dd22'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["CopySelection method MMC", "CopySelection method MMC , View object", "View object MMC , CopySelection method", "CopySelection method MMC , View interface", "View interface MMC , CopySelection method"]
topic_type:
- apiref
api_name:
- View.CopySelection
- View.CopySelection
api_location:
- Mmc.exe
api_type:
- COM
---

# View::CopySelection method

The **CopySelection** method copies the selected item's data object to the clipboard.

## Syntax


```VB
View.CopySelection()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Examples


```VB
' Copy the selection's data object to the clipboard.
objView.CopySelection
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_View is defined as 6EFC2DA2-B38C-457E-9ABB-ED2D189B8C38<br/>               |



## See also

<dl> <dt>

[**View.CopyScopeNode**](view-copyscopenode.md)
</dt> </dl>

 

 





