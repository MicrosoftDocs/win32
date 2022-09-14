---
description: The IPortableDevicePropVariantCollection interface holds a collection of indexed PROPVARIANT values of the same VARTYPE.
ms.assetid: 41224958-a5a0-4e09-8733-d0ae036f68b9
title: IPortableDevicePropVariantCollection interface (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDevicePropVariantCollection
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDevicePropVariantCollection interface

The **IPortableDevicePropVariantCollection** interface holds a collection of indexed **PROPVARIANT** values of the same VARTYPE. The VARTYPE of the first item that is added to the collection determines the VARTYPE of the collection. An attempt to add an item of a different VARTYPE may fail if the **PROPVARIANT** value cannot be changed to the collection's current VARTYPE. To change the VARTYPE of the collection, call **ChangeType**.

This interface can be retrieved from a method or, if a new object is required, call **CoCreate** with **CLSID\_PortableDevicePropVariantCollection**.

## Members

The **IPortableDevicePropVariantCollection** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IPortableDevicePropVariantCollection** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPortableDevicePropVariantCollection** interface has these methods.



| Method                                                                | Description                                                                         |
|:----------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| [**Add**](iportabledevicepropvariantcollection-add.md)               | Adds an item to the collection.<br/>                                          |
| [**ChangeType**](iportabledevicepropvariantcollection-changetype.md) | Converts all items in the collection to the specified VARTYPE.<br/>           |
| [**Clear**](iportabledevicepropvariantcollection-clear.md)           | Frees, and then removes, all items from the collection.<br/>                  |
| [**GetAt**](iportabledevicepropvariantcollection-getat.md)           | Retrieves an item from the collection by a zero-based index.<br/>             |
| [**GetCount**](iportabledevicepropvariantcollection-getcount.md)     | Retrieves the number of items in this collection.<br/>                        |
| [**GetType**](iportabledevicepropvariantcollection-gettype.md)       | Retrieves the data type of the items in the collection.<br/>                  |
| [**RemoveAt**](iportabledevicepropvariantcollection-removeat.md)     | Removes the element stored at the location specified by the given index.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**Collection Interfaces**](collection-interfaces.md)
</dt> </dl>

 

