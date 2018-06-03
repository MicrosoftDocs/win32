---
title: SetObjectElement method of the BcdObject class
description: Sets the specified object element.
ms.assetid: 2f8ec103-f118-4f27-801d-5b5ca8601a4b
keywords:
- SetObjectElement method Boot Config
- SetObjectElement method Boot Config , BcdObject class
- BcdObject class Boot Config , SetObjectElement method
topic_type:
- apiref
api_name:
- BcdObject.SetObjectElement
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

# SetObjectElement method of the BcdObject class

Sets the specified object element.

## Syntax


```mof
boolean SetObjectElement(
  [in] uint32 Type,
  [in] string Id
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The element type. This parameter is one of the Object element types from the following enumerations:

-   [**BcdBootMgrElementTypes**](bcdbootmgrelementtypes.md)
-   [**BcdDeviceObjectElementTypes**](bcddeviceobjectelementtypes.md)
-   [**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
-   [**BcdMemDiagElementTypes**](bcdmemdiagelementtypes.md)
-   [**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)

It can also be a custom element type created for your own use.

</dd> <dt>

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

[**BcdObjectElement**](bcdobjectelement.md)
</dt> <dt>

[**BcdObject**](bcdobject.md)
</dt> </dl>

 

 





