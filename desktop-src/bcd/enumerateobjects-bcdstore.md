---
title: EnumerateObjects method of the BcdStore class
description: Enumerates the objects of the specified type.
ms.assetid: '81834c12-3565-4a55-ae55-cc248e2d2aee'
keywords: ["EnumerateObjects method Boot Config", "EnumerateObjects method Boot Config , BcdStore class", "BcdStore class Boot Config , EnumerateObjects method"]
topic_type:
- apiref
api_name:
- BcdStore.EnumerateObjects
api_location:
- Root\WMI
api_type:
- COM
---

# EnumerateObjects method of the BcdStore class

Enumerates the objects of the specified type.

## Syntax


```mof
boolean EnumerateObjects(
  [in]  uint32    Type,
  [out] BcdObject Objects[]
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The object type. For more information, see the **Type** property of the [**BCDObject**](bcdobject.md) class.

</dd> <dt>

*Objects* \[out\]
</dt> <dd>

An array of objects.

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

 

 





