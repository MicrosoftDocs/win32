---
title: GetElement method of the BcdObject class
description: Gets the specified element.
ms.assetid: '34edc143-a0b6-40d4-bdd2-e799e0a12a72'
keywords: ["GetElement method Boot Config", "GetElement method Boot Config , BcdObject class", "BcdObject class Boot Config , GetElement method"]
topic_type:
- apiref
api_name:
- BcdObject.GetElement
api_location:
- Root\WMI
api_type:
- COM
---

# GetElement method of the BcdObject class

Gets the specified element.

## Syntax


```mof
boolean GetElement(
  [in]  uint32     Type,
  [out] BcdElement Element
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

</dd> <dt>

*Element* \[out\]
</dt> <dd>

The element.

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

[**BcdObject**](bcdobject.md)
</dt> </dl>

 

 





