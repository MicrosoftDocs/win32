---
title: OpenObject method of the BcdStore class
description: Opens the specified object.
ms.assetid: ce717a16-a86c-495c-9847-4dbf429822d5
keywords:
- OpenObject method Boot Config
- OpenObject method Boot Config , BcdStore class
- BcdStore class Boot Config , OpenObject method
topic_type:
- apiref
api_name:
- BcdStore.OpenObject
api_location:
- cdosys.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OpenObject method of the BcdStore class

Opens the specified object.

## Syntax


```mof
boolean OpenObject(
  [in]  string    Id,
  [out] BcdObject Object
);
```



## Parameters

<dl> <dt>

*Id* \[in\]
</dt> <dd>

The object identifier. This is a GUID in string form, surrounded by curly braces.

</dd> <dt>

*Object* \[out\]
</dt> <dd>

The object.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Namespace<br/>                | Root\\WMI<br/>                                                                |
| Header<br/>                   | <dl> <dt>Cdosys.h</dt> </dl> |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl>  |



## See also

<dl> <dt>

[**BcdStore**](bcdstore.md)
</dt> </dl>

 

 





