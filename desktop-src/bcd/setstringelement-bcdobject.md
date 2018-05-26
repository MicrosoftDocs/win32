---
title: SetStringElement method of the BcdObject class
description: Sets the specified string element.
ms.assetid: 91745d36-eacb-4aa2-b654-0ae91f64be9d
keywords:
- SetStringElement method Boot Config
- SetStringElement method Boot Config , BcdObject class
- BcdObject class Boot Config , SetStringElement method
topic_type:
- apiref
api_name:
- BcdObject.SetStringElement
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

# SetStringElement method of the BcdObject class

Sets the specified string element.

## Syntax


```mof
boolean SetStringElement(
  [in] uint32 Type,
  [in] string String
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The element type. This parameter is one of the String element types from the following enumerations:

-   [**BcdBootMgrElementTypes**](bcdbootmgrelementtypes.md)
-   [**BcdDeviceObjectElementTypes**](bcddeviceobjectelementtypes.md)
-   [**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
-   [**BcdMemDiagElementTypes**](bcdmemdiagelementtypes.md)
-   [**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)

It can also be a custom element type created for your own use.

</dd> <dt>

*String* \[in\]
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

[**BcdObject**](bcdobject.md)
</dt> <dt>

[**BcdStringElement**](bcdstringelement.md)
</dt> </dl>

 

 





