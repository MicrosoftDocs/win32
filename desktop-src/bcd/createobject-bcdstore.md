---
title: CreateObject method of the BcdStore class
description: Creates the specified object.
ms.assetid: ab5a685d-f3bc-4e5b-a7dc-6b69cbf23089
keywords:
- CreateObject method Boot Config
- CreateObject method Boot Config , BcdStore class
- BcdStore class Boot Config , CreateObject method
topic_type:
- apiref
api_name:
- BcdStore.CreateObject
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

# CreateObject method of the BcdStore class

Creates the specified object.

## Syntax


```mof
boolean CreateObject(
  [in]  string    Id,
  [in]  uint32    Type,
  [out] BcdObject Object
);
```



## Parameters

<dl> <dt>

*Id* \[in\]
</dt> <dd>

The object identifier. This is a GUID in string form, surrounded by curly braces.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The object type.

</dd> <dt>

*Object* \[out\]
</dt> <dd>

The object.

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

 

 





