---
title: EnumerateElementTypes method of the BcdObject class
description: Enumerates the types of elements in the object.
ms.assetid: 11b6d2cd-2f34-4460-b49e-37f362a1aea0
keywords:
- EnumerateElementTypes method Boot Config
- EnumerateElementTypes method Boot Config , BcdObject class
- BcdObject class Boot Config , EnumerateElementTypes method
topic_type:
- apiref
api_name:
- BcdObject.EnumerateElementTypes
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

# EnumerateElementTypes method of the BcdObject class

Enumerates the types of elements in the object.

## Syntax


```mof
boolean EnumerateElementTypes(
  [out] uint32 Types[]
);
```



## Parameters

<dl> <dt>

*Types* \[out\]
</dt> <dd>

An array of element types. Each array element can be one of the values from the following enumerations:

-   [**BcdBootMgrElementTypes**](bcdbootmgrelementtypes.md)
-   [**BcdDeviceObjectElementTypes**](bcddeviceobjectelementtypes.md)
-   [**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
-   [**BcdMemDiagElementTypes**](bcdmemdiagelementtypes.md)
-   [**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)

It can also be a custom element type created for your own use.

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

[**BcdObject**](bcdobject.md)
</dt> </dl>

 

 





