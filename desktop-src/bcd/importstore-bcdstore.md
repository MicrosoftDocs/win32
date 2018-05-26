---
title: ImportStore method of the BcdStore class
description: Marks the specified store as the system store.
ms.assetid: a9ffb4cb-be35-487e-9f64-29954048c767
keywords:
- ImportStore method Boot Config
- ImportStore method Boot Config , BcdStore class
- BcdStore class Boot Config , ImportStore method
topic_type:
- apiref
api_name:
- BcdStore.ImportStore
api_location:
- Root\WMI
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ImportStore method of the BcdStore class

Marks the specified store as the system store.

## Syntax


```mof
boolean ImportStore(
  [in] string File
);
```



## Parameters

<dl> <dt>

*File* \[in\]
</dt> <dd>

The full path to the store. The store could be created by [**ExportStore**](exportstore-bcdstore.md) or [**CreateStore**](createstore-bcdstore.md) method or by the **BcdEdit /export** or **BcdEdit /createstore** command.

</dd> </dl>

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
</dt> <dt>

[**ExportStore**](exportstore-bcdstore.md)
</dt> <dt>

[**ImportStoreWithFlags**](importstorewithflags-bcdstore.md)
</dt> </dl>

 

 





