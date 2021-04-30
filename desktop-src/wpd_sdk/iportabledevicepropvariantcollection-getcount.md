---
description: The GetCount method retrieves the number of items in this collection.
ms.assetid: b7c8acd2-67f2-47d3-b42a-26aa701fd613
title: IPortableDevicePropVariantCollection::GetCount method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDevicePropVariantCollection.GetCount
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDevicePropVariantCollection::GetCount method

The **GetCount** method retrieves the number of items in this collection.

## Syntax


```C++
HRESULT GetCount(
  [in] DWORD *pcElems
);
```



## Parameters

<dl> <dt>

*pcElems* \[in\]
</dt> <dd>

Pointer to a **DWORD** that contains the number of items in the collection.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                               | Description                                          |
|-------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The method succeeded.<br/>                     |
| <dl> <dt>**E\_POINTER**</dt> </dl> | A required pointer argument was **NULL**.<br/> |



 

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

[Retrieving Supported Service Events](retrieving-supported-events.md)
</dt> <dt>

[Retrieving Supported Service Formats](retrieving-supported-formats.md)
</dt> <dt>

[Retrieving Supported Service Methods](retrieving-supported-methods.md)
</dt> <dt>

[Retrieving the Functional Categories Supported by a Device](retrieving-the-functional-categories-supported-by-a-device.md)
</dt> <dt>

[Setting Properties for Multiple Objects](setting-properties-for-multiple-objects.md)
</dt> </dl>

 

 




