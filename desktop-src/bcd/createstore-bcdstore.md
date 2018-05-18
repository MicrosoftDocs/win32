---
title: CreateStore method of the BcdStore class
description: Creates a new store.
ms.assetid: 'e53199be-d5f1-493b-892c-ea3d96da9a7b'
keywords: ["CreateStore method Boot Config", "CreateStore method Boot Config , BcdStore class", "BcdStore class Boot Config , CreateStore method"]
topic_type:
- apiref
api_name:
- BcdStore.CreateStore
api_location:
- Root\WMI
api_type:
- COM
---

# CreateStore method of the BcdStore class

Creates a new store.

## Syntax


```mof
boolean CreateStore(
  [in]  string   File,
  [out] BcdStore Store
);
```



## Parameters

<dl> <dt>

*File* \[in\]
</dt> <dd>

The full path to the store to be created.

</dd> <dt>

*Store* \[out\]
</dt> <dd>

A BcdStore object.

</dd> </dl>

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdStore**](bcdstore.md)
</dt> </dl>

 

 





