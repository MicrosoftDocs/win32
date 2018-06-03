---
title: OpenStore method of the BcdStore class
description: Opens a store.
ms.assetid: 94015735-28bf-4f64-8359-393bbf7ca8c0
keywords:
- OpenStore method Boot Config
- OpenStore method Boot Config , BcdStore class
- BcdStore class Boot Config , OpenStore method
topic_type:
- apiref
api_name:
- BcdStore.OpenStore
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

# OpenStore method of the BcdStore class

Opens a store.

## Syntax


```mof
boolean OpenStore(
  [in]  string   File,
  [out] BcdStore Store
);
```



## Parameters

<dl> <dt>

*File* \[in\]
</dt> <dd>

The full path to the store to be opened. If this parameter is an empty string (""), the method opens the system store.

</dd> <dt>

*Store* \[out\]
</dt> <dd>

A BcdStore object.

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
</dt> </dl>

 

 





