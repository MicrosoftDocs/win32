---
title: DeleteElement method of the BcdObject class
description: Deletes the specified element.
ms.assetid: 5f806b25-c5a4-425d-b2c3-cc7275fd2545
keywords:
- DeleteElement method Boot Config
- DeleteElement method Boot Config , BcdObject class
- BcdObject class Boot Config , DeleteElement method
topic_type:
- apiref
api_name:
- BcdObject.DeleteElement
api_location:
- ahadmin.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeleteElement method of the BcdObject class

Deletes the specified element.

## Syntax


```mof
boolean DeleteElement(
  [in] uint32 Type
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The element type. This parameter is one of the values from the following enumerations:

-   [**BcdBootMgrElementTypes**](bcdbootmgrelementtypes.md)
-   [**BcdDeviceObjectElementTypes**](bcddeviceobjectelementtypes.md)
-   [**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
-   [**BcdMemDiagElementTypes**](bcdmemdiagelementtypes.md)
-   [**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)

It can also be a custom element type created for your own use.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Namespace<br/>                | Root\\WMI<br/>                                                                 |
| Header<br/>                   | <dl> <dt>Ahadmin.h</dt> </dl> |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl>   |



## See also

<dl> <dt>

[**BcdObject**](bcdobject.md)
</dt> </dl>

 

 





