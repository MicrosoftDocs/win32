---
description: Removes the current IWiaItem2 object from the device's object tree.
ms.assetid: 247eb36f-3e5c-4030-8334-1a4028b3eb44
title: IWiaItem2::DeleteItem method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaItem2.DeleteItem
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaItem2::DeleteItem method

Removes the current [**IWiaItem2**](-wia-iwiaitem2.md) object from the device's object tree.

## Syntax


```C++
HRESULT DeleteItem(
  [in] LONG lFlags
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Currently unused. Should be set to zero.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The Windows Image Acquisition (WIA) 2.0 run-time system represents each WIA 2.0 hardware device connected to the user's computer as a hierarchical tree of [**IWiaItem2**](-wia-iwiaitem2.md) objects. A given WIA 2.0 device may or may not allow applications to delete **IWiaItem2** objects from its tree. Items that have children cannot be deleted. The [**IEnumWIA\_DEV\_CAPS**](/windows/desktop/api/wia_xp/nn-wia_xp-ienumwia_dev_caps) interface must be used to query the device for item deletion capability.

If the device supports item deletion in its [**IWiaItem2**](-wia-iwiaitem2.md) tree, call the **IWiaItem2::DeleteItem** method to remove the **IWiaItem2** object. Note that this method only deletes an object after all references to the object have been released. If the deletion of an item has failed, E\_DELETEITEM is returned. The numeric value for this error is not yet defined.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 




