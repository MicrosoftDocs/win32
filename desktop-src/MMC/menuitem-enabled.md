---
title: MenuItem Enabled property
description: The Enabled property returns whether the menu item is enabled or disabled. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a61af446-e9f1-4426-8108-9738ed5c72e7
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Enabled property MMC
- Enabled property MMC , MenuItem object
- MenuItem object MMC , Enabled property
- Enabled property MMC , MenuItem interface
- MenuItem interface MMC , Enabled property
topic_type:
- apiref
api_name:
- MenuItem.Enabled
- MenuItem.Enabled
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MenuItem::Enabled property

The **Enabled** property returns whether the menu item is enabled or disabled. This property is read-only.

## Syntax


```VB
Property Enabled As Long
```



## Property value

1 if the menu item is enabled; otherwise, the return value is 0.

## Examples


```VB
' Retrieve the Enabled property for the MenuItem object.
Dim nEnabled As Long
nEnabled = objMenuItem.Enabled
If (1 = nEnabled) Then
    MsgBox (objMenuItem.DisplayName & " is enabled")
Else
    MsgBox (objMenuItem.DisplayName & " is disabled")
End If
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_MenuItem is defined as 0178FAD1-B361-4B27-96AD-67C57EBF2E1D<br/>             |



## See also

<dl> <dt>

[**MenuItem.Execute**](menuitem-execute.md)
</dt> </dl>

 

 





