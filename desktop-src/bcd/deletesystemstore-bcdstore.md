---
title: DeleteSystemStore method of the BcdStore class
description: Deletes the system BCD store. The caller must hold the SE\_BACKUP\_PRIVILEGE, and this method only works on the Windows Preinstallation Environment (Windows PE) or a non-BCD aware operating system.
ms.assetid: 518b1ae4-9e80-4c4a-8bdc-b36dc25fe0ce
keywords:
- DeleteSystemStore method Boot Config
- DeleteSystemStore method Boot Config , BcdStore class
- BcdStore class Boot Config , DeleteSystemStore method
topic_type:
- apiref
api_name:
- BcdStore.DeleteSystemStore
api_location:
- Root\WMI
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeleteSystemStore method of the BcdStore class

Deletes the system BCD store. The caller must hold the **SE\_BACKUP\_PRIVILEGE**, and this method only works on the Windows Preinstallation Environment (Windows PE) or a non-BCD aware operating system.

## Syntax


```mof
boolean DeleteSystemStore();
```



## Parameters

This method has no parameters.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdStore**](bcdstore.md)
</dt> </dl>

 

 





