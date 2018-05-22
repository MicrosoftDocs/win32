---
Description: 'The IPortableDeviceValuesCollection interface holds a collection of zero-based indexed IPortableDeviceValues interfaces.'
ms.assetid: '8bce9d27-f240-41ec-acf4-fefccdd95e9f'
title: IPortableDeviceValuesCollection interface
---

# IPortableDeviceValuesCollection interface

The **IPortableDeviceValuesCollection** interface holds a collection of zero-based indexed **IPortableDeviceValues** interfaces. This interface can be retrieved from a method, or if a new object is required, call **CoCreate** with **CLSID\_PortableDeviceValuesCollection**.

## Members

The **IPortableDeviceValuesCollection** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IPortableDeviceValuesCollection** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPortableDeviceValuesCollection** interface has these methods.



| Method                                                       | Description                                                                         |
|:-------------------------------------------------------------|:------------------------------------------------------------------------------------|
| [**Add**](iportabledevicevaluescollection-add.md)           | Adds an item to the collection<br/>                                           |
| [**Clear**](iportabledevicevaluescollection-clear.md)       | Releases all items from the collection.<br/>                                  |
| [**GetAt**](iportabledevicevaluescollection-getat.md)       | Retrieves an item from the collection by a zero-based index.<br/>             |
| [**GetCount**](iportabledevicevaluescollection-getcount.md) | Retrieves the number of items in the collection.<br/>                         |
| [**RemoveAt**](iportabledevicevaluescollection-removeat.md) | Removes the element stored at the location specified by the given index.<br/> |



 

## Requirements



|                    |                                                                                                    |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**Collection Interfaces**](collection-interfaces.md)
</dt> </dl>

 

 




