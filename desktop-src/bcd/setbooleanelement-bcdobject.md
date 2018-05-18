---
title: SetBooleanElement method of the BcdObject class
description: Sets the specified Boolean element.
ms.assetid: 'c4b8d4c4-aa7f-4972-b040-14cc35ad50a6'
keywords: ["SetBooleanElement method Boot Config", "SetBooleanElement method Boot Config , BcdObject class", "BcdObject class Boot Config , SetBooleanElement method"]
topic_type:
- apiref
api_name:
- BcdObject.SetBooleanElement
api_location:
- Root\WMI
api_type:
- COM
---

# SetBooleanElement method of the BcdObject class

Sets the specified Boolean element.

## Syntax


```mof
boolean SetBooleanElement(
  [in] uint32  Type,
  [in] boolean Boolean
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The element type. This parameter is one of the Boolean element types from the following enumerations:

-   [**BcdBootMgrElementTypes**](bcdbootmgrelementtypes.md)
-   [**BcdDeviceObjectElementTypes**](bcddeviceobjectelementtypes.md)
-   [**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
-   [**BcdMemDiagElementTypes**](bcdmemdiagelementtypes.md)
-   [**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)

It can also be a custom element type created for your own use.

</dd> <dt>

*Boolean* \[in\]
</dt> <dd>

The element value.

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

[**BcdBooleanElement**](bcdbooleanelement.md)
</dt> <dt>

[**BcdObject**](bcdobject.md)
</dt> </dl>

 

 





