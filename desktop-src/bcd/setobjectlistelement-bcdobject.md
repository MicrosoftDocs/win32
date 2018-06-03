---
title: SetObjectListElement method of the BcdObject class
description: Sets the specified object list element.
ms.assetid: 3c1d327e-5dc0-44cc-b258-5f4b20f4fd81
keywords:
- SetObjectListElement method Boot Config
- SetObjectListElement method Boot Config , BcdObject class
- BcdObject class Boot Config , SetObjectListElement method
topic_type:
- apiref
api_name:
- BcdObject.SetObjectListElement
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

# SetObjectListElement method of the BcdObject class

Sets the specified object list element.

## Syntax


```mof
boolean SetObjectListElement(
  [in] uint32 Type,
  [in] string Ids[]
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The element type. This parameter is one of the ObjectList element types from the following enumerations:

-   [**BcdBootMgrElementTypes**](bcdbootmgrelementtypes.md)
-   [**BcdDeviceObjectElementTypes**](bcddeviceobjectelementtypes.md)
-   [**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
-   [**BcdMemDiagElementTypes**](bcdmemdiagelementtypes.md)
-   [**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)

It can also be a custom element type created for your own use.

</dd> <dt>

*Ids* \[in\]
</dt> <dd>

An array of object identifiers. Each element is a GUID in string form, surrounded by curly braces.

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

 

 





