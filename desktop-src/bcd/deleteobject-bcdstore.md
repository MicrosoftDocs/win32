---
title: DeleteObject method of the BcdStore class
description: Deletes the specified object.
ms.assetid: 6db6b2ed-fcf3-480b-a436-9b7c34b45fcb
keywords:
- DeleteObject method Boot Config
- DeleteObject method Boot Config , BcdStore class
- BcdStore class Boot Config , DeleteObject method
topic_type:
- apiref
api_name:
- BcdStore.DeleteObject
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

# DeleteObject method of the BcdStore class

Deletes the specified object.

## Syntax


```mof
boolean DeleteObject(
  [in] string Id
);
```



## Parameters

<dl> <dt>

*Id* \[in\]
</dt> <dd>

The object identifier. This is a GUID in string form, surrounded by curly braces.

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

 

 





