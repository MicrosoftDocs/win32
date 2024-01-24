---
description: IPortableDevicePropVariantCollection::GetAt method - The GetAt method retrieves an item from the collection by a zero-based index.
ms.assetid: c7119ba6-e6fc-4cb6-a8ab-3bf7b6bfe850
title: IPortableDevicePropVariantCollection::GetAt method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDevicePropVariantCollection.GetAt
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDevicePropVariantCollection::GetAt method

The **GetAt** method retrieves an item from the collection by a zero-based index.

## Syntax


```C++
HRESULT GetAt(
  [in]  const DWORD       dwIndex,
  [out]       PROPVARIANT *pValue
);
```



## Parameters

<dl> <dt>

*dwIndex* \[in\]
</dt> <dd>

**DWORD** that contains the zero-based index of the item to retrieve.

</dd> <dt>

*pValue* \[out\]
</dt> <dd>

Pointer to a **PROPVARIANT** structure. The caller is responsible for freeing this memory by calling **PropVariantClear**.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                  | Description                                               |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method succeeded.<br/>                          |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | A required pointer argument was **NULL**.<br/>      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The index that was passed in was out of range.<br/> |



 

## Examples

For an example of how to use this method see [Retrieving the Functional Categories Supported by a Device](retrieving-the-functional-categories-supported-by-a-device.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md)
</dt> <dt>

[Retrieving an Object Identifier from a Persistent Unique Identifier](retrieving-an-object-identifier-from-a-persistent-unique-identifier.md)
</dt> <dt>

[Retrieving Supported Service Events](retrieving-supported-events.md)
</dt> <dt>

[Retrieving Supported Service Formats](retrieving-supported-formats.md)
</dt> <dt>

[Retrieving Supported Service Methods](retrieving-supported-methods.md)
</dt> <dt>

[Retrieving the Content Types Supported by a Device](retrieving-the-content-types-supported-by-a-device.md)
</dt> <dt>

[Retrieving the Functional Categories Supported by a Device](retrieving-the-functional-categories-supported-by-a-device.md)
</dt> <dt>

[Retrieving the Functional Object Identifiers for a Device](retrieving-the-functional-object-identifiers-for-a-device.md)
</dt> <dt>

[Retrieving the Rendering Capabilities Supported by a Device](retrieving-the-rendering-capabilities-supported-by-a-device.md)
</dt> <dt>

[Setting Properties for Multiple Objects](setting-properties-for-multiple-objects.md)
</dt> </dl>

 

 




