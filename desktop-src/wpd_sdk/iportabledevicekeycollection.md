---
description: The IPortableDeviceKeyCollection interface holds a collection of PROPERTYKEY values. This interface can be retrieved from a method or, if a new object is required, call CoCreate with CLSID\_PortableDeviceKeyCollection.
ms.assetid: 2460f5bc-6b1c-4e3b-bdb9-faaa6d6c87fd
title: IPortableDeviceKeyCollection interface (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceKeyCollection
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceKeyCollection interface

The **IPortableDeviceKeyCollection** interface holds a collection of **PROPERTYKEY** values. This interface can be retrieved from a method or, if a new object is required, call **CoCreate** with **CLSID\_PortableDeviceKeyCollection**.

## Members

The **IPortableDeviceKeyCollection** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IPortableDeviceKeyCollection** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPortableDeviceKeyCollection** interface has these methods.



| Method                                                    | Description                                                                         |
|:----------------------------------------------------------|:------------------------------------------------------------------------------------|
| [**Add**](iportabledevicekeycollection-add.md)           | Adds a property key to the collection.<br/>                                   |
| [**Clear**](iportabledevicekeycollection-clear.md)       | Deletes all items from the collection.<br/>                                   |
| [**GetAt**](iportabledevicekeycollection-getat.md)       | Retrieves a **PROPERTYKEY** from the collection by index.<br/>                |
| [**GetCount**](iportabledevicekeycollection-getcount.md) | Retrieves the number of keys in this collection.<br/>                         |
| [**RemoveAt**](iportabledevicekeycollection-removeat.md) | Removes the element stored at the location specified by the given index.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**Collection Interfaces**](collection-interfaces.md)
</dt> </dl>

 

