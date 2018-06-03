---
title: SetIntegerElement method of the BcdObject class
description: Sets the specified integer element.
ms.assetid: 86cd8053-b3cc-4621-9c32-9542a75daf93
keywords:
- SetIntegerElement method Boot Config
- SetIntegerElement method Boot Config , BcdObject class
- BcdObject class Boot Config , SetIntegerElement method
topic_type:
- apiref
api_name:
- BcdObject.SetIntegerElement
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

# SetIntegerElement method of the BcdObject class

Sets the specified integer element.

## Syntax


```mof
boolean SetIntegerElement(
  [in] uint32 Type,
  [in] uint64 Integer
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The element type. This parameter is one of the Integer element types from the following enumerations:

-   [**BcdBootMgrElementTypes**](bcdbootmgrelementtypes.md)
-   [**BcdDeviceObjectElementTypes**](bcddeviceobjectelementtypes.md)
-   [**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
-   [**BcdMemDiagElementTypes**](bcdmemdiagelementtypes.md)
-   [**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)

It can also be a custom element type created for your own use.

</dd> <dt>

*Integer* \[in\]
</dt> <dd>

The element value.

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

[**BcdIntegerElement**](bcdintegerelement.md)
</dt> <dt>

[**BcdObject**](bcdobject.md)
</dt> </dl>

 

 





