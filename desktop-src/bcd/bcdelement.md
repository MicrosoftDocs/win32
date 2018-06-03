---
title: BcdElement class
description: The base class for all BCD elements.
ms.assetid: f8182914-2f5c-4d48-9e7c-400957a6d081
keywords:
- BcdElement class Boot Config
- BcdElement class Boot Config , described
topic_type:
- apiref
api_name:
- BcdElement
- BcdElement.StoreFilePath
- BcdElement.ObjectId
- BcdElement.Type
api_location:
- Root\WMI
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BcdElement class

The base class for all BCD elements.

## Syntax

``` syntax
class BcdElement
{
  string StoreFilePath;
  string ObjectId;
  uint32 Type;
};
```

## Members

The **BcdElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdElement** class has these properties.

<dl> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The identifier of the object for this element.

</dd> <dt>

**StoreFilePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The file path of the store for this element.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The element type. The layout of this value is described in [**BcdElementType**](bcdelementtype.md).

This parameter can be one of the values from the following enumerations:

-   [**BcdBootMgrElementTypes**](bcdbootmgrelementtypes.md)
-   [**BcdDeviceObjectElementTypes**](bcddeviceobjectelementtypes.md)
-   [**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
-   [**BcdMemDiagElementTypes**](bcdmemdiagelementtypes.md)
-   [**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)

It can also be a custom element type created for your own use.

</dd> </dl>

## Remarks

All BCD elements share a common header. The remainder of the element is determined by the element's data format.

All data in an element is byte-packed to ensure consistent unpacking by all consumers.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdBooleanElement**](bcdbooleanelement.md)
</dt> <dt>

[**BcdDeviceElement**](bcddeviceelement.md)
</dt> <dt>

[**BcdIntegerElement**](bcdintegerelement.md)
</dt> <dt>

[**BcdObjectElement**](bcdobjectelement.md)
</dt> <dt>

[**BcdObjectListElement**](bcdobjectlistelement.md)
</dt> <dt>

[**BcdStringElement**](bcdstringelement.md)
</dt> <dt>

[**EnumerateElements**](enumerateelements-bcdobject.md)
</dt> <dt>

[**GetElement**](getelement-bcdobject.md)
</dt> </dl>

 

 





