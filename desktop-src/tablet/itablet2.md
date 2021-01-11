---
description: Extends the ITablet Interface.
ms.assetid: dd4f3b2e-7f63-4d5b-b50e-64458719c17a
title: ITablet2 interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITablet2
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITablet2 interface

Extends the [**ITablet Interface**](itablet.md).

## Members

The **ITablet2** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITablet2** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITablet2** interface has these methods.



| Method                                          | Description                                                                                              |
|:------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| [**GetDeviceKind**](itablet2-getdevicekind.md) | Returns the type of hardware device the tablet object represents such as mouse, pen or touch.<br/> |



 

## Remarks

This interface was introduced in Windows Vista.

Developers should not use this interface.

The following code describes how the **ITablet2** interface is defined.

``` syntax
[
    object,
    uuid(C247F616-BBEB-406A-AED3-F75E656599AE),
    pointer_default(unique)
]
interface ITablet2 : IUnknown
{
    HRESULT GetDeviceKind([out] TABLET_DEVICE_KIND *pKind);

    HRESULT GetMatchingScreenRect([out] RECT *prcInput);
};
```

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



 

