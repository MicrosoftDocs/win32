---
description: The IPortableDeviceValues interface holds a collection of PROPERTYKEY/PROPVARIANT pairs.
ms.assetid: a73cbb4e-15d2-4c8d-9267-aaec9a0fd09f
title: IPortableDeviceValues interface (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues interface

The **IPortableDeviceValues** interface holds a collection of **PROPERTYKEY**/**PROPVARIANT** pairs. Values in the collection do not need to be the same VARTYPE.

Values are stored as key-value pairs; each key must be unique in the collection. Clients can search for items by **PROPERTYKEY** or zero-based index. Data values are stored as **PROPVARIANT** structures. You can add or retrieve values of any type by using the generic methods **SetValue** and **GetValue**, or you add items by using the method specific to the type of data added.

The **Get...** methods require the caller to release any retrieved values appropriately. The **Set...** methods copy the value into the collection.

When an **IPortableDeviceValues** interface is released, it calls **Clear**, which frees the memory that was allocated for all its members appropriately.

This interface can be retrieved from a method or, if a new object is required, call **CoCreate** with **CLSID\_PortableDeviceValues**.

## Members

The **IPortableDeviceValues** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IPortableDeviceValues** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPortableDeviceValues** interface has these methods.



| Method                                                                                                                     | Description                                                                                                            |
|:---------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|
| [**Clear**](iportabledevicevalues-clear.md)                                                                               | Deletes all items from the collection.<br/>                                                                      |
| [**CopyValuesFromPropertyStore**](iportabledevicevalues-copyvaluesfrompropertystore.md)                                   | Copies the contents of an **IPropertyStore** into the collection.<br/>                                           |
| [**CopyValuesToPropertyStore**](iportabledevicevalues-copyvaluestopropertystore.md)                                       | Copies all the values from a collection into an **IPropertyStore** interface.<br/>                               |
| [**GetAt**](iportabledevicevalues-getat.md)                                                                               | Retrieves a value from the collection using the supplied zero-based index.<br/>                                  |
| [**GetBoolValue**](iportabledevicevalues-getboolvalue.md)                                                                 | Retrieves a **BOOL** value (type VT\_BOOL) specified by a key.<br/>                                              |
| [**GetBufferValue**](iportabledevicevalues-getbuffervalue.md)                                                             | Retrieves a byte array value (type VT\_VECTOR \| VT\_UI1) specified by a key.<br/>                               |
| [**GetCount**](iportabledevicevalues-getcount.md)                                                                         | Retrieves the number of items in the collection.<br/>                                                            |
| [**GetErrorValue**](iportabledevicevalues-geterrorvalue.md)                                                               | Retrieves an **HRESULT** value (type VT\_ERROR) specified by a key.<br/>                                         |
| [**GetFloatValue**](iportabledevicevalues-getfloatvalue.md)                                                               | Retrieves a **FLOAT** value (type VT\_R4) specified by a key.<br/>                                               |
| [**GetGuidValue**](iportabledevicevalues-getguidvalue.md)                                                                 | Retrieves a **GUID** value (type VT\_CLSID) specified by a key.<br/>                                             |
| [**GetIPortableDeviceKeyCollectionValue**](iportabledevicevalues-getiportabledevicekeycollectionvalue.md)                 | Retrieves an **IPortableDeviceKeyCollection** value (type VT\_UNKNOWN) specified by a key.<br/>                  |
| [**GetIPortableDevicePropVariantCollectionValue**](iportabledevicevalues-getiportabledevicepropvariantcollectionvalue.md) | Retrieves an **IPortableDevicePropVariantCollection** value (type VT\_UNKNOWN) specified by a key.<br/>          |
| [**GetIPortableDeviceValuesCollectionValue**](iportabledevicevalues-getiportabledevicevaluescollectionvalue.md)           | Retrieves an **IPortableDeviceValuesCollection** value (type VT\_UNKNOWN) specified by a key.<br/>               |
| [**GetIPortableDeviceValuesValue**](iportabledevicevalues-getiportabledevicevaluesvalue.md)                               | Retrieves an **IPortableDeviceValues** value (type VT\_UNKNOWN) specified by a key.<br/>                         |
| [**GetIUnknownValue**](iportabledevicevalues-getiunknownvalue.md)                                                         | Retrieves an **IUnknown** interface value (type VT\_UNKNOWN) specified by a key.<br/>                            |
| [**GetKeyValue**](iportabledevicevalues-getkeyvalue.md)                                                                   | Retrieves a **PROPERTYKEY** value specified by a key.<br/>                                                       |
| [**GetSignedIntegerValue**](iportabledevicevalues-getsignedintegervalue.md)                                               | Retrieves a **LONG** value (type VT\_I4) specified by a key.<br/>                                                |
| [**GetSignedLargeIntegerValue**](iportabledevicevalues-getsignedlargeintegervalue.md)                                     | Retrieves a **LONGLONG** value (type VT\_I8) specified by a key.<br/>                                            |
| [**GetStringValue**](iportabledevicevalues-getstringvalue.md)                                                             | Retrieves a string value (type VT\_LPWSTR) specified by a key.<br/>                                              |
| [**GetUnsignedIntegerValue**](iportabledevicevalues-getunsignedintegervalue.md)                                           | Retrieves a **ULONG** value (type VT\_UI4) specified by a key.<br/>                                              |
| [**GetUnsignedLargeIntegerValue**](iportabledevicevalues-getunsignedlargeintegervalue.md)                                 | Retrieves a **ULONGLONG** value (type VT\_UI8) specified by a key.<br/>                                          |
| [**GetValue**](iportabledevicevalues-getvalue.md)                                                                         | Retrieves a **PROPVARIANT** value specified by a key.<br/>                                                       |
| [**RemoveValue**](iportabledevicevalues-removevalue.md)                                                                   | Removes an item from the collection.<br/>                                                                        |
| [**SetBoolValue**](iportabledevicevalues-setboolvalue.md)                                                                 | Adds a new **Boolean** value (type VT\_BOOL) or overwrites an existing one.<br/>                                 |
| [**SetBufferValue**](iportabledevicevalues-setbuffervalue.md)                                                             | Adds a new **BYTE**\* value (type VT\_VECTOR \| VT\_UI1) or overwrites an existing one.<br/>                     |
| [**SetErrorValue**](iportabledevicevalues-seterrorvalue.md)                                                               | Adds a new **HRESULT** value (type VT\_ERROR) or overwrites an existing one.<br/>                                |
| [**SetFloatValue**](iportabledevicevalues-setfloatvalue.md)                                                               | Adds a new **FLOAT** value (type VT\_R4) or overwrites an existing one.<br/>                                     |
| [**SetGuidValue**](iportabledevicevalues-setguidvalue.md)                                                                 | Adds a new **GUID** value (type VT\_CLSID) or overwrites an existing one.<br/>                                   |
| [**SetIPortableDeviceKeyCollectionValue**](iportabledevicevalues-setiportabledevicekeycollectionvalue.md)                 | Adds a new **IPortableDeviceKeyCollectionValue** value (type VT\_UNKNOWN) or overwrites an existing one.<br/>    |
| [**SetIPortableDevicePropVariantCollectionValue**](iportabledevicevalues-setiportabledevicepropvariantcollectionvalue.md) | Adds a new **IPortableDevicePropVariantCollection** value (type VT\_UNKNOWN) or overwrites an existing one.<br/> |
| [**SetIPortableDeviceValuesCollectionValue**](iportabledevicevalues-setiportabledevicevaluescollectionvalue.md)           | Adds a new **IPortableDeviceValuesCollection** value (type VT\_UNKNOWN) or overwrites an existing one.<br/>      |
| [**SetIPortableDeviceValuesValue**](iportabledevicevalues-setiportabledevicevaluesvalue.md)                               | Adds a new **IPortableDeviceValues** value (type VT\_UNKNOWN) or overwrites an existing one.<br/>                |
| [**SetIUnknownValue**](iportabledevicevalues-setiunknownvalue.md)                                                         | Adds a new **IUnknown** value (type VT\_UNKNOWN) or overwrites an existing one.<br/>                             |
| [**SetKeyValue**](iportabledevicevalues-setkeyvalue.md)                                                                   | Adds a new **PROPERTYKEY** (type VT\_UNKNOWN) value or overwrites an existing one.<br/>                          |
| [**SetSignedIntegerValue**](iportabledevicevalues-setsignedintegervalue.md)                                               | Adds a new **LONG** value (type VT\_I4) or overwrites an existing one.<br/>                                      |
| [**SetSignedLargeIntegerValue**](iportabledevicevalues-setsignedlargeintegervalue.md)                                     | Adds a new **LONGLONG** value (type VT\_I8) or overwrites an existing one.<br/>                                  |
| [**SetStringValue**](iportabledevicevalues-setstringvalue.md)                                                             | Adds a new string value (type VT\_LPWSTR) or overwrites an existing one.<br/>                                    |
| [**SetUnsignedIntegerValue**](iportabledevicevalues-setunsignedintegervalue.md)                                           | Adds a new **ULONG** value (type VT\_UI4) or overwrites an existing one.<br/>                                    |
| [**SetUnsignedLargeIntegerValue**](iportabledevicevalues-setunsignedlargeintegervalue.md)                                 | Adds a new **ULONGLONG** value (type VT\_UI8) or overwrites an existing one.<br/>                                |
| [**SetValue**](iportabledevicevalues-setvalue.md)                                                                         | Adds a new **PROPVARIANT** value or overwrites an existing one.<br/>                                             |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**Collection Interfaces**](collection-interfaces.md)
</dt> </dl>

 

