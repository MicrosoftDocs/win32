---
title: SetIntegerListElement method of the BcdObject class
description: Sets the specified integer list element.
ms.assetid: 25a11e8d-7a2f-4e0f-a6e9-480d588750d3
keywords:
- SetIntegerListElement method Boot Config
- SetIntegerListElement method Boot Config , BcdObject class
- BcdObject class Boot Config , SetIntegerListElement method
topic_type:
- apiref
api_name:
- BcdObject.SetIntegerListElement
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

# SetIntegerListElement method of the BcdObject class

Sets the specified integer list element.

## Syntax


```mof
boolean SetIntegerListElement(
  [in] uint32 Type,
  [in] uint64 Integers[]
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The element type. This parameter is one of the ObjectList element types from the following enumeration types:

-   [**BcdBootMgrElementTypes**](bcdbootmgrelementtypes.md)
-   [**BcdDeviceObjectElementTypes**](bcddeviceobjectelementtypes.md)
-   [**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
-   [**BcdMemDiagElementTypes**](bcdmemdiagelementtypes.md)
-   [**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)

It can also be a custom element type created for your own use.

</dd> <dt>

*Integers* \[in\]
</dt> <dd>

An array of integers. Each element is an integer in string form.

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

[**BcdObjectListElement**](bcdobjectlistelement.md)
</dt> <dt>

[**BcdObject**](bcdobject.md)
</dt> </dl>

 

 





